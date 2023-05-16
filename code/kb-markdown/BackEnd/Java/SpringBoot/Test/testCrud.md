```

public interface StudentRepository extends CrudRepository<Student, Long> {

}

@Test
public void testCreateStudent() {

    Student student = new Student();
    student.setName("John");
    student.setCourse("Java Web Services");
    student.setFee(30d);

    studentRepository.save(student);
}


@Test
public void testFindStudentById() {
    Optional<Student> optionalStudent = studentRepository.findById(1l);
    if (optionalStudent.isPresent()) {
        Student student = optionalStudent.get();
        System.out.println(student);
    }
}

@Test
public void testUpdateStudent() {
    Optional<Student> optionalStudent = studentRepository.findById(3l);
    if (optionalStudent.isPresent()) {
        Student student = optionalStudent.get();
        student.setFee(40d);
        studentRepository.save(student);
    }
}

@Test
public void testDeleteStudent() {
    Student student = new Student();
    student.setId(1l);
    studentRepository.delete(student);
}

```