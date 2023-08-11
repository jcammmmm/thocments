A quick debugging guide for Java
=================================================
In order to debug a Java application you must start the JVM (_Java Virtual Machine_) in debugging mode (_step 1_). After that, your JVM will become a server to which you must to connect to. Finally, to debug your application you must connect to this server with the _JDB_ client, a piece of software that comes with your _JDK_ (_Java Development Kit_) distribution (_step 2_).

Step 1
---------------------------------------
With the following command you can configure the JVM debugging port `address=port` and if the application shall stop before the `main(String... args)` method with the `suspend=y` attribute.
```sh
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=9393 MyClass
```

Step 2
---------------------------------------
Begin a debugging session. To do so connect to the debugging server with the 
_JDB_ client. The `-attach` attibute will specify the url, in this case we only provide the port. The `-sourcepath` will indicate where to look for Java source file in order to display the line by line debugging, each folder must be separated with colons `:`
```sh
jdb -attach 9393 -sourcepath /home/jcammmmm/repo.o/tomcat/test:/home/jcammmmm/repo.o/tomcat/java
```

Commands
=================================================
* `help`: will display all available commands.
* `run`: run the _main_ method from the main class. (start the application).
* `stop classname:line`: set a brekpoint.
* `step`: execute current line.
* `step up`: execute all the code until return to its parent caller.
* `next`: execute current line, stepping over calls
* `where`: display the call stack.
* `dump`, `eval`: print variables
