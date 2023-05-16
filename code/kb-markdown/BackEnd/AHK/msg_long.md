```

::1::
(
 try {
            Person pojo = new Person()

            XmlMapper xmlMapper = new XmlMapper()
            xmlMapper.enable(SerializationFeature.INDENT_OUTPUT)
            String str = "Helwewewelo jhguhg\n"
            BufferedWriter writer = new BufferedWriter(new FileWriter("simple_bean.xml"))
            writer.write(str)
            xmlMapper.writeValue(writer, pojo)
            writer.close()


        } catch(Exception e) {
            e.printStackTrace()
        }

)



```


