# intent

## simple

``` java
<Button
    android:id="@+id/button"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Button" />

// MainActivity
Button button = findViewById(R.id.button);
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Intent intent = new Intent(MainActivity.this, Main2Activity.class);
        startActivity(intent);
    }
});
```

## with data

``` java
// MainActivity
Intent intent = new Intent(MainActivity.this, Main2Activity.class);
intent.putExtra("price", 10);
intent.putExtra("gender", "male");
startActivity(intent);

// Main2Activity
getIntent().getIntExtra("price", 0);
getIntent().getStringExtra("gender");

```

## with result

``` java
// MainActivity
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == 5) {
        if (resultCode == Activity.RESULT_OK) {
            Log.d(TAG, data.getStringExtra("gender"));
        } else if (resultCode == Activity.RESULT_CANCELED) {

        }
    }
}

public void onClick(View v) {
    Intent intent = new Intent(MainActivity.this, Main2Activity.class);
    startActivityForResult(intent, 5);
}

// Main2Activity
Intent intent = new Intent();
intent.putExtra("gender", "female");
setResult(Activity.RESULT_OK, intent);
finish();

```

```
// How to pass an object from one activity to another on Android
//To pass:
intent.putExtra("MyClass", obj);

// To retrieve object in second Activity
getIntent().getSerializableExtra("MyClass");
```