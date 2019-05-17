import pandas as pd
from bs4 import BeautifulSoup
import urllib2

base_url = 'http://stats.espncricinfo.com'
url = 'http://stats.espncricinfo.com/indian-premier-league-2014/engine/records/team/match_results_year.html?class=6;id=4343;type=team'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"lxml")

for link in soup.find_all('a',{"class":"QuoteSummary"}):
    link_to_follow = base_url + link.get('href')
    year = link.text
    page = urllib2.urlopen(link_to_follow)
    page_text = BeautifulSoup(page,"lxml")
    bs_tables = page_text.find_all('table')[0]
    panda_table = pd.read_html(bs_tables, header=0, parse_dates=['Match Date'])[0]
    match_dates = panda_table['Match Date'].tolist()
    filename = './csk/output_csk_' + year + '.csv';
    panda_table.to_csv(filename, index=False)
    csv_text = pd.read_csv(filename, sep=",", header=0, parse_dates=['Match Date'])
    #print csv_text.dtypes
