## isNetworkAvailable

```
public boolean isNetworkAvailable(Context context) {
    ConnectivityManager connectivityManager = ((ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE));
    assert connectivityManager != null;
    return connectivityManager.getActiveNetworkInfo() != null && connectivityManager.getActiveNetworkInfo().isConnected();
}
```

## readJSON

```
public String readJSON() {
    String json = null;
    try {
        // Opening data.json file
        InputStream inputStream = getAssets().open("temp.json");
        int size = inputStream.available();
        byte[] buffer = new byte[size];
        // read values in the byte array
        inputStream.read(buffer);
        inputStream.close();
        // convert byte to string
        json = new String(buffer, "UTF-8");
    } catch (IOException e) {
        e.printStackTrace();
        return json;
    }
    return json;
}
```