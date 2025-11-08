Debian Setup
===============================================================================
See at the end of this document for useful software and commands.

## sudo
If sudo is not installed on the system simply issue ```apt install sudo```
1. Note that ```su -``` is different from ```su -i```
2. ```su -```
3. Once you are the root open the ```/etc/sudoers``` file. Some times will require that you change the file permisions in order to be capable to edit, to so type `chmod 644 /etc/sudoers`. After completing the edit do not forget to restore the permissions, without that sudo would not work.
4. Then look for the root permissions line ```root ALL=(ALL:ALL) ALL```
5. Add a new line but now instead of ```root``` put your ```username```
6. Finally type ```:``` and then throw a ```w!```
7. Now your user can throw ```sudo commands```

## apt 
1. Comment out the ```cdrom://``` url line on ```sudo nano /etc/apt/sources.list```
2. Check the [documentation](https://wiki.debian.org/SourcesList#Example_sources.list) for examples on the official repositories.
3. Add this entry to ```sources.list```:     
    ```deb http://deb.debian.org/debian bookworm main```
4. ```sudo apt update```

## initial customizations
1. Add the following line to your `.bashrc` file:
  ```sh
  alias ll='ls --color=auto -lX'
  alias tree='tree --dirsfirst'
  ```
2. Launch a new terminal to apply this changes.

## mount
```/etc/fstab``` file (filesystem table) can help to automate the mounting tasks by defining
common mount points and the objective devices.
1. ```mkdir /media/usb```
2. ```fdisk -l```
3. Locate your drive. ```sd?``` will point to your drive, ```sd?n``` will point to your drive instance.
4. ```mount /dev/sd?n /media/usb```. Where ? is a letter (a, b, c) and ```n``` a number.
5. Check you mount points:
	```lsblk````

## fstab file
Edit this file to mount drives at startup
1. Open ```fstab``` file:
	```sudo vim /etc/fstab```
2. Get the drive's UUID:
	```sudo blkid```
3. Get the drive location
	```fdisk -l```
4. Add the following line. Note that this line follows the patter of the current defined mounting points.
	```UUID=109F14D1584B8AF4 /media/data ntfs-3g defaults      0       0```

If your files system is formated with NTFS, remember that the backend implementation was done with ```ntfs-3g```. If you launch your Windows OS you can get a detached state error since hibernation data can be stored in your system.

## openssh-server
0. ```apt update```
1. ```apt install openssh-server```
2. ```systemctl status ssh```
You can ```systemctl start|stop enable|disable```. The ```start|stop``` will work for current process, the another couple will enable or disable the process on system startup.

## Usage conventions
Put new software in ```/opt``` folder.


Installing Software
===============================================================================
Most of the time installing software consist in moving it to _opt_ folder and then adding the binaries to the _PATH_. But what _add to the PATH_ means?
Your system uses something called _environemnt variables_. Each particular value of these variables gives you a particular instance of your system environment (the collection of software). One of these variables is _PATH_. `PATH` stores all the filesystem path where your command line looks for comandline software.

1. Download binaries
2. Extract them into ```/opt```: 
    ```
    sudo mkdir -p /opt/app
    sudo tar -xJvf node-$VERSION-$DISTRO.tar.xz -C /opt/app
    ```
3. Then add this entry to your path in ```~/.profile``` file:
    ```
    export PATH=/usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin:$PATH
    ```
4. If you want that your app display an icon add an entry to ```/usr/share/applications/``` folders.
   The files already located there can help you to place your new definitions.

Windows 11 dual boot
===============================================================================
## GRUB fix
For Win11 the disk partition scheme must be UEFI-GPT. For this there is a dedicated partition that handles the boot. If you launch Windows when you already installed Debian, this can override your GRUB bootloader. To fix this, is only a matter to configure boot process from WinOS:
1. List your Win bootloaders: ```bcdedit```
2. Mount the ```EFI``` partition: ```mountvol X: \S```
3. Navigate ```X:``` volume and search for your debian boot files, in particular ```grubx64.efi```
4. Then, change the boot file:
    ```bcdedit {bootmgr} path \EFI\debian\grubx64.efi```
    
### Share data
1. Install the ntfs-3g driver. NTFS is from Microsoft this is a driver for linux.
2. Install GParted
3. Create a NTFS partition.
4. Point Downloads there and link your user folders there.
5. Add this drive to ```/etc/fstab``` to mount this drive on each start up automatically.

#### NOTES
Your edited ```fstab``` file that will automount your shared NTFS drive could trigger the ```ACPI BIOS ERROR (Bug)``` or ```broken ACPI BIOS``` error after you boot Windows and try to boot into Debian.
To fix that, try to remove the mount definition entry on your ```fstab``` file. 
Also you can approach this problem by remembering what was the last change you do to the system and then undo the changes.


Recommended Software
===============================================================================
### Software
- htop
- tree
- network-manager
    * nmcli: ```nmcli dev wifi connect ESSID password PASSWORD```
- ranger
- kolourpaint
- onboard (on screen keyboard)
- curl

PDF Tools
---------------------------------------
This tools will be pretty usefull for documentations tasks.
* `pdfinfo`: Returns pdf metada such as producer name (scanner name, software), number of pages etc.
* `pdfimages`: Extracts images from a PDF file. If you want to extract every image from `book.pdf` and store each image file with the filename `page-*` this command could help `pdfimages book.pdf out/page`.
* `libimage-exiftool-perl`: Edit PDF metadata such as display title or author.

`tesseract-ocr`
---------------------------------------
This software utility will detect text from an image. It is open source. If you want to use an specific language trained ML model under the hood you should download the training data from the official [repo](https://github.com/tesseract-ocr/tessdoc/blob/main/Data-Files.md#data-files-for-version-400-november-29-2016). Then place the files under `/usr/share/tesseract-ocr/4.00/tessdata` folder. For instance, after adding for the training data for _Deutsch_ language the folder should look like this:
```
    drwxr-xr-x 2 root root     4096 Jul  2 06:39 configs
=>  -rw-r--r-- 1 root root 20193615 Jul  2 06:55 deu.traineddata
    -rw-r--r-- 1 root root  4113088 Sep 15  2017 eng.traineddata
    -rw-r--r-- 1 root root 10562727 Sep 15  2017 osd.traineddata
    -rw-r--r-- 1 root root      572 Feb  4  2021 pdf.ttf
    drwxr-xr-x 2 root root     4096 Jul  2 06:39 tessconfigs
```
Here are a collection of useful commands. _PSM_ means _Page Segmenation Mode_.
* Output in the terminal the recognized text mantaining the format. Wow!
  ```sh
  tesseract wichtigeVerben-dat.png out -l deu --psm 11 pdf && pdftotext -layout out.pdf - >> wverb.txt
  ```
* Create a file named `out2.pdf` with selectable text
  ```sh
  tesseract wichtigeVerben-akkAndDat.png out2 -l deu --psm 11 pdf
  ```
* Output text preserving the spaces:
  ```sh
  tesseract wichtigeVerben-akkAndDat.png - -l deu --psm 6 -c preserve_interword_spaces=1
  ```

`rsync`
---------------------------------------
If you feel that `cp -rv` does not display enough information while you are copying folders using the terminal, `rsync` tool can help. This is tool is popular among GNU/Linux users according to my experience. Recalling the man pages: _This gives a bored user something to watch._
1. Download the utility `sudo apt install rsync`.
2. Open its man page: `man rsync`.
3. To copy from folder _A_ to folder _B_:
  ```
   rsync -r --info=progress2 /home/ ./homebk/
  ```
  - `-r`: recursive
  - `--info=progress2`: print overall progress
  
`wget`
---------------------------------------
Whit this command you can download a website recursively:
```
get --mirror -p --convert-links -P ./a6400man https://helpguide.sony.net/ilc/1810/v1/en/index.html
```
[source](https://askubuntu.com/questions/20463/how-can-i-download-an-entire-website)
  
Effortless system usage
===============================================================================
- openssl
```
  openssl genrsa -des -out ca.key 2048

  cat ca_ex.key | base64 -d | xxd
  cat ca_ex.key | base64 -d | od -t x1z

  cat ca_ex.key | base64 -d | xxd -p > key.hex

  cat /etc/*-release
```
- w
- hostname -I
- ip a
- modprobe

* Count words `wc`

* Getting help. `help` and `man` could provide some useful help.    
	```sh
	help -m set
	man grep
	```
	
* Softlinks (shortcuts). Crate a reference to the linked file. Access modifiers to the origin node will remain to the linkname reference.
  ```sh
  ln -s target/path/name linkname
  ```
    
* Partition management   
    ```sh
    lsblk
    ```
    ```blkid```
    ```sudo fdisk -l```
    ```sudo parted -l```
* User management commands
    ```getent group```   
    ```id```   
    ```getent group```   
    ```groups <username>```   
    ```sudo usermod -a -G vboxusers jcammmmm```
* List, sort by extension
    ```ls -lX```

* Open tty in GUI mode (F1 to F6)
    ```Ctrl Alt F2```
  to exit this tty:
    ```Ctrl Alt F7```
* Extract
    ```tar -xvf filename```
* Shutdown your system    
    ```sudo shutdown -h now```
* Search Text for ```pattern``` inside of your files    
    ```grep -rn 'folder' -e 'pattern'```
* Search Text for ```pattern``` inside of your PDF  files  
    ```pdfgrep -n fähr.*ab completebook.ocr.pdf```
    ```pdfgrep -n 'fä[[:alpha:][:punct:][:space:]]{,50}ab' completebook.ocr.pdf ```
    ```pdfgrep -n 'abgeflo[[:alpha:][:punct:][:space:]]{,20}' completebook.ocr.pdf```
 

* Search strings with tokens:
    ``` find . | grep "projectM.*\..*o" --color```
* Retrieve the libraries instaled on your current sytem   
    ```ldconfig -p | grep libname```
* GPU (`radeontop`) and CPU usage (`lm-sensors`)
    ```radeontop -c```
    ```sensors```
* Create bootable USB. Umount the target device partitions first, then copy iso contents.
    1. ```sudo umount /dev/sdb1```
    2. ```sudo dd bs=4M if=debian-live-11.7.0-amd64-kde+nonfree.iso of=/dev/sdb conv=fdatasync status=progress```
* Compare two files byte by byte:
	```cmp fileA fileB```
* Upgrade only one package. Use the same install command.
    ```sudo apt install <pkgname>```
* Save your command history
  ```history -a```

### Shortcuts
#### KDE
- ```Ctrl Q```: Close
- Maximize window
    ```Meta PgPrev```
- Move window half left  - right
    ```Meta Left``` or ```Meta Right```
- Move window by quarters. First install [Mudeer](https://github.com/darkstego/Mudeer/)
    ```Meta Z```, ```Meta X```, ```Meta C```, ```Meta V``` respectively for each quarter.
- Mouse mark. Delete mouse mark
    ```Meta Shift```
    ```Meta Shift F11```
- Open a new terminal
    ```Ctrl Alt T```

## Software management
* Querying your local software database:
  - `dpkg -l` list packages
  - `dpkg -L` list install location
  - `dpkg-query -L <package-name>`
- `dmesg` system logs
- `journalctl` 



Troubleshooting
===============================================================================
Brightness Keys does not work
--------------------------------------
Change the brighness by modifying a system file:
1. `cd /sys/class/backlight`
Because on each system could be different I recommend to cd into based on your case:
2. `cd /amdgpu_b10`
3. `sudo vim brightness`


(PipeWire Error) Screen Sharing Error
---------------------------------------
Install this software:
1. `sudo apt install pipewire`

Background noise
---------------------------------------
If your speakers have a noise every after you play something, the following command could help. This issue also happens in Apple MacBooks.
1. `pulseaudio -k`


Bluetooth Audio does not work
---------------------------------------
Pulseaudio needs aditional packages in order to emit audio through Bluetooth.
```
sudo apt install pulseaudio-module-bluetooth 
pulseaudio -k
pulseaudio --start
```
Change to the new Pipewire audio server
```
sudo apt install bluez-firmware
sudo systemctl status bluetooth
sudo systemctl start bluetooth
sudo apt install bluedevil
sudo apt remove pulseaudio-module-bluetooth 
sudo apt install libspa-0.2-bluetooth 
# restart computer
sudo systemctl start bluetooth
```
See for more [details][blutfix].

Restart KDE UI 
---------------------------------------
1. ```kquitapp5 plasmashell```
2. ```kstart5 plasmashell```

Read-only NTFS drive
---------------------------------------
If you are dual booting your system, this issue can be triggered because windows is creating hibernation files on your shared NTFS drive. To fix that only is required to run ```sudo ntfsfix \dev\sd??``` where ```sd??``` is your NTFS formatted drive.

Mouse speed
---------------------------------------
1. ```sudo apt install xinput```
2. ```xinput --list```: list input devices
3. ```xinput --list-props <devid>```
4. ```xinput --set-prop <devid> <prop> <newval>```

Per display scaling
---------------------------------------
1. List your monitors `xrandr --listmonitors`
2. Scale your screen `xrandr --output eDP --scale 1.0x1.0`
3. Scale your screen `xrandr --output eDP --scale 0.5x0.5`

Network is slow on wifi
---------------------------------------
Slow page load may be experienced this may be related to a driver issue since pages load fastly through cable, a simple restart could solve this issue.

1. Install `speedtest-cli`
2. `speedtest-cli --secure`

1. `ip a`
2. `ip link set enp4s0 down`
3. `ip link set enp4s0 up`

1. ```nmcli dev show```
2. ```nmcli dev disconnect wlp3s0```
3. ```nmcli dev wifi```

1. ```systemctl restart NetworkManager```

Missing firmware
---------------------------------------
In general, the process involves to look at Debian package repositories for the hardware brand and the kind of firmware do you need. This issues happens because most of this drivers are not _open source_.
While we are talking about firmware here, is important to note that a command that could help is ```sudo lspci -v```.

### Check
- ```lsmod``` List kernel modules
- ```lspci -v``` List drivers
- ```rmmod``` remove module
- ```modprobe``` load kernel module

### Download
#### Realtek drivers (wifi, ethernet, bluetooth)
The network drivers for both _Lenovo H520s_ and _HP G8 245_ can be found [here](https://packages.debian.org/bullseye/firmware-realtek)
#### Amd drivers (Radeon graphics)
The graphics drivers for both _Lenovo H520s_ and _HP G8 245_ can be found [here](https://packages.debian.org/bullseye/firmware-amd-graphics)

1. mount your drive with the ```.deb``` firmware packages
2. ```apt install firmware-????-????```


REFERENCES
=====================================================================
[blutfix]: https://wiki.debian.org/BluetoothUser/a2dp
