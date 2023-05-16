package org.example;

import java.io.FileOutputStream;
import java.sql.*;

class JDBCTest {
public static void main(String args[]) {
Connection conn = null;
PreparedStatement preparedStatement = null;

        String query = "select * from table1 where c1 = 1";

        try {
            //get connection
            conn = Database.getConnection();

            //create preparedStatement
            preparedStatement = conn.prepareStatement(query);

            //execute query
            ResultSet resultSet = preparedStatement.executeQuery();
            resultSet.next();

            Blob clob = resultSet.getBlob(2);
            byte[] byteArr = clob.getBytes(1, (int) clob.length());

            FileOutputStream fileOutputStream =
                    new FileOutputStream("D:\\Temporary\\savedImage.jpg");
            fileOutputStream.write(byteArr);

            System.out.println("Image retrieved successfully.");

            //close connection
            fileOutputStream.close();
            preparedStatement.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

class Database {
public static Connection getConnection() {
Connection connection = null;
try {
Class.forName("com.mysql.cj.jdbc.Driver");
String url = "jdbc:mysql://localhost:3306/sms";
String username = "root";
String password = "root";
connection = DriverManager.getConnection(url, username, password);
} catch (Exception e) {
e.printStackTrace();
}
return connection;
}
}