```
public boolean isValidEmail(String email) {
    // String regex = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]{2,6}$";

    String emailRegex = "^[a-zA-Z0-9_+&*-]+(?:\\."+
            "[a-zA-Z0-9_+&*-]+)*@" +
            "(?:[a-zA-Z0-9-]+\\.)+[a-z" +
            "A-Z]{2,7}$";

    Pattern pat = Pattern.compile(emailRegex);
    if (email == null) return false;
    return pat.matcher(email).matches();

}
```

import java.util.regex.*;  