Intro
===========================================================
Together with this posts is also usefull to give a look to to this [repo](???) it contains my exploration of the documentation and how to use it correctly. The base working code was obtained after following the _getting started guides_ available [here](https://docs.jboss.org/hibernate/orm/6.2/quickstart/html_single/).
From my professional experience, it seems that this framework is the first option choosen when the bussiness logic is about to be implemented in Java, and not in the form of the stored procedures in the database. As a reason of that several componentes such as _hibernate-hikaricp_ and _hiberante-jcache_ appear in the preable of the guide. We hope in futer guides review them. Keep an eye on the main index for them.
This framework is a main dependency in _Springboot_, in fact it makes part of one of most commonly used starters: [here.](https://repo1.maven.org/maven2/org/springframework/boot/spring-boot-starter-data-jpa/3.1.1/spring-boot-starter-data-jpa-3.1.1.pom)

Downloading and running a release
===========================================================
To keep the focus for now I will [download](https://sourceforge.net/projects/hibernate/files/hibernate-orm/) an already compiled binary and then try to run it standalone. After, in a further section I will compile by myself the binaries and debug some important gearing behind the implementation. Please note that connection pooling utilities such as _c3p0_ may be operating under the hood.

I believe that writting some code by hand is important so what I will try to do is to compile everything by hand at its minimum dependency requirements. So in the following sections several commands will be displayed.


Building from source
===========================================================











===
As a we note from the other articles, it is need to give a look to JUnit test framework. 


---------------------------------------
