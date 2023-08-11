Purpose
=================================================
In order to make explicit the significant role of _Hibernate_, in this guide I will run the examples provided in the [user guide](https://docs.jboss.org/hibernate/orm/6.2/userguide/html_single/Hibernate_User_Guide.html). The big difference of this guide from others is that I ran _Hibernate_ as terminal application and as a standalone library without mixing it with other frameworks. If you run the offcial examples that came with the [Getting Started](https://docs.jboss.org/hibernate/orm/6.2/quickstart/html_single/) you can get confused since the minimal examples are being executed on top of the _JUnit_ testing framework.

A minimal example
===========================================================
The minimal example was taken from the Getting Started guide. In this [guide](../java-why-maven/main.md) you can see how I obtained the minimal example. The minimal example is located at `src` folder. The source code provided in the official guide was modified to reflect our proposed changes.

Dependencies
---------------------------------------
The dependencies needed to get this application running are the following:

- `hibernate-core-6.0.0.CR2.jar`
- `jakarta.persistence-api-3.0.0.jar`
- `jakarta.transaction-api-2.0.0.jar`
- `jboss-logging-3.4.3.Final.jar`
- `jandex-2.4.2.Final.jar`
- `classmate-1.5.1.jar`
- `hibernate-commons-annotations-6.0.0.CR1.jar`
- `byte-buddy-1.12.7.jar`
- `jakarta.activation-api-2.0.1.jar`
- `jakarta.xml.bind-api-3.0.1.jar`
- `jakarta.activation-2.0.1.jar`
- `jaxb-runtime-3.0.2.jar`
- `jaxb-core-3.0.2.jar`
- `txw2-3.0.2.jar`
- `istack-commons-runtime-4.0.1.jar`
- `jakarta.inject-api-2.0.0.jar`
- `antlr4-runtime-4.9.1.jar`
- `slf4j-simple-1.7.5.jar`
- `slf4j-api-1.7.5.jar`
- `junit-4.13.2.jar`
- `hamcrest-core-1.3.jar`
- `h2-1.4.197.jar`

ORM mappings
---------------------------------------
In order to use Hibernate you should describe the ORM mappings and the database connection details. These files are located in the `target` folder. These files were put there in order the runtime _Class Loader_ picks them by default:
- `hibernate.cfg.xml`
- `Event.hbm.xml`

Argument files
---------------------------------------
I use _argument files_ to compile and run the application. The arguments provided there should be modified according to where you downloaded the _jar_ files.
- `opt.arg`
- `opt.argc`
- `cls.argc`

Compile and run
---------------------------------------
To compile the application execute:  
```sh
javac @argc
```

To run the application execute:  
```sh
cd target && java @../arg
```

Debugging
---------------------------------------
1. Start the server:  
```sh
cd target && java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=9393 @../opt.arg
```
2. Open another terminal emulator and connect to the debugging session:  
```sh
jdb -attach 9393 -sourcepath /home/jcammmmm/repo.m/thocments/java-hibernate/src
```
3. Sample commands when you are in a debugging session
```
stop at NativeApiIllustrationTest:51
```