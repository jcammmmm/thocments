Intro
===========================================================
In this text I will describe my journey trying to debug one of the most used web server software in the world [Apache Tomcat](https://tomcat.apache.org/). Beyond of being one of the most used web server software, it also implements several of the tools that makes part of the Jakarta EE (previously Java 2E) ecosystem. 
First I will clone the main project repository hosted publicly on GitHub. Then I will read the build documentation and run some of the tests. After that I will try to find how the webserver manages the internal Servlet and how this web server manages concurrency, on of the topics that interests me the most.
So let's go and start this short journey. For now I expect to invest all the day on this. In the following series of articles I will disect SpringBoot base servlet and show how integrates with tomcat.


Environment Setup
===========================================================
Tomcat is developed with Java techonology so having a JDK installed is mandatory. I opt to install OpenJDK from [here](https://packages.debian.org/bullseye/default-jre).


Cloning
===========================================================
For this I will clone the project from its public mirror on [GitHub](https://github.com/apache/tomcat). When you read the documentation you will reach serveral repositories, but most of them are addon feature software added to _Tomcat_ software core.

1. Clone the repository:
    ```sh
    git clone https://github.com/apache/tomcat
    ```
    
Building
===========================================================
The main file that contains the building steps is `BUILDING.txt`. Note that markdown or some more broader documentation style is used in apache tomcat, this let see us how old is the project, or at least the style of the people that leads the project. In this file you will encounter several values enclosed between `@` symbols. These values are defined in `build.xml` its inner values are taken from `build.properties.default`.

The build system employed is [Apache Ant](https://ant.apache.org/) version `1.10.2`. Such version was downloaded from [here](https://archive.apache.org/dist/ant/binaries/). 

The developers recomend to override some of the configurations found in `build.properties.default` in file called `build.properties`. This file will be placed at the seme level that `build.properties.default`. Ant should be available from the `PATH` environment variable so there is no need to modify the `build.properties` config file. The install steps of Ant are as usuall: download, extract and point append the installation path to the `PATH` environment variable.

To build the project is only need to run the command `ant` in the terminal when you are located at the root of the source code repository. When executed this a redirect error appeared. There was invalid the redirect from the legacy HTTP dependency to the new HTTPS. To avoid wasting time on this, I downloaded the redirected dependency `ecj-4.20` to a folder where the project dependencies are being dowloaded following the pattern that previously dowloaded dependencies followed. After that the project got built sucessfully.

The build logs can be found with this document [here](build.log) **TODO**: Write an analysis of the build after reading the build logs.

Compared to another software such as corporative software that I have been written, and the other source I have read (Blender or projectm) Apache Tomcat is pretty easy to setup and build. In fact the documentation says that if you want to update the fully functional executable, is only need to update the repository with git and run the Ant builder again.

Note that there are several types of build. The text written above comments about an standar `deploy` build. If you want for example to build the documentation or a debug build you should try the approach commented below.


Running
===========================================================
I always used Tomcat as an embedded webserver for microservices and also as already setted up software for running the applications that I wrote. For that reason I will provide here details on how you can run an standole webserver based on Tomcat.

The `RUNNING.txt` file comments that is needed to setup the `CATALINA_HOME` environment variable to point the root folder that contains the Apache Tomcat executables (Section 2. Note b) at the end). So after building our webserver software I will point this variable to `/home/jcammmmm/repo.o/tomcat/output/build`.

A recurrent trick here is running `source ~/.profile` each time that you create a new global environment variable in `.profile` file. After that issue `$CATALINA_HOME/bin/startup.sh` in your terminal and the webserver will start up ![img](./pic1-webserverup). 

To stop the webserver issue a `%CATALINA_HOME%\bin\catalina.bat stop` and you will be done.

Running Tomcat JUnit Tests
===========================================================
Following the documentation, you must specify the test cases to run in the `build.properties` file. For example:
    ```properties
    test.entry=org.apache.catalina.util.TestServerInfo
    ```
and then running Ant in test mode.
    ```sh
    ant test
    ```
    
After hitting enter the logs will display that new dependencies are being downloaded. Also the logs show that three sets of tests were executed: nio, nio2 and apr; the Tomcat connectors. A connector is a piece of software that lets Catalina behave as a standole webserver and also execute servelts, in fact this software is the component that actually listens the TCP connections.
The output results of this unit test are output to `output/build/bin`.

Analysis Expression Lang Test
---------------------------------------
The unitest for `org.apache.el.lang.TestELArithmetic` basically test the code that performs the arithmetic on _expression language_, the imperative code that can be embedded on XML templates that represents server side UIs. For example, tests how the code handles `null` operators, big integer quantities, empty string operators, dot-without-zero notation and a bug `47371`.

Analysis of Max Connections test
---------------------------------------
With this test is easy to see that at this level is Apache Tomat who provides the concurrency handling on the server, not the server. I expect that this idea will develop better below and when springboot will be debugged. 
When I think of concurrency I'm thinking about how several HTTP requests are performed in parallel; session concurrency i.e. serveral clients talking with the server is handled with cookies since HTTP is a stateless protocol.
Up to now the `build.properties` file looks like this:
    ```
    base.path=/home/jcammmmm/Downloads/tomcat-build-libs
    test.entry=org.apache.catalina.connector.TestMaxConnections
    # test.entry.methods=testMultiply01,testMultiply02
    ```
The log output revealed that the max connections test failed 2 test for the `apr` connector. Trying to understand the error I got how the Tomcat-Servlet relationship is forged.

Many servlets per connector?
---------------------------------------
While debugging I found that when the connector is defined in the tomcat instance one attribute on its definition is the number of threads. Up to here we have that one Tomcat has many connectors, but the question now is, each conector has one servlet instance. My guess is that for each connector you would have one servlet. To reach there I need to find how the connector passes the request to the servlet.

While I was reviewing how can I debug the test cases, I found that this project uses JaCoCo to produce coverage reports for the unit tests. So in further sections I will try to find the html output of those reports.

From `build.properties` the property `compile.debug`controls if `javac` should output debug binaries. Compared with C/C++ in java we need to generate debug information when the compilation is made. This configuration is made in the `javac` ant [task](https://ant.apache.org/manual/Tasks/javac.html).

I do not like to get bogged down when you can do the stuff directly without putting over and over other abstraction layers, such as for example an IDE and the pluggins required to do debugging or code inspection. For instance, now I am using Visual Studio code without any linters or Java language processors, I think that only for this quest the search-in-all-files utility and being able to run the code is sufficient.

JDB
---------------------------------------
Running an standalone application in debug mode is in some extend easy once you want to debug the unit tests. After reading some posts here and [there](https://stackoverflow.com/questions/13680257/trying-to-run-ant-junit-target-in-debug-mode-in-eclipse) the trick to begin a debuging session with `jdb` is to run those test in a new JVM, then the trick is to get attached to that process. To achieve that, when you build box is Ant, you should fork your `JUnit` Ant task. Fortunatelly, when the `runtest` task is defined in the `build.xml` file the configure this needed fork:
```xml
  ...
  <macrodef name="runtests"
            description="Runs the unit tests using the specified connector.
              Does not stop on errors, but sets 'test.result.error' and 'test.result.failure' properties.">
    ...
    <sequential>
        ...
        <junit printsummary="yes" fork="yes" dir="." showoutput="${test.verbose}"
          errorproperty="test.result.error"
          failureproperty="test.result.failure"
          haltonfailure="${test.haltonfailure}"
          threads="${test.threads}">
    ...
        </junit>
    </sequential>
  </macrodef>
```
As you can see the `forkmode` attribute is not configured, so the defaut behavior is to launch a new JVM instance per test. Having that set up I will launch again the Tomcat webserver and see what changes on my process manager. Due to the test takes time I was able to take the following screenshot that shows that a new process was created to run the new set of `test-nio2` test when `tert-nio` was completed.

To attach to this newly created JVM I will add a couple of configurations to the `junit` task listed above by adding a couple of nested `jvmarg` [tags](https://ant.apache.org/manual/Tasks/junit.html). In order to attach JDB to a running JVM, this JVM should be start with a couple of paramaters that are described [here](https://docs.oracle.com/en/java/javase/11/tools/jdb.html):
```sh
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=9393 MyClass
```
Now the application logs display this new line:
```log
[junit] Listening for transport dt_socket at address: 54659
```
And after trying to attach to that port, this is the result:
```log
jcammmmmm@laptop: jdb -attach 9939
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
Initializing jdb ...
> 
The application exited
```

The trick here may to put a breakpoint on the `TestMaxConnections` class, and wait to the debugger to stay there. After visiting this awesome [slides](https://people.apache.org/~csutherl/ApacheCon%20NA%202019/Tips%20for%20Debugging%20Tomcat%20and%20Web%20Applications%20(2019).pdf), I see that the programmer set the `JPDA_SUSPEND` script variable to `y`. After following the core script `catalina.sh` I found that this variable is modifying the `agentlib` argument that is being passed to the JVM in order to be debuggeable. Then, the updated and working attribute added to the `build.xml` file looks like this:
```xml
    <junit printsummary="yes" fork="yes" dir="." showoutput="${test.verbose}"
          errorproperty="test.result.error"
          failureproperty="test.result.failure"
          haltonfailure="${test.haltonfailure}"
          threads="${test.threads}">
      ...
      <jvmarg value="-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=9939"/>
      ...
    </junit>

```
Please note in this listing the the `suspend` attrib being set to `y` and the port configured through the `address` attribute. 
After playing a couple of minutes with the debugger I found that in order to put a breakpoint you should specify the fully qualified name of the class, in our case `org.apache.catalina.connector.TestMaxConnections` in order to be able to step through that code:
```jdb
stop in org.apache.catalina.connector.TestMaxConnections.testConnector()
cont
```

After issuing a `where` command within the JDB session this is the output:

```jdb
main[1] where
  [1] org.apache.catalina.connector.TestMaxConnections.testConnector (TestMaxConnections.java:49)
  [2] jdk.internal.reflect.NativeMethodAccessorImpl.invoke0 (native method)
  [3] jdk.internal.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)
  [4] jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
  [5] java.lang.reflect.Method.invoke (Method.java:566)
  [6] org.junit.runners.model.FrameworkMethod$1.runReflectiveCall (FrameworkMethod.java:59)
  [7] org.junit.internal.runners.model.ReflectiveCallable.run (ReflectiveCallable.java:12)
  [8] org.junit.runners.model.FrameworkMethod.invokeExplosively (FrameworkMethod.java:56)
  [9] org.junit.internal.runners.statements.InvokeMethod.evaluate (InvokeMethod.java:17)
  [10] org.junit.internal.runners.statements.RunBefores.evaluate (RunBefores.java:26)
  [11] org.junit.internal.runners.statements.RunAfters.evaluate (RunAfters.java:27)
  [12] org.junit.rules.TestWatcher$1.evaluate (TestWatcher.java:61)
  [13] org.junit.runners.ParentRunner$3.evaluate (ParentRunner.java:306)
  [14] org.junit.runners.BlockJUnit4ClassRunner$1.evaluate (BlockJUnit4ClassRunner.java:100)
  [15] org.junit.runners.ParentRunner.runLeaf (ParentRunner.java:366)
  [16] org.junit.runners.BlockJUnit4ClassRunner.runChild (BlockJUnit4ClassRunner.java:103)
  [17] org.junit.runners.BlockJUnit4ClassRunner.runChild (BlockJUnit4ClassRunner.java:63)
  [18] org.junit.runners.ParentRunner$4.run (ParentRunner.java:331)
  [19] org.junit.runners.ParentRunner$1.schedule (ParentRunner.java:79)
  [20] org.junit.runners.ParentRunner.runChildren (ParentRunner.java:329)
  [21] org.junit.runners.ParentRunner.access$100 (ParentRunner.java:66)
  [22] org.junit.runners.ParentRunner$2.evaluate (ParentRunner.java:293)
  [23] org.junit.internal.runners.statements.RunBefores.evaluate (RunBefores.java:26)
  [24] org.junit.internal.runners.statements.RunAfters.evaluate (RunAfters.java:27)
  [25] org.junit.runners.ParentRunner$3.evaluate (ParentRunner.java:306)
  [26] org.junit.runners.ParentRunner.run (ParentRunner.java:413)
  [27] junit.framework.JUnit4TestAdapter.run (JUnit4TestAdapter.java:50)
  [28] org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner.run (JUnitTestRunner.java:536)
  [29] org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner.launch (JUnitTestRunner.java:1,205)
  [30] org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner.main (JUnitTestRunner.java:1,048)
```

When I try to navigate through the code this is the output:
```jdb
main[1] list
Source file not found: TestMaxConnections.java
```

By adding `-sourcepath dir1:dir2` you will indicate JDB where to look for source files and by then the posibility to navigate the code wiht `list` command.

```
jdb -attach 9939 -sourcepath /home/jcammmmm/repo.o/tomcat/test/
```

This is a good oportunity to put here the available commands on JDB:
```
threads - list threds, 
where, wherei - will show the call stack,
up, down - descend, ascend in the call stack
print, dump, eval, locals - display current values
stop in, stop at - put a breakpoint
clear :, clear . - remove breakpoint, and display breakpoints
trace, untrace - tstop in method entry/exited
step, step up, stepi, next, cont - control execution
use - change the sourcepath
classpath - display the current classpath
classes - list all clases loaded up to now
lock, threadlocks - 
```

While debugging the app, I found that sources where missing to display the listing, in particular for `jakarta.servlet.http.HttpServlet.java` class. In order to provide those source to JDB and also make them available to me, now I'm just finding the package that holds that code. After issuing `classpath` command this was the output (formatted):

```
/home/jcammmmm/repo.o/tomcat/output/build/webapps/examples/WEB-INF/classes
/home/jcammmmm/repo.o/tomcat/output/testclasses
/home/jcammmmm/repo.o/tomcat/output/i18n
/home/jcammmmm/Downloads/tomcat-build-libs/junit-4.13.2/junit-4.13.2.jar
/home/jcammmmm/Downloads/tomcat-build-libs/hamcrest-2.2/hamcrest-2.2.jar
/home/jcammmmm/Downloads/tomcat-build-libs/easymock-4.3/easymock-4.3.jar
/home/jcammmmm/Downloads/tomcat-build-libs/cglib-3.3.0/cglib-nodep-3.3.0.jar
/home/jcammmmm/Downloads/tomcat-build-libs/objenesis-3.3/objenesis-3.3.jar
/home/jcammmmm/Downloads/tomcat-build-libs/unboundid-6.0.6/unboundid-ldapsdk-6.0.6.jar
/home/jcammmmm/Downloads/tomcat-build-libs/derby-10.16.1.1/derby-10.16.1.1.jar
/home/jcammmmm/Downloads/tomcat-build-libs/derby-10.16.1.1/derby-shared-10.16.1.1.jar
/home/jcammmmm/Downloads/tomcat-build-libs/derby-10.16.1.1/derby-tools-10.16.1.1.jar
/home/jcammmmm/Downloads/tomcat-build-libs/bnd-6.3.1/biz.aQute.bnd-6.3.1.jar
/home/jcammmmm/Downloads/tomcat-build-libs/ecj-4.20/ecj-4.20.jar
/home/jcammmmm/Downloads/tomcat-build-libs/jaxrpc-1.1-rc4/geronimo-spec-jaxrpc-1.1-rc4.jar
/home/jcammmmm/Downloads/tomcat-build-libs/wsdl4j-1.6.3/wsdl4j-1.6.3.jar
/home/jcammmmm/Downloads/tomcat-build-libs/migration-1.0.4/jakartaee-migration-1.0.4-shaded.jar
/home/jcammmmm/repo.o/tomcat/output/classes
/opt/apache-ant-1.10.2/lib/ant-launcher.jar
/opt/apache-ant-1.10.2/lib/ant.jar
/opt/apache-ant-1.10.2/lib/ant-junit.jar
/opt/apache-ant-1.10.2/lib/ant-junit4.jar
```

So, basically we see that it cames from mainly three parts: 1. our compilation output, 2. the downloaded libraries and our recently Apache Ant instalation. In order to provide a good dependency analysis here there are the dependencies explained and their purporse:
* **junit**: Unit testing
* **hamcrest**: Unit testing and assertion [tool.](https://hamcrest.org/JavaHamcrest/tutorial)
* **easymock**: Unit testing and mocking [tool.](https://easymock.org/). (Read the what section.)
* **cglib**: Transform and generation of Java bytecode [tool.](https://github.com/cglib/cglib)
* **objenesis**: Helps to instantiate a new object of particular class. Docs [here.](https://github.com/cglib/cglib)
* **unboundid**: Software to communicate with LDAP servers. [Docs here.](https://github.com/pingidentity/ldapsdk)
* **derby**: Relational database entirely implemented in Java. [Docs.](https://db.apache.org/derby/)
* **bnd**: Helps to bundle Java software in a modular fashion following OSGi. [Docs.](https://bnd.bndtools.org/chapters/110-introduction.html) [About OSGi](https://enroute.osgi.org/FAQ/520-bnd.html) and bnd. 
* **ecj**: The Eclipse Standalone [Compiler](https://projectlombok.org/setup/ecj)
* **jaxrpc**: Java APIs for XML-based Remote Procedure Call. More [here.](https://www.oracle.com/technical-resources/articles/javase/getstartjaxrpc.html)
* **wsdl**: Language to describe SOAP based webservices.
* **jakartaee-migration**: _"take a web application written for Java EE 8 that runs on Apache Tomcat 9 and convert it automatically so it runs on Apache Tomcat 10"_ taken from [here](https://mvnrepository.com/artifact/org.apache.tomcat/jakartaee-migration)

After doing this intensive research on what this libraries do, I realize that Tomcat is in fact the implation of _Jakarta Servlet_, _Jakarta Expression Language (EL)_ and _Websocket technologies_ ([more here]https://en.wikipedia.org/wiki/Apache_Tomcat). Since, at the start of this debugging I only pointed out that the location of the source are here:

```
jdb -attach 9939 -sourcepath /home/jcammmmm/repo.o/tomcat/test/
```

I will point the debugger to look for source into the non-test sources: `/java`. Issuing the following command into the JDB:
```
sourcepath /home/jcammmmm/repo.o/tomcat/java:/home/jcammmmm/repo.o/tomcat/test
```
This is the complete command:
```
jdb -attach 9939 -sourcepath /home/jcammmmm/repo.o/tomcat/test:/home/jcammmmm/repo.o/tomcat/java
```


Will give us the listing for the desired class `HttpServlet.java`!

```java
main[1] list
94        private static final String HEADER_IFMODSINCE = "If-Modified-Since";
95        private static final String HEADER_LASTMOD = "Last-Modified";
96    
97        private static final String LSTRING_FILE = "jakarta.servlet.http.LocalStrings";
98 =>     private static final ResourceBundle lStrings = ResourceBundle.getBundle(LSTRING_FILE);
99    
100        private static final Set<String> SENSITIVE_HTTP_HEADERS = new HashSet<>();
101    
102        private final transient Object cachedAllowHeaderValueLock = new Object();
```

Debugging several threads
---------------------------------------
When you start JDB you will be placed on the main thread by default. You can switch to the other threads by typing `thread id` where `id` is the hexadecimal number that appears right next to thread type when you type `thread`. In the following of this section I will describe briefly what each thread does. 

After the `init()` method call several threads are created per each connector, for Catalina and a master parent thread:

```
  (org.apache.tomcat.util.threads.TaskThread)0xa62 http-nio2-127.0.0.1-auto-1-exec-1  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa63 http-nio2-127.0.0.1-auto-1-exec-2  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa64 http-nio2-127.0.0.1-auto-1-exec-3  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa65 http-nio2-127.0.0.1-auto-1-exec-4  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa66 http-nio2-127.0.0.1-auto-1-exec-5  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa67 http-nio2-127.0.0.1-auto-1-exec-6  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa68 http-nio2-127.0.0.1-auto-1-exec-7  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa69 http-nio2-127.0.0.1-auto-1-exec-8  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa6a http-nio2-127.0.0.1-auto-1-exec-9  cond. waiting
  (org.apache.tomcat.util.threads.TaskThread)0xa6b http-nio2-127.0.0.1-auto-1-exec-10 cond. waiting
  (java.lang.Thread)0xa7c                          Thread-1                           running
  (org.apache.tomcat.util.threads.TaskThread)0xb08 Catalina-utility-1                 running
  (org.apache.tomcat.util.threads.TaskThread)0xb0d Catalina-utility-2                 running

```

So this threads are created to support the testing framework:

```
Group system:
  (java.lang.ref.Reference$ReferenceHandler)0x1ec Reference Handler running
  (java.lang.ref.Finalizer$FinalizerThread)0x1ed  Finalizer         cond. waiting
  (java.lang.Thread)0x1ee                         Signal Dispatcher running
Group main:
  (java.lang.Thread)0x1                           main              running
Group InnocuousThreadGroup:
  (jdk.internal.misc.InnocuousThread)0x1ef        Common-Cleaner    cond. waiting

```

Tomcat thread hierarchy
---------------------------------------
In order to see how the connectors are ins2tanced, we need to see how the Tomcat server object starts. `start()` implementation is located in `LifecycleBase.java` file, here is the base implementation of `Lifecycle.java` interface.

Now we are debugging the tomcat startup to see how the connectors are instantiated. This debug is being performed from a unit testing code called `TestMaxConnections.java`. From there, I put a break point in `org.apache.catalina.startup.Tomcat.start()` method. From the code review it seems that there is only one connector, the HTTP connector, and for this connector are configured several threads. In order to proof this I will put a bread point at `stop in org.apache.catalina.startup.Tomcat.getConnector()`. After running the test, the connector is already instantiated, let's look for that. We know up to know that the connectors belongs to the inner _service_ wrapped by the Tomcat instance. This service is initialized when a call to `Tomcat.getServer()` is made for first time. To see that I will restart the test case and put another breakpoint there: `stop in org.apache.catalina.startup.Tomcat.getServer()`.

Since, we are debugging a test case, the initialization of Tomcat is being made in `TomcatBaseTest.java`. There, the connector is being created in the `setUp()` method. It is important to note here that the testing framework calls this method, before anything else. The protocol's kind `Http11NioProtocol` and it is being initialized as such because we are not providing another protocol in properties file.

In order to arrive to our conclusion, we need to see where the max number of thread is being used. While researching on this I found that this property that is being setted to the `Connector` in fact is being setted to the `ProtocolHandler`. This property is being setted through java reflection utils. I was expecting a dictionary here it seems that they are changing the attribute of that handler.

Why reflection utils
---------------------------------------
When I arrive to reflexive code in java it seems bizarre to me bacause, parsers and linters always show a warning. As expected the method that set the properties for a given object is annotated with `@SuppressWarnings`. After following the code quickly, I found that since no exception is thrown the attribute `maxThreads` in class `ProtocolHandler` is being setted. Why to set in that way? Because `maxConnections` is a property that is on top of a chain of abstract classes whose current type is hard to guess without to know in advance what what protocol is being used now.

Endpoints and Executor
---------------------------------------
After reading the `ProtocolHandler` code and arriving at `AbstractProtocol` code, I found the max threads property it is being setted in `Endpoint` class. The code documentation say that `Endpoint` program provides low level network I/O, so I think that our answer can be found in the object hierarchy that decends from `Endpoint` class. Something that can be reviewed is the generic relationship between `AbstractProtocol` and  `Endpoint`, but we are now focused on our main quest regarding how the several threads are created.

AbstractEnpoint
  - attrib is executor
  - chain: TomcatBaseTest -> Connector -> ProtocolHandler -> AbstractProtocol -> AbstractEnpoint -> Executor
  
Tomcat [Java docs](https://tomcat.apache.org/tomcat-10.1-doc/api/index.html)
  
stop in org.apache.tomcat.util.net.AbstractEndpoint.setMaxThreads(int)
stop in org.apache.tomcat.util.net.AbstractEndpoint.createExecutor()

Finally, I am about to complete this debug session, I learnend a lot on how the abstractions are employed to produce high performant production code. In fact the call stack that I'm debuggin is 
```
stop in org.apache.tomcat.util.net.AbstractEndpoint.createExecutor()
```
Inside this method the worker threads will process the future requests that are being created. Now the handling and processing of requests will be handled by the pool of threads abstracted by this executor. In the end your endpoint will have one executor that will have many threads. How the tasks are passed to this worker threads is the purpose of the following section.

Requests, Poller and Executor
---------------------------------------
Once the endpoint executor is created in `AbstractEndpoint.createExecutor()`, several threads are created and pooled. In fact they are exactly 10, as defined in the `TestMaxConnections` unit test. 
Regarding to how several requests are fullfilled in parallel we need to recall again the unit test implementation and put some breakpoints there.
```
stop in org.apache.catalina.connector.TestMaxConnections$SimpleServlet.service(jakarta.servlet.http.HttpServletRequest, jakarta.servlet.http.HttpServletResponse)
```
This is the call stack at the given breakpoint. As you may know it is not possible to know who is the parent thread that spawned the current thread at frame 20.
```log
  [1] org.apache.catalina.connector.TestMaxConnections$SimpleServlet.service (TestMaxConnections.java:137)
  [2] jakarta.servlet.http.HttpServlet.service (HttpServlet.java:792)
  [3] org.apache.catalina.core.ApplicationFilterChain.internalDoFilter (ApplicationFilterChain.java:223)
  [4] org.apache.catalina.core.ApplicationFilterChain.doFilter (ApplicationFilterChain.java:158)
  [5] org.apache.catalina.core.StandardWrapperValve.invoke (StandardWrapperValve.java:197)
  [6] org.apache.catalina.core.StandardContextValve.invoke (StandardContextValve.java:97)
  [7] org.apache.catalina.authenticator.AuthenticatorBase.invoke (AuthenticatorBase.java:542)
  [8] org.apache.catalina.core.StandardHostValve.invoke (StandardHostValve.java:119)
  [9] org.apache.catalina.valves.ErrorReportValve.invoke (ErrorReportValve.java:92)
  [10] org.apache.catalina.core.StandardEngineValve.invoke (StandardEngineValve.java:78)
  [11] org.apache.catalina.connector.CoyoteAdapter.service (CoyoteAdapter.java:356)
  [12] org.apache.coyote.http11.Http11Processor.service (Http11Processor.java:399)
  [13] org.apache.coyote.AbstractProcessorLight.process (AbstractProcessorLight.java:65)
  [14] org.apache.coyote.AbstractProtocol$ConnectionHandler.process (AbstractProtocol.java:868)
  [15] org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun (NioEndpoint.java:1,762)
  [16] org.apache.tomcat.util.net.SocketProcessorBase.run (SocketProcessorBase.java:49)
  [17] org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker (ThreadPoolExecutor.java:1,191)
  [18] org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run (ThreadPoolExecutor.java:659)
  [19] org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run (TaskThread.java:61)
  [20] java.lang.Thread.run (Thread.java:829)
```

Now with this breakpoint I am attempting to find how the executor got called.
```
stop in org.apache.tomcat.util.threads.ThreadPoolExecutor.execute(java.lang.Runnable)
```

The thread handling the incoming requests to the server is `http-nio-127.0.0.1-auto-1-Poller`. After looking for the work `-Poller` in the source code I found that at `NioEndpoint.startInternal()` method a new thread is spawned and it will be running the `Runnable` class `Poller`. Here is the code snippet:
```java
  // Start poller thread
  poller = new Poller();
  Thread pollerThread = new Thread(poller, getName() + "-Poller");
  pollerThread.setPriority(threadPriority);
  pollerThread.setDaemon(true);
  pollerThread.start();
```

`Poller` class is a nested class in `NioEndpoint` and expands roughly for 500 lines. When this poller object is instantiated, a call to `java.nio.channels.Selector.open()` is made. Please note that this is JDK software and that `nio` means Non-Blocking I/O. In the other hand after reading the JDK [docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/channels/package-summary.html) a `Selector` is a multiplexer. The Poller internally runs a `while(true)` loop. Here is a breakpoint in that loop:
```
stop in org.apache.tomcat.util.net.NioEndpoint$Poller.run()
```
You may think that between each loop you can lost requests, that is, while your are in the current iteration may be another requests can be arriving to the server and since they weren 't at the beginning of the loop they will be lost. The thing is that the requests are being placed in a request queue that are being processed in `NioEndpoint$Poller.events()` method.
```
stop in org.apache.tomcat.util.net.NioEndpoint$Poller.addEvent(org.apache.tomcat.util.net.NioEndpoint$PollerEvent)
```
But, how the requests arrive and queued? The following section will review that.

Requests and Acceptor
---------------------------------------
After analysing the call stack behind the `addEvent(PollerEvent)` method I found that the `auto-1-Acceptor` threads queues the incomming events. Recalling our previous analysis, after the `Poller` queue is initialized, the `Acceptor` queue is anitialized:
```java
  poller = new Poller();
  Thread pollerThread = new Thread(poller, getName() + "-Poller");
  pollerThread.setPriority(threadPriority);
  pollerThread.setDaemon(true);
  pollerThread.start();

  startAcceptorThread();
```
The reference to the hold element is made in `AbstractEndpoint.java`:
```java
  /**
    * Thread used to accept new connections and pass them to worker threads.
    */
  protected Acceptor<U> acceptor;
```
Note that `Acceptor` resides in the same package that `NioEndpoint` while `Poller` is a nested class, so both threads are created by `NioEndpoint`. Also, `Acceptor` runs a `while(true)`, but the same question arises here, how every request is processed without missing something between loops? It seems that the protocol handles that, this listing has some lights on that:
```java
  try {
      //if we have reached max connections, wait
=>    endpoint.countUpOrAwaitConnection();
      
      // Endpoint might have been paused while waiting for latch
```

In order to understand [how](https://developer.mozilla.org/en-US/docs/Web/HTTP/Session) the requests are not lost between loops, it is necesary to give a look to the HTTP client implemented in the test unit. May be this will be something related to TCP, since this is the underlying transport protocol for HTTP. When you review the client code you find that a socket is behind the `SimpleHttpClient` provided by Tomcat project. This socket is provided by the JDK in `java.net.Socket` class. To implement this, the wrapped the socket with and `OutputStream` object, a write throught it.

Our abstraction networking limit is the socket, if do not put a boundary to this reasearch will going to deep and this document will be too broad. After reading the [docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/SocketImpl.html#setPerformancePreferences(int,int,int)) for `SocketImpl`, the underlying connection is created on TCP protocol.

After reading the Wikipedia [article](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Protocol_operation) on TCP, it is shown that the underlyin connection is managed by the operating system through an Internet Socket. Also the definition provided in MDN [docs](https://developer.mozilla.org/en-US/docs/Glossary/TCP_handshake) also relates the terms socket and TCP. Following our previous guesses, the requests are not lost since the connection it is being mantained in TCP.

Basically, requests are not lost until the server decides to accept new incomming TCP connections; that means to complete the three way [handshake] https://developer.mozilla.org/en-US/docs/Glossary/TCP_handshake. Following this code snipet from `Acceptor`, you can see that the request will not be process until the server decides to start to process it.
```java
U socket = null;
try {
    // Accept the next incoming connection from the server
    // socket
    socket = endpoint.serverSocketAccept();
} catch (Exception ioe) {
    // We didn't get a socket
    endpoint.countDownConnection();
    if (endpoint.isRunning()) {
        // Introduce delay if necessary
        errorDelay = handleExceptionWithDelay(errorDelay);
        // re-throw
        throw ioe;
    } else {
        break;
    }
}
```
The euristic here is that no request got lost if the are not accepted by the server. In other words, nothing will be missed if you do not have nothing to miss.
