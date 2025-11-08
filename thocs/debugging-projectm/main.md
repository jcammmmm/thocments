INTRO
===========================================================
> This journey begins almost 6 years ago, when I started to use GNU/Linux and opensource software. I found this application as the default visualizer for Clementine audio player. And since then was one of my personal backlog projects to open the source code and put some efforts to understand it.

INSTALL CMAKE
===========================================================
The portable version zip was [choosen][cmakeportable].
Keep [care][cmakeinfo] setting up the CMAKE_ROOT variable 
This variable should point where you extracted CMake binaries.

Install GLEW (OpenGL Extension Wrangler Library)
------------------------------------------------
Download the library from [here][glewdownload].   
After trying to build, you may notice an error related to GLEW GLEW is a library that lets you to interface OpenGL.
The nextion will explain what is glew.

GLEW
------------------------------------------------
Glew is an static library that helps to recognize the OpenGL version and features on the target platform. GLEW can be obtained from here:
https://glew.sourceforge.net/index.html
And the install instructions here:
https://glew.sourceforge.net/install.html

After reading more docs on projectM the recommended and easy way to install GLEW is throught vcpkg

### vcpkg
`vcpkg` is a C/C++ library manager on WinOS, MacOS and Linux. A quick start guide can be found here:
https://vcpkg.io/en/getting-started.html

Then run ```vcpkg install glew sdl2```


BUILDING
===========================================================
Before building it is important to note that _ProjectM_ perse is a library. If you want to actually run the visualizations you should write the graphical application. The project references a couple of projects where you can pick up a demo implemenation. 

1. `git clone https://github.com/projectM-visualizer/frontend-sdl2`
2. `git clone https://github.com/projectM-visualizer/projectm.git`
3. `git clone https://github.com/pocoproject/poco/tree/poco-1.13.3-release`
4. Compile _ProjectM_. Follow the readme file. Be aware that your projectm library will be installed in `/usr/local` folder.
5. Compile and install _POCO_ library.
    1. `mkdir cmake-build && cd cmake-build`
    2. `cmake ..`
    3. `cmake --build . --target install`
6. Compile the _frontend_.   
    1. `cmake -S . -B cmake-build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local`
    2. `cmake --build cmake-build --config Release`
5. Run the system:
    `LD_LIBRARY_PATH=/usr/local/lib ./cmake-build/src/projectMSDL --presetPath ../projectm/presets-cream-of-the-crop/ --texturePath ../projectm/presets-milkdrop-texture-pack/`. The first of this command configures the lookup of the linker so it can find our POCO library that causes some problems.

HISTORY
===========================================================
### 240614
Today I found that in cmake build folder you can find a file called install_manifiest.txt. Since this is a maniefiest file, here you find the list of files that are being installed on the system. I pass this file through `xargs` to the `rm` command and I removed the poco library. Again I want to replicate the build error from last time in order to understand and debug the C++ build process.

### 240611
The last time I tried to work on this I was looking how to create a sandboxed environment in order to build the software more clearly on each build. I did not get anything similar to `virtualenv` in Python


### 240525
Now I will execute the code and try to run again. There is one task and it is to review the github page where some explained why the application did not run. I remember that that was not the case for me beacuase was the troubleshooting for another library. I just remembered what it was.   
From previous time I was troubling with the POCO library. It happens that after a year without reviewing this, now the developer changed the library requirements. Now the version 3.9 is being used. Happens that such library is not available from the apt repository for debian. I have had to compiled and run. But happened that beacuase the default installation location I must to indicate to the `ld` command where to look for these new library resources. This is the [link][pocolibdicuss] of the discussion.   
The efforts will be focused for now in to understand the frontend. This is an interesting project to work, that lets to understand easily how the toolchain works in C++.

### 2405??
Log begins. But remembering what I had done previously was to compile and install the library in `/usr/local` folder. Then compiled the frontend written in sdle and also install it in `/usr/local`.   
From the previous time I remember that I was trying to run projectm without the provided app that implements it throught SDL2; that is, running the application with GLEW. After that I found that it is easier and I could learn more if I try the example application. That is what I'm doing now.
  

REFERENCES

[cmakeportable]: https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-windows-x86_64.zip
[cmakeinfo]: https://cmake.org/cmake/help/latest/variable/CMAKE_ROOT.html
[glewdownload]: https://github.com/nigels-com/glew#downloads
[pocolibdicuss]: https://github.com/pocoproject/poco/issues/2543
