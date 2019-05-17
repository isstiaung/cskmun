import pandas as pd
from bs4 import BeautifulSoup
import urllib2
import sys

base_url = 'https://en.wikipedia.org'
url = 'https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._seasons'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"lxml")
draw = "#ffffdd"
loss = "#ffdddd"
win = "#ffdddd"
row_number = 0
number_of_rows = 0
for table in soup.find_all('table',{"class" : "wikitable sortable"}):
    number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))

for row in soup.find_all('table',{"class":"wikitable sortable"})[0].tbody.findAll('tr'):
    if row_number < (number_of_rows-12):
        row_number+=1
    else:
        link = row.findAll('th')[0].findAll('a')[0]
        link_to_follow = base_url + link.get('href')
        year = link.text
        print link_to_follow
        page = urllib2.urlopen(link_to_follow)
        page_text = BeautifulSoup(page,"lxml")
        table = ''
        matches_span = page_text.find('span',{'id':'Matches'})
        if matches_span != None:
            table = matches_span.findNext('table')
        else:
            premier_league = page_text.find('span',{'id':'Premier_League'})
            table = premier_league.findNext('table')
        is_header=True
        for row in table.tbody.findAll('tr'):
            if is_header:
                is_header = False
            else:
                bgcolor = row["bgcolor"]
                result = "win"
                if bgcolor == draw:
                    result =  "draw"
                elif bgcolor == loss:
                    result = "loss"
                else:
                    result = "win"
                row.find('a',{'class' : 'external text'}).replace_with(result)
        panda_table = pd.read_html(str(table), header=0, parse_dates=['Date'])[0]
        filename = './mun/output_mun_' + year + '.csv';
        panda_table.to_csv(filename, index=False, encoding='utf8')
        csv_text = pd.read_csv(filename, sep=",", header=0, parse_dates=['Date'])
        #print csv_text.dtypes
