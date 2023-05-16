package com.company;

import javax.swing.*;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreeModel;
import java.awt.*;
import java.io.IOException;
import java.net.URL;

public class MyFrame1 extends JFrame {
private JTree tree1;
private JPanel panel1;
private JLabel label1;
private JEditorPane editorPane1;

    public MyFrame1() throws HeadlessException {
        setContentPane(panel1);




        DefaultMutableTreeNode root = new DefaultMutableTreeNode("Style");
        DefaultMutableTreeNode color = new DefaultMutableTreeNode("color");
        DefaultMutableTreeNode font = new DefaultMutableTreeNode("font");

        root.add(color);
        root.add(font);
        TreeModel treeModel = new DefaultTreeModel(root);

        tree1.setModel(treeModel);
        setMinimumSize(new Dimension(1000, 650));
        setLocationRelativeTo(null);
        setExtendedState(getExtendedState() | JFrame.MAXIMIZED_BOTH);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tree1.getSelectionModel().addTreeSelectionListener(new TreeSelectionListener() {
            @Override
            public void valueChanged(TreeSelectionEvent e) {
                DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode) tree1.getLastSelectedPathComponent();
                label1.setText(selectedNode.getUserObject().toString());
                URL url = null;
                if (label1.getText().equals("Style")) {
                    url= MyFrame1.class.getResource("test.htm");
                } else if (label1.getText().equals("color")) {
                    url= MyFrame1.class.getResource("color.htm");
                }
                try {
                    editorPane1.setPage(url);
                } catch (IOException e1) {
                    editorPane1.setContentType("text/html");
                    editorPane1.setText("<html>Page not found.</html>");
                }
            }
        });
        // tree1.addTreeSelectionListener(new TreeSelectionListener() {
        //     @Override
        //     public void valueChanged(TreeSelectionEvent e) {
        //         JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), "msg", "title", JOptionPane.ERROR_MESSAGE);
        //     }
        // });
    }

    public static void main(String[] args) {

        new MyFrame1();
    }

}


<html>
<head>
    <title>Swing Tester</title>
</head>
<body>
<p>Swing API is a set of extensible GUI Components
    to ease the developer's life to create JAVA based Front End/GUI
    Applications. It is build on top of AWT API and acts as a replacement of
    AWT API, since it has almost every control corresponding to AWT controls.
    Swing component follows a Model-View-Controller architecture to
    fulfill the following criterias.</p>
<ul>
    <li><p>A single API is to be sufficient to support multiple look and feel.</p></li>
    <li><p>API is to be model driven so that the highest level API is not required to have data.</p></li>
    <li><p>API is to use the Java Bean model so that Builder Tools and IDE can provide better services to the developers for use.</p></li>
</ul>
<h2>MVC Architecture</h2>
<p>Swing API architecture follows loosely based MVC architecture in the following manner.</p>
<ul>
    <li><p>Model represents component's data.</p></li>
    <li><p>View represents visual representation of the component's data.</p></li>
    <li><p>Controller takes the input from the user on the view and reflects the changes in Component's data.</p></li>
    <li><p>Swing component has Model as a seperate element, while the View and Controller part are clubbed in the User Interface elements. Because of which, Swing has a pluggable look-and-feel architecture.</p></li>
</ul>
<h2>Swing Features</h2>
<ul>
    <li><p><b>Light Weight</b> − Swing components are independent of native Operating System's API as Swing API controls are rendered mostly using pure JAVA code instead of underlying operating system calls.</p></li>
    <li><p><b>Rich Controls</b> − Swing provides a rich set of advanced controls like Tree, TabbedPane, slider, colorpicker, and table controls.</p></li>
    <li><p><b>Highly Customizable</b> − Swing controls can be customized in a very easy way as visual apperance is independent of internal representation.</p></li>
    <li><p><b>Pluggable look-and-feel</b> − SWING based GUI Application look and feel can be changed at run-time, based on available values.</p></li>
</ul>
</body>
</html>