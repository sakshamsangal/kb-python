import glob

ls = [
    'bin',
    '.settings',
    '.classpath',
    '.project'
]
for name in glob.glob(
        fr'C:\Users\saksangal\Downloads\Saksham\project\kb-java17\src\com\app\design_patt\design_patterns\*'):
    for i in range(2):
        print(f'rmdir "{name}\{ls[i]}" /s /q')

    for i in range(2,4):
        print(f'del "{name}\{ls[i]}"')
