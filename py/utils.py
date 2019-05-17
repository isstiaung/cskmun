from bs4 import BeautifulSoup
import pandas as pd
import urllib2
from config import *

def soupen_url(url):
    page = urllib2.urlopen(url)
    return BeautifulSoup(page,lxml)

def get_no_of_rows(soup):
    number_of_rows = 0
    for table in soup.find_all(ctable,{mun_table_type : mun_table_attrs}):
        number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))
    return number_of_rows

def get_row(soup,is_united):
    if is_united:
        rows = soup.find_all(ctable,{mun_table_type:mun_table_attrs})[0].tbody.findAll(ctable_row)
        return rows
    else:
        print "csk_row"

def get_table(soup,is_united):
    if is_united:
        matches_span = soup.find('span',{'id':'Matches'})
        table = ''
        if matches_span != None:
            table = matches_span.findNext('table')
        else:
            premier_league = soup.find('span',{'id':'Premier_League'})
            table = premier_league.findNext('table')
        return table
    else:
        return soup.find_all('table')[0]

def get_follow_link(base_url,url):
    return base_url + url

def get_result(bgcolor):
    result = "win"
    if bgcolor == draw:
        result =  "draw"
    elif bgcolor == loss:
        result = "loss"
    else:
        result = "win"
    return result

def get_panda_table(table,is_united):
    if is_united:
        return pd.read_html(str(table), header=0, parse_dates=[mun_date_column])[0]
    else:
        return pd.read_html(str(table), header=0, parse_dates=[csk_date_column])[0]

def get_filename(year,is_united):
    if is_united:
        return mun_dir + '/output_mun_' + year + '.csv'
    else:
        return csk_dir + '/output_csk_' + year + '.csv'

def write_panda_to_csv(panda_table,filename):
    panda_table.to_csv(filename, index=False, encoding='utf8')

def get_links(soup,is_united):
    if is_united:
        print "utd links"
    else:
        links = soup.find_all(clinks,{csk_link_type:csk_link_attrs})
        return links
