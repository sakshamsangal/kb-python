# JSON parsing

```
JSONObject jsonObject = new JSONObject(readJSON());
JSONArray jsonArray = jsonObject.getJSONArray("formulas");

for(int i = 0; i < jsonArray.length(); i++){
    JSONObject object = jsonArray.getJSONObject(i);
    String name = object.getString("formulae");
    String salary = object.getString("url");
}
```
