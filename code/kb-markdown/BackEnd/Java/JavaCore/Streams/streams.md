## anyMatch

```
import java.util.ArrayList;
import java.util.List;

public class Source {
    public static void main(String[] args) {

        List<Student> students =  new ArrayList<>();
        students.add(new Student(1, "John"));
        students.add(new Student(2, "Lisa"));

        System.out.println(students.stream().anyMatch(t -> t.name.equals("John"))); // true
        System.out.println(students.stream().anyMatch(t -> t.name.equals("Mary"))); // false
    }
}

class Student {

    int id;
    String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

## sum

```
int[] a = {10,20,30,40,50};
int sum = IntStream.of(a).sum();
System.out.println("The sum is " + sum);
```

## example

```
import java.util.*;
import java.util.stream.*;

class Source {
    public static void checkPassengers(Stream<Passenger> passengerStream) {
        /*
         * TODO: Print space-separated passenger names in all capital letters where passenger id
         * is <= 10
         */


        passengerStream
                .filter(p -> p.getId() <= 10)
                .map(p -> p.getName().toUpperCase() + " ")
                .forEach(System.out::print);
    }

    public static void main(String[] args) {
        List<Passenger> passengers;
        if (args != null && args.length != 0) {
            passengers = getPassengersFromMainArgs(args);
        } else {
            passengers = getPassengers1();
            //uncomment below line and comment above line for testing sample test case 2
//         passengers = getPassengers2();
        }
        checkPassengers(passengers.stream());

    }

    public static List<Passenger> getPassengers1() {
        Passenger p1 = new Passenger(3, "aakash");
        Passenger p2 = new Passenger(13, "Aayush");
        Passenger p3 = new Passenger(6, "Karan");

        Passenger p4 = new Passenger(8, "Swati");
        Passenger p5 = new Passenger(25, "MAYA");
        Passenger p6 = new Passenger(30, "Rakesh");

        Passenger p7 = new Passenger(7, "alex");
        Passenger p8 = new Passenger(18, "john");
        return Arrays.asList(p1, p2, p3, p4, p5, p6, p7, p8);
    }

    public static List<Passenger> getPassengers2() {
        Passenger p1 = new Passenger(3, "Joseph");
        Passenger p2 = new Passenger(4, "Yeshwanth");
        Passenger p3 = new Passenger(5, "Rahul");
        Passenger p4 = new Passenger(6, "Meena");
        return Arrays.asList(p1, p2, p3, p4);
    }

    public static List<Passenger> getPassengersFromMainArgs(String[] args) {
        List<Passenger> list = new ArrayList<>();
        for (int i = 0; i < args.length; i++) {
            String[] arr = args[i].split(",");
            if (arr.length >= 2) {
                Passenger p = new Passenger(Integer.parseInt(arr[0]), arr[1]);
                list.add(p);
            }
        }

        return list;
    }
}

class Passenger {
    private int id;
    private String name;

    public Passenger(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
```

## sort

```
list.sort((o1, o2) -> o1.getSalary() - o2.getSalary()) // ascending
list.sort((o1, o2) -> o2.getSalary() - o1.getSalary()) // descending
```

## 3 distinct min in array

```
int[] arr
copy of arr 
sort 
print first 3 of arr 

using stream 
// create stream 
IntStream.of(arr) 

// process stream 
.distinct()
.sort()
.limit(3)

// consume 
.forEach(x -> sout(x))

or  
// process stream 
.distinct()
.sort()
.limit(3)
.sum 

// consume 
.getAsInt()
```

## on objects

find 3 highest salary name
list of employess

// given
employess = list of employess

// create stream
employess.stream()

// process
.sorted(Comparator.comparingInt(Employee::getSalary).reversed())
.filter(x -> isActive(x))
.limit(3)
.map(Employee::getName)

//consume
.forEach(x -> sout(x))
.collect(Collectors.toList())

## name join

Collectors.joining(", ")

## group by dept

civil -> ram, shyam
cs -> saksham, sahitya

Collectors.groupingBy(x -> x.dept)

## count of emp in each dept

Collectors.groupingBy(Employee::getDept, Collectors.counting())

## multi threading

.parallel()

Arrays.stream(arr).sum(); // sum
Arrays.stream(arr).filter(x -> x < 4).foreach(print)

