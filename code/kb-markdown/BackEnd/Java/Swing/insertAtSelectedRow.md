package org.example;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Form1 {
private JTable table1;
private JPanel panel1;
private JButton button1;
private DefaultTableModel model;

    public Form1() {
        Object[][] data = new Object[][]{{"101", "Ramesh"}, {"102", "Adithya"}, {"103", "Jai"}, {"104", "Sai"}};
        String[] columnNames = new String[]{"ID", "Name"};
        model = new DefaultTableModel(data, columnNames);
        table1.setModel(model);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {
                model.removeRow(2);
                model.insertRow(2, new Object[] {"107", "ExpressJS" });
            }
        });
    }

    public static void main(String[] args) {
        JFrame jFrame = new JFrame("Student Management System");

        jFrame.setContentPane(new Form1().panel1);
        jFrame.setMinimumSize(new Dimension(700, 650));
        jFrame.setLocationRelativeTo(null);
        jFrame.setVisible(true);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

}
