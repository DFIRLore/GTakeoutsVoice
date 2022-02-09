# Get Google Voice Search parser
# Author: Camille Lore
# Date: 2/4/2022
# Version 0.0.1
# Requirements: BeautifulSoup, html2text


import re
from bs4 import BeautifulSoup, NavigableString, Tag
import html2text
from itertools import islice

with open("MyActivity.html", 'r', encoding='utf-8') as f_html:
    html=f_html.read() 
    contents = f_html.read()
    soup = BeautifulSoup(contents, 'lxml')
    strings = soup.find_all(string=re.compile('Said'))
    for a in soup.findAll('a'):
        del a['href']
        
              
with open('DevSaidParse.txt', 'wb') as f: #prints to new file
    text_maker = html2text.HTML2Text()
    text_maker.SINGLE_LINE_BREAK = True
    f.write(html2text.html2text(html).encode('utf-8'))
       
SearchKey = 'Said'

with open('DevSaidParse.txt', 'r', encoding = 'utf-8') as f: 
    for line in f:
        if SearchKey in line:
            print(line, end='')
            print(''.join(islice(f, 3))) 



    



    

    
