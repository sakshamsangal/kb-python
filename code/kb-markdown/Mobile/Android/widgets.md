# UI components

## TextView

```
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginTop="@dimen/md_keylines"
    android:layout_marginBottom="@dimen/md_keylines"
    android:text="Price"
    android:textColor="?attr/colorAccent"
    android:textSize="@dimen/article_titles" />
```

## Auto complete text view

```
String[] input
ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, input);
autoCompleteTextView.setAdapter(adapter);
```

## Radio group

```
RadioGroup
    RadioButton
    RadioButton
    RadioButton

radioGroup.setOnCheckedChangeListerner(new RadioGroup.onCheckedChangeListerner(){
    onCheckedChange(group, id) {
        R.id.radioButton1
    }
})
```

## Checkbox, toggle button, switch

```
isChecked() // true or false
```

## Rating bar

```
getRating()
```

## Seek bar

```
setOnSeekBarChangeListener => SeekBar.onSeekBarChangeListener
onProgressChanged
```

## Spinner

same as autoCompleteTextView but change the layout to
_simple_spinner_dropdown_item_

```
setOnItemSelected => AdapterView.OnItemSelectedListener
```

## Time picker

```
setOnTimeChangeListener => TimePicker.onTimeChangeListener
```

## Alert dialog

```
AlertDialog.Builder builder = new AlertDialog.Builder(this);
builer.setCancellable(false);
builer.setTitle("Exit");
builer.setMessage("Are you sure?");
builer.setPositiveButton("Yes", DialogInterface.onClickListener(){
    onClick(){}
})
builer.create();
builer.show();

onBackPressed = automatically call when back button is pressed.
```
