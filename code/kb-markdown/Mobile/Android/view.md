## Recycler View

``` 
<androidx.recyclerview.widget.RecyclerView
    android:id="@+id/recyclerView"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />

Student
    int rollNumber
    String name

mRecyclerView = findViewById(R.id.recyclerView);
List<Student> students = new ArrayList<>();    
students.add(new Student(12, "saksham"));
students.add(new Student(42, "sahitya"));        
StudentRecyclerAdapter studentRecyclerAdapter = new StudentRecyclerAdapter(students);

mRecyclerView.setLayoutManager(new LinearLayoutManager(this));
// mRecyclerView.setLayoutManager(new GridLayoutManager(this, 2)); 
mRecyclerView.setAdapter(studentRecyclerAdapter);
```

## ListView

```
String[] arr = {"c1", "c2", "c3", "c4"};

ArrayAdapter<String> category = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, arr);

ListView listView = findViewById(R.id.list_view);
listView.setAdapter(category);


<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <ListView
        android:id="@+id/list_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
</LinearLayout>

listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        // position = index
        // listView.getItemAtPosition(position) = item
    }
});

```




