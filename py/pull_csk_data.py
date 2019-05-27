import pandas as pd
from bs4 import BeautifulSoup
import urllib2
from config import *
from utils import *
import sys
import re
import json

def pull_csk_data():
    is_united = False
    soup = soupen_url(start_csk_url)

    for link in get_links(soup,is_united):
        print link
        link_to_follow = get_follow_link(base_csk_url,link.get(chref))
        year = link.text
        page_text = soupen_url(link_to_follow)
        bs_tables = get_table(page_text,is_united)
        rows = bs_tables.find('tbody').find_all('tr')
        start_times=[]

        for row in rows:
            print row
            match_url = get_follow_link(base_csk_url,row.find_all('td')[-1].find_all(clinks)[0].get(chref)).replace("scorecard","game")
            time_soup = soupen_url(match_url)
            full_script = time_soup.find_all('script',{"type" : "text/javascript"})[6].string.strip()
            regex = re.compile('.*\"hoursOfPlay\":\"(.*?)\",')
            hours_of_play = regex.match(full_script)
            if hours_of_play:
                start_time = str(hours_of_play.groups()[0].split(',')[0].split(" ")[0])
                start_time = start_time.replace(".",":")
                start_times.append(start_time)

        panda_table = get_panda_table(bs_tables,is_united)
        panda_table.rename(columns = {"Match Date" : "newdate"},inplace=True)
        print start_times
        panda_table['date'] = pd.to_datetime(panda_table['newdate'])
        if len(start_times) > 0:
            for index,row in panda_table.iterrows():
                print index
                panda_table.at[index,'time'] =  start_times[index]
        else:
            panda_table['time'] =  pd.to_timedelta(10,unit='s')
        print panda_table['date']
        print panda_table['time']
        filename = get_filename(year,is_united)

        panda_table.to_csv(filename, index=False)
        csv_text = read_panda_csv(filename,False)

        print csv_text
    print "Done pulling csk data"

pull_csk_data()
