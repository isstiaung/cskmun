import pandas as pd
from bs4 import BeautifulSoup
import urllib2
import sys
from config import *
from utils import *

def pull_utd_data():
    is_united = True
    soup = soupen_url(start_utd_url)
    row_number = 0
    number_of_rows = get_no_of_rows(soup)

    for row in get_row(soup,is_united):
        if row_number < (number_of_rows-mun_seasons):
            row_number+=1
        else:
            link = row.findAll(ctable_header)[0].findAll(clinks)[0]
            link_to_follow = get_follow_link(base_utd_url,link.get(chref))
            year = link.text

            page_text = soupen_url(link_to_follow)
            table = get_table(page_text,is_united)

            is_header=True
            for row in table.tbody.findAll(ctable_row):
                if is_header:
                    is_header = False
                else:
                    result = get_result(row[mun_bgcolor])
                    row.find(clinks,{mun_link_type : mun_link_attrs}).replace_with(result)

            panda_table = get_panda_table(table,is_united)
            filename = get_filename(year,is_united)

            write_panda_to_csv(panda_table,filename)
            csv_text = pd.read_csv(filename, sep=",", header=0, parse_dates=[mun_date_column])
            print csv_text.dtypes

pull_utd_data()
