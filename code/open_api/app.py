import re

dict = {

    "data": [
        {
            "frn": "0004372322",
            "file_id": "137230",
            "file_name": "UScellular - Iowa Concede Service Change Challenge Response.pdf",
            "supporting_document_type": 1,
            "supporting_document_type_desc": "Fixed Challenge Initial Review Concede",
            "uploaded_by": "uscdlsa3automationengineering@uscellular.com",
            "uploaded_date": "2023-03-09T23:54:16.658Z"
        },
        {
            "frn": "0004372322",
            "file_id": "140889",
            "file_name": "UScellular - Arizona Disputed Challenge Response.pdf",
            "supporting_document_type": 2,
            "supporting_document_type_desc": "Fixed Challenge Initial Review Dispute",
            "uploaded_by": "uscdlsa3automationengineering@uscellular.com",
            "uploaded_date": "2023-03-10T17:56:04.718Z"
        }
    ]

}

pattern = r"Alabama|Alaska|American Samoa|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|District of Columbia|Florida|Georgia|Guam|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|North Dakota|Northern Mariana Islands|Ohio|Oklahoma|Oregon|Pennsylvania|Puerto Rico|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|U.S. Virgin Islands|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming"

map = {
    "Iowa":"AZ",
    "Arizona":"SD"
}
def get_state_name(filename):
    heroRegex = re.compile(pattern)
    mo1 = heroRegex.search(filename)
    return mo1.group()


def process():
    var = dict["data"]
    for i in var:
        fn = i["file_name"]
        x = get_state_name(fn)
        print(map[x])



if __name__ == '__main__':
    process()
