```text
Hi Divya,

Collections.reverse() reverses the order of elements in a list passed as an argument.  The elements need to be of object type. 


You can do something like this:

import java.util.Arrays;
import java.util.Collections;

class Main {
    public static void main(String[] args) {
        Integer[] arr = {1,2 ,3};
        Collections.reverse(Arrays.asList(arr));
        System.out.println(Arrays.toString(arr)); // [3, 2, 1]
    }
}
I hope it helps!
```

```
import java.util.Stack;

class Demo {
    public static void main(String[] args) {
        int[] arr  = {1,2,3};
        reverseArray(arr);
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
            // 3 2 1 
    }

    private static void reverseArray(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        for (int value : arr) {
            stack.add(value);
        }

        int i = 0;
        while (!stack.empty()) {
            arr[i++] = stack.pop();
        }

    }
}
```