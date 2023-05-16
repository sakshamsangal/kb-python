```
run time memory allocation: memory is allocated at run time. e.g. linked list
compile time memory allocation: memory is allocated at compile time. e.g. int a


1. Does it allocates memory at compile time - when the class or method is invoked?
Class gets memory at compile time while object gets memory at run time.


2. At which step while compiling the memory is allocated.
When JVM takes the byte code, it is then compiled. Java code is converted into byte code and then JVM converts the byte code into machine code.


3. Why stack memory is used and not heap memory at compile time.
Stack is used to store static memory allocation(whose size is fixed) and heap is used for dynamic memory allocation.
```