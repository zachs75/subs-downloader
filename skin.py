
from Components.MenuList import MenuList

class SubsDownloaderApplication(Screen, OpenSubtitles, NapiProjekt, Napisy24_pl):
	#TODO SKIN SIZE SELECTRO DEPENDLY BY RESOLUTION
	global HDSkn
	global is_libmediainfo
	if HDSkn:
		screen_weight = getDesktop(0).size().width()
		screen_high = getDesktop(0).size().height() - 80
		skin_weight = round(screen_weight*0,9)
		screen_high = round(screen_high*0,9)
		skin = """
		<screen position="" + "center,"+str(round(skin_high*0,07)) size=""+ str(skin_weight)+","+str(skin_high) title= "Subtitle downloader" >
		<widget name="fileList" position="10,10" size="862,183" scrollbarMode="showOnDemand" />
		<widget name="subsList" position="10,203" size="862,183" scrollbarMode="showOnDemand" />
		<widget name="commertialPicture" position="10,390" size="1170,193" zPosition="1" alphatest="on" />
		<widget name="serverPicture" position="882,10" size="290,55" zPosition="1" alphatest="on" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_menu.png" position="882,70" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_menu" render="Label" position="925,70" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_help.png" position="882,100" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_help" render="Label" position="925,100" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_text.png" position="882,130" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_text" render="Label" position="925,130" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_next.png" position="882,160" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_next" render="Label" position="925,160" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_last.png" position="882,190" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_last" render="Label" position="925,190" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_info.png" position="882,220" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_info" render="Label" position="925,220" zPosition="1" size="220,26" font="Regular;20" halign="left" valign="center" transparent="1" />
		</screen>"""	
			
		else:
			skin = """
			<screen position="center,77" size="900,450" title="Subtitle downloader" >
			<widget name="fileList" position="7,7" size="659,150" scrollbarMode="showOnDemand" />
			<widget name="subsList" position="7,180" size="659,150" scrollbarMode="showOnDemand" />
			<widget name="commertialPicture" position="7,333" size="886,113" zPosition="1" alphatest="on" />
			<widget name="serverPicture" position="670,7" size="225,45" zPosition="1" alphatest="on" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_menu.png" position="670,60" size="36,26" zPosition="1" alphatest="on" />
			<widget source="key_menu" render="Label" position="710,60" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_help.png" position="670,90" size="36,26" zPosition="1" alphatest="on" />
			<widget source="key_help" render="Label" position="710,90" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_text.png" position="670,120" size="36,26" zPosition="1" alphatest="on" />
			<widget source="key_text" render="Label" position="710,120" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_next.png" position="670,150" size="36,26" zPosition="1" alphatest="on" />
			<widget source="key_next" render="Label" position="710,150" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_last.png" position="670,180" size="36,26" zPosition="1" alphatest="on" />	
			<widget source="key_last" render="Label" position="710,180" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_info.png" position="670,210" size="36,26" zPosition="1" alphatest="on" />	
			<widget source="key_info" render="Label" position="710,210" zPosition="1" size="175,26" font="Regular;18" halign="left" valign="center" transparent="1" />
			</screen>"""
			#	
	else:
		skin = """
		<screen position="center,80" size="620,450" title="Subtitle downloader" >
		<widget name="fileList" position="7,7" size="449,150" scrollbarMode="showOnDemand" />
		<widget name="subsList" position="7,180" size="449,150" scrollbarMode="showOnDemand" />
		<widget name="commertialPicture" position="7,333" size="606,113" zPosition="1" alphatest="on" />
		<widget name="serverPicture" position="463,7" size="152,37" zPosition="1" alphatest="on" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_menu.png" position="463,50" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_menu" render="Label" position="505,50" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_help.png" position="463,83" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_help" render="Label" position="505,83" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_text.png" position="463,116" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_text" render="Label" position="505,116" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_next.png" position="463,149" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_next" render="Label" position="505,149" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_last.png" position="463,182" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_next" render="Label" position="505,182" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/SubsDownloader2/pic/buttons/HD/key_info.png" position="463,215" size="36,26" zPosition="1" alphatest="on" />
		<widget source="key_info" render="Label" position="505,215" zPosition="1" size="105,26" font="Regular;16" halign="left" valign="center" transparent="1" />
		</screen>"""
			
