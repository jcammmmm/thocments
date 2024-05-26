Apache Zookeeper setup with Podman
====================================================================
> In this document you will find how to setup an _Apache Zookeeper_ system with Podman. The main aim of this guide is to assemble a distributed system quickly that lets you to understand the utility and what does Zookeeper.

Podman
====================================================================
You must have Podman installed. This [document](./containers-beg/main.md) could help.

Building Zookeeper image
====================================================================
To build and image from a Container file description (_Dockerfile_):
1. Clone this repository `https://github.com/31z4/zookeeper-docker`
2. Go to `3.9.1` or your desired version.
3. Then throw `sudo podman build -t zookeeper:3.9.1 .` in the console.
4. Voila! your image was build.

`docker-entrypoint.sh` script
---------------------------------
This [documentation][1] and `man test` (for conditionals) could help you to understand the script. The script begins by throwing a `set -e`, that makes that your current terminal exits immediatily on a non-zero status i.e. after any error.

Then checks if the `zkServer.sh` was passed as first parameter and if the current user is `root` i.e. user id `0`. If that is true then take the ownership of necessary zookeeper server folders.

Then checks if `zoo.cfg` file exists (`test -f`). If not, then create the file and populate it with the given configurations.

Please note that this file is called from the _ContainerFile_ in the `ENTRYPOINT` sentence and in the `CMD` sentence the script arguments are provided. Remember that `ENTRYPOINT` lets you start a process within your container so you con bring to life your application and `CMD` is a mean to provide default values for this initialization. There are more details on this depending if you call each of this sentences as a JSON array or not. More details can be found [here][2]


Basic Setup
====================================================================
Server Setup
------------------------
1. Launch a ZooKeeper container: 
  `sudo podman run --name zkserver1 --rm -d -p 2181:2181 -e "TERM=xterm-256color" zookeeper:3.9.1`
	
Client Setup
------------------------
1. `cd samples`
2. Compile the client example:   
	`javac -cp .:slf4j-api-1.7.30.jar:zookeeper-3.4.14.jar -d out Executor.java`   
	`cd out`   
4. Launch you application in debugging mode:   
	`java -cp .:../slf4j-api-1.7.30.jar:../zookeeper-3.4.14.jar Executor localhost:2181 /aa bb ls`
2. Enter to that container, to alter the ZooKeeper nodes state and trigger the application.
	```sudo podman exec -ti zkserver1 bash```
9. Create a node and a data file inside it:
	```
	you@container$ bin/zkCli.sh -server 127.0.0.1:2181
	you@zookeeper] create /myzknode myzknode-file1
	you@zookeeper] get -s /myzknode
	```


### Debugging
1. `alias javadbg='java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=9394'`
2. `javadbg -cp .:slf4j-api-1.7.30.jar:zookeeper-3.4.14.jar Executor 127.0.0.1:2181 /myzknode myzknode-file1 ls`
3. `jdb -attach 9394 -sourcepath .`. Please note that the sourcepath is the current folder, then you must `cd` first.	
4. `stop in Executor:40`
5. `stop in Executor:71`
6. `stop in DataMonitor:61`
6. `stop in DataMonitor:95`

Example Analysis
------------------------
Since the only operation from `Watcher` interface is `process(WatchedEvent)` is easy to guess that the 




1. java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=9393
2. jdb -attach 9393 -sourcepath .

Running the examples
====================================================================
This code is provided [here][3]
1. search the dependency https://mvnrepository.com/artifact/org.apache.zookeeper/zookeeper; choose the version; Download the _jar_.
2. Move the downloaded jar together with the sample files.
3. 

Tracking log
====================================================================
### 240525   
  Since I do not write this kind of logs, I redo the work of recreating the image since
  I reinstalled Debian on my personal computer.   
  I got a misfunction since the program reports a 'Retry' on the terminal. I review 
  the code and found that I am reciving an error code from the server. After looking 
  on this I was reading how the `exists` methods works on the client base `Zookeeper`
  class works. I found some statement locks that I review again from the Java tuto 
  official documentation.
  I tried also to generate de java docs, but I prefer to navigate by searching the 
  source code. The effort now is try to understand how this basic example works and 
  to understand how thw parts works and then mount a replicated installation and
  throw million of requests on int.
  I will left this log on each repo in order to work more efficiently and with other
  software projects at the same time.
### 2311??   
  Reading about the project. Debugging some code. The docker image for zookeeper was 
  created from a private company project in github.

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
