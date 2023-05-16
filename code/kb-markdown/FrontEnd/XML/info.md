#step hello.xsd
```xml
<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:include schemaLocation="temp.xsd"/>
    <xsd:include schemaLocation="temp2.xsd"/>
    <xsd:element name="p">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="a" type="xsd:string"/>
                <xsd:element name="b" type="xsd:string"/>
                <xsd:element ref="r"/>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>

</xsd:schema>


```

#step sample.xml
```xml
<?xml version="1.0"?>
<p xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="hello.xsd">
    <a>asas</a>
    <b>12</b>
    <r>
        <a>asa</a>
        <b>asa</b>
    </r>
</p>


```

#step temp2.xsd
```xml
<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="r">
    <xsd:complexType >
      <xsd:all>
        <xsd:element name="a" type="xsd:string"/>
        <xsd:element name="b" type="xsd:string"/>
      </xsd:all>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>

```

#step temp.xsd
```xml

<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="q" type="xsd:string"/>
</xsd:schema>
```

#step oxygen
```text

book/chp/section/s1/a1


/chap/Section[1]
/chap/Section[2]
/chap/Section[3]

//section[preceding-sibling::section]

/section/section
//section[]

important
//section[parent::chap] ==  parent

```