<h2><strong>ABOUT PLUGIN<br>
<blockquote></strong>
</h2></blockquote>

<table width='800' border='0'>
<blockquote><tr>
<blockquote><td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/IHAD_AVALIABLE.jpg' alt='GP3_iHAD_Avaliable' width='100' height='100' /></td>
<td>Subtitle Downloader, written in Python subtitle searching program (contains simple file browser and media player). It's main functionality is searching, downloading and converting the best fitting subtitle to given media content (supported video files: avi, mkv, mp4, mov, 3gp, other). Subtitle Downloader operating system is Enigma2TM (<a href='http://www.dream-multimedia-tv.de/'>Dream-Multimedia</a> DVB-S(2)/T/C set-top  receivers system).</blockquote></blockquote>

</td>
<blockquote></tr>
</table></blockquote>

<p><strong>Homepage:</strong> <a href='http://code.google.com/p/subs-downloader/'>http://code.google.com/p/subs-downloader/</a><br>
<strong>Developer:</strong> Dawid "SileliS" Bańkowski<br>
<p>Any errors and suggestion should be sent to project members.<br>

<p>Program uses different free routines that was found in GOOGLE and adjust to my requirements:<br>
<blockquote>- DreamExplorerII (part to play media, file info function, myFileList),<br>
- Periscope,<br>
- XBMC subtitles,<br>
- Subsconv,<br>
- GetFPS,<br>
- pyNapi,<br>
- Beautifull Soup,<br>
- Chardet.<br>
<p>The subtitles websites which are handled and currently supported:</blockquote>

<table>
<tr>
<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/OpenSubtitle.jpg' alt='Open Subtitle' width='180' height='50' /></td>

<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/NapiProject.jpg' alt='NapiProjekt' width='180' height='55' /></td>

<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/Napisy24.jpg' alt='Napisy24' width='180' height='55' /></td>

<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/BierDopje.jpg' alt='BierDopje' width='180' height='55' /></td>
</tr>
<tr>
<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/Subtitulos.jpg' alt='Subtitulos' width='180' height='55' /></td>

<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/Napisyme.jpg' alt='Subtitulos' width='180' height='55' /></td>

<td><img src='http://subs-downloader.googlecode.com/svn/files/pictures/project_home/Itasa.jpg' alt='Subtitulos' width='180' height='55' /></td>
</tr>

</table>
</p>

<h2><strong>Full list of features:</strong></h2>
- support for Itasa server,<br>
- support for  Napisy.me server,<br>
- support for Open Subtile server,<br>
- support for Bier Dopje server,<br>
- support for Napisy24 server,<br>
- support for Napi Projekt server,<br>
- support for Subtitulos  server,<br>
- local subtitle conversion to SRT,<br>
- supported input subtitle formats: MLP2, TMP, MDVD, SUB2, SRT,<br>
- Subtitle Downloader light and extended version avaliable (extended ver. supports libMediaInfo comprehensive library for detecting movie informations),<br>
- libMediaInfo and libzen auto installation on user request,<br>
- movie resume time support (cuts file support),<br>
- auto-update,<br>
- play movie and audio, show picture,<br>
- file browser and manager,<br>
- display file size,<br>
- 0 button shows/ hides skin,<br>
- enable/disable file browser media patern filter,<br>
- enable/disable file browser last path save.<br>

<p><strong>TODO:</strong><br>
<blockquote>- plugin.py linia self.session.open(MessageBox, <i>("There is no subtitle on this server to Your movie. \nPlease try another language or subtitle server.\n\nIf error still appears please check network connection with server."), MessageBox.TYPE_INFO, timeout = 5) usunąć, a w zamian dać MessageBoxy w poszczególnych in service.py,</i><br>
- move Napisy24_pl and NapiProjekt modul import to subtitle initialization if (less memory required),<br>
- Napisy24 XML_to_Dict in Napisy24_pl.py change to BeautifullSoup,<br>
- cache directory management in configuration menu,<br>
- Subtitle Source handling,<br>
- Subscene handling,<br>
- Addic7ed handling,<br>
- TheSubDB handling,<br>
- file decompresser (zip, rar, 7zip, bzip, etc),<br>
- Enigma2 skin font size and color for movie handling,<br>
- IMDb handling, <br>
- users suggestions and known bugs.<br>
<p><strong>KNOWN BUG:</strong><br>
- a long conversion for srt subtitles (reason unknown) <br>
- add opkg upgate at the preinst script (???mabey???) <br>
- program is sensitive for corrupted subtitles where end-line char is omitted<br>
i.e {12}{45}text{59}{70}text1{75}{90}text2.</blockquote>


<img src='http://s09.flagcounter.com/count/ydb/bg_FFFFFF/txt_000000/border_CCCCCC/columns_6/maxflags_42/viewers_0/labels_1/pageviews_1/=something_that_ends_with.png' />