import httplib
import xml.dom.minidom
import time
import re
import os
from urllib import quote
from operator import itemgetter, attrgetter
import zipfile

#  Copyright (C) 2011 Dawid Baďż˝ski <enigma2subsdownloader@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

class XML_to_Dict():
    def __init__(self):
	pass
    
    def xmltodict(self, xmlstring):
	doc = xml.dom.minidom.parseString(xmlstring)
	self.remove_whilespace_nodes(doc.documentElement)
	return self.elementtodict(doc.documentElement)

    def elementtodict(self, parent):
	child = parent.firstChild
	if (not child):
		return None
	elif (child.nodeType == xml.dom.minidom.Node.TEXT_NODE):
		return child.nodeValue
	
	d={}
	while child is not None:
		if (child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE):
			try:
				d[child.tagName]
			except KeyError:
				d[child.tagName]=[]
			d[child.tagName].append(self.elementtodict(child))
		child = child.nextSibling
	return d

    def remove_whilespace_nodes(self, node, unlink=True):
	remove_list = []
	for child in node.childNodes:
		if child.nodeType == xml.dom.Node.TEXT_NODE and not child.data.strip():
			remove_list.append(child)
		elif child.hasChildNodes():
			self.remove_whilespace_nodes(child, unlink)
	for node in remove_list:
		node.parentNode.removeChild(node)
		if unlink:
			node.unlink()

