interface Car {
public void color();
public void price();
}

class Celerio implements Car {
public void color() {
System.out.println("white");
}
public void price() {
System.out.println("600000");
}
}

interface Bike {
public void gear();
}

class Pulsar implements Bike {
public void gear() {
System.out.println("4");
}
}

class CarAdapter implements Bike {
Car car;

    public CarAdapter(Car car) {
        this.car = car;
    }

    public void gear() {
        car.price();
    }

}

class Main {
public static void main(String[] args) {
Celerio celerio = new Celerio();
celerio.color();
celerio.price();

        Bike bike = new Pulsar();
        bike.gear();

        Bike birdAdapter = new CarAdapter(celerio);
        birdAdapter.gear();
    }

}
