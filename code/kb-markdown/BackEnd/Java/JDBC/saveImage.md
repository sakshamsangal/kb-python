package org.example;

import java.io.FileInputStream;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
class InsertImageToMySqlDB {
public static void main(String args[]) throws Exception{
//Registering the Driver
DriverManager.registerDriver(new com.mysql.jdbc.Driver());
//Getting the connection
String mysqlUrl = "jdbc:mysql://localhost/sms";
Connection con = DriverManager.getConnection(mysqlUrl, "root", "root");
System.out.println("Connection established......");
PreparedStatement pstmt = con.prepareStatement("INSERT INTO table1 VALUES(1,?)");
InputStream in = new FileInputStream("D:\\Temporary\\images.png");
pstmt.setBlob(1, in);
//Executing the statement
pstmt.execute();
System.out.println("Record inserted......");
}
}