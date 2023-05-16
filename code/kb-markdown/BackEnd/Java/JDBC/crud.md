```
public class Crud {

    public static Statement statement;

    public static void delete(int studentRollNumber) throws SQLException {
        String sql = "DELETE FROM student WHERE student_roll_number = " + studentRollNumber;
        statement.executeUpdate(sql);
    }

    public static void insert(long studentRollNumber, String studentName) throws SQLException {
        String sql = "INSERT INTO student VALUES (" + studentRollNumber + ", '" + studentName + "')";
        statement.executeUpdate(sql);
    }

    public static void update(int studentRollNumber, String studentName) throws SQLException {
        String sql = "UPDATE student SET student_name = '" + studentName + "' " + " WHERE student_roll_number = " + studentRollNumber;
        statement.executeUpdate(sql);
    }

    public static Student search(int studentRollNumber) throws SQLException {
        String sql = "SELECT * FROM student WHERE student_roll_number = " + studentRollNumber;
        ResultSet resultSet = statement.executeQuery(sql);

        Student student = new Student();
        if (resultSet.next()) {
            student.setRollNumber(resultSet.getInt(1));
            student.setStudentName(resultSet.getString(2));
        }
        return student;
    }

    public static List<Student> view() throws Exception {
        String sql = "SELECT * FROM student";
        ResultSet resultSet = statement.executeQuery(sql);

        List<Student> students = new ArrayList<>();
        while (resultSet.next()) {
            Student student = new Student();
            student.setRollNumber(resultSet.getInt(1));
            student.setStudentName(resultSet.getString(2));
            students.add(student);
        }
        return students;
    }

    static {
        try {
            Crud.statement = Database.getConnection().createStatement();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

}


```