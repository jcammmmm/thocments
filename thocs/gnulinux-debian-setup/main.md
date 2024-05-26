Setup Script for debian
===========================================================
> Here you will find a collection of config files and scripts that will configure Debian after a fresh installation. This configurations are personal customizations that are always set each time I perform a fresh system install.


Config files collection
===========================================================
Following items must be executed in order
- Take ownership of `/opt` folder:
	* `sudo chown jcammmmm:jcammmmm /opt`
- Install `apt`
	* edit `/etc/apt/sources.list` file
- Install `sudo`
	* edit `/etc/sudoers` file
- Install `vim`
	* Copy config files
- Install `git`
- Install `kde-spectacle`
- Install `filezilla`
- Install `dolphin`
- Install `okular`
- Install `kolourpaint`
- Install `make`
- Install `gcc`
- Install `vlc`
- Install `python`
	* Install `pip`: `sudo apt install python3.11-pip`
	* Install `venv`: `sudo apt install python3.11-venv`
	* Install `youtube-dl`: `pip install -vvv --upgrade youtube-dl`
- Install `tree`
- Install `ranger`
- Install `qps` a system monitor
- Install `renameutils` this package contains `qmv` an utility for bulk renaming.
- Donwload and install `codium`
	* Download the package and install
	* Override key shourtcuts:
		- Copy Mappings `windows.keybindings.json` for custom shortcuts and font sizes.
		- Ctrl + P to open the command palette
		- Look for _Open Keyboard Shortcuts (JSON)_
		- Paste everything there.
	* Preferred plugins
	  - max-ss.cyberpunk: https://github.com/prometheux-ar/cyberpunk
	  - rsbondi.highlight-words: ??
		- vscjava.vscode-java-debug: https://github.com/Microsoft/vscode-java-debug.git
		- redhat.java: https://github.com/redhat-developer/vscode-java.git
		- koalamer.labeled-bookmarks: https://github.com/koalamer/vsc-labeled-bookmarks.git
	* Check for custom settings:
	  - Enable sticky scroll
- Donwload and install `chromium`
	* Download the package and install
- Donwload and install `xaos`; the fractal generator
- Install a torrent download manager: `transmission`
- `ncdu`: NCurses Disk Usage. A disk usage analyzer so you can see where your ara wasting storage space  
- `img2pdf`: Convert your images to PDF.
- Install Java11 more info [here][1]
	* Go to the release archive page [here][2] and download your desired version
	* Move the compressed file to `/opt`
	* Extract the package `tar xvf openjdk-11.0.2_linux-x64_bin.tar.gz`
	* Append `export JAVA_HOME=/opt/jdk-11.0.2` to your `.bashrc` shell config file.
	* And update your `PATH` by appending this line to  `.bashrc` file: `export PATH=$PATH:$JAVA_HOME/bin`
	
	
	
[1]: https://openjdk.org/install/
[2]: https://jdk.java.net/archive/




