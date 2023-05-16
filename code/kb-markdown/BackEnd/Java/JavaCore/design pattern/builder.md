class Student {
int rollNumber;
String name;

    public Student(DoSetterInjectionForMe doSetterInjectionForMe) {
        rollNumber = doSetterInjectionForMe.rollNumber;
        name = doSetterInjectionForMe.name;
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollNumber=" + rollNumber +
                ", name='" + name + '\'' +
                '}';
    }

}
class DoSetterInjectionForMe {
int rollNumber;
String name;

    public void setRollNumber(int rollNumber) {
        this.rollNumber = rollNumber;
    }

    public void setName(String name) {
        this.name = name;
    }

}
class Source {
public static void main(String[] args) {
DoSetterInjectionForMe injection = new DoSetterInjectionForMe();
injection.setRollNumber(123);
injection.setName("Saksham");
Student student = new Student(injection);
System.out.println(student);
}
}

Student{rollNumber=123, name='Saksham'}

class Student {
int rollNumber;
String name;

    public Student(DoSetterInjectionForMe doSetterInjectionForMe) {
        rollNumber = doSetterInjectionForMe.rollNumber;
        name = doSetterInjectionForMe.name;
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollNumber=" + rollNumber +
                ", name='" + name + '\'' +
                '}';
    }

    static class DoSetterInjectionForMe {
        int rollNumber;
        String name;

        public DoSetterInjectionForMe setRollNumber(int rollNumber) {
            this.rollNumber = rollNumber;
            return this;
        }

        public DoSetterInjectionForMe setName(String name) {
            this.name = name;
            return this;
        }

        Student getStudentObject() {
            return new Student(this);
        }
    }

}

class Source {
public static void main(String[] args) {
Student student = new Student.DoSetterInjectionForMe().setRollNumber(123).setName("Saksham").getStudentObject();
System.out.println(student);
}
}

Student{rollNumber=123, name='Saksham'}
