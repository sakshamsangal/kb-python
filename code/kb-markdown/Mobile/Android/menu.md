# Option menu

## On create options menu

``` 
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.menu_main, menu);
    return true;
}
```

## On options item selected

```
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    if (item.getItemId() == R.id.settings) {
        Toast.makeText(this, "settings", Toast.LENGTH_SHORT).show();
    } else if(item.getItemId() == R.id.about) {
        Toast.makeText(this, "about", Toast.LENGTH_SHORT).show();
    }
    return super.onOptionsItemSelected(item);
}
```

## menu/menu_main.xml

``` xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/settings"
        android:title="Settings" />
    <item
        android:id="@+id/about"
        android:title="About" />
</menu>
```