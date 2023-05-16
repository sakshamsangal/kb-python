```
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.ObjectInputStream;

public class Source {
   public static User deserializeUserData(String fileName) {

      /*
       * TODO: Read the file and deserialize the user data; convert the data into
       * User object
       */

      User user = null;
      try (InputStream is = new FileInputStream(fileName);) {
         ObjectInputStream in = new ObjectInputStream(is);
         user = (User) in.readObject();
      } catch (Exception e) {
         e.printStackTrace();
      }
      return user;
   }

   public static void main(String args[]) {
      String fileName;
      if(args != null && args.length != 0) {
         fileName = args[0];
      } else {
         fileName = "src/user1.txt";
      //uncomment below line and comment above line for testing sample test case 2
//         fileName = "/code/workspace/user2.txt";
      }

      User user = deserializeUserData(fileName);
      System.out.print(user.getName() + " " + user.getEmail());
   }
}


import java.io.Serializable;

public class User implements Serializable {
   private String name;
   private String email;

   public String getName () {
      return name;
   }
   
   public String getEmail () {
      return email;
   }

   public void setName(String name) {
      this.name = name;
   }

   public void setEmail(String email) {
      this.email = email;
   }
}


¬í sr UserUý¸ÑÈŽ L emailt Ljava/lang/String;L nameq ~ xpt arun@gmail.comt Arun
```