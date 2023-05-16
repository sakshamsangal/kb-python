x= Arrays.asList(x).stream().map(String::toLowerCase).toArray(String[]::new);
String[] elements) {
elements= Arrays.stream(elements).map(String::toLowerCase).toArray(String[]::new);
