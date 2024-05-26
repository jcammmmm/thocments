Debugging C++
=====================================================================
> In this guide I will remember how to debug software written in C++.

Tools Install
=====================================================================
I use GDB to debug C++ programs. This utility came installed (it seems) when you install `g++` or `gcc`.

How to
=====================================================================
This is a debug session:
1. Compile with debug options: `-g`
2. Launch GDB with your programm: `gdb yourapp`
3. Within GDB add breakpoints: `b filename.c:n`
4. Find where are you located, this give you the line number: `frame`
5. List source code around that line: `list n`.
6. Step (go into), next (skip call), finish (go to caller): `s`, `n`, `f`.
7. Where, print the call stack: `where`.

In order to debug an executable this must compiled with debug flags and as thumbrule without optimizations: ```gcc src -g -O0```.
If your executable is being built with CMake set the following config var ```-DCMAKE_BUILD_TYPE=Debug``` (Normal builds are triggered by setting this var to ```Release```.

## Check
You can check if your executable contains debug information by running ```readelf -w <executablename>```

## Notes
By default gdb will read the current executable folder for the source files listing. If you launch gdb by specifying the executable with a path then the listing will not work.

## Commands
* Set a break point in `filename.c` and line number `x`
    ```(gdb) b filename.c:x```
* Set a break point in `filename.c` and line number `x`
    ```(gdb) b filename.c:methodname```
* List all breakpoints
    ```(gdb) info b```
    ```(gdb) i b```
* List current stack frame
		```f```
		```frame```
* List source code
		```l```
		```list```
* Show current stacktrace, for this the program must be paused (Ctrl C or break)
		```bt```
    ```backtrace```
    ```where```
* Remove (disable) break point. First get the breakpoint id then disable that id:
		```d <id>```
    ```disable <id>```
* How to use ```command```
    ```(gdb) help command```
* If you do not remember ```comm``` name:
    ```(gdb) apropos name```
    
TUI
=====================================================================
Review how to use another window.
More info [here](https://sourceware.org/gdb/current/onlinedocs/gdb.html/TUI.html)

Shared Libraries
=====================================================================
When you are debugging complex applications, you work with several dependencies.
Sometimes, after you reproduce everything you get unment dependencies. To debug
that the following commands are useful:
* List shared object dependencies. When your library is not found, the output shows `somelib => not found`.
  ```ldd executable```
* Verify that the shared library exists in your local repo of libraries:
  ```
  ll /usr/local | grep lib 
  ```





Useful resources
=====================================================================
[1](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)
[2](https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf) (TODO)
[3](https://bytes.usc.edu/cs104/wiki/gdb/)
    


