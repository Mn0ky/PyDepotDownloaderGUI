PyDepotDownloaderGUI
====================
<p align="center">
  <img src="https://img.shields.io/badge/status-Beta-blue" />
 </p>
 
A graphical user interface written in Python with PyQt5 for [**DepotDownloader**][depotdownloader] (tested on Windows and MacOS). 
<br/>Includes functionality to allow for multiple manifests to be specified and downloaded sequentially.
<br/>Compiled releases for Windows and MacOS can be found in the [**Releases**][releases] section.
<br/>Not all features are currently in the GUI.
#### Requirements/Information
.NET Core Runtime is *required* and can be downloaded [**here**][msdotnet2.1].
<br/>You *might* need the visual c++ redistributable from [**here.**][vc] (Users running Windows 10 should not)
<br/>SteamDB provides the info needed for games which can be found [**here**][steamdatabase].

A video tutorial for downloading a release version and using the GUI can be found here: **coming soon**
### Instructions for downloading a release and using the GUI:

1. Head over to the [**Releases**][releases] section and download the latest version

2. Extract the ZIP archive and then run the executable

### Instructions for downloading the Python script and using the GUI:
(It is *recommended* to use a [**Python virtual environment**][virtualenv])

1. Run the command ``git clone https://github.com/Mn0ky/PyDepotDownloaderGUI.git`` 
<br/>then ``cd PyDepotDownloaderGUI``

2. Install the necessary dependencies with ``pip install -r requirements.txt``

3. Finally, run ``python3 PyDepotDownloaderGUI.py``

[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
[depotdownloader]: https://github.com/SteamRE/DepotDownloader
[releases]: https://github.com/Mn0ky/PyDepotDownloaderGUI/releases/latest
[msdotnet2.1]: https://dotnet.microsoft.com/download/dotnet/2.1
[steamdatabase]: https://steamdb.info/
[vc]: https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0
