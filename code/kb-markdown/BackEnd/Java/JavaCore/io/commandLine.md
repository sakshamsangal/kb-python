```
class Main {
    public static void main(String[] args) {

        // command line argument: john mary kat
        for (String val : args) {
            System.out.println(val);
        }

        // output:
        // john
        // mary
        // kat
    }
}
```