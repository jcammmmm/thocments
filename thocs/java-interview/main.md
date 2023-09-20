About
=====================================================================
This guide not intends to explain each of the topics that appears on the TOC,
instead provides some text that will clarify and refine your cocepts on the
addressed terms.


TOC
=====================================================================
Technical interview might cover topics like: 
* Core Java
    - Stream API
    - Multithreading
    - String pool
    - Optional (orElse, orElseGet, != null)
    - Immutability (mutable vs. immutable)
    - Java Collections
    - Exceptions (checked and unchecked)
* git
* Spring
    - Spring Framework
    - Spring Boot
        - Actuator
        - @Component vs @Service
        - @Qualifier
        - @Scope("prototype")
* JUnit
    - @ExtendWith
    - @ParametrizedTest
* Mockito
    - @mockito vs Mockito.spy()
* Messaging Pipelines [2h]
    - Kafka
    - RabbitMQ
* Databases [2h]
    - Stored procedures MSSQL/Oracle
* Software design [1h]
    - OOP principles
    - SOLID
    - Design Patterns
    - Design Principles
    - SDLC
    - DRY 
    - TDD
    - Integration tests
    - Test pyramid
    - High Quality Code Features?
* CI/CD tools (Chef, Jenkins) [2h]
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
The examples for this subsection can be found in [App.java](code/stdguide/src/main/java/smpl/jcammmmm/App.java). 

