C++ Grammar and ecosystem information
=====================================================================
> In this document I plan to add any relevant information that was not clear to me at the moment to work with this technology. I found through this process (7 years) that the technology around this languages in some cases is over documented and takes a lot of time to grasp the concepts. Since I understand object oriented programming with Java, some of the concepts are portrayed by making comparisons with Java technology.

Single-header libraries
=====================================================================
Is a library that it is contained in a single file [](1), contrary to that you will find out there, libraries are composed of serveral files and because of that you will need in the end some external tool in order to link that library (now dependency) to your proyect. Since this libraries come in a single file they are easy to manage.
We recommend to read the readme that comes with _stb_ a well now single header library for C/C++.

`inline`
=====================================================================
This specifier will tell the compiler to replace the code implementation in each function call. This has the advantage to reduce the function call overhead in those functions that are short and frequently called for instance, getters and setters. Those benefits are lost when you define `inline` to functions that have large bodies.

Errors
=====================================================================

Header errors
---------------------------------------
If the `g++` compiler has a first line similar to the following, it could indicate a circular or inconsistent import loop.

```
In file included from hittable.h:4,
                 from renderer.h:7,
                 from vec3.h:6,
                 from color.h:6,
                 from main.cpp:3:
```

Const reference function args
=====================================================================
https://stackoverflow.com/questions/3967177/when-to-use-const-and-const-reference-in-function-args

Virtual function
=====================================================================
The similar concept in Java is _abstract methods_ in _abstract classes_. Virtual functions are functions meant to be implemented in derived classes. 

As you can see is a extrange syntax. Here is the comments about its creator:
_"The curious =0 syntax was chosen ... because at the time I saw no chance of getting a new keyword accepted."_


Pure virtual function `virtual f() const = 0`
=====================================================================
The similar concept in Java is _abstract methods_ in _interfaces_, since you cannot provide an implementation on an interface, at least you are using `default`.

References
=====================================================================
[1](https://github.com/nothings/stb#how-do-i-use-these-libraries)
