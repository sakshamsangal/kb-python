```

package java.util;

public class Stack<E> extends Vector<E> {
    public Stack() { }

    public E push(E item) {
        addElement(item);
        return item;
    }

    public synchronized E pop() {
        E obj;
        int len = size();
        obj = peek();
        removeElementAt(len - 1);
        return obj;
    }

    public synchronized E peek() {
        int len = size();
        if (len == 0) throw new EmptyStackException();
        return elementAt(len - 1);
    }

    public boolean empty() {
        return size() == 0;
    }

    public synchronized int search(Object o) {
        int i = lastIndexOf(o);
        if (i >= 0) return size() - i;
        return -1;
    }
}

```

```
Stack is the subclass of Vector. Since stack follows LAST IN FIRST OUT order, So we can stack for reversing list.

Basic structure of Stack class in Java 8.
package java.util;
public class Stack<E> extends Vector<E> {
    public Stack() {}
    public E push(E item) {}
    public synchronized E pop() {}
    public synchronized E peek() {}
    public boolean empty() {}
    public synchronized int search(Object o) {}
}


let list = [10, 20, 30]

There are 4 ways in which we can reverse the list.
Method 1:
import java.util.*;
class Demo {
    static void reverseArrayList(ArrayList<Integer> list) {
        Stack<Integer> stack = new Stack<>();

        for (int value : list) {
            stack.add(value); // add item to stack
        }

        int i = 0;
        while (!stack.empty()) {
            list.set(i++, stack.pop()); // 30 20 10
        }
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        reverseArrayList(list);
        System.out.println(list); // [30, 20, 10]
    }
}


Method 2: Using stack.addAll(list) and list.clear()
Instead of for loop we can directly put all items of list into the stack by:

import java.util.*;

class Demo {
    static void reverseArrayList(ArrayList<Integer> list) {
        Stack<Integer> stack = new Stack<>();
        stack.addAll(list); // [10, 20, 30]

        list.clear();
        while (!stack.empty()) {
            list.add(stack.pop()); // 30 20 10
        }
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        reverseArrayList(list);
        System.out.println(list); // [30, 20, 10]
    }
}

Method 3: Using Collections.reverse(list)
import java.util.*;

class Demo {
    static void reverseArrayList(ArrayList<Integer> list) {
        Collections.reverse(list);
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        reverseArrayList(list);
        System.out.println(list); // [30, 20, 10]
    }
}



Method 4: Using for-loop and iterate the list in backward direction.
import java.util.*;

class Demo {
    static void reverseArrayList(ArrayList<Integer> list) {
        ArrayList<Integer> revArrayList = new ArrayList<>();
        for (int i = list.size() - 1; i > -1; i--) {
            revArrayList.add(list.get(i));
        }
        list.clear();
        list.addAll(revArrayList);
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        reverseArrayList(list);
        System.out.println(list); // [30, 20, 10]
    }
}

```