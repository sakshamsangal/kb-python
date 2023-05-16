# XML validation in java

## input

- xml
- xsd

## output

- valid
- invalid - list of errors

## solution

- no external library
- java17 spring boot

### ide shortcut

- file:xmlValidation

### Step 1. test

```java


import com.example.demo.exception.XSDValidationFailed;
import com.example.demo.model.ApiError;
import org.junit.jupiter.api.Test;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class XmlValidatorUnitTest {

    private static final String BAELDUNG_XML_PATH = "xml/validation/baeldung.xml";
    private static final String PERSON_XSD_PATH = "xml/validation/person.xsd";
    private static final String FULL_PERSON_XSD_PATH = "xml/validation/full-person.xsd";


    @Test
    public void givenInvalidXML_WhenListParsingExceptions_ThenHasThree() throws IOException, SAXException {
        List<String> errorMsg = new XmlValidator(FULL_PERSON_XSD_PATH, BAELDUNG_XML_PATH).listParsingExceptions();
        if (errorMsg.size() != 0){
            throw new XSDValidationFailed( errorMsg);
        }
    }

}

```

### Step 2. validator

```java


import com.example.demo.model.ApiError;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import javax.xml.XMLConstants;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class XmlValidator {

    private static final Logger LOGGER = LoggerFactory.getLogger(XmlValidator.class);

    private final String xsdPath;
    private final String xmlPath;

    public XmlValidator(String xsdPath, String xmlPath) {
        this.xsdPath = xsdPath;
        this.xmlPath = xmlPath;
    }

    public boolean isValid() throws IOException, SAXException {
        Validator validator = initValidator(xsdPath);
        try {
            validator.validate(new StreamSource(getFile(xmlPath)));
            return true;
        } catch (SAXException e) {
            return false;
        }
    }

    public List<String> listParsingExceptions() throws IOException, SAXException {
        XmlErrorHandler xsdErrorHandler = new XmlErrorHandler();
        Validator validator = initValidator(xsdPath);
        validator.setErrorHandler(xsdErrorHandler);
        try {
            validator.validate(new StreamSource(getFile(xmlPath)));
        } catch (SAXParseException e) {}
        ArrayList<String> msg = new ArrayList<>();
        xsdErrorHandler.getExceptions().forEach(e -> {
            msg.add(e.getMessage());
            LOGGER.info(e.getMessage());
        });
        return msg;
    }

    private Validator initValidator(String xsdPath) throws SAXException {
        SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        Source schemaFile = new StreamSource(getFile(xsdPath));
        Schema schema = factory.newSchema(schemaFile);
        return schema.newValidator();
    }

    private File getFile(String location) {
        return new File(getClass().getClassLoader().getResource(location).getFile());
    }

}

```


### 2.1
```java
package com.example.demo;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.io.ByteArrayResource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import javax.xml.XMLConstants;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class XmlValidator {

    private static final Logger LOGGER = LoggerFactory.getLogger(XmlValidator.class);

    private final String xsdPath;
    private final String xmlString;
    private final ByteArrayResource byteArrayResource;

    public XmlValidator(String xsdPath, String xmlString) {
        this.xsdPath = xsdPath;
        this.xmlString = xmlString;
        this.byteArrayResource = new ByteArrayResource(xmlString.getBytes()) {
            @Override
            public String getFilename() {
                return "temp.xml";
            }
        };
    }

    public boolean isValid() throws IOException, SAXException {
        Validator validator = initValidator(xsdPath);
        try {
            validator.validate(new StreamSource(byteArrayResource.getInputStream()));
            return true;
        } catch (SAXException e) {
            return false;
        }
    }

    public List<String> listParsingExceptions() throws IOException, SAXException {
        XmlErrorHandler xsdErrorHandler = new XmlErrorHandler();
        Validator validator = initValidator(xsdPath);
        validator.setErrorHandler(xsdErrorHandler);
        try {
            validator.validate(new StreamSource(byteArrayResource.getInputStream()));
        } catch (SAXParseException e) {}
        ArrayList<String> msg = new ArrayList<>();
        xsdErrorHandler.getExceptions().forEach(e -> {
            msg.add(e.getMessage());
            LOGGER.info(e.getMessage());
        });
        return msg;
    }

    private Validator initValidator(String xsdPath) throws SAXException {
        SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        Source schemaFile = new StreamSource(getFile(xsdPath));
        Schema schema = factory.newSchema(schemaFile);
        return schema.newValidator();
    }

    private File getFile(String location) {
        return new File(getClass().getClassLoader().getResource(location).getFile());
    }

}
```
### Step 3. error handler

```java


import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXParseException;

import java.util.ArrayList;
import java.util.List;

public class XmlErrorHandler implements ErrorHandler {

    private final List<SAXParseException> exceptions;

    public XmlErrorHandler() {
        this.exceptions = new ArrayList<>();
    }

    public List<SAXParseException> getExceptions() {
        return exceptions;
    }

    @Override
    public void warning(SAXParseException exception) {
        exceptions.add(exception);
    }

    @Override
    public void error(SAXParseException exception) {
        exceptions.add(exception);
    }

    @Override
    public void fatalError(SAXParseException exception) {
        exceptions.add(exception);
    }
}

```

### Step 4. xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<individual>
    <name>Baeldung</name>
    <address>
        <zip>00001</zip>
        <city>New York</city>
    </address>
</individual>

```

### Step 5. xsd

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<individual>
    <name>Baeldung</name>
    <address>
        <zip>00001</zip>
        <city>New York</city>
    </address>
</individual>

```
```java
    @ExceptionHandler(XSDValidationFailed.class)
    public ResponseEntity<ApiError> xSDValidationFailed(final XSDValidationFailed e) {
        ApiError apiError = new ApiError();
        apiError.setCode("500 XSD_VALIDATION_FAILED");
        e.getInvalidAges().forEach(apiError::addMessage);
        return ResponseEntity.internalServerError().body(apiError);
    }
```