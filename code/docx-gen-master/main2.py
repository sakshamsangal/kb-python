from docx.shared import Mm, Cm
from docxtpl import DocxTemplate, InlineImage


def gen_docx():
    doc = DocxTemplate("temp.docx")
    img_size = Cm(10)  # sets the size of the image
    context = {
        'row_contents': [
            {
                'description': 'Eggs',
                'img': InlineImage(doc, 'temp2.png', img_size),
            }, {
                'description': 'All Purpose Flour',
                'img': InlineImage(doc, 'temp.png', img_size),

            }, {
                'description': 'Eggs1',
                'img': InlineImage(doc, 'temp2.png', img_size),
            }
        ]
    }
    doc.render(context)
    doc.save("generated_doc1.docx")


gen_docx()
