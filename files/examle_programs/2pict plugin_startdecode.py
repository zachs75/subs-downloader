import os
from os import stat as os_stat
from os import walk as os_walk
from Screens.Screen import Screen
from Components.config import config, ConfigSubList, ConfigSubsection, ConfigInteger, ConfigYesNo, ConfigText, getConfigListEntry, ConfigDirectory, ConfigSelection
from Components.ConfigList import ConfigListScreen
from Components.MenuList import MenuList
from Components.Label import Label
from Components.Pixmap import Pixmap
from Components.Sources.StaticText import StaticText
from Components.Label import MultiColorLabel
from Screens.MessageBox import MessageBox
from Screens.InfoBar import MoviePlayer as MP_parent
from Components.AVSwitch import AVSwitch
from Components.ActionMap import ActionMap
from Plugins.Plugin import PluginDescriptor
from Tools.HardwareInfo import HardwareInfo
from Components.FileList import *
from re import compile as re_compile
from os import path as os_path, listdir
from enigma import eConsoleAppContainer, eServiceReference, ePicLoad, getDesktop, eServiceCenter


#import players like Picture player, dvd player, music palyer
if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/PicturePlayer/plugin.pyo") or os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/PicturePlayer/plugin.pyc"):
	from Plugins.Extensions.PicturePlayer.plugin import Pic_Thumb, picshow
	PicPlayerAviable = True
else:
	PicPlayerAviable = False

# END of import players like Picture player, dvd player, music palyer

explSession = None
HDSkn = False
sz_w = getDesktop(0).size().width()
if sz_w > 800:
	HDSkn = True
else:
	HDSkn = False

class PictureExplorerII(Screen):
	
	getDesktop(0).size().width()
	
	skin="""
	<screen position="0,0" size="1280,720" title="Picture-Explorer" backgroundColor="#00121214">
	        <widget name="Picture" position="0,0" size="350,300" zPosition="1" alphatest="on" />
	        <widget name="Picture1" position="0,310" size="350,300" zPosition="1" alphatest="on" />
	</screen>"""
		#
		
	def __init__(self, session, whatPic = None):
		self.skin = PictureExplorerII.skin
		Screen.__init__(self, session)
		self.session = session
		self.whatPic = whatPic
			
		
		self["actions"] = ActionMap(["WizardActions", "DirectionActions"],
		{
			"back": self.close,
			"down": self.close
		}, -1)
		
		#PICTURES INITIALIZATION
		self.EXscale = (AVSwitch().getFramebufferScale())
		self.EXpicload = ePicLoad()
		self["Picture"] = Pixmap()
		self.EXpicload.PictureData.get().append(self.DecodeAction)

		self.whatPic = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/nnnn.jpg"
		self.onLayoutFinish.append(self.Show_Picture)
		
		self.whatPic = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture1.jpg"
		self.EXpicload.startDecode(self.whatPic)
		
		
		self.EXpicload1 = ePicLoad()
		self["Picture1"] = Pixmap()
		self.EXpicload1.PictureData.get().append(self.DecodeAction1)

		self.whatPic = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/nnnn.jpg"
		self.onLayoutFinish.append(self.Show_Picture1)
		
		self.whatPic = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture1.jpg"
		self.EXpicload1.startDecode(self.whatPic)
		
		
		
	def Show_Picture(self):
		self.EXpicload.setPara([self["Picture"].instance.size().width(), self["Picture"].instance.size().height(), self.EXscale[0], self.EXscale[1], 0, 1, "#002C2C39"])
		self.EXpicload.startDecode(self.whatPic)
			
		
	def DecodeAction(self, pictureInfo=""):
		ptr = self.EXpicload.getData()
		self["Picture"].instance.setPixmap(ptr)
		#text = picInfo.split('\n',1)    #WYSWIETLA INFORMACJE NA TEMAT OBRAZKA
		#self["label"].setText(text[1])  #WYSWIETLA INFORMACJE NA TEMAT OBRAZKA

		
	def Show_Picture1(self):
		self.EXpicload1.setPara([self["Picture1"].instance.size().width(), self["Picture1"].instance.size().height(), self.EXscale[0], self.EXscale[1], 0, 1, "#002C2C39"])
		self.EXpicload1.startDecode(self.whatPic)
			
		
	def DecodeAction1(self, pictureInfo=""):
		ptr = self.EXpicload1.getData()
		self["Picture1"].instance.setPixmap(ptr)
		#text = picInfo.split('\n',1)    #WYSWIETLA INFORMACJE NA TEMAT OBRAZKA
		#self["label"].setText(text[1])  #WYSWIETLA INFORMACJE NA TEMAT OBRAZKA		
		
		
		
###########################################################################

def main(session, **kwargs):
	print "\n[SubsDownloaderApplication] start\n"	
	session.open(PictureExplorerII, "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture2.jpg")
	
###########################################################################

def Plugins(**kwargs):
	return PluginDescriptor(
        name="2 pictures",
        description="Download subtitle to any movie",
        where = PluginDescriptor.WHERE_PLUGINMENU,
        icon="silelis_gasoline.png",
        fnc=main)