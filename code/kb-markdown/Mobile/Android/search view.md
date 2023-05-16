# Search view primitive

``` 
import android.widget.SearchView;
public class MainActivity extends AppCompatActivity implements SearchView.OnQueryTextListener{

    ArrayList<String> list;
    ArrayAdapter<String> adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SearchView searchView = findViewById(R.id.searchView);
        list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Pineapple");
        list.add("Orange");
        list.add("Lychee");
        list.add("Gavava");
        list.add("Peech");
        list.add("Melon");
        list.add("Watermelon");
        list.add("Papaya");

        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, list);
        ListView listView = findViewById(R.id.lv1);
        listView.setAdapter(adapter);

        searchView.setOnQueryTextListener(this);
         <!-- searchView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String query) {
                return false;
            }

            @Override
            public boolean onQueryTextChange(String newText) {
                adapter.getFilter().filter(newText);
                return false;
            }
        }); -->
    }


    @Override
    public boolean onQueryTextSubmit(String query) {
        return false;
    }

    @Override
    public boolean onQueryTextChange(String newText) {
        adapter.getFilter().filter(newText);
        return false;
    }
}
<SearchView
    android:id="@+id/searchView"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:queryHint="Search Here" />

//  ## Search view object

public class MainActivity extends AppCompatActivity {

    StudentRecyclerAdapter studentRecyclerAdapter;
    RecyclerView mRecyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = findViewById(R.id.recyclerView);

        List<Student> students = new ArrayList<>();

        students.add(new Student(12, "rohan"));
        students.add(new Student(42, "rohit"));
        students.add(new Student(12, "saksham"));
        students.add(new Student(12, "sahitya"));
        students.add(new Student(42, "sakshi goel"));
        students.add(new Student(12, "sakshi singhal"));
        students.add(new Student(42, "sakshai singhal 173"));
        students.add(new Student(12, "samriddhi"));

        studentRecyclerAdapter = new StudentRecyclerAdapter(students);

        mRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        mRecyclerView.setAdapter(studentRecyclerAdapter);

        SearchView searchView = findViewById(R.id.searchView);
        searchView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String text) {
                return false;
            }

            @Override
            public boolean onQueryTextChange(String text) {
                studentRecyclerAdapter.getFilter().filter(text);
                return true;
            }
        });
    }


    static class StudentRecyclerAdapter extends RecyclerView.Adapter<StudentRecyclerAdapter.StudentViewHolder> implements Filterable {
        private List<Student> mStudents;
        private List<Student> filteredData;

        public StudentRecyclerAdapter(List<Student> students) {
            mStudents = students;
            filteredData = mStudents;
        }

        @NonNull
        @Override
        public StudentRecyclerAdapter.StudentViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.student_row, parent, false);
            return new StudentViewHolder(view);
        }

        @Override
        public void onBindViewHolder(@NonNull StudentRecyclerAdapter.StudentViewHolder holder, int position) {
            holder.mRollNumberTextView.setText(String.valueOf(filteredData.get(position).getRollNumber()));
            holder.mNameTextView.setText(filteredData.get(position).getName());
        }

        @Override
        public int getItemCount() {
            return filteredData.size();
        }

        @Override
        public Filter getFilter() {
            return new Filter() {
                @Override
                protected FilterResults performFiltering(CharSequence charSequence) {
                    FilterResults results = new FilterResults();

                    //If there's nothing to filter on, return the original data for your list
                    if (charSequence == null || charSequence.length() == 0) {
                        results.values = mStudents;
                        results.count = mStudents.size();
                    } else {
                        List<Student> filterResultsData = new ArrayList<>();
                        for (Student data : mStudents) {
                            if (data.getName().toLowerCase().contains(charSequence.toString().toLowerCase())) {
                                filterResultsData.add(data);
                            }
                        }
                        results.values = filterResultsData;
                        results.count = filterResultsData.size();
                    }
                    return results;
                }
                @Override
                protected void publishResults(CharSequence charSequence, FilterResults filterResults) {
                    filteredData = (ArrayList<Student>) filterResults.values;
                    notifyDataSetChanged();
                }
            };
        }

        public static class StudentViewHolder extends RecyclerView.ViewHolder {
            TextView mRollNumberTextView;
            TextView mNameTextView;
            public StudentViewHolder(@NonNull View itemView) {
                super(itemView);
                mRollNumberTextView = itemView.findViewById(R.id.rollNumber);
                mNameTextView = itemView.findViewById(R.id.name);
            }
        }
    }
}
```

## better approach

```
class StudentRecyclerAdapter extends RecyclerView.Adapter<StudentRecyclerAdapter.StudentViewHolder> implements Filterable {
    private List<Student> mStudents;
    private List<Student> temp;

    public StudentRecyclerAdapter(List<Student> students) {
        mStudents = students;
        temp = new ArrayList<>(mStudents);
    }

    @NonNull
    @Override
    public StudentRecyclerAdapter.StudentViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.row, parent, false);
        return new StudentViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull StudentRecyclerAdapter.StudentViewHolder holder, int position) {
        holder.mRollNumberTextView.setText(String.valueOf(mStudents.get(position).getRollNumber()));
        holder.mNameTextView.setText(mStudents.get(position).getName());
    }

    @Override
    public int getItemCount() {
        return mStudents.size();
    }

    @Override
    public Filter getFilter() {
        return new Filter() {
            @Override
            protected FilterResults performFiltering(CharSequence constraint) {
                List<Student> filteredList = new ArrayList<>();
                if (constraint == null || constraint.length() == 0) {
                    filteredList.addAll(temp);
                } else {
                    String filterPattern = constraint.toString().toLowerCase().trim();
                    for (Student item : temp) {
                        if (item.getName().toLowerCase().contains(filterPattern)) {
                            filteredList.add(item);
                        }
                    }
                }
                FilterResults results = new FilterResults();
                results.values = filteredList;
                return results;
            }

            @Override
            protected void publishResults(CharSequence constraint, FilterResults results) {
                mStudents.clear();
                mStudents.addAll((List) results.values);
                notifyDataSetChanged();
            }
        };
    }


    public static class StudentViewHolder extends RecyclerView.ViewHolder {
        TextView mRollNumberTextView;
        TextView mNameTextView;
        public StudentViewHolder(@NonNull View itemView) {
            super(itemView);
            mRollNumberTextView = itemView.findViewById(R.id.tv1);
            mNameTextView = itemView.findViewById(R.id.tv2);
        }
    }
}



```

## activity_main.xml

``` xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <SearchView
        android:id="@+id/searchView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
</LinearLayout>
```

## student_row.xml

``` xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/rollNumber"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="TextView" />

    <TextView
        android:id="@+id/name"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="TextView" />
</LinearLayout>
```

