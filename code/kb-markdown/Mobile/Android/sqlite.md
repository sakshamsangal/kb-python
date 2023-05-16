```
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    DbHelper db;

    EditText editTeasyd ,editTextName ,editTextEmail ,editTextMobile;
    Button buttonInsert, buttonView, buttonDelete,buttonUpdate, buttonSearch;

    String id;
    String name;
    String email;
    String mobile;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTeasyd = findViewById(R.id.edit_id);
        editTextName = findViewById(R.id.edit_name);
        editTextEmail = findViewById(R.id.edit_email);
        editTextMobile = findViewById(R.id.edit_mobile);

        buttonInsert = findViewById(R.id.button_insert);
        buttonView = findViewById(R.id.button_view);
        buttonDelete = findViewById(R.id.button_delete);
        buttonUpdate = findViewById(R.id.button_update);
        buttonSearch = findViewById(R.id.button_search);

        buttonInsert.setOnClickListener(this);
        buttonView.setOnClickListener(this);
        buttonDelete.setOnClickListener(this);
        buttonUpdate.setOnClickListener(this);
        buttonSearch.setOnClickListener(this);

        db=new DbHelper(this);
    }

    @Override
    public void onClick(View v) {

        switch (v.getId()){

            case R.id.button_insert:
                name=editTextName.getText().toString();
                email=editTextEmail.getText().toString();
                mobile=editTextMobile.getText().toString();
                if(name.equals("") | email.equals("") | mobile.equals("")){
                    Toast.makeText(this, "Please fill the Fields", Toast.LENGTH_SHORT).show();
                }else {
                    db.insertStudent(name,email,mobile);
                    editTeasyd.setText("");
                    editTextName.setText("");
                    editTextEmail.setText("");
                    editTextMobile.setText("");
                    Toast.makeText(this, "saved successfully", Toast.LENGTH_SHORT).show();
                }
                break;

            case R.id.button_view:
                Intent intent=new Intent(getApplicationContext(),ViewSQLiteData.class);
                startActivity(intent);
                break;

            case R.id.button_delete:
                id = editTeasyd.getText().toString();
                if(id.equals("")){
                    Toast.makeText(this, "Plase fill the Id", Toast.LENGTH_SHORT).show();
                }else {
                    long l = Long.parseLong(id);
                    db.deleteStudent(l);
                    editTeasyd.setText("");
                    editTextName.setText("");
                    editTextEmail.setText("");
                    editTextMobile.setText("");
                    Toast.makeText(this, "deleted successfully", Toast.LENGTH_SHORT).show();
                }
                break;

            case R.id.button_update:
                id=editTeasyd.getText().toString().trim();
                name=editTextName.getText().toString();
                email=editTextEmail.getText().toString();
                mobile=editTextMobile.getText().toString();
                if(id.equals("") | name.equals("") | email.equals("") | mobile.equals("")){
                    Toast.makeText(this, "Please fill all the fields", Toast.LENGTH_SHORT).show();
                }else {
                    long l= Long.parseLong(id);
                    db.updateStudent(l,name,email,mobile);
                    editTeasyd.setText("");
                    editTextName.setText("");
                    editTextEmail.setText("");
                    editTextMobile.setText("");
                    Toast.makeText(this, "updated successfully", Toast.LENGTH_SHORT).show();
                }
                break;
            case R.id.button_search:
                id=editTeasyd.getText().toString().trim();
                if(id.equals("")){
                    Toast.makeText(this, "Please Fill the Id", Toast.LENGTH_SHORT).show();
                }else {
                    try {
                        long l1= Long.parseLong(id);
                        name=db.getName(l1);
                        email=db.getEmail(l1);
                        mobile=db.getMobile(l1);

                        editTextName.setText(name);
                        editTextEmail.setText(email);
                        editTextMobile.setText(mobile);
                        Toast.makeText(this, "searched successfully", Toast.LENGTH_SHORT).show();

                    }
                    catch (Exception e)
                    {
                        Toast.makeText(this, "Id is not Available", Toast.LENGTH_SHORT).show();
                    }
                }
                break;
        }
    }
}

```

``` 

public class ViewSQLiteData extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_s_q_lite_data);

        TextView textView = findViewById(R.id.view_data);

        DbHelper db = new DbHelper(this);

        String data = db.getData();
        textView.setText(data);
        textView.setMovementMethod(new ScrollingMovementMethod());
    }
}
```

