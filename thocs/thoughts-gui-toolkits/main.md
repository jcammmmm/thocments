A review to GUI Toolkits (August 2024)
====================================================================
> A summary of my review of Desktop GUI Toolkits on the night of 31th August 2024.


Observations
====================================================================
- If you want something that looks native you need to go definitively with Qt. But the cost is that at the beggining the licensing seems scary.
- You election will depend on the language. And many trade offs. 

Tradeoffs
=====================================================================
T0: Do you really want a desktop application?
T1: Dependency management is easy?
T2: Is Desktop Crossplatform (GNULinux/Windows/MacOS)?
T4: Is the language easy to work with?
T3: Learning curve of the toolkit/framework?
T4: Licensing. Which is the licensing mode?
T5: Do you want to freeze your application?
T6: Do you want to learn something new?


T0: Desktop Applications
--------------------------------
Technology had advanced very quickly and in interestings forms. Nowadays from my experience in distribuited backends, seems that GUIs are being relegated to web browsers and HTTP technology. I do not know if the same happens in Desktop applications.
When you see this objectively, you will find that the split is good and both benefitial to backends andfront ends. The logic is made with any language in the cloud while the presentation is made with HTML documents or mobile applications. That is really good. So good that we have beatifully made frontend frameworks such as React, MaterialUI or Bootstrap. In fact, the most used code editor (vscode) runs in a web browser!
So, you really need a desktop application?


T1: Dependency Management
--------------------------------
### C++
If you plan to work with C++ you will need to work with CMake, if you want crossplatform support, and CMake is not easy. Yes, many great applications are built with CMake but that requires time.

### Java
Java and maven is the best pick for me. Gradle, requires to understand groovy if you want to feel confident with your build box, and that also takes time.


T2: Crosplatform
-------------------------------
C++ with CMake is crossplatform and Java is platform so there is nothing more to add here. 


T3: Language easeness
-------------------------------
As everything is a trade off, do you need speed in you application, that means, do you need that you form UI will be fast? I mean, do you really need your UI in C++. In my opion yes I want to try other kinds of technology.


T4: Licensing
-------------------------------
It's time to contribute to open source communities, so any one can benefit for it!


T5: Freeze
-------------------------------
Web based UI are subject to attacks of the most used protocol HTTP. You need to update constantly. If you only use plain SSH for you connections, you wont need to update constantly it seems. I feel C++ has more points here.


T6: Yes.
-------------------------------

Other Aspects to consider
====================================================================

Desktop Application
-------------------------------
If your application will run in a desktop computer, why will you bother with all the stuff surrounding web application, i.e. all web security etc.
Then you may think, hey it could be fine to have native appeareance, then you need to work with C++. In C++ you have two options Qt or wxWidgets. Both are hard to package if you do not have experience with C++ developement. Here appear the Java alternatives, packaging java is more easy. Then you may think, I want to create this so in the future I can use another technology to build the UI.
To make that design you need to create some kind of local server.



Conclusions
====================================================================
- If you want something that looks native you need to go definitively with Qt. But the cost is that at the beggining


Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
