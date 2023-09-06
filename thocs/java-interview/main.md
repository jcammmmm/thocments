About
=====================================================================
This guide not intends to explain each of the topics that appears on the TOC,
instead provides some text that will clarify and refine your cocepts on the
addressed terms.

TOC
=====================================================================
Technical interview might cover topics like: 
* Core Java [3h]
    - multithreading
    - Immutability (mutable vs. immutable)
        * How to avoid mutability of inner objects
    - collections
    - exceptions (checked and unchecked)
    - Error vs Exceptions
    - Optional (orElse, orElseGet)
    - Why Optional is nice 
* git [3h]
* Spring [3h]
    - Actuator
    - @Component vs @Service
    - @Qualifier
    - @Scope("prototype")
* Spring boot [2h]
* Mockito [2h]
    - @mockito vs Mockito.spy()
* JUnit [2h]
    - @ExtendWith
    - @ParametrizedTest
* Software design [1h]
    - OOP principles
    - SOLID
    - Design Patterns
    - Design Principles
    - SDLC
    - TDD
    - Integration tests
    - Test pyramid
    - High Quality Code Features?
* Databases [2h]
    - Stored procedures MSSQL/Oracle
* CI/CD tools (Chef, Jenkins) [2h]
* Messaging Pipelines [2h]
    - RabbitMQ or Kafka
* Front End 
    - React
    - Angular 2+ (not AngulaJS)
* Cloud GCP/AWS

How to
=====================================================================
The code for this quick study guide is found together this document in `code` folder.
The code was structured with [Maven Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html), using the following command:
```sh
mvn archetype:generate
:  groupId: smpl.jcammmmm
:  artifactId: stdguide
:  version: 1.0-SNAPSHOT
:  package: smpl.jcammmmm
```

Core Java
=====================================================================
### Stream API
#### Intermediate ops
#### Final ops
#### findFirst() vs findAny()

### String Pool
### Optional and != null
### Flatmap vs Map

Git
=====================================================================
### merge
### rebase
### cherry-pick
### squash


Spring
=====================================================================


Spring Boot
=====================================================================
### Anotation Scope