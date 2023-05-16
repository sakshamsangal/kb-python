Inheritance:

Inheritance is one in which a new class is created that inherits the properties of the already exist class. It supports
the concept of code reusability and reduces the length of the code in object-oriented programming.

class Car {
void show() {
System.out.println("Car");
}
}

// inheritance
class SuperCar extends Car {

    // run time polymorphism
    @Override
    void show() {
        System.out.println("SuperCar");
    }

}

class Main {
public static void main(String[] args) {
SuperCar superCar = new SuperCar();
superCar.show(); // SuperCar
}
}
