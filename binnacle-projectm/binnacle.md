# Intro
This journey begins almost 6 years ago, when I started to use GNU/Linux and
opensource software. I found this application as the default visualizer for Clementine audio player. And since then was one of my personal backlog projects to open the source code and put some efforts to understand it.

# Install CMake
The portable version zip was choosen
https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-windows-x86_64.zip

Keep care setting up the CMAKE_ROOT variable
https://cmake.org/cmake/help/latest/variable/CMAKE_ROOT.html
This variable should point where you extracted CMake binaries.

## Install GLEW (OpenGL Extension Wrangler Library)
https://github.com/nigels-com/glew#downloads

After trying to build, you may notice an error related to GLEW. GLEW is a library that lets you to interface OpenGL.

But what is GLEW

### GLEW
Glew is an static library that helps to recognize the OpenGL version and features on the target platform. GLEW can be obtained from here:
https://glew.sourceforge.net/index.html
And the install instructions here:
https://glew.sourceforge.net/install.html

After reading more docs on projectM the recommended and easy way to install GLEW is throught vcpkg

### vcpkg
```vcpkg``` is a C/C++ library manager on WinOS, MacOS and Linux. A quick start guide can be found here:
https://vcpkg.io/en/getting-started.html

Then run ```vcpkg install glew sdl2```

### 