class Napisy24_pl(XML_to_Dict):    
    def __init__(self,moviePath):	
        self.MovieName = ((moviePath.rsplit("/",1))[-1]).rsplit(".",1)[0]
        self.MovieDir = (moviePath.rsplit("/",1))[0]
        self.ZipFilePath = self.MovieDir+'/'+((moviePath.rsplit("/",1))[-1]).rsplit(".",1)[0]+'.zip'
	self.subtitle_dict = []
	self.NAPISY24_url = "napisy24.pl"
    
    def __IMDB_idenifier_search(self):
	dir_list = os.listdir(self.MovieDir)
	dir_count = 0
	for x in dir_list:
	    if x.split(".")[-1].lower()=="nfo":
		print "find NFO in %i list" % dir_count
		break
	    dir_count=dir_count+1
	try:	
	    nfo_file = open(self.MovieDir+"/"+dir_list[dir_count],"r")
	    buffor = nfo_file.read()
	    nfo_file.close
	    #IMDB line in nfo: iMDB: http://www.imdb.com/title/tt1219289/	    
	    char_count = 0
	    while (char_count+len("http://www.imdb.com/title/")) < len(buffor):
		if buffor[char_count:(char_count+len("http://www.imdb.com/title/"))] == "http://www.imdb.com/title/":
		    print "%s" % str(char_count+len("http://www.imdb.com/title/"))
		    self.dd11 = IMDB_begining = char_count+len("http://www.imdb.com/title/")
		    break
		char_count=char_count+1
	    char_count=IMDB_begining+1   
	    while char_count < len(buffor):
		if buffor[char_count:(char_count+1)] == "/":
		    print "%s" % str(char_count)
		    self.dd22 = IMDB_ending = char_count
		    break
		char_count=char_count+1
	    return buffor[IMDB_begining:IMDB_ending]
	#tutaj trzeba sprawdziÄ paretn IMDB numeru jeĹli jest oka to zwraca informacjÄ jeĹli jest nie oka to zwraca bĹÄd
	except:	    
	    print "blad IMBN"
	    return False
	    #( #tu trzeba zwrĂłciÄ informacjÄ jeĹli jest jakiĹ bĹÄd
    
    def __connect_with_server(self,get_operatoin,server_reuest_type):
	"""Function connect with server and downloades avaliable subtitle
	list or avaliable subtitle zip file	
	"""
	what_is_downloaded = server_reuest_type
	self.XML_String = None
	self.zip_string = None
	try:
	    conn = httplib.HTTPConnection(self.NAPISY24_url)
	    conn.request("GET", get_operatoin)
	    r1 = conn.getresponse()
	    print r1.status, r1.reason
	    if what_is_downloaded == "downloada_subtitle_list_by_film_name" or what_is_downloaded == "downloada_subtitle_list_by_IMDB":
		self.XML_String = r1.read()
	    elif what_is_downloaded  == "download_subtilte_zip":		
		self.zip_string = r1.read()
	    return r1.status#, r1.reason
	except (IOError, OSError), e:
	    print >> sys.stderr, "Napisy24.pl server connection error."
	    time.sleep(0.5)
        
    def getNapisy24_SubtitleListXML(self, subtitle_list_reuest_type):	
        repeat = 3
	if subtitle_list_reuest_type == "downloada_subtitle_list_by_film_name":
	    request_subtitle_list = "/libs/webapi.php?title=%s" % quote(self.MovieName)		
	elif subtitle_list_reuest_type == "downloada_subtitle_list_by_IMDB":
	    request_subtitle_list = "/libs/webapi.php?imdb=%s" % "tt1219289"
        while repeat > 0:  
            repeat = repeat - 1
	    r1_status = self.__connect_with_server(request_subtitle_list, "downloada_subtitle_list_by_film_name")            
            if r1_status != 200 and r1_status != 400:
                print  "Fetching subtitle list failed, HTTP code: %s" % (str(r1_status))
                time.sleep(0.5)
                continue
	    elif r1_status == 400:
		print "Fetching subtitle list failed, HTTP code: %s \n Bad request in string: %s." % (str(r1_status), request_subtitle_list)
		repeat = -1
            else:
                repeat = 0
    
            if self.XML_String == ('brak wynikow'):
                print  "Subtitle list NOT FOUND"
                repeat = 0
                continue

            if self.XML_String is None or self.XML_String == "":
                print "Subtitle list download FAILED"
                continue
                
        if r1_status != 200 or self.XML_String == 'brak wynikow' or self.XML_String == "" or self.XML_String is None:
            return False
        else:
	    if self.return_xml_dict() == True:
		return True
	    else:
		return False
              
    def Correct_MultiRoot_XML(self):
        if self.XML_String[0] == "\n":
            self.XML_String=self.XML_String[1:]
        SECONDLINE_CHAR = 0
        for x in self.XML_String:
            SECONDLINE_CHAR = SECONDLINE_CHAR+1
            if x =="\n":
                break
        self.XML_String = self.XML_String[0:SECONDLINE_CHAR] + "<lista>"+ self.XML_String[(SECONDLINE_CHAR+1):]+"</lista>"
	self.XML_String = re.sub("&", "and", self.XML_String)
	self.XML_String = self.XML_String.decode("CP1252").encode("UTF-8")
    
    def return_xml_dict(self):
	try:
	    self.Correct_MultiRoot_XML()
	    self.subtitle_dict = sorted(self.xmltodict(self.XML_String)['subtitle'],key=itemgetter('imdb','cd'))
	    #self.subtitle_dict = self.xmltodict(self.XML_String)['subtitle']
	    print "XML subtitle list downloaded and converted to dict"
	    return True
	except:
	    print "XML subtitle list  not downloaded or converterd."
	    return False
	    
    
    def return_xml_dict_entry_value(self,dict_entry, dict_entry_position):
	value = self.subtitle_dict[dict_entry][dict_entry_position]
	return value[0]

    def save_downloaded_zip(self, dict_entry_to_download):
	if self.download_subtitle_zip(dict_entry_to_download) == True:
	    try:
		zip_file1 = open(self.ZipFilePath,"wb")
		zip_file1.write(self.zip_string)
		zip_file1.close
		print "Zipfile: %s saved on hdd." % self.ZipFilePath
		return True
	    except:
		print "Problems with Zipfile: %s saveing on hdd." % self.ZipFilePath
		return False
	
    def download_subtitle_zip(self, dict_entry_to_download):
	request_subtitle_list = "http://napisy24.pl/download/%i/" % int(self.return_xml_dict_entry_value(dict_entry_to_download,'id'))
	repeat = 3
	while repeat > 0:  
            repeat = repeat - 1
	    #request_subtitle_list = "/libs/webapi.php?title=%s" % self.MovieName
	    r1_status = self.__connect_with_server(request_subtitle_list, "download_subtilte_zip")            
            if r1_status != 302:
                print  "Fetching subtitle failed, HTTP code: %s" % (str(r1_status))
                time.sleep(0.5)
                continue
            else:
                repeat = 0
    
            if self.zip_string == None:
                print  "Subtitle NOT DOWNLOADED"
                repeat = 0
                continue

            if self.zip_string is None or self.zip_string == "":
                print "Subtitle NOT DOWNLOADED"
                continue
                
        if self.zip_string[0:2] == 'PK':
	    print "Success to download subtitle zip."
            return True
        else:
	    print "Reild to download subtitle zip."
            return False



aa = Napisy24_pl("C:/!!!!!!!!!!/Lord of the ring.avi")
aa.getNapisy24_SubtitleListXML("downloada_subtitle_list_by_film_name")
aa.save_downloaded_zip(1)

aa = Napisy24_pl("127")
aa = Napisy24_pl("C:/!!!!!!!!!!/American Horror Story.avi") #przypadek z dwona pĹytami http://napisy24.pl/download/53028/
aa = Napisy24_pl("C:/!!!!!!!!!!/Limitless.avi")


if aa.getNapisy24_SubtitleListXML("downloada_subtitle_list_by_film_name")== True:

if aa.__IMDB_idenifier_search()!= False:
    if aa.getNapisy24_SubtitleListXML("downloada_subtitle_list_by_IMDB")== True:
	
  
if aa.download_subtitle_zip(1) == True:
aa.save_downloaded_zip(1)
	

ZipFile.printdir()

   
#write to file:
file_xml = open("C:/!!!!!!!!!!/1.xml","w")
file_xml.write(aa.subtitle_dict[])
file_xml.close