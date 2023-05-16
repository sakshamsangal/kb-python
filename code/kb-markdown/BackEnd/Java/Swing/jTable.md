# jTable

```
private static JTable table(String[] column, String[][] data) {
    final JTable jt = new JTable(data, column);
    jt.setCellSelectionEnabled(true);
    ListSelectionModel select = jt.getSelectionModel();
    select.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
    select.addListSelectionListener(e -> {
        String Data = null;
        int[] row = jt.getSelectedRows();
        int[] columns = jt.getSelectedColumns();
        for (int value : row) {
            for (int i : columns) {
                Data = (String) jt.getValueAt(value, i);
            }
        }
        System.out.println("Table  element  selected  is:  " + Data);
    });
    return jt;
}
```

```
String[] column = {"ID", "NAME", "SALARY"};
String[][] data = {
        {"101", "Amit", "670000"},
        {"102", "Jai", "780000"},
        {"101", "Sachin", "700000"}
};

f.add(new JScrollPane(table(column, data)));
```