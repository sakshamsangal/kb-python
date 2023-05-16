# crud

## Algorithm

```
create a maven quick start project
add mysql dependency
create design pattern
create database class 
create crud class 
create util class 
create swing form
```

## design pattern

```
org.example
    db 
        Database.java
    frames
        MyFrame1 swing form 
    repo 
        UserCrud.java
    util 
        Util.java
    Main 
```

```
public class MyFrame1 extends JFrame {
    public MyFrame1() throws Exception {
        super("CRUD");

        Util.setUpTable(this);
        Util.setUpListener(this);
        Util.setUpComboBox(this);

        Defualt frame code 
    }
}

```

## Defualt frame code (place at the end)

```
setContentPane(panel1);
setMinimumSize(new Dimension(1000, 650));
setLocationRelativeTo(null);
setExtendedState(getExtendedState() | JFrame.MAXIMIZED_BOTH);
setVisible(true);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
```

## Util methods

```
Util.setUpTable(this);
Util.setUpListener(this);
Util.setUpComboBox(this);
```

## MyFrame1

```
public class MyFrame1 extends JFrame {
    declare JComponents; 
    make default table model
    make table row sorter
    make array list of component

    public MyFrame1() {
        call util methods
        Defualt frame code
    }
}
```

# UserCrud

```
public class UserCrud {
    initailise static block
    select
    insert
    update
    delete
}
```

## make static block to initailise statement of database

```
static {
    try {
        statement = Database.getConnection().createStatement();
    } catch (SQLException e) {
        e.printStackTrace();
    }
}
```

## define select method

```
public static void select(MyFrame1 myFrame1) throws Exception {
    MyFrame1.model.setRowCount(0);
    String sql = "SELECT * FROM user";
    ResultSet resultSet = statement.executeQuery(sql);
    while (resultSet.next()) {
        Object[] row = new Object[11];
        row[0] = resultSet.getString(1);
        row[1] = resultSet.getString(2);
        row[2] = resultSet.getString(3);
        row[3] = resultSet.getString(4);
        row[4] = resultSet.getString(5);
        row[5] = resultSet.getString(6);
        row[6] = resultSet.getString(7);
        row[7] = resultSet.getString(8);
        row[8] = resultSet.getString(9);
        row[9] = resultSet.getString(10);
        row[10] = resultSet.getString(11);
        MyFrame1.model.addRow(row);
    }

}
```

## insert method

```
public static void insert() throws SQLException {
    ArrayList<String> l = MyFrame1.componentList;
    String sql = "select 1 from user where id=" + l.get(0);
    ResultSet rs = statement.executeQuery(sql);
    if (rs.first()) {
        Util.alert("Please provide a different id number", "Similar id found");
    } else {
        sql = "INSERT INTO user VALUES (" + l.get(0) + ", '" + l.get(1) + "', '" + l.get(2) + "', '" + l.get(3) + "', '" + l.get(4) + "', '" + l.get(5) + "', " + l.get(6) + ", " + l.get(7) + ", " + l.get(8) + ", '"  + l.get(9) + "', '"+ l.get(10) + "')";
        statement.executeUpdate(sql);
        ArrayList<Object> row = new ArrayList<>(l);
        MyFrame1.model.addRow(row.toArray());
        // Dialog.clear(TF1, TF2, TF3);
    }
}
```

## update method

```
public static void update(MyFrame1 myFrame1) throws SQLException {
    ArrayList<String> l = MyFrame1.componentList;

    String sql = "UPDATE user SET name='" + l.get(1) + "',email='" + l.get(2) + "',mobile_number='" + l.get(3) + "',city='" + l.get(4) + "',address='" + l.get(5) + "',hindi=" + l.get(6) + ",english=" + l.get(7) + ",telugu=" + l.get(8) + ",gender='" + l.get(9) + "', image_path='" + l.get(10) + "' WHERE id=" + l.get(0);
    statement.execute(sql);

    int rowIndex = myFrame1.getTable1().getSelectedRow();

    DefaultTableModel tableModel = (DefaultTableModel) myFrame1.getTable1().getModel();
    ArrayList<Object> row = new ArrayList<>(l);

    int actualIndex = myFrame1.getTable1().convertRowIndexToModel(rowIndex);
    tableModel.removeRow(actualIndex);
    tableModel.insertRow(actualIndex, row.toArray());
    // Dialog.clear(TF1, TF2, TF3);
}
```

## delete method

```
public static void delete(MyFrame1 myFrame1) throws Exception {
    int length = myFrame1.getTable1().getSelectedRows().length;
    if (length == 1) {
        if (Util.getDeleteConfirmation() == 0) {
            int i = myFrame1.getTable1().getSelectedRow();
            String s = myFrame1.getTable1().getValueAt(i, 0).toString();
            String sql = "DELETE FROM user WHERE id=" + s;
            statement.execute(sql);
            int actualIndex = myFrame1.getTable1().convertRowIndexToModel(i);
            MyFrame1.model.removeRow(actualIndex);
        }
    } else {
        Util.alert("Please select a single row to delete");
    }
}
```

# Util

