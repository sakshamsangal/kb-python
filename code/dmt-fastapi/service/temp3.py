import re

if __name__ == '__main__':
    input = '''16 content management
17 the new media play
18 the 5g evolution
19 digital signaling 
20 central office tour  part 1
21 the data driven economy
22 inside media and entertainment
23 industry jumpstart tmt
24 basics of voice transport
25 making money in the tmt industry
26 storage asaservice    
27 inside telecommunication
28 sports subsector overview
'''



    # s = re.sub(r'[^a-zA-Z0-9\s]', '', input)
    s = re.sub(r'\n', '#', input)
    s1 = re.sub(r'(\s)+', '_', s)
    s2 = re.sub('#', '\n', s1)
    # print(s.lower())
    print(s2)
