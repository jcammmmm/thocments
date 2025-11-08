# What is a computer program
Is a set of _ordered_ instructions that alter the state of an electronic 
memory. Every computer program has an entry and an output that can be empty. 
Emptyness is as important here as having the number zero in our numbering 
systems.

A computer program can have another computer programs nested within it. Given
that, we can have a full graph of computer programs that are in relationship
ones with anothers, each one having clearly defined its inputs and outputs.




# How we store computer programs today
As an electronic text files.


# Splitting computer programs
When you begin to work on complete solutions of computer software, you 
will get an inconvenient state where you find that the text files are 
too big. So appears the need to split the program in chunks.

How you can do that. Well you first identify, that a program can have
a several set of inputs that characterizes every run, so why not
to set appart the variables that will encolose your program, and then
define several subprograms grouped into that program...

# Pass by value and pass reference
In bash you only have pass by value, that is you do not have the behavior
as in matemathics e.g.:

  x = 4 
  d = 2x
  x = 6
  print(d) # 8
  
In bash you need to reevaluate the expression to become this true:
  
  x = 4 
  d = 2x
  x = 6
  d = 2x
  print(d) # 12
  