```
public class Util {
    static ButtonGroup buttonGroup;
    public static File f = new File("C:/Users/DELL/Documents/noPic.png");
}
```

## alert

```
public static void alert(String msg, String title) {
    JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), msg, title, JOptionPane.ERROR_MESSAGE);
}

public static void alert(String msg) {
    JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), msg);
}
```

## get delete confirmation

```
public static int getDeleteConfirmation() {
    return JOptionPane.showConfirmDialog(JOptionPane.getRootFrame(), "Are you sure you want to Delete?", "Delete confirmation", JOptionPane.YES_NO_OPTION);
}
```

## refresh search TF

```
public static void refresh(MyFrame1 myFrame1) {
    myFrame1.getTFRefresh().setText("");
}
```

## clear

```
public static void clear(MyFrame1 myFrame1) {
    set text empty
}
```

## set text empty

```
myFrame1.getImageLabel().setIcon(null);
myFrame1.getTFId().setText("");
myFrame1.getTFName().setText("");
myFrame1.getTFEmail().setText("");
myFrame1.getTFMobile().setText("");
myFrame1.getComboBox1().setSelectedIndex(0);
myFrame1.getTA1().setText("");
myFrame1.getHindiCheckBox().setSelected(false);
myFrame1.getEnglishCheckBox().setSelected(false);
myFrame1.getTeluguCheckBox().setSelected(false);
buttonGroup.clearSelection();
```

## checkForEmptyField

```
public static boolean checkForEmptyField(MyFrame1 myFrame1) {
    clear list
    check JComponents
    return true;
}
```

## image check

```
if (f.getAbsolutePath().equals("C:/Users/DELL/Documents/noPic.png")) {
    MyFrame1.componentList.add("C:/Users/DELL/Documents/noPic.png");
} else {
    String[] arr = Util.f.getAbsolutePath().split("\\\\");
    String join = String.join("/", arr);
    MyFrame1.componentList.add(join);
}
```

## comboBox1 check

```
if (Objects.equals(myFrame1.getComboBox1().getSelectedItem(), "Select a city")) {
    alert("fill city");
    return false;
} else {
    MyFrame1.componentList.add(myFrame1.getComboBox1().getSelectedItem().toString());
}
```

## TA check

```
if (myFrame1.getTA1().getText().equals("")) {
    alert("fill address");
    return false;
} else {
    MyFrame1.componentList.add(myFrame1.getTA1().getText());
}
```

## TF check

```
if (myFrame1.getTFId().getText().equals("")) {
    alert("fill id");
    return false;
} else {
    MyFrame1.componentList.add(myFrame1.getTFId().getText());
}
```

## checkbox check

```
if (myFrame1.getHindiCheckBox().isSelected()) {
    MyFrame1.componentList.add("1");
} else {
    MyFrame1.componentList.add("0");
}

if (myFrame1.getEnglishCheckBox().isSelected()) {
    MyFrame1.componentList.add("1");
} else {
    MyFrame1.componentList.add("0");
}
```

## Radio button check

```
if (!myFrame1.getMaleRadioButton().isSelected() && !myFrame1.getFemaleRadioButton().isSelected()) {
    alert("fill gender");
    return false;
} else {
    if (myFrame1.getMaleRadioButton().isSelected()) {
        MyFrame1.componentList.add("male");
    } else {
        MyFrame1.componentList.add("female");
    }
}
```

## whenRowIsSelected

```
public static void whenRowIsSelected(MyFrame1 myFrame1) throws IOException {
    int i = myFrame1.getTable1().getSelectedRow();


    myFrame1.getTFId().setText(myFrame1.getTable1().getValueAt(i, 0).toString());
    myFrame1.getTFName().setText(myFrame1.getTable1().getValueAt(i, 1).toString());
    myFrame1.getTFEmail().setText(myFrame1.getTable1().getValueAt(i, 2).toString());
    myFrame1.getTFMobile().setText(myFrame1.getTable1().getValueAt(i, 3).toString());
    switch (myFrame1.getTable1().getValueAt(i, 4).toString()) {
        case "Mumbai":
            myFrame1.getComboBox1().setSelectedIndex(1);
            break;
        case "Pune":
            myFrame1.getComboBox1().setSelectedIndex(2);
            break;
        case "Chennai":
            myFrame1.getComboBox1().setSelectedIndex(3);
            break;
        case "Hyderabad":
            myFrame1.getComboBox1().setSelectedIndex(4);
            break;
    }
    myFrame1.getTA1().setText(myFrame1.getTable1().getValueAt(i, 5).toString());
    if (myFrame1.getTable1().getValueAt(i, 6).toString().equals("1")) myFrame1.getHindiCheckBox().setSelected(true);
    else myFrame1.getHindiCheckBox().setSelected(false);

    if (myFrame1.getTable1().getValueAt(i, 7).toString().equals("1"))
        myFrame1.getEnglishCheckBox().setSelected(true);
    else myFrame1.getEnglishCheckBox().setSelected(false);

    if (myFrame1.getTable1().getValueAt(i, 8).toString().equals("1"))
        myFrame1.getTeluguCheckBox().setSelected(true);
    else myFrame1.getTeluguCheckBox().setSelected(false);

    buttonGroup = new ButtonGroup();

    buttonGroup.add(myFrame1.getMaleRadioButton());
    buttonGroup.add(myFrame1.getFemaleRadioButton());

    if (myFrame1.getTable1().getValueAt(i, 9).toString().equals("male"))
        myFrame1.getMaleRadioButton().setSelected(true);
    else myFrame1.getFemaleRadioButton().setSelected(true);

    String path = myFrame1.getTable1().getValueAt(i, 10).toString();
    f = new File(path);
    ImageIcon imageIcon = new ImageIcon(new ImageIcon(ImageIO.read(f.getAbsoluteFile())).getImage().getScaledInstance(200, 200, Image.SCALE_DEFAULT));
    myFrame1.getImageLabel().setIcon(imageIcon);

}
```

