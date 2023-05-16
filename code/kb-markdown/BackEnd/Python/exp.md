```

from datetime import datetime, timedelta

import pandas as pd

ls = []
diff = datetime.now() + timedelta(days=-2)
d = str(diff.strftime("%d/%b/%Y"))


class Expense:
    def __init__(self):
        self.amt = 0

    def amount_to_pay(self):
        return self.amt

    def add_to_cart(self, my_item):
        if my_item['actual_exp'] is None:
            my_item['actual_exp'] = my_item['mrp_per_kg'] * my_item['kg_taken']
        self.amt += my_item['actual_exp']
        ls.append(my_item)


x = Expense()
x.add_to_cart({
    'date': d,
    'name': 'tomato_avg',
    'mrp_per_kg': 10,
    'kg_taken': 2,
    'expected_expense': None,
    'actual_exp': None
})

print(x.amount_to_pay())


def m_xpath():
    df = pd.DataFrame()
    df = pd.concat([df, pd.DataFrame.from_records(ls)])
    df.to_excel(f'out.xlsx', index=False)


if __name__ == '__main__':
    m_xpath()


```
