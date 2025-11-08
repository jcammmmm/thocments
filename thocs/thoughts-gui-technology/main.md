Thoghts on how GUI Software Development almost workds
====================================================================
> These days I was researching on which is the best techonology to develop desktop graphical user interfaces. I found that you will end editing labeled document, most of the time linked to your IDE. We dislike the idea because, we think that you should only need an editor text to develop thesoftware.

Review Over the technologies
====================================================================

Android
---------------------------------
Now, they are selling develop programmatically with Kotlin, but in the past, and I expect in current codebases, the UI programming was made with the help of XML files

Java
---------------------------------
For GUI it seems that you need to use the Eclipse IDE, the description is made also with XML files.

C++
---------------------------------
With Qt it seems that the UI programming is made with the assistance of the Qt IDE, there you need to use XML to describe your UI.

JavaScript
---------------------------------
Yes HTML, this is XML.

Python
---------------------------------
I donot, but a good reference is the UI that comes by default with git.

Current Trends
====================================================================
When you look at software currently used by the majority of people you see that the folowing applications are made with JavaScript, that is, they were made as web applications:
- Spotify: Why? because the web and desktop app are the same. I donot know if mobile is also made with JS.
- Visual Studio Code: Its made with TypeScript and runs on chromium.
- MS Teams, MS Office 365
- Google Sheets, Docs and Slides
- Youtube
- Redit: Some parts where made with react native
- Whatsapp Desktop: is a PWA from the web version

Final Sad Comments!
----------------------------------
After a very good amount of hours trying to look for the best technology, I found that there is no a silver bullet to do this. At the end of this journey I thought, well I learn react and Javascript and make the app, but how the heck will bundle that as an application? Then I look into ReactNative. I was happy with the idea to use my text editor and my terminal, but the problem is that I need to install Android Studio as well, and I was avoiding this from the beginning! So, it seems that there is no simple work around for this, or I write the software Kotlin 100% or write the software with react native 100% with JS. 

Then two classic options appeared, Cordova and Google Bubblewrap. I read some comments out there and the app is running in a webview, and trying to access the camera and other things that probably I will need in the future like the microphone or the ability to call some native interface (graphics card) will move the balance to write the application native in Kotlin again, because I will need to use a extrange workaround to fill this gaps that I initialize skip because I only want an app avoiding all the native stuff. 


Other
====================================================================
To build and image from a Container file description (_Dockerfile_):
1. Clone this repository `https://github.com/31z4/zookeeper-docker`
2. Go to `3.9.1` or your desired version.
3. Then throw `sudo podman build -t zookeeper:3.9.1 .` in the console.
4. Voila! your image was build.

other
p---------------------------------
This [documentation][1] 


Other
====================================================================

Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

### 250123
Edits

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
