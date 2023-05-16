## dependencies

```
implementation 'com.google.code.gson:gson:2.8.6'
implementation 'com.google.code.gson:gson:2.8.5'
implementation 'androidx.recyclerview:recyclerview:1.1.0'
implementation 'com.github.bumptech.glide:glide:4.7.1'
```

## Permission

```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

## Theme

```
android:theme="@style/Theme.AppCompat.Light.DarkActionBar"
?android:attr/selectableItemBackground
```

## Title bar

```
getSupportActionBar()).setTitle(R.string.feedback);
getSupportActionBar().setDisplayHomeAsUpEnabled(true);
```

## Night mode

```
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
```

## List divider

```
recyclerView.addItemDecoration(new DividerItemDecoration(getContext(), DividerItemDecoration.VERTICAL));
```

## drawable/selector.xml

```
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="#FFEB3B" android:state_checked="true" />
    <item android:color="#E91E63" />
</selector>
```

## TypedArray

```
String[] mPlaces = resources.getStringArray(R.array.places);

TypedArray a = resources.obtainTypedArray(R.array.places_picture);
mPlacePictures = new Drawable[a.length()];
for (int i = 0; i < mPlacePictures.length; i++) {
    mPlacePictures[i] = a.getDrawable(i);
}
a.recycle();
```

## get image from drawable

```
String imageName = item.getString("category_image");
Resources resources = context.getResources();
final int resourceId = resources.getIdentifier(imageName, "drawable", context.getPackageName());

Drawable drawable = resources.getDrawable(resourceId);
category_image.add(drawable);
```