Stream API
-------------------------------------------------
### Intermediate ops
Intermediate operations return always an `Stream`.
That is well documented [here](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/package-summary.html#StreamOps).
Examples
- `Stream.filter`
- `Stream.map`

### Final ops
Final operations currently trigger the stream execution. The calls provided in
the intermediate operations only define the transformations triggered by the final
operations.
- `Stream.forEach`
- `Stream.reduce`

### findFirst() vs findAny()
- `findFirst()`: returns an `Optional` that wraps the first element of the stream. 
- `findAny()`: take one element randomly wrapped in an `Optional`. Non-Deterministic.

### flatmap() vs map()
- `flatmap(Function<T, Stream<R>>)`: transforms an stream into another, by making a 
    1-to-many mapping. For each element in origin stream the associated stream is
    replaced.
- `map(Function<T, R>)`: transforms an stream into another, but without mapping against
    another stream.

### Paralelism
Only use the `parallel()` method provided by the API. Keep a note that parallelism 
could change your results based on if your intermediate operations are stateless 
or not. Also, the `limit()` operation could affect negatively the performance of
parallelization.

### Value Objects
* LocalDateTime
* Optional
* Mentioned in _Mockito_ documentation. Do not mock value objects.

Multithreading
-------------------------------------------------
All the toolset to perform multithreading programming can be found in `java.util.concurrent`
[package](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/package-summary.html). This toolset is provided as the following set of interfaces an 
implementation hierarchies. Keep a note that this tools supports the returning of result with
`Callable`, and not the only processing features (`return void`) of `Thread` and `Runnable`.
(_dashes_ are _interfaces_, _stars_ are _implementations_):

- `Executor`
    - `ExecutorService`
        - `ScheduledExecutorService`
            * `ThreadPoolExecutor`
                * `ScheduledThreadPoolExecutor`
    - `CompletionService` (uses an `Executor` inside)
        - `ExecutorCompletionService` TODO: An example
    - `AbstractExecutorService` 
        *  `ForkJoinPool`

The previous multithreading frameworks abstract the tasks and their results
through the following classes:
- `Task` (placeholder, this element does not exist in java)
    - `Callable`
    - `Runnable`
- `Result` (placeholder, this element does not exist in java)
    - `Future<T>`
        * `FutureTask<T>` 
        * `ForkJoinTask<V>` TODO: An example

In addition, since several threads needs to update one common data structure, the
Java standard library provides thread-safe data structures:
* `ConcurrentLinkedQueue<T>` TODO: An example
* `ConcurrentLinkedDeque<T>`
* `ConcurrentHashMap<T,U>`  TODO: An example
- `BlockingQueue<E>`
    * `LinkedBlockingQueue<T>`
    * `PriorityBlockingQueue<T>`

An has the implementation of common sinchronization idioms:
* `Semaphore` TODO: An example
* `Phaser`


String Pool
-------------------------------------------------
Strings are special elements in computer programs and in informatics in general. Since
they can use important amounts of memory, when you define them as literals, i.e. with
double quotes (`"`), the are being allocated an special memory space, in order to reference
that location when the same string is newly defined in the future. You can sen any
`String` object you have directly to that special address space with the `String.intern()` method.


Optional (orElse, orElseGet, != null)
-------------------------------------------------
As per the [documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Optional.html).
Is a wrapper that can contain or not a non-`null`.  Its purpose is merely sintact through the 
`orElse(T)` and `ifPresent(Consumer<T>)` methods.

### Why Optional is nice?
It will help you to avoid _NullPointerException_.


Immutability
-------------------------------------------------
Is said that an object is immutable if cannot be modified after its creation. There is 
discussion around this since for some programmers is better to create new instances instead
of modifying the currently existing ones.

### How to avoid mutability of inner objects
- Make them final.
- Do not associate any setter method to that objects.
- Return new object after modification or computations were made.

Java Standard Library a.k.a _Java Collections_
-------------------------------------------------
The collections framework consists of well defined Interfaces, its implementations, algorithms for efficient manipulations and a good API infraestucture. Typically have names in the form of <Implementation-style><Interface>
([docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/doc-files/coll-overview.html)):
* Collection interfaces:
    - `Collection`
        - `Set`: No duplicate elements permitted.
            - `SortedSet`: A set whose elements are automatically
                - `NavigableSet`: Reports closest matches for given search targets.
                    * `TreeSet`: Red-black tree implementation.
            * `HashSet`: Hash table implementation. The best all-around implementation.
            * `LinkedHashSet`: Hash table and linked list implementation 
        - `List`: Ordered collection, also known as a sequence.
            * `ArrayList`: Resizable array implementation. The best all-around implementation.
            * `LinkedList`: Doubly-linked list implementation. Better perfomance in high frequency thant array list.
        - `AbstractQueue`
            - `Queue` 
                - `BlockingQueue` (in `java.concurrent`)
                    - `TransferQueue` (in `java.concurrent`)
                - `Deque`
                    - `BlockingDeque` (in `java.concurrent`)
                    * `ArrayDeque`: Efficient, resizable array implementation
            - `PriorityQueue`: Heap implementation of an unbounded priority queue.
        - `Map`: A mapping from keys to values. 
            - `SortedMap`: A map whose mappings are automatically sorted by key.
                - `NavigableMap`: Reports closest matches for given search targets.
                    * `TreeMap`: Red-black tree implementation.
            - `ConcurrentMap` (in `java.concurrent`)
                - `ConcurrentNavigableMap`
            * `HashMap`: Hash table implementation. The best all-around implementation.
            * `LinkedHashMap`: Hash table and linked list implementation.
        
* Concurrent implementations:
    - `ConcurrentLinkedQueue` - An unbounded first in, first out (FIFO) queue based on linked nodes.
    - `LinkedBlockingQueue` - An optionally bounded FIFO blocking queue backed by linked nodes.
    - `ArrayBlockingQueue` - A bounded FIFO blocking queue backed by an array.
    - `PriorityBlockingQueue` - An unbounded blocking priority queue backed by a priority heap.
    - `DelayQueue` - A time-based scheduling queue backed by a priority heap.
    - `SynchronousQueue` - A simple rendezvous mechanism that uses the BlockingQueue interface.
    - `LinkedBlockingDeque` - An optionally bounded FIFO blocking deque backed by linked nodes.
    - `LinkedTransferQueue` - An unbounded TransferQueue backed by linked nodes.
    - `ConcurrentHashMap` - A highly concurrent, high-performance ConcurrentMap implementation based on a hash table. This implementation never blocks when performing retrievals and enables the client to select the concurrency level for updates. It is intended as a drop-in replacement for Hashtable. In addition to implementing ConcurrentMap, it supports all of the legacy methods of Hashtable.
    - `ConcurrentSkipListSet` - Skips list implementation of the NavigableSet interface.
    - `ConcurrentSkipListMap` - Skips list implementation of the ConcurrentNavigableMap interface.

* Algorithms - The `Collections` class contains these useful static methods.
    - `sort(List)`: Sorts a list using a merge sort algorithm, which provides average case performance comparable to a high quality quicksort, guaranteed O(n*log n) performance (unlike quicksort), and stability (unlike quicksort). A stable sort is one that does not reorder equal elements.
    - `binarySearch(List, Object)`: Searches for an element in an ordered list using the binary search algorithm.
    - `reverse(List)`: Reverses the order of the elements in a list.
    - `shuffle(List)`: Randomly changes the order of the elements in a list.
    - `fill(List, Object)`: Overwrites every element in a list with the specified value.
    - `copy(List dest, List src)`: Copies the source list into the destination list.
    - `min(Collection)`: Returns the minimum element in a collection.
    - `max(Collection)`: Returns the maximum element in a collection.
    - `rotate(List list, int distance)`: Rotates all of the elements in the list by the specified distance.
    - `replaceAll(List list, Object oldVal, Object newVal)`: Replaces all occurrences of one specified value with another.
    - `indexOfSubList(List source, List target)`: Returns the index of the first sublist of source that is equal to target.
    - `lastIndexOfSubList(List source, List target)`: Returns the index of the last sublist of source that is equal to target.
    - `swap(List, int, int)`: Swaps the elements at the specified positions in the specified list.
    - `frequency(Collection, Object)`: Counts the number of times the specified element occurs in the specified collection.
    - `disjoint(Collection, Collection)`: Determines whether two collections are disjoint, in other words, whether they contain no elements in common.
    - `addAll(Collection<? super T>, T...)`: Adds all of the elements in the specified array to the specified collection.
* Infrastructure:
    - Iterators:  Similar to the familiar Enumeration interface, but more powerful, and with improved method names.
        `Iterator`: In addition to the functionality of the Enumeration interface, enables the user to remove elements from the backing collection with well-defined, useful semantics.        
        `List Iterator`: Iterator for use with lists. In addition to the functionality of the Iterator interface, supports bidirectional iteration, element replacement, element insertion, and index retrieval.
    - Ordering
        `Comparable`: Imparts a natural ordering to classes that implement it. The natural ordering can be used to sort a list or maintain order in a sorted set or map. Many classes were retrofitted to implement this interface.
        `Comparator`: Represents an order relation, which can be used to sort a list or maintain order in a sorted set or map. Can override a type's natural ordering or order objects of a type that does not implement the Comparable interface.
    - Runtime exceptions
        `UnsupportedOperationException`: Thrown by collections if an unsupported optional operation is called.
        `ConcurrentModificationException`: Thrown by iterators and list iterators if the backing collection is changed unexpectedly while the iteration is in progress. Also thrown by sublist views of lists if the backing list is changed unexpectedly.
    - Performance
        `RandomAccess`: Marker interface that lets List implementations indicate that they support fast (generally constant time) random access. This lets generic algorithms change their behavior to provide good performance when applied to either random or sequential access lists.


Exceptions
-------------------------------------------------
### Checked vs Unchecked
* Unchecked exceptions: They are all exceptions (and its subclasses) of type `RuntimeException`. This
  kind of exceptions are not need to be declared in methods or constructor signatures. ([docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/RuntimeException.html))
* Checked exceptions: Those exceptions that **are not** `RuntimeException` are checked exceptions.
  They are checked since you need to declare them in methods and constructor signatures. ([docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html))

### `Exception` vs `Error`
To see the difference is enough to see the interface and class hierarchy:
- `Object`
    - `Throwable`
        - `Error`: indicates serious problems that a reasonable application should not try to catch. It is recommended that they should not be thrown.
        - `Exception`: The class Exception and its subclasses are a form of Throwable that indicates conditions that a reasonable application might want to catch. 

So the difference is merely semantic!!


Git
=====================================================================
The definitions of this concepts where taken from the [documentation](https://git-scm.com/docs)
### `merge`
From docs: _Join two or more development histories together._   

### `rebase`
In the documention _rebase_ is under the _Patching_ section.   
From docs: _Reapply commits on top of another base tip_.   
When you execute `git rebase release dev`, git will try to apply each of the commits made
on `dev` branch on top of `release` branch. In other words, it will apply as many
patches over the `HEAD` of `release` as `dev` commits have.    
Moreover, if `dev` has _n_ commits, `git rebase` will try to perform _n_ merges with each 
one of the commit of `dev` on top of `release`. For that reason, if any of this merges will
have a conflict, you will be promted to solve by hand such conflicts.
The command specify which branch (`dev`) goes on top (`master`):
```sh
git rebase release dev
```
Here we have two different branches with a common ancestor and divergent stories:
```
* 4ce3629c1c381e107c114215c576283877d81e59 (master) »#ð.ð#»
* bb6f20fa077e22ecef2dfa79ff8911afab973e4c »#.#»
* 7c710455d4e1c0dee63870c736d8629d633054e5 .#.#.
| * 37936269ceb3cff2a7299e476bb6a69dd8da42b7 (HEAD -> dev) xæ~æx
| * 98c9ba64579d9e3d0db94b3b803e9d0cb70fc429 x.~.x
| * c43386cbbc7a41e65c1ba1ef0b81d50a0178c3ff x·x
|/  
*   ca77ca1bc2f2b917d3a23d4cea74aa5ae33d4a68 5··
```
The first step of `git rebase master dev` will apply `x·x`

### `cherry-pick`
In the documention _cherry-pick_ is under the _Patching_ section.    
From docs: _Apply the changes introduced by some existing commits_.    
As the docs said, `cherry-pick` will allow you to apply any commits in another branch to your 
current branch. Is a specialized version of `rebase`, however here you select what commits 
and in which order applied. It is a good way to apply a patch.  
The command specify from which branch you want to take the commits, and whats commits you will
apply:
```sh
git cherry-pick dev~5 dev~9
```

### squash
Not supported as an official operation within Git. To _squash_ commits means to 
join together several commits into one. This can be achieved with git rebase 
interactive session.

### fast-forwarding
After merging or applying patches your joined branches will share a common history and
the `HEAD` pointers could be mismatched after the operation:
```
* da9c60fa0eb023fe9a019d40e17c897ab4c097bd (HEAD -> dev) xæ~æx
* 81e5a5f3927434bc59f4f720847ef13b4b4bf4b2 x.~.x
* 3229ba2aba6e2002dee60a2d5cd1f4d7738c48ea x·x
* 4ce3629c1c381e107c114215c576283877d81e59 (master) »#ð.ð#»
* bb6f20fa077e22ecef2dfa79ff8911afab973e4c »#.#»
* 7c710455d4e1c0dee63870c736d8629d633054e5 .#.#.
*   ca77ca1bc2f2b917d3a23d4cea74aa5ae33d4a68 5··
|\  
| * 3f510a5c909e312747df5692fec208c741915748 ·25
| * 00654c4c7c32460cfb6095142fb1d3c6f798dfa4 .=ø|ø=.
| * 582f100bd55a4a2f60300747aa76e65c619a3f03 .=|=.
| * 4e69eda90c41c3876f0322e10ca9e1e54d763b5a .=.
* | bff1ee25219a4425532b1962b11ab89e62744f91 .o-|-o.
* | 02710fa9dc83eea717a2895a46baee6a02bfd3ce .o-o.
* | 5dd4d59bfd02694eb42adb8e9df25d83d3574508 .oo.
* | 28c1eb419fd01b23ba674bcf0c7b8ece5aa0eaa6 ··
* | c3cf575ac6ea8a23502610adc5c1283bb0a04657 ++
```
_fast forwarding_ means to advance the pointer of the left behind brances.
It is colled _fast_ since does not involve any merging computation:

```
* da9c60fa0eb023fe9a019d40e17c897ab4c097bd (HEAD -> master, dev) xæ~æx
* 81e5a5f3927434bc59f4f720847ef13b4b4bf4b2 x.~.x
* 3229ba2aba6e2002dee60a2d5cd1f4d7738c48ea x·x
* 4ce3629c1c381e107c114215c576283877d81e59 »#ð.ð#»
* bb6f20fa077e22ecef2dfa79ff8911afab973e4c »#.#»
* 7c710455d4e1c0dee63870c736d8629d633054e5 .#.#.
*   ca77ca1bc2f2b917d3a23d4cea74aa5ae33d4a68 5··
|\  
| * 3f510a5c909e312747df5692fec208c741915748 ·25
| * 00654c4c7c32460cfb6095142fb1d3c6f798dfa4 .=ø|ø=.
| * 582f100bd55a4a2f60300747aa76e65c619a3f03 .=|=.
| * 4e69eda90c41c3876f0322e10ca9e1e54d763b5a .=.
* | bff1ee25219a4425532b1962b11ab89e62744f91 .o-|-o.
* | 02710fa9dc83eea717a2895a46baee6a02bfd3ce .o-o.
* | 5dd4d59bfd02694eb42adb8e9df25d83d3574508 .oo.
* | 28c1eb419fd01b23ba674bcf0c7b8ece5aa0eaa6 ··
* | c3cf575ac6ea8a23502610adc5c1283bb0a04657 ++
```


Spring Boot
=====================================================================

Spring Framework
-------------------------------------------------
What is:
- Application Framework.
    - Can be used on any app.
    - Has extensions that can be used for web applications.
- Inversion of Control web container (more below).

At this point, to setup and run this framework is hard due the great amount of configurations.
_Spring Boot_ appears as an auto-configurable and standalone solution for writting 
web applications.

### Web Container
Is the component of a **web server** software that interacts with **Java Servelts**.

### Inversion of Control
Inversion control is a software architecture where you write program snippets
that will be called by the coordinating framework. Since you are not writting
the _main_ programm, the control of your software is being driven by the framework,
for that reason is called _inversion of control_.


Spring Boot
-------------------------------------------------
Is the _Spring Framework_ previously defined but with the following added capabilities:
- Is stand-alone. You do not need to configure a web server appart (e.g. Tomcat)
    * This avoid to have to deploy _war_ files and the associated overhead.
- Comes with _starters_, a precofigured collection dependencies that ease the job.
- Driven by _convention over configuration_
- No XML configuration.

### Actuator
This sample was taken from the official [guide](https://spring.io/guides/gs/actuator-service/#scratch).

To run and try the sample [application](code/actuatordemo/src/main/java/smpl/jcammmmm/actuatordemo/ActuatordemoApplication.java):
0. Must have the `Java 11` runtime
1. `mvn compile`
2. `mvn spring-boot:run`
3. `curl http://localhost:8080/actuator/health`
4. `curl http://localhost:8080/hi?name=Kami`

### @Component vs @Service
Both belong to `org.springframework.stereotype` package. Here you will find _Annotations denoting the roles of types or methods in the overall architecture (at a conceptual, rather than implementation, level)._
- `@Component`: Such classes are considered as candidates for auto-detection when using annotation-based configuration and classpath scanning.
- `@Service`: Specialization of `@Component`. Only offers a semantic difference. _Originally defined by Domain-Driven Design (Evans, 2003) as "an operation offered as an interface that stands alone in the model, with no encapsulated state"_. Is a general purpose stereotype left to let the teams decide its semantics based on its particular usage within the system.
- `@Repository`: Specialization of `@Component`.
- `@Controller`: Specialization of `@Component`.

Then, the difference again is merely semantic! You use `@Component` when you have something that perform something very generic, but a `@Service` when you have something that does not enclose an encapsulated state.

### @Qualifier
When applied to a field or parameter, will allow you to choose which bean to inject when that field is defined by an interface. In other words, will allow you to aim the polymorphic behavior of what is bein injected at runtime.
From [documentation](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/factory/annotation/Qualifier.html): _This annotation may be used on a field or parameter as a qualifier for candidate beans when autowiring. It may also be used to annotate other custom annotations that can then in turn be used as qualifiers._

### Anotation Scope and @Scope("prototype")
To understand this it is important to know what _scope_ means. Following the [docs](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html), _scope_ is a _Class bean_ attribute that specifies how the instances are being returned by the framework. There are several kinds of _scopes_:
* singleton: single bean definition to a single object instance for each Spring IoC container.
* prototype: the non-singleton prototype scope of bean deployment results in the creation of a new bean instance every time a request for that specific bean is made. That is, the bean is injected into another bean or you request it through a `getBean()` method call on the container. 
* request: single bean definition per a single HTTP request.
* session: single bean definition per HTTP Session.
* application: single bean definition per lifecycle of a ServletContext.

So when you anotate a bean with `@Scope("prototype")`, it will create a new instance each time a bean is defined. For that reason it is recommended when is important to you the state of your application.

JUnit
=====================================================================
Unit testing focuses on interfaces, that means to check the methods return values based on a given value. JUnit is framework on which you can write and execute unit tests.
The code samples was taken from [JUnit samples](https://github.com/junit-team/junit5-samples/tree/r5.10.0/junit5-jupiter-starter-maven) repository.

@ParametrizedTest
-------------------------------------------------
With this annotation you can provide input for each of your test scenarios so you can run the test several times for each of these inputs.   
The sample of [this](code/utest/src/test/java/sampl/jacammmmm/AppTest.java) unit tests illustrates the `@Parametrized` annotation usage.   
Together with this annotation it is important to know how to provide that input to the method. That input can be provided with the following annotations. More details can be found in the [docs](https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests):   

* `@ArgumentsSource`
* `@MethodSource`
* `@ValueSource`
* `@EnumSource`
* `@CsvSource`


@ExtendWith
-------------------------------------------------
In the context of _Spring Boot_ programming, one can infer that `@ExtendWith` annotation integrates contexts to the _JUnit Jupiter_ programming model.
Whe you write test for an SpringBoot application, you must put the `@SpringBootTest` annotation. This annotation is defined [as](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/test/context/SpringBootTest.html) follows:
```java
@Target(TYPE)
@Retention(RUNTIME)
@Documented
@Inherited
@BootstrapWith(SpringBootTestContextBootstrapper.class)
@ExtendWith(org.springframework.test.context.junit.jupiter.SpringExtension.class)
public @interface SpringBootTest
```

The `SpringExtension` extension has the following signature:

```java
public class SpringExtension
extends Object
implements org.junit.jupiter.api.extension.BeforeAllCallback, org.junit.jupiter.api.extension.AfterAllCallback, org.junit.jupiter.api.extension.TestInstancePostProcessor, org.junit.jupiter.api.extension.BeforeEachCallback, org.junit.jupiter.api.extension.AfterEachCallback, org.junit.jupiter.api.extension.BeforeTestExecutionCallback, org.junit.jupiter.api.extension.AfterTestExecutionCallback, org.junit.jupiter.api.extension.ParameterResolver
```

After reading the [documention](https://junit.org/junit5/docs/current/user-guide/#extensions) on JUnit extensions, one can see through the examples that what an _extension_ does is to prepare the test execution context by defining what it is being injected or what shall be executed before or after each unit testing method.

`MockitoExtension` [extension](https://javadoc.io/doc/org.mockito/junit-jupiter/latest/index.html) allows you to create mocks in your unit tests.


Mockito
=====================================================================
Unit testing focuses on interfaces, that means to check the methods return values based on a given value.   
A single method can call serveral methods in its definition block, so the current return result of this method is function of those inner results. One way to control the test scenarios is by _mocking_ the objects (.i.e creating fake objects) that perform that innercalls, that in turn will return values that you want to test.   
In particular, sometimes one of those inner calls implements a database query, so in order to ease the code testing it is better to mock that database calls.
_Mockito_ is a mock framework that let you to create mock instances in your testing code. The sample code can be found [here](code/utest). That code was generated with _maven archetypes_.

In order to have Mockito integrated with JUnit I followed this [documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html#junit5_mockito) and [this](https://javadoc.io/doc/org.mockito/mockito-junit-jupiter/latest/org/mockito/junit/jupiter/MockitoExtension.html).


`@Mock` vs `Mockito.spy()`
-------------------------------------------------
- `mock(Something.class)`: mockito framework will instance a mock of `Something` for you.
- `spy(somethig)`: you must create first the instance, and the stub method calls will be made over this `something` instance. The documentation refer to this as _partial mocking_. In fact, your are spying the method calls of your created instance.

The following usages are quivalent:
* `A a = mock(A.class);` == `@Mock A a;` == `A a = Mockito.mock(A.class);`
* `A a = spy(e);` == `@Spy A a = new A();` == `A a = Mockito.spy(e);`

Kafka
=====================================================================
1. Install Docker
2. Pull the image from Docker hub `docker pull bitnami/kafka`
3. Run the docker-compose.yml they provide in the page `docker compose up -d`
```yml
version: "2"

services:
  kafka:
    image: docker.io/bitnami/kafka:3.5
    ports:
      - "9092:9092"
    volumes:
      - "kafka_data:/bitnami"
    environment:
      # KRaft settings
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka:9093
      # Listeners
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
volumes:
  kafka_data:
    driver: local
```
4. Go to the Kafka [quickstart](https://kafka.apache.org/quickstart)
5. Follow the tutorial.
    * Simple topic consuming
        1. Access the container: `docker exec -ti kafka-kafka-1 bash`
        2. `cd /opt/bitnami/kafka`
        3. Create a topic with `bin/kafka-topics.sh`
        4. Produce and put messages with `bin/kafka-console-producer.sh`
        5. Read message from `$ bin/kafka-console-consumer.sh`
    * Reading-then-writting to a file with _Kafka Connect_
        1. Update the configuration `echo "plugin.path=libs/connect-file-3.5.0.jar" >> config/connect-standalone.properties`
        2. Create the message source file `echo -e "foo\nbar" > test.txt`
        3. Launch the connector `bin/connect-standalone.sh config/connect-standalone.properties`
        4. See the populated topic `bin/kafka-console-consumer.sh`
        5. See how the file is being written `more test.sink.txt`
    * Implement some _Kafka Streams_
        1. 

Relational Databases
=====================================================================
- docker volumes
    - https://docs.docker.com/storage/volumes/#use-a-volume-with-docker-compose
    - https://github.com/docker-library/docs/blob/master/postgres/README.md#arbitrary---user-notes
- docker-compose up -d
- sudo apt install postgresql-client
- psql -U postgres -h 192.168.0.20 
- pg_restore -U postgres -h 192.168.0.20 -d dvdrental dvdrental.tar 
- sample database: https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/
- schema: https://www.postgresqltutorial.com/wp-content/uploads/2018/03/printable-postgresql-sample-database-diagram.pdf

Stored Procedures
-------------------------------------------------
install dbeaver to develop more easyly the stored procedure.


Software Design
=====================================================================
- OOP principles
    * Abstraction
    * Encapsulation
    * Inheritance
    * Polymorphism
- SOLID
    * Single-responsability: clear defined purpose of each class.
    * Open-closed: open for extension closed for modification
    * Liskov substitution: all you can do to a class, it can be done to any child subclass (polymorphism).
    * Interface segregation: do not implement interfaces you donot use.
    * Dependency inversion: Depend on abstraction, not in concretions.
- Design Patterns
- SDLC (Software Development Life Cycle)
    * Design
    * Develop
    * Test
    * Integrate
    * Deploy
    * Mantain
    * Evaluate
- DRY (Don't repeat yourself)
    * If something repeates, replace it with an abstraction
    * Every recognizable piece of order (information) should be unique within the system.
- TDD (Test driven development)
    * Write test first, implement after
- Integration tests
    * Run tests mixing several layers of you MVC
- Test pyramid
    1. UI Tests
    22. Integration tests
    333. Unitests
- High Quality Code Features?