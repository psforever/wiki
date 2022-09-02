# Connection Guide

To connect to the PSForever Server, follow the steps below. If you have any further questions, join us on [Discord](http://chat.psforever.net) and ask us your question in the *help* channel.

If you’re a returning player, make sure you set the server port to 51000. The old server/launcher used to be a default port of 51200, which is wrong.

### 1. Download and extract PlanetSide

[Google Drive :material-download:](https://drive.google.com/file/d/0B9EQ4wD-WnFIQTJON0hJb0dldWM/view?usp=sharing&resourcekey=0-MYrYhIKx60vg7_EWfu_fDQ){.md-button}
[Mega :material-download:](https://mega.nz/#!N5xTBR6Q!kVd0Po1L2mhvqPJYXx9s2UvQ-Ac1aXtuH3llCGs1uA8){.md-button}


### 2. Download and extract the PSForever Launcher (does not have to be in Planetside folder)

[PSForever Launcher :material-download:](https://github.com/psforever/GameLauncher/releases/download/v1.2.0.1/PSForever_Launcher_1.2.0.1.zip){.md-button}

1. Open the launcher
1. Click Settings
1. Click Choose
1. In the **Browse For Folder** window, browse for and click on the PlanetSide folder, then press OK
1. Check **Skip Launcher**, as you do not need to enter a username and password until you get in game
1. Click **Launch**

  Troubleshooting: If you get an error when attempting to launch the game, right click the PlanetSide client executable (Planetside.exe) in the PlanetSide folder, click **Properties**, click the **Compatibility** tab, check **Run this program as an Administrator**, and press **OK**.
  If you are still having issues, try running the PSForever_Launcher.exe as an administrator. Otherwise, follow the **Launcher workaround**/**Shortcut Method** found below, near the bottom of the page.

### 3. Connect to PSForever in the game client
1. Create an account by entering any name/password you want
2. (**Optional**) Change Bandwidth Settings<br>
    The client download will default to the ‘Low’ Bandwidth setting. I would recommend ‘Medium’, so you don’t get spammed for a few seconds with capture messages after the first loading world or zoning. If you run into soft locks/load screen freezes, go back to Low. ‘High’ is not recommended and will cause load screens to fail.
    The Bandwidth Settings are found by going to Options > Game > Bandwidth Settings. You can do this before choosing a character.
3. Choose the PSForever server
4. Click **PLAY**

### 4. Create a character

1. Click **CREATE CHARACTER** and customize a character to your likings, then press **FINISH**.
  Please use an appropriate name or you could lose access to the server.

### 5. Enter the game world
With your new character selected, press **PLAY** to enter the game

### Launcher Workaround (Shortcut Method)
If you are having trouble using the Launcher, you can circumvent it by taking these steps:

1. In your PlanetSide folder, open **client.ini** and change the IP to play.psforever.net:51000
1. Right click planetside.exe
1. Click **Create shortcut**
1. Find planetside.exe - Shortcut
1. Right click planetside.exe - Shortcut
1. Click **Properties**
1. Click the **Shortcut** tab
1. Find Target: and add a space, then `/K:StagingTest /CC` to the end, minding spaces. It is advised you copy and paste and add this exactly, otherwise you will get an **Invalid Target** error.
1. Example: `"C:\Planetside\planetside.exe" /K:StagingTest /CC`
1. Click the **Apply** button
1. Click the **Compatibility** tab
1. Under Settings, check the **Run this program as an administrator** checkbox.
1. Click **OK**
1. Run the game from the shortcut

### Wine Workarounds

* **Crashes to desktop after intro credits**:  Enable the "virtual desktop" feature within wine, seems to be a resolution based problem

* **No sound**: Install the ubuntu package libasound2-plugins:i386, may also be on other distros or an equivalent on others.
