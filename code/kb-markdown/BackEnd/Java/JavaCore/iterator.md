```
You can remove objects using an iterator, but you can't do it with a for each loop

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


class Test {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            list.add(i);
        }
        Iterator<Integer> itr = list.iterator();

        while (itr.hasNext()) {
            // removing odd numbers   
            if (itr.next() % 2 != 0) itr.remove();
        }
        System.out.println(list);
        // 0 2 4 6 8
    }
}
And there is the ListIterator<E> which provides two-way traversal it.next() and it.previous().

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

class Test {
    public static void main(String[] args) {

        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        ListIterator<Integer> itr = list.listIterator(list.size());

        while (itr.hasPrevious()) {
            System.out.println(itr.previous());
        }
        // 30 20 10
    }
}
```