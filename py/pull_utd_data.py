import pandas as pd
from bs4 import BeautifulSoup
import urllib2
import sys
from config import *
from utils import *


def pull_utd_data():
    is_united = True
    year = 2008
    start_url = start_utd_url
    while year <= 2019:
        if year > 2008:
            start_url = start_url.replace(str(year-1),str(year))
        soup = soupen_url(start_url)
        table = soup.findAll(ctable,{mun_table_type:"standard_tabelle"})[0]
        panda_table = pd.read_html(str(table), header=1, parse_dates={'datetime': ['date','date.1']})[0]
        strings_to_drop = ['Premier','FA','League','date']
        panda_table = panda_table[~panda_table.datetime.str.contains('|'.join(strings_to_drop))]
        #print panda_table
        filename = get_filename(str(year),is_united)
        year +=1
        write_panda_to_csv(panda_table,filename)
        csv_text = read_panda_csv(filename,is_united)
        #print csv_text.dtypes
        #sys.exit()
    print "Done pulling united data"

#pull_utd_data()
