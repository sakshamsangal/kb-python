import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Main {

    public static void main(String[] args) {
        // Assemble all the pieces of the MVC
        Model m = new Model("Sylvain", "Saurel");
        View v = new View("MVC with SSaurel");
        Controller c = new Controller(m, v);
        c.initController();
    }

}
