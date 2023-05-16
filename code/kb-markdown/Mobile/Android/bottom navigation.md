# Bottom navigation view

## Layout

```
<com.google.android.material.bottomnavigation.BottomNavigationView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:menu="@menu/tabs" />
```

## menu/tabs.xml

``` xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:icon="@mipmap/ic_launcher"
        android:id="@+id/tab1"
        android:title="tab1" />
    <item
        android:id="@+id/tab2"
        android:title="tab2" />
    <item
        android:id="@+id/tab3"
        android:title="tab3" />
</menu>
```

## Activity

``` java
BottomNavigationView bnv = findViewById(R.id.bnv);
bnv.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        Toast.makeText(MainActivity.this, menuItem.getTitle(), Toast.LENGTH_SHORT).show();
        return true;
    }
});
```
