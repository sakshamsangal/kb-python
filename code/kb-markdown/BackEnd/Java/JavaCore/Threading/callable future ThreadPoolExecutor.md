```
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class Source {

    public static void createAndExecuteTasks(int m, int n) {
        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(3);
        List<Future<Integer>> resultList = new ArrayList<>();

        /**
         * TODO 1: create callable tasks of type Task with student id and given number n.
         * submit each task object to executor and store the task result in resultList
         */
        for (int i = 0; i < m; i++) {
            Task task = new Task(i + 1, n);
            Future<Integer> result = executor.submit(task);
            resultList.add(result);
        }

        executor.shutdown();
        getResults(resultList);
    }

    public static void getResults(List<Future<Integer>> resultList) {
        for(Future<Integer> result : resultList) {
            try {
                System.out.println(result.get());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        int m;
        int n;
        if(args != null && args.length == 2) {
            m = Integer.parseInt(args[0]);
            n = Integer.parseInt(args[1]);
        } else {
            // m = 10; n = 4;
            //uncomment below line and comment above line for testing sample test case 2
        m = 6; n = 12;
        }
        createAndExecuteTasks(m, n);
    }
}
```

***

```
class Task implements Callable<Integer> {
    private int id;
    private int n;
    public Task(int id, int n) {
        this.id = id;
        this.n = n;
    }

    @Override
    public Integer call() throws Exception {
        return id*n;
    }
}
```