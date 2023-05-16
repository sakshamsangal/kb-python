protected is same as public except in the case when the package is different and class is not sub class.

```
package  p1;
public class Coffee {
     protected void order() {
        System.out.println("Coffee");
    }
}

package p2;
import p1.Coffee;

class Cappuccino {
    public static void main(String args[]) {
        Coffee c = new Coffee();
        c.order(); // not allowed
    }
}
```

For reference:
https://www.geeksforgeeks.org/access-modifiers-java/