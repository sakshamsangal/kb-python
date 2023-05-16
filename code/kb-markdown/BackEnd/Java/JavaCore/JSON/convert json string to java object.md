### convert json string to java object using gson

```
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
import com.google.gson.Gson;

class Product {
    String name;
    int price;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}

public class App {

    private static Product getProductObject() {
        String product = "{\"name\": \"colgate\",\"price\": \"10\"}";
        Gson gson = new Gson();
        return gson.fromJson(product, Product.class);
    }
    public static void main(String[] args) {
        System.out.println(getProductObject());
    }

}
```