## setUpTable

```
public static void setUpTable(MyFrame1 myFrame1) throws Exception {
    JTable table1 = myFrame1.getTable1();
    String[] columnNames = {"Id", "Name", "Email", "Mobile number", "City", "Address", "Hindi", "English", "Telugu", "Gender" , "Image path"};
    Object[][] rowData = {};
    MyFrame1.model = new DefaultTableModel(rowData, columnNames);
    UserCrud.select(myFrame1);
    table1.setModel(MyFrame1.model);
    MyFrame1.sorter = new TableRowSorter<>(MyFrame1.model);
    table1.setRowSorter(MyFrame1.sorter);

    table1.getColumnModel().getColumn(1).setPreferredWidth(180);
    table1.getColumnModel().getColumn(3).setPreferredWidth(100);
    table1.getColumnModel().getColumn(2).setPreferredWidth(300);
    table1.getColumnModel().getColumn(5).setPreferredWidth(250);
}
```

## setUpListener: insert

```
myFrame1.getInsertButton().addActionListener(e -> {
    try {
        if (checkForEmptyField(myFrame1)) {
            UserCrud.insert();
        }
    } catch (Exception ex) {
        ex.printStackTrace();
    }
});
```

## setUpListener: update

```
myFrame1.getUpdateButton().addActionListener(e -> {
    try {
        if (myFrame1.getTable1().getSelectedRows().length == 0) {
            alert("Please select a row");
        } else if (checkForEmptyField(myFrame1)) {
            UserCrud.update(myFrame1);
        }
    } catch (Exception ex) {
        ex.printStackTrace();
    }
});
```

## setUpListener: delete

```
myFrame1.getDeleteButton().addActionListener(e -> {
    try {
        UserCrud.delete(myFrame1);
    } catch (Exception ex) {
        ex.printStackTrace();
    }
});
```

## setUpListener: table

```
myFrame1.getTable1().addMouseListener(new MouseAdapter() {
    @Override
    public void mousePressed(MouseEvent e) {
        super.mousePressed(e);
        try {
            whenRowIsSelected(myFrame1);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
});
```

## setUpListener: getTFRefresh

```
myFrame1.getTFRefresh().getDocument().addDocumentListener(new DocumentListener() {
    @Override
    public void insertUpdate(DocumentEvent e) {
        search(myFrame1.getTFRefresh().getText());
    }

    @Override
    public void removeUpdate(DocumentEvent e) {
        search(myFrame1.getTFRefresh().getText());
    }

    @Override
    public void changedUpdate(DocumentEvent e) {
        search(myFrame1.getTFRefresh().getText());
    }

    public void search(String str) {
        if (str.length() == 0) {
            MyFrame1.sorter.setRowFilter(null);
        } else {
            MyFrame1.sorter.setRowFilter(RowFilter.regexFilter(str));
        }
    }
});

```

## make table non-editable

```
myFrame1.getTable1().setDefaultEditor(Object.class, null);
```

## setUpListener: getRefreshButton

```
myFrame1.getRefreshButton().addActionListener(e -> refresh(myFrame1));

```

## setUpListener: getRefreshFormButton

```
myFrame1.getRefreshFormButton().addActionListener(e -> clear(myFrame1));

```

## setUpListener: getChooseImageButton

```
myFrame1.getChooseImageButton().addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        JFileChooser chooser = new JFileChooser();
        chooser.showSaveDialog(null);
        f = chooser.getSelectedFile();
        ImageIcon imageIcon = null;
        try {
            imageIcon = new ImageIcon(new ImageIcon(ImageIO.read(new File(f.getAbsolutePath()))).getImage().getScaledInstance(200, 200, Image.SCALE_DEFAULT));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        myFrame1.getImageLabel().setIcon(imageIcon);
    }
});
```

## setUpListener

```
public static void setUpListener(MyFrame1 myFrame1) { }
```

## setUpComboBox

```
public static void setUpComboBox(MyFrame1 myFrame1) {
    DefaultComboBoxModel<String> dcm = new DefaultComboBoxModel<>(new String[]{"Select a city", "Mumbai", "Pune", "Chennai", "Hyderabad"});
    myFrame1.getComboBox1().setModel(dcm);
}
```

## Main

```
public class Main {
    public static void main(String[] args) throws Exception {

        new MyFrame1();
        
    }
}
```