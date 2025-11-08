How development works in C/CPP world
====================================================================
> Here you will find some hacks to join the interesting world of software development in
C/C++

Conventions to follow
====================================================================

Compilation
---------------------------------
Most of C/C++ projects compiles this way:
  1. Configuring: The script that checks if the environment has the dependencies to build and install the software.
     Also here you declare the path were your executable will be dropped:
     
        ./configure --prefix=/output/folder

  2. Run the make script to execute the default actions: build and install

        make

  3. Go and look for your executable

        cd /output/folder
        ./exec-name

Missing Dependencies
---------------------------------
C/C++ relies on `/usr/bin` system folders to look for header files and libraries. Most of the time you will have missing 
dependencies. You can install them by following this convention:

    lib<name>-dev

Some examples of this:

- `libgd-dev`: When building `libanalogtv`.
- `libpq-dev`: When using some postgres database client.

Projects that follow the Conventions
====================================================================
- [diffutils](https://www.gnu.org/software/diffutils/): The default diff checker in GNU/Linux
- [XScreenSaver](https://www.jwz.org/xscreensaver/download.html): Why not to see amazing computer graphics?



Tracking log
====================================================================
### 250520
This is the first time trying to work with php technology

References
====================================================================
