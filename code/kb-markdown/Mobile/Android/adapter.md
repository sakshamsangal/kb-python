# Recycler view design pattern

## Class

```java
class StudentRecyclerAdapter extends RecyclerView.Adapter<StudentRecyclerAdapter.StudentViewHolder> {
    // onCreateViewHolder
    // onBindViewHolder
    // getItemCount
    // ViewHolder
}
```

## Field

```java
private List<Student> mStudents;
```

## Constructor

```java
public StudentRecyclerAdapter(List<Student> students) {
    mStudents = students;
}
```

## onCreateViewHolder

```java
@NonNull
@Override
public StudentRecyclerAdapter.StudentViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.student_row, parent, false);
    return new StudentViewHolder(view);
}
```

## getItemCount

```java
@Override
public int getItemCount() {
    return mStudents.size();
}
```

## onBindViewHolder

```java
@Override
public void onBindViewHolder(@NonNull StudentRecyclerAdapter.StudentViewHolder holder, int position) {
    holder.mRollNumberTextView.setText(String.valueOf(mStudents.get(position).getRollNumber()));
    holder.mNameTextView.setText(mStudents.get(position).getName());
}
```

## ViewHolder

```java
public static class StudentViewHolder extends RecyclerView.ViewHolder {
    TextView mRollNumberTextView;
    TextView mNameTextView;
    public StudentViewHolder(@NonNull View itemView) {
        super(itemView);
        mRollNumberTextView = itemView.findViewById(R.id.rollNumber);
        mNameTextView = itemView.findViewById(R.id.name);
    }
}
```

```java
public static class StudentViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener

public StudentViewHolder(@NonNull View itemView) {
    super(itemView);
    itemView.setOnClickListener(this);
    mRollNumberTextView = itemView.findViewById(R.id.rollNumber);
    mNameTextView = itemView.findViewById(R.id.name);
}

@Override
public void onClick(View v) {
    Toast.makeText(v.getContext(), "position " + getLayoutPosition() + mNameTextView.getText(), Toast.LENGTH_SHORT).show();
}
```

# Listview custom adapater

## class

```java
class CustomListAdapter extends ArrayAdapter<String> {
    // getView
}

class CustomListAdapter extends ArrayAdapter<Product> { 
    // getView
}
```

## Field

```
String[] arr;
private Product[] arr;
private static final String TAG = "s170";
```

## Constructor

```
public CustomListAdapter(@NonNull Context context, int resource, String[] arr) {
    super(context, resource, arr);
    this.arr = arr;
}

CustomListAdapter(@NonNull Context context, int resource, Product[] arr) {
    super(context, resource, arr);
    this.arr = arr;
}
```

## getView

```
@NonNull
@Override
public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {

    LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
    View view = layoutInflater.inflate(R.layout.row, parent, false);

    TextView textView = view.findViewById(R.id.textView);
    textView.setText(arr[position]);

    Button buttonDelete = view.findViewById(R.id.buttonDelete);
    buttonDelete.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            removeHero(position);
        }
    });
    return view;
}
```

```
@NonNull
@Override
public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
    Log.d(TAG, "getView:  = " + arr[0].getName());

    LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
    View view = layoutInflater.inflate(R.layout.support_simple_spinner_dropdown_item, parent, false);

    TextView textView = view.findViewById(android.R.id.text1);
    Log.d(TAG, "getView:  = " + arr[position].getName());
    textView.setText(arr[position].getName());

    return view;
}
```

## Imports

```
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;
```

## Main

```
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

Product[] arr = {new Product("sa", 221), new Product("edwe", 56)};
final CustomListAdapter customListAdapter = new CustomListAdapter(this, R.layout.support_simple_spinner_dropdown_item, arr);
ListView listView = findViewById(R.id.lv);
listView.setAdapter(customListAdapter);
```

## SearchView

```
SearchView searchView = findViewById(R.id.sv);
searchView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
    @Override
    public boolean onQueryTextSubmit(String query) {
        return false;
    }
    @Override
    public boolean onQueryTextChange(String newText) {
        customListAdapter.getFilter().filter(newText);
        return false;
    }
});
```

---

asas

asas

asas

| asas | sas  | sas |     |     |
|------|------|-----|-----|-----|
|      |      |     |     |     |
|      | asas |     |     |     |
|      |      |     |     |     |
|      |      |     |     |     |

$$
sum((a + b)^2)
$$