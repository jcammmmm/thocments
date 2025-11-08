Intro
===========================================================
Together with this posts is also useful to give a look to to this [repo](???) it contains my exploration of the documentation and how to use it correctly. The base working code was obtained after following the _getting started guides_ available [here](https://docs.jboss.org/hibernate/orm/6.2/quickstart/html_single/).

From my experience, it seems that this framework is the first option one chooses when the bussigness logic is about to be implemented in Java, and not in the form of the stored procedures in the database. As a reason of that several components such as _hibernate-hikaricp_ and _hiberante-jcache_ appear in the preamble of the guide. We hope in futer guides review them. Keep an eye on the main index for them.

This framework is a main dependency in _Spring Boot_, in fact it makes part of one of the most commonly used [starters](https://repo1.maven.org/maven2/org/springframework/boot/spring-boot-starter-data-jpa/3.1.1/spring-boot-starter-data-jpa-3.1.1.pom)

Downloading and running a release
===========================================================
To keep the focus for now I will [download](https://sourceforge.net/projects/hibernate/files/hibernate-orm/) an already compiled binary and then try to run it standalone. After, in a further section I will compile the source code and debug some important gearing behind the implementation. Please note that connection pooling utilities such as _c3p0_ may be operating under the hood.

I believe that writting some code by hand is important so what I will try to do is to compile everything by hand at its minimum dependency requirements. So in the following sections several commands will be displayed. The process of getting the minimal example running without using build tools such as _Maven_ or _Gradle_ can be found in this [guide.](../java-why-maven)

Debugging and the release
===========================================================
The debugging will be performed with _JDB_, this [guide](../java-quick-debugging) contains a quick overview on the debugging process on Java. In order to step through the source code, we need to download the _jar_ sources, the same guide provide an step by step overview of that process.
















===
As a we note from the other articles, it is need to give a look to JUnit test framework. 


---------------------------------------
