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
    - DRY 
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


### Anotation Scope