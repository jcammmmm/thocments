Android Backups
===========================================================
> How to install and use effortlessly the ADB (Android Debug bridge) to perform your backups.

Accessing your phone with CLI
============================================================
Since we need only the `adb` tool, we proceed by downloading the tool set [here](https://developer.android.com/studio/releases/platform-tools). The official [documentation](https://developer.android.com/tools/adb) offers a clear description.

Basically the process now (2024-05) is:
1. Download standalone ADB tools.
2. Add that tools to your PATH environment variable.
3. Configure your phone:
  - Enable developer mode by touching the version of your OS
  - Go developer options an enable the wireless debugging option.
  - After this you will get your local IP address and a port.
4. Pair your device `adb pair 192.168.0.1:93934`
5. Now run `adb connect 192.168.0.1:93934`
6. If your device does not show, restart the computer.
7. Now you can throw commands to your phone with `adb shell`, for instance: `adb shell ls -l /storage/emulated/0/DCIM/Camera | wc -l` 

Backing up your photos
===========================================================
1. Compute digests for each file in your `DCIM` folder.
   `adb shell sha1sum /storage/emulated/0/DCIM/Camera/* > src.sha256sum`
   Or more easyly, start a shell session and navigate to the folder:
   ```
   $ adb shell
   $ cd /storage/emulated/0/DCIM/Camera/                         
   $ sha256sum * > src.sha256sum
   ```
2. Copy all the contents of `Camera` folder to another device.
3. Compute digests for the copied photos.
4. Compare the output digests.
   `vimdiff src.sha256sum ~/dst.sha256sum`
   Attached to this post you will find the output of this command.
5. If digests are equals, you can remove the photos from your phone. 
 
