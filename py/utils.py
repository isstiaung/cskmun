from bs4 import BeautifulSoup
import pandas as pd
import urllib2
from config import *
import os

def soupen_url(url):
    page = urllib2.urlopen(url)
    return BeautifulSoup(page,lxml)

def get_no_of_rows(soup):
    number_of_rows = 0
    for table in soup.find_all(ctable,{mun_table_type : mun_table_attrs}):
        number_of_rows = len(table.findAll(lambda tag: tag.name == ctable_row and tag.findParent(ctable) == table))
    return number_of_rows

def get_row(soup,is_united):
    if is_united:
        rows = soup.find_all(ctable,{mun_table_type:mun_table_attrs})[0].tbody.findAll(ctable_row)
        return rows
    else:
        print csk_text

def get_table(soup,is_united):
    if is_united:
        matches_span = soup.find(span,{mun_span_type:mun_span_attrs})
        table = ''
        if matches_span != None:
            table = matches_span.findNext(ctable)
        else:
            premier_league = soup.find(span,{mun_span_type:mun_span_alt_attrs})
            table = premier_league.findNext(ctable)
        return table
    else:
        return soup.find_all(ctable)[0]

def get_follow_link(base_url,url):
    return base_url + url

def get_result(bgcolor):
    result = t_win
    if bgcolor == draw:
        result =  t_draw
    elif bgcolor == loss:
        result = t_loss
    else:
        result = t_win
    return result

def get_panda_table(table,is_unified):
    if is_unified:

        return pd.read_html(str(table), header=0, parse_dates=[unified_date_column])[0]
    else:
        return pd.read_html(str(table), header=0, parse_dates=[default_date_column])[0]

def get_filename(year,is_united):
    if is_united:
        return mun_dir + mun_filler + year + csv
    else:
        return csk_dir + csk_filler + year + csv

def write_panda_to_csv(panda_table,filename):
    panda_table.to_csv(filename, index=False, encoding=utf8)

def get_links(soup,is_united):
    if is_united:
        print mun_text
    else:
        links = soup.find_all(clinks,{csk_link_type:csk_link_attrs})
        return links

def clean_read_csv(filename,is_united):
    if is_united:
        return pd.read_csv(filename, sep=c_sep, header=0, parse_dates=[unified_date_column])
    else:
        return pd.read_csv(filename, sep=c_sep, header=0, parse_dates=[unified_date_column])

def read_panda_csv(filename,is_united):
    if is_united:
        return pd.read_csv(filename, sep=c_sep, header=0, parse_dates=[unified_date_column])
    else:
        return pd.read_csv(filename, sep=c_sep, header=0, parse_dates=[unified_date_column])

def concat_panda(panda_tables):
    return pd.concat(panda_tables,sort=True,axis=0, ignore_index=True)


def get_combined_file(dir,file,is_united):
    os.chdir(dir)
    return clean_read_csv(file,is_united)

def write_combined_file(combined_frame,dir,file):
    os.chdir(dir)
    write_panda_to_csv(combined_frame,file)
