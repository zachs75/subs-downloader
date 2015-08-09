# Introduction #

This manula will perform You through Subtitle Downloader installation proces


# Details #

## **0)** THIS STEP SHOULD BE DONE BY USERS WHO USE CLEAR iCVS image (i.e without GP3 extension) ##

Download iCVS\_libs.zip located in "downloads" menu and install all content manually.
I suppose that libs aren't added to iCVS ipk repository so Uou have to install it by Yourself.

**1)** Copy enigma2-plugin-extensions-subsdownloaderVERSIONmipsel.ipk file via ftp (or other mechanism) to Your sat receiver.

_I prefer /tmp directory so this manual will show You installation for this case._


**2)** Change directory to tmp dir:

_root@DM8000:cd /tmp_


**3**) Install IPK file:

_root@DM8000:opkg install enigma2-plugin-extensions-subsdownloader_ _VERSION_ _mipsel.ipk_

You should see telnet respond as below:

http://subs-downloader.googlecode.com/svn/files/pictures/wiki/installation/installation_telnet.JPG


**4)** Restart Enigma2 to add Subs Downloader to plugin list:

_root@DM8000:killall -9 enigma2_