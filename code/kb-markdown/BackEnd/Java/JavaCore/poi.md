```java
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.poi.xwpf.usermodel.*;

import java.util.Scanner;

class Main {
    //Main Function
    public static void main(String[] args) throws Exception {
        //Instantiate WordGenerator Class
        WordGenerator wg = new WordGenerator();

        //VK lines text filename
        // String vkFilename = "src/vk_no.txt";

        //Gather VK Lines from text file
        // List<String> vkLines = wg.getLines(vkFilename);

        //Create word document according to VK lines
        wg.createWord();
    }
}

class WordGenerator {

    public void createWord() throws IOException {
        XWPFDocument document = new XWPFDocument();
        FileOutputStream out = new FileOutputStream(new File("temp.docx"));

        //Set Bold an Italic
        XWPFParagraph title = document.createParagraph();
        title.setAlignment(ParagraphAlignment.CENTER);
        XWPFRun myTitle = title.createRun();
        myTitle.setBold(true);
        myTitle.setFontSize(20);
        myTitle.setText("Aadhaar dedupe");
        myTitle.addBreak();
        myTitle.setUnderline(UnderlinePatterns.THICK);


        // subTitle.setAlignment(ParagraphAlignment.CENTER);

        File input = new File("src/test.txt");
        FileWriter fileWriter = new FileWriter("src/output.txt");

        Scanner fileReader = new Scanner(input);
        Scanner console = new Scanner(System.in);

        String data;
        String str;
        List<String> headerList = new ArrayList<>(Arrays.asList("URL", "method", "content-type"));


        XWPFParagraph paragraph = document.createParagraph();

        List<XWPFRun> xwpfRuns = new ArrayList<>();
        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());

        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());


        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());

        xwpfRuns.add(paragraph.createRun());
        xwpfRuns.add(paragraph.createRun());


        int count  = 0;
        for (int i = 0; i < 3; i++) {
            data = fileReader.nextLine();
            System.out.println("[pan-dedupe] " + headerList.get(i) + ": " + data);
            System.out.print("change(y/n): ");
            str = console.nextLine();
            if (str.equals("y")) {
                String item = console.nextLine();
                fileWriter.write(item + "\n");
                data = item;
            } else fileWriter.write(data + "\n");

            xwpfRuns.get(count).setBold(true);
            xwpfRuns.get(count).setFontSize(12);
            xwpfRuns.get(count).setFontFamily("Arial");
            xwpfRuns.get(count).setText(headerList.get(i) + ": ");
            count++;

            xwpfRuns.get(count).setFontSize(12);
            xwpfRuns.get(count).setFontFamily("Arial");
            xwpfRuns.get(count).setText(data);
            xwpfRuns.get(count).addBreak();
            count++;
        }

        List<String> payload = new ArrayList<>(Arrays.asList("Request", "Response"));

        for (int i = 0; i < 2; i++) {
            xwpfRuns.get(count).addBreak();
            xwpfRuns.get(count).setBold(true);
            xwpfRuns.get(count).setFontSize(12);
            xwpfRuns.get(count).setFontFamily("Arial");
            xwpfRuns.get(count).setText(payload.get(i) + ": ");
            xwpfRuns.get(count).addBreak();
            count++;

            // default value
            StringBuilder result;
            result = new StringBuilder();
            while (fileReader.hasNextLine()) {
                data = fileReader.nextLine();
                if (data.trim().isEmpty()) {
                    break;
                } else {
                    result.append(data).append("\n");
                }
            }
            System.out.println("[pan-dedupe] " + payload.get(i) + ": ");
            System.out.println(result);
            System.out.print("change(y/n): ");


            // based on choice
            str = console.nextLine();
            if (str.equals("y")) {
                String lineNew;
                while (console.hasNextLine()) {
                    lineNew = console.nextLine();
                    if (lineNew.isEmpty()) break;
                    fileWriter.write(lineNew + "\n");
                }
            } else {
                fileWriter.write(String.valueOf(result));
                String[] request = result.toString().split("\n");
                for (String req : request) {

                    xwpfRuns.get(count).setFontSize(12);
                    xwpfRuns.get(count).setFontFamily("Arial");
                    xwpfRuns.get(count).setText(req);
                    xwpfRuns.get(count).addBreak();

                }
            }
            count++;

        }

        fileWriter.close();
        fileReader.close();

        document.write(out);
        out.close();
        System.out.println("done");
    }
}

class ReadFile {
    public List<String> readLines(String filename) throws IOException {
        FileReader fileReader = new FileReader(filename);

        BufferedReader bufferedReader = new BufferedReader(fileReader);
        List<String> lines = new ArrayList<String>();
        String line = null;

        while ((line = bufferedReader.readLine()) != null) {
            lines.add(line);
        }

        bufferedReader.close();
        return lines;
    }
}

```