# Row

## List

```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">
    <ImageView
        android:layout_width="100dp"
        android:layout_height="100dp"
        app:srcCompat="@drawable/e" />
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:orientation="vertical">

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="TextView" />

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="TextView" />
    </LinearLayout>
</LinearLayout>
```

## Tile

```
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="8dp"
    app:cardCornerRadius="5dp"
    app:cardElevation="5dp"
    app:cardMaxElevation="5dp">

    <ImageView
        android:id="@+id/tile_picture"
        android:layout_width="match_parent"
        android:layout_height="@dimen/tile_height"
        android:foreground="?android:attr/selectableItemBackground"
        android:scaleType="centerCrop"
        tools:src="@drawable/hair_oil" />

    <ImageView
        android:layout_width="match_parent"
        android:layout_height="@dimen/tile_height"
        android:alpha="0.5"
        android:background="@color/dark_grey" />

    <TextView
        android:id="@+id/tile_title"
        android:layout_width="match_parent"
        android:layout_height="@dimen/tile_height"
        android:layout_gravity="center"
        android:gravity="center"
        android:textColor="@color/white"
        android:textSize="@dimen/article_titles" />
```

```
@Override
public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    RecyclerView recyclerView = (RecyclerView) inflater.inflate(R.layout.recycler_view, container, false);
    ContentAdapter adapter = new ContentAdapter(recyclerView.getContext());
    recyclerView.setAdapter(adapter);
    recyclerView.setHasFixedSize(true);

    recyclerView.setLayoutManager(new GridLayoutManager(getActivity(), 2));
    return recyclerView;
}
```

## Card

```
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="12dp"
    app:cardCornerRadius="5dp"
    app:cardElevation="5dp">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        <ImageView
            android:layout_width="match_parent"
            android:layout_height="300dp"
            android:scaleType="centerCrop"
            android:src="@drawable/e" />
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Saksham Sangal" />
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="horizontal">
            <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Action" />
            <ImageButton
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                app:srcCompat="@drawable/ic_favorite" />
            <ImageButton
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                app:srcCompat="@drawable/ic_share" />
        </LinearLayout>
    </LinearLayout>
</androidx.cardview.widget.CardView>
```

