from enigma import ePicLoad, getDesktop
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.Pixmap import Pixmap, MovingPixmap
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Sources.StaticText import StaticText
from Components.AVSwitch import AVSwitch
from Components.ConfigList import ConfigList, ConfigListScreen

def getScale():
	return AVSwitch().getFramebufferScale()

class picshow(Screen):
	skin = """
		<screen name="picshow" position="center,center" size="560,440" title="PicturePlayer" >
			<widget name="thn" position="10,40" size="180,160" alphatest="on" />
			<widget name="thn1" position="264,40" size="180,160" alphatest="on" />
	        </screen>"""

	#self["thn"] - left picture widget
	#self["thn1"] - right picture widget
	
	def __init__(self, session):
		Screen.__init__(self, session)

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "DirectionActions"],
		{
		        "cancel": self.KeyExit,       # EXIT APLICATION
		        "red": self.KeyRed,           # SHOULD ACTIVATE LEFT WIDGET BUT DON'T DO THIS
		        "green": self.KeyGreen,       # SWITCH AVTIVE WIDGET PISTURE TO path 1
		        "yellow": self.KeyYellow,     # SWITCH AVTIVE WIDGET PISTURE TO path 2
		        "blue": self.KeyBlue          # ACTIVATE RIGHT WIDGET BAND DO THIS
		}, -1)

	
		#self.picPath = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/napiprojekt.jpg"
		
		self.pictureWidget=0 #pomocniczna do ktorej przekazywane sa aktywne witget
		self.activePicture =0 #pomocniczna do ktorej przekazywane sa aktywne nazwy klasy obrazka
		self.PictureList = [] #pomocnicza przekazuje dane do self.onLayoutFinish.append(self.setConf) w ktorej jest kasowana
		self["thn"] = Pixmap()
		self.pictureWidget = self["thn"]
		self.picload = ePicLoad()
		self.activePicture = self.picload
		self.activePicture.PictureData.get().append(self.showPic)
		self.PictureList.append(self.activePicture)
		self.onLayoutFinish.append(self.setConf)
		
		self["thn1"] = Pixmap()
		self.pictureWidget = self["thn1"]
		self.picload1 = ePicLoad()
		self.activePicture = self.picload1
		self.activePicture.PictureData.get().append(self.showPic)
		self.PictureList.append(self.activePicture) #POTRZEBNE TYLKO DLA AUTOMATYCZNEGO onLayoutFinish.append w ktorym jest kasowany
		self.picPath = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture2.jpg"
		self.activePicture.getThumbnail(self.picPath)		
		self.onLayoutFinish.append(self.setConf)
		
		self.pictureWidget = self["thn"]
		self.activePicture = self.picload
		self["thn"].show()
		self.picPath = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture1.jpg"
		self.activePicture.getThumbnail(self.picPath)
		self.pictureWidget.show()
		self.activePicture.startDecode(self.picPath)
		self.onLayoutFinish.append(self.setConf)
		

	def KeyRed(self):
		self.pictureWidget = self["thn"]
		self.activePicture = self.picload
		self["thn"].show()
		
	def KeyGreen(self):
		self.picPath = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture1.jpg"
		self.activePicture.getThumbnail(self.picPath)
		self.pictureWidget.show()
	
	def KeyYellow(self):
		self.picPath = "/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/picture2.jpg"
		self.activePicture.getThumbnail(self.picPath)
		self.pictureWidget.show()

	def KeyBlue(self):
		self.pictureWidget = self["thn1"]
		self.activePicture = self.picload1
		self["thn1"].show()
		
	def showPic(self, picInfo=""):
		ptr = self.activePicture.getData()
		if ptr != None:
			self.pictureWidget.instance.setPixmap(ptr.__deref__())
			self.pictureWidget.show()

	def setConf(self):
		self.setTitle(_("PicturePlayer"))
		sc = getScale()
		#0=Width 1=Height 2=Aspect 3=use_cache 4=resize_type 5=Background(#AARRGGBB)
		x = 0
		while x < len(self.PictureList):
			self.PictureList[x].setPara((self.pictureWidget.instance.size().width(), self.pictureWidget.instance.size().height(), sc[0], sc[1], 0, 1, "#00000000"))
			x = x +1
		
	def KeyExit(self):
		del self.picload
		self.close()

def main(session, **kwargs):
	session.open(picshow)
	
def Plugins(**kwargs):
	return \
		[PluginDescriptor(name=_("2 Pictures"), description=_("2 widget dynamic pictures"), where = PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
