# Convert JSON To CSV

## pom

``` xml 
<!--  for csv file support  -->
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>1.4</version>
</dependency>

<!-- for json support -->
<dependency>
    <groupId>org.json</groupId>
    <artifactId>json</artifactId>
    <version>20180813</version>
</dependency>
```

## App.java

``` java 
public static void convertJsonToCsv(String json) {
    JSONObject jsonObject;
    try {
        jsonObject = new JSONObject(json);

        // fetching json array by using key
        // here the key name is "fileName"
        JSONArray jsonArray = jsonObject.getJSONArray("fileName");

        // creating a csv file
        File file = new File("empDetails.csv");

        // converting json array to string
        String str = CDL.toString(jsonArray);

        // writing csv string to file
        FileUtils.writeStringToFile(file, str);
    } catch(Exception e) {
        e.printStackTrace();
    }
}
public static void main(String[] args) throws JSONException {
    String json = "{\"fileName\": [{\"first name\": \"Ravi\",\"last name\": \"Chandra\",\"location\": \"Bangalore\"}]}";
    convertJsonToCsv(json);
}
```

## output

```
by opening empDetails.csv we get the following data

last name,first name,location
Chandra,Ravi,Bangalore
```

![CSV](./image/convertJsonToCsv.png)