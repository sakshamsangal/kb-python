```
// database name = localhost:port:SID
// localhost = hostname
// 1521 = port 
// xe = SID
```

## oracle database connection

```
try {
    Class.forName("oracle.jdbc.driver.OracleDriver");
    String url = "jdbc:oracle:thin:@localhost:1521:xe"; 
    String username = "SYSTEM"; 
    String password = "Mayankbagga@10"; 

    con = DriverManager.getConnection(url, username, password);
    System.out.println("connection established");
} catch(Exception e){
    System.out.println(e);
}
```

## mysql connection

```
try {
    Class.forName("com.mysql.cj.jdbc.Driver");
    String url = "jdbc:mysql://localhost:3306/springjdbctemplate";
    String username = "root"; 
    String password = "root"; 

    con = DriverManager.getConnection(url, username, password);
    System.out.println("connection established");
}
catch(Exception e){
    System.out.println(e);
}
```

## Database class

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database {
    public static Connection getConnection() {
        Connection connection = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/school";
            String username = "root";
            String password = "root";
            connection = DriverManager.getConnection(url, username, password);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return connection;
    }
}

```