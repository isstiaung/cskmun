import pandas as pd
from bs4 import BeautifulSoup
import urllib2
from config import *
from utils import *

def pull_csk_data():
    is_united = False
    soup = soupen_url(start_csk_url)

    for link in get_links(soup,is_united):
        link_to_follow = get_follow_link(base_csk_url,link.get(chref))
        year = link.text
        page_text = soupen_url(link_to_follow)
        bs_tables = get_table(page_text,is_united)

        panda_table = get_panda_table(bs_tables,is_united)
        panda_table.rename(columns = {"Match Date" : "datetime"},inplace=True)

        filename = get_filename(year,is_united)

        panda_table.to_csv(filename, index=False)
        csv_text = read_panda_csv(filename,False)
        print csv_text.dtypes
    print "Done pulling csk data"

#pull_csk_data()
