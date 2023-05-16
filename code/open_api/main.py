import os

import sqlite3
import sys

# def list_files(startpath):
#     flink = open(f'{startpath}/link/link.html', 'w')
#     flink.write('<html><body>\n')
#
#     for root, dirs, files in os.walk(startpath+'/out'):
#         r = f'<strong>{root}</strong>'
#         flink.write(f'{r}\n')
#         flink.write('<ol>')
#         for f in files:
#             fn = root + '/' + f
#             flink.write(f'<li><a href="{fn}">{f}</a> </li>' + '\n')
#         flink.write('</ol>\n')
#     flink.write('</body></html>\n')
#     flink.close()
mm2 = {
    "crytpography": "backend",
    "design pattern": "backend",
    "DesignPattern": "backend",
    "io": "backend",
    "JSON": "backend",
    "OOP": "backend",
    "Streams": "backend",
    "String": "backend",
    "Threading": "backend",
    "simple": "backend",
    "Annotation": "backend",
    "Life cycle": "backend",
    "mvc": "backend",
    "scope": "backend",
    "controller": "backend",
    "crud": "backend",
    "pojo": "backend",
    "repository": "backend",
    "util": "backend",
    "view": "backend",
    "layout": "backend"
}
my_map = {
    "Android": "mobile",
    "Guide": "dsa",
    "C++": "dsa",
    "tree": "dsa",
    "Java": "backend",
    "Tree": "dsa",
    "Git": "backend",
    "Core": "backend",
    "OOP": "backend",
    "Hibernate": "backend",
    "JDBC": "backend",
    "JSP": "backend",
    "Maven": "backend",
    "Microservice": "backend",
    "apigateway": "backend",
    "contact_service": "backend",
    "e_server": "backend",
    "user_service": "backend",
    "Servlet": "backend",
    "Spring framework": "backend",
    "SpringBoot": "backend",
    "ProjectSop": "backend",
    "Guide2": "backend",
    "SpringSecurity": "backend",
    "Swing": "backend",
    "MySQL": "db",
    "Oracle": "db",
    "Python": "backend",
    "Windows": "backend",
    "Angular": "frontend",
    "Bootstrap": "frontend",
    "CSS": "frontend",
    "HTML": "frontend",
    "Javascript": "frontend",
    "React": "frontend"
}


def sak():
    in_dir = "C:/Users/saksangal/Documents/saksham/document/lang/front_end/atom"
    conn = sqlite3.connect('kb.db')
    print("Opened database successfully")

    for (root, dirs, files) in os.walk(in_dir, topdown=True):
        for file in files:
            fread = open(root + '/' + file)
            # x = str(fread.read())
            # print(x)
            # sys.exit(0)

            # conn.execute(f"INSERT INTO COMPANY (dir,val) \
            #       VALUES ('{root}', '{x}')")
            # fread.close()

            file_content = fread.read()
            fread.close()
            a, b, c, d = str(root).rsplit('\\', 3)
            # print(b, c, d)
            if c == 'Guide':
                try:
                    conn.execute(f'INSERT INTO {mm2[d]} (topic, tag, val) VALUES (?,?,?)', (c, d, file_content))
                except:
                    conn.execute(f'INSERT INTO dsa (topic, tag, val) VALUES (?,?,?)', (c, d, file_content))
            else:
                conn.execute(f'INSERT INTO {my_map[c]} (topic, tag, val) VALUES (?,?,?)', (c, d, file_content))

            conn.commit()
    print("Records created successfully")


def tb():
    conn = sqlite3.connect('kb.db')
    ls = ['frontend', 'backend', 'dsa', 'mobile', 'db']
    for item in ls:
        conn.execute(f'''CREATE TABLE {item}(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     topic           TEXT,
                     tag           TEXT,
                     val           TEXT);''')
        print(f"{item} Table created successfully")


if __name__ == '__main__':
    tb()
    sak()
