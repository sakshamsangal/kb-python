from docx.shared import Mm, Cm
from docxtpl import DocxTemplate, InlineImage


def gen_docx():
    doc = DocxTemplate("temp.docx")
    img_size = Cm(6)  # sets the size of the image
    context = {
        'row_contents': {
            "1":{
                "rule_no": 1,
                "tag": "lavi",
                "map_tag": "",
                "has_rule": "",
                "rule": "",
                "citation": "",
                "is_rendered": "",
                "temp": "",
                "file_name": "",
                "prod": "",
                "tag_desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, reiciendis",
                "count": 1,
                "xml_img": [
                    'temp.png',
                    'temp.png',
                ],
                "pdf_img": [
                ],
                "att": {}
            },
            "2":{
                "rule_no": 2,
                "tag": "Customer",
                "map_tag": "",
                "has_rule": "",
                "rule": "this is rule",
                "citation": 1,
                "is_rendered": 1,
                "temp": "",
                "file_name": "my_file.xml",
                "prod": "my_prod",
                "tag_desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, reiciendis",
                "count": 4,
                "xml_img": [
                    'temp.png',
                    'temp.png'
                ],
                "pdf_img": [
                    'temp.png',
                    'temp.png',
                ],
                "att": [
                    {
                        "att_key": "CustomerID",
                        "att_desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, reiciendis",
                        "xml_img": [
                            'temp.png',
                            'temp.png'
                        ],
                        "pdf_img": [
                            'temp.png',
                            'temp.png'
                        ],
                        "att_val": [
                            "GREAL",
                            "LAZYK",
                            "HUNGC"
                        ]
                    },
                    {
                        "att_key": "sak",
                        "att_desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, reiciendis",
                        "xml_img": [
                            'temp.png',
                            'temp.png'
                        ],
                        "pdf_img": [
                            'temp.png',
                            'temp.png'
                        ],
                        "att_val": [
                            "hello"
                        ]
                    }
                ]
            }
        }
    }
    doc.render(context)
    doc.save("generated_doc1.docx")


gen_docx()
