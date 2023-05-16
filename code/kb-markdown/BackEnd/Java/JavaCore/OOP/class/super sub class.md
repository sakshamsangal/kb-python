# What happens if both superclass and subclass have a field with same name?

```
Field value gets override.

class Car {
    String color = "white";
}

class SuperCar extends Car {
    String color = "yellow";
}

class Main {
    public static void main(String[] args) {
        SuperCar superCar = new SuperCar();
        System.out.println(superCar.color); // yellow
    }
}
 

if SuperCar is empty then,

class Car {
    String color = "white";
}

class SuperCar extends Car {
    // String color = "yellow";
}

class Main {
    public static void main(String[] args) {
        SuperCar superCar = new SuperCar();
        System.out.println(superCar.color); // white
    }
}

```