```
Hi Vaibhav,

Abstraction is the process of hiding certain details and showing only essential information to the user. A class which is declared with the abstract keyword is known as an abstract class in Java. It can have abstract and non-abstract methods (method with the body).


Example:
abstract class Person {
    abstract void setNationality();
}

class Student extends Person {

    @Override
    void setNationality() {
        System.out.println("Indian");
    }
}
class Main {
    public static void main(String[] args) {
        new Student().setNationality(); // Indian
    }
} 


You can read more details on the same at the following link.
https://www.javatpoint.com/abstract-class-in-java

Hope this helps!
```