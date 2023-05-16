```java
class Student {
    String name;
    String rollNo;


    public Student(String name, String rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", rollNo='" + rollNo + '\'' +
                '}';
    }
}

class StudentBuilder {
    String name;
    String rollNo;

    public StudentBuilder setName(String name) {
        this.name = name;
        return this;
    }

    public StudentBuilder setRollNo(String rollNo) {
        this.rollNo = rollNo;
        return this;
    }

    public Student build(){
        return new Student(name, rollNo);
    }
}

class Main {
    public static void main(String[] args) {
        Student student = new StudentBuilder().setName("saksham").setRollNo("123").build();

        System.out.println(student);
        // Student{name='saksham', rollNo='123'}
    }
}
```