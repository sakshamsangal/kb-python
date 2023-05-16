```python
import glob
import json
import re

from lxml import etree
import pandas as pd

tag_dic = {}


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def xml_traverse(parent, root, xpath):
    tag_name = etree.QName(root).localname
    if tag_name not in tag_dic:
        tag_dic[tag_name] = {
            'tag': tag_name,
            'parent': parent,
            'attrib': {},
            'text': 'no',
            'child': set()
        }
    # print(len(root.text))
    pattern = '(\n|\s)*'
    if root.text is not None and not re.fullmatch(pattern, root.text):
        tag_dic[tag_name]['text'] = 'yes'

    if root.tail is not None and not re.fullmatch(pattern, root.tail):
        tag_dic[tag_dic[tag_name]['parent']]['text'] = 'yes'

    for k, v in root.attrib.items():
        if k not in tag_dic[tag_name]['attrib']:
            tag_dic[tag_name]['attrib'][k] = set()
        tag_dic[tag_name]['attrib'][k].add(v)

    for child in root:
        if not (type(child) == etree._ProcessingInstruction) and not (type(child) == etree._Comment):
            tag_dic[tag_name]['child'].add(etree.QName(child).localname)
            xml_traverse(tag_name, child, f'{xpath}/{etree.QName(child).localname}')


if __name__ == '__main__':
    # xml_folder = input('xml folder loc: ')
    # for xml_file in glob.glob(f"{xml_folder}/*.xml"):
    for xml_file in glob.glob(f"*.xml"):
        tree = etree.parse(xml_file)
        root = tree.getroot()
        xml_traverse(None, root, etree.QName(root).localname)
        df = pd.DataFrame(tag_dic.values())
    # out = input('output loc:    ')
    # df.to_excel(f'{out}/mastersheet.xlsx', index=False)
    df.to_excel(f'mastersheet.xlsx', index=False)

```


```python
import re

import pandas as pd


df_p = pd.read_excel('akshu_p.xlsx', sheet_name='pat')
df = pd.read_excel('akshu.xlsx', sheet_name='Sheet1')

for index1, row1 in df_p.iterrows():
    for index, row in df.iterrows():
        if pd.isnull(df.loc[index, 'comp']):
            print(row1['pat'], row['xpath'])
            pat = re.compile(row1['pat'])
            if re.fullmatch(pat, row['xpath']):
                df.iat[index, 2] = row1['comp']
                df.iat[index, 3] = row1['style']

df.to_excel('akshu.xlsx', index=False)



```


```python
import json

from flask import Flask, jsonify

app = Flask(__name__)
x = {}

# Todo 1: Returns % of players above a particular year.
#  Input could be any year for example, 1989.
#  All players born on or after 1989 should be
#  considered and the percentage should be calculated.
@app.route('/year/<int:year>')
def get_player_by_year(year):
    z = []
    year -= 1
    for dic in x.values():
        try:
            y = int('19' + dic['DOB'].rsplit('-', 1)[1])
        except:
            y = -1
        if year < y:
            z.append(dic)
    per = str(round(len(z) / len(x) * 100, 2))
    return jsonify({"player_percentage": per + "%"})


# Todo 2: Average age of players in the different teams.
@app.route('/avg-age')
def average_age():
    ans_dic = {}
    for dic in x.values():
        if dic['Country'] != "":
            y = int('19' + dic['DOB'].rsplit('-', 1)[1])
            if dic['Country'] in ans_dic:
                ans_dic[dic['Country']].append(2022 - y)
            else:
                ans_dic[dic['Country']] = [2022 - y]

    for k, v in ans_dic.items():
        ans_dic[k] = round(sum(v) / len(v), 2)

    return jsonify(ans_dic)


# Todo 3: Which country has the maximum number of left-hand batsmen.
@app.route('/left-hand')
def left_hand():
    ans_dic = {}
    for dic in x.values():
        if dic['Country'] != "":
            if dic['Batting_Hand'] == 'Left_Hand':
                v = ans_dic.get(dic['Country'], 0)
                ans_dic[dic['Country']] = v + 1

    k, v = max(ans_dic.items(), key=lambda k: k[1])
    return jsonify({k: v})

# Todo 4: List all the players whose Country is not identified in the dataset.
@app.route('/und-player')
def und_player():
    ls = []
    for dic in x.values():
        if dic['Country'] == "":
            ls.append(dic['Player_Name'])
    return jsonify(ls)


# Todo 5: List of all players in an input Country
@app.route('/country/<string:country>')
def get_player_by_country(country):
    ls = []
    for dic in x.values():
        if dic['Country'] == country:
            ls.append(dic['Player_Name'])
    return jsonify(ls)


def load_json():
    global x
    with open('static/player.json') as f:
        x = json.load(f)


load_json()

if __name__ == '__main__':
    app.run()

```


```python

import csv
import json


def make_json(csv_path, json_path):
    data = {}
    with open(csv_path, encoding='utf-8-sig') as csvf:
        reader = csv.DictReader(csvf)
        for rows in reader:
            key = rows['Player_Name']
            data[key] = rows

    with open(json_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    csv_path = r'static/Players.csv'
    json_path = r'static/player.json'
    make_json(csv_path, json_path)


```


```text
Steps to run:

pip install -r requirements.txt
run csv_to_json.py
run app.py

host:
http://127.0.0.1:5000

end point:
/year/<int:year>
/avg-age
/left-hand
/und-player
/country/<string:country>
```


```txt
Flask~=2.1.1
app~=0.0.1
```


```python
from app import app
import unittest


class FlaskTest(unittest.TestCase):

    def test_get_player_by_year(self):
        tester = app.test_client(self)
        res = tester.get('/year/1989')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(b'{"player_percentage":"21.2%"}\n', res.data)

    def test_average_age(self):
        tester = app.test_client(self)
        res = tester.get('/avg-age')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'{"Australia":40.03,"Bangladesh":35.8,"England":40.29,"India":36.17,"Netherlands":42.0,"New Zealand":37.77,"Pakistan":41.31,"South Africa":39.33,"Sri Lanka":41.1,"West Indies":37.89,"Zimbabwea":42.5}\n',
            res.data)

    def test_left_hand(self):
        tester = app.test_client(self)
        res = tester.get('/left-hand')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(b'{"India":58}\n', res.data)
        # self.assertEqual(, res.data)

    def test_und_player(self):
        tester = app.test_client(self)
        res = tester.get('/und-player')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'["A Choudhary","A Dananjaya","A Hales","A Joseph","A Roy","A Turner","AJ Tye","Ankit Soni","AR Bawne","AS Yadav","Avesh Khan","B Stanlake","BA Stokes","Basil Thampi","C de Grandhomme","C Ingram","CR Woakes","D Shorey","D Short","D Willey","DM Bravo","E Lewis","H Brar","H Gurney","H Klaasen","H Vihari","H Viljoen","Harmeet Singh (2)","I Sodhi","J Archer","J Bairstow","J Behrendorff","J Dala","J Denly","J Searles","JJ Roy","K Ahmed","K Gowtham","K Khejroliya","K Paul","K Rabada","KM Asif","L Ferguson","L Livingstone","L Ngidi","L Plunkett","LH Ferguson","M Ali","M Lomror","M Markande","M Santner","M Ur Rahman","M Wood","MJ Henry","Mohammad Nabi","Mohammed Siraj","N Naik","N Pooran","NB Singh","Niraj Patel","O Thomas","P Chopra","P Krishna","P R Barman","P Raj","P Shaw","R Bhui","R Parag","R Salam","R Singh","RA Tripathi","Rashid Khan","RD Chahar","S Curran","S Dube","S Gill","S Hetmyer","S Kuggeleijn","S Lamichhane","S Mavi","S Midhun","S Rutherford","S Sharma","S Singh","S Warrier","SD Lad","SP Jackson","SS Agarwal","T Curran","T Natarajan","Tejas Baroka","TS Mills","V Chakravarthy","Vishnu Vinod","Washington Sundar"]\n',
            res.data)

    def test_get_player_by_country(self):
        tester = app.test_client(self)
        res = tester.get('/country/England')
        sc = res.status_code
        self.assertEqual(sc, 200)
        self.assertEqual(res.content_type, 'application/json')
        self.assertEqual(
            b'["A Flintoff","AC Thomas","AD Mascarenhas","CJ Jordan","CK Langeveldt","EJG Morgan","GR Napier","JC Buttler","LJ Wright","MJ Lumb","OA Shah","PD Collingwood","RS Bopara","SW Billings"]\n',
            res.data)


if __name__ == '__main__':
    unittest.main()

```


