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

Downloading sources
=================================================
The purpose of this guides is to perform certain tasks by hand in order to understand what the build tool does to get your complex application running.

Download by hand
---------------------------------------
If you want to step and display the code that it is currently executed, you must download the sources.

1. Go to _MVN Repository_ [mvnrepository.com/](https://mvnrepository.com/)
2. Search your package, for example [Hibernate ORM Hibernate Core.](https://mvnrepository.com/artifact/org.hibernate.orm/hibernate-core)
3. Select your version, for example [v6.2.0.Final.](https://mvnrepository.com/artifact/org.hibernate.orm/hibernate-core/6.2.0.Final)
4. List all the files after click the [view all](https://repo1.maven.org/maven2/org/hibernate/orm/hibernate-core/6.2.0.Final/) link.
5. Download the _jar_ named [hibernate-core-6.2.0.Final-sources.jar](https://repo1.maven.org/maven2/org/hibernate/orm/hibernate-core/6.2.0.Final/hibernate-core-6.2.0.Final-sources.jar)

Download by in batch
---------------------------------------
If the project is currently managed with maven you can save time by downloading the source for each of your dependencies with this command:
```
mvn eclipse:eclipse -DdownloadSources=true
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

Argfiles
=================================================
Argument files can be used when you invoque the _JVM_ in debugging mode.