```

public class DbHelper extends SQLiteOpenHelper {
    private static final String TAG = "s90";
    private SQLiteDatabase db;

    private static final String DATABASE_NAME = "database.db";
    private static final int DATABASE_VERSION = 1;

    private static final String TABLE_STUDENT = "_student";

    private static final String KEY_ID = "id";
    private static final String KEY_NAME = "name";
    private static final String KEY_EMAIL = "email";
    private static final String KEY_MOBILE = "mobile";

    DbHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String Query_Table = " CREATE TABLE " + TABLE_STUDENT + "(" + KEY_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + KEY_NAME + " TEXT, " + KEY_EMAIL + " TEXT, " + KEY_MOBILE + " TEXT);";
        // CREATE TABLE _student(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, mobile TEXT);
        Log.d(TAG, "onCreate: " + Query_Table);
        db.execSQL(Query_Table);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_STUDENT);
        onCreate(db);
    }

    void insertStudent(String name, String email, String mobile) {
        db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(KEY_NAME, name);
        values.put(KEY_EMAIL, email);
        values.put(KEY_MOBILE, mobile);
        db.insert(TABLE_STUDENT, null, values);
    }

    String getData() {
        db = this.getReadableDatabase();
        String[] columns = new String[]{KEY_ID, KEY_NAME, KEY_EMAIL, KEY_MOBILE};
        Cursor cursor = db.query(TABLE_STUDENT, columns, null, null, null, null, null);

        int iId = cursor.getColumnIndex(KEY_ID);
        int iName = cursor.getColumnIndex(KEY_NAME);
        int iEmail = cursor.getColumnIndex(KEY_EMAIL);
        int iMobile = cursor.getColumnIndex(KEY_MOBILE);
        StringBuilder result = new StringBuilder();

        for (cursor.moveToFirst(); !cursor.isAfterLast(); cursor.moveToNext()) {
            result.append("Id: ").append(cursor.getString(iId)).append("\n").append("Name: ").append(cursor.getString(iName)).append("\n").append("Email: ").append(cursor.getString(iEmail)).append("\n").append("Mobile: ").append(cursor.getString(iMobile)).append("\n\n");
        }
        db.close();
        return result.toString();
    }

    void deleteStudent(long l) {
        db = this.getWritableDatabase();
        db.delete(TABLE_STUDENT, KEY_ID + "=" + l, null);
    }

    void updateStudent(long l, String name, String email, String mobile) {
        db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(KEY_NAME, name);
        values.put(KEY_EMAIL, email);
        values.put(KEY_MOBILE, mobile);
        db.update(TABLE_STUDENT, values, KEY_ID + "=" + l, null);
        db.close();
    }

    String getName(long l1) {
        db = this.getReadableDatabase();
        String[] columns = new String[]{KEY_ID, KEY_NAME, KEY_EMAIL, KEY_MOBILE};
        Cursor cursor = db.query(TABLE_STUDENT, columns, KEY_ID + "=" + l1, null, null, null, null);
        if (cursor != null) {
            cursor.moveToFirst();
            return cursor.getString(1);
        }
        return null;
    }

    String getEmail(long l1) {
        db = this.getReadableDatabase();
        String[] columns = new String[]{KEY_ID, KEY_NAME, KEY_EMAIL, KEY_MOBILE};
        Cursor cursor = db.query(TABLE_STUDENT, columns, KEY_ID + "=" + l1, null, null, null, null);
        if (cursor != null) {
            cursor.moveToFirst();
            return cursor.getString(2);
        }
        return null;
    }

    String getMobile(long l1) {
        db = this.getReadableDatabase();
        String[] columns = new String[]{KEY_ID, KEY_NAME, KEY_EMAIL, KEY_MOBILE};
        Cursor cursor = db.query(TABLE_STUDENT, columns, KEY_ID + "=" + l1, null, null, null, null);
        if (cursor != null) {
            cursor.moveToFirst();
            return cursor.getString(3);
        }
        return null;
    }
}
```

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    tools:context=".MainActivity">

    <EditText
        android:id="@+id/edit_id"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Id"
        android:layout_margin="10dp"
        android:inputType="number"/>

    <EditText
        android:id="@+id/edit_name"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Name"
        android:layout_margin="5dp"
        android:inputType="text"/>

    <EditText
        android:id="@+id/edit_email"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Email"
        android:layout_margin="5dp"
        android:inputType="textEmailAddress"/>

    <EditText
        android:id="@+id/edit_mobile"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Mobile"
        android:layout_margin="5dp"
        android:inputType="phone"/>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <Button
            android:id="@+id/button_insert"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="save"
            android:textSize="20sp"
            android:layout_weight="1"
            android:layout_marginTop="20dp"/>

        <Button
            android:id="@+id/button_view"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="view"
            android:textSize="20sp"
            android:layout_weight="1"
            android:layout_marginTop="20dp"/>
    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <Button
            android:id="@+id/button_delete"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="delete"
            android:textSize="20sp"
            android:layout_weight="1"
            android:layout_marginTop="20dp"/>

        <Button
            android:id="@+id/button_update"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="update"
            android:textSize="20sp"
            android:layout_weight="1"
            android:layout_marginTop="20dp"/>
    </LinearLayout>

    <Button
        android:id="@+id/button_search"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="search"
        android:textSize="20sp"
        android:layout_marginTop="20dp"/>

</LinearLayout>

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"
    tools:context=".ViewSQLiteData">

    <TextView
        android:id="@+id/view_data"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:textSize="20sp"
        android:textColor="@android:color/black"
        android:scrollbars="vertical"/>

</RelativeLayout>

```