import httplib
#import xml.dom.minidom    
#import xml.etree.cElementTree as ElementTree


#import xml.dom.minidom


#http://www.blog.pythonlibrary.org/2010/11/12/python-parsing-xml-with-minidom/

#  Copyright (C) 2011 Dawid Ba�ski <enigma2subsdownloader@gmail.com>
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

class Napisy24_pl():
    def __init__(self,moviePath):
        self.MovieName = ((moviePath.rsplit("/",1))[-1]).rsplit(".",1)[0]
        self.MovieDir = (moviePath.rsplit("/",1))[0]
        self.ZipFilePath = str(moviePath.rsplit).rsplit(".", 1)[0]+'.zip'
        
    def getNapisy24_SubtitleListXML(self):
        repeat = 3
        while repeat > 0:  
            repeat = repeat - 1
            try:
                conn = httplib.HTTPConnection("napisy24.pl")
                conn.request("GET", "/libs/webapi.php?title=%s" % self.MovieName)
                r1 = conn.getresponse()
                print r1.status, r1.reason
                self.XML_String = r1.read()
            except (IOError, OSError), e:
                print >> sys.stderr, "Napisy24.pl server connection error."
                time.sleep(0.5)
                continue
            
            if r1.status != 200:
                print  "Fetching subtitle failed, HTTP code: %s" % (str(r1.status))
                time.sleep(0.5)
                continue
            else:
                repeat = 0
    
            if self.XML_String == ('brak wynikow'):
                print  "Subtitle NOT FOUND"
                repeat = 0
                continue

            if self.XML_String is None or self.XML_String == "":
                print "Subtitle download FAILED"
                continue
                
        if self.XML_String != 'brak wynikow':
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
        
 """   def XML_to_diary(self):
        try:
            dom = xml.dom.minidom.parseString(self.XML_String)
            self.aa = dom.getElementsByTagName("subtitle")
        except:
            pass"""
                    



aa = Napisy24_pl("127.avi")
if aa.getNapisy24_SubtitleListXML()== True:
    aa.Correct_MultiRoot_XML()
    print "Sa napisy"
    aa.XML_to_diary()  
else:
    print "Nie ma napisow"
    



