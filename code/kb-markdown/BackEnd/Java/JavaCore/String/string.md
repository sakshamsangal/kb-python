To print an object means we are calling toString() method implemented by the class. If the class has not implemented
toString() method then className@hashcode will be printed.

## int to string

```
 public static void main(String[] args) {
        int a = 12;
        // method 1
        String str = a + "";

        // method 2
        String.valueOf(a);

        // method 3
        Integer.toString(a);
    }
```