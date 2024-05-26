Understanding Distributed Systems
===========================================================
> In this document I will write my research about the understanding of distributed system. At time of this writting (202405) there was not an unified resource that guide you to the concepts in a reasonable time, without to read a entire book (e.g. Tannebaum book on Distributed Computing).   
> What I'm searching is a sort of standarized notation, a computer model and a set of problems proposed on this computer model with the standarized notation, that allow me to understand efficiently the problems.   
> At this time I do not find such kind of learning materials, so in this document I will document my findings.  

Looking for Bibliography
===========================================================
When I started to study this subject I begin with the Zookeeper doucmentation. I arrived to that project after being acquanted of the popularity of Apache Kafka. In some [part](https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html) of the introductory material a tech talk at Yahoo! is linked.    
After looking at that video, I reached a [class](https://www.youtube.com/watch?v=pbmyrNjzdDk) on the same subject. The teacher there uses a nice notation that resembles something like this:   
_Write to variable x value 0_:= `|---------Wx0-----------|`   
_Read variable x the value 1_:= `|---------Rx1-----------|`   
I found this notation interesting since timelines in distributing computing are important, and this notation makes emphasis on that,I feel that this something that I will use in my career.   
After watching this videos I realized that the problem is called _Consensus_.   
There was another [professor](http://www.distributedsystemscourse.com/) that I reached through YouTube. In my opinion he is putting an effort on these since as I state in the introduction of these ddocument there is no a bible about this subject. He did a great work. After following the course page, I found that the first introductory problem he handles is called _The Bizantine Fault_.    
At the beginning a did not understand the problem. After reading a couple of hours I found that this problem was [stated](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/) by Leslie Lamport a well know computer scientist in 1982. In on this paper he says that this problem is the generalization of the _Chinese Generals Problem_.   

Starting study material
===========================================================
### Concepts Basics
* [Two General's Problem](https://en.wikipedia.org/wiki/Two_Generals'_Problem)
* [Lamport's Paper](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/)

### Online Open Courses
* https://ocw.mit.edu/courses/6-824-distributed-computer-systems-engineering-spring-2006/pages/syllabus/
  - This syllabus references the Tanenbaum's book.
* [Chris Colohan Free course](http://www.distributedsystemscourse.com/)
  - This course also reference the Tanenbaum's book.

### Papers
* https://lamport.azurewebsites.net/pubs/solved-and-unsolved.pdf
* https://crypto.ethz.ch/publications/files/Fitzi03.pdf

### Related documents:
These three documents are related, after a quick scroll and looking at similar diagrams.
* [Presentation from Imperial College London](https://www.doc.ic.ac.uk/~jnm/DistrAlg/Notes/Byzantine-4up-final.pdf)
* [Presentation Free Course](https://docs.google.com/presentation/d/1FXzVtuvhOzaLdbr-c8poClewx7b7Yi48eO1j_RuLLkI/edit#slide=id.g17ffff97a2_0_42)
* [Lamport's Paper](https://lamport.azurewebsites.net/pubs/byz.pdf)
