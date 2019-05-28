import pandas as pd
from utils import *
from config import *
from datetime import datetime,timedelta

def set_played_first():
    os.chdir(unified_dir)
    unified_data = read_panda_csv(unified_file,False)
    for index,row in unified_data.iterrows():
        mun_time = row['time_x']
        csk_time = row['time_y']
        #convert to gmt
        csk_time = str((datetime.strptime(csk_time, '%H:%M') - timedelta(hours=5,minutes=30)).time())
        played_first = 0 #csk
        if mun_time<csk_time:
            played_first = 1
        unified_data.at[index,'played_first'] = played_first
    write_panda_to_csv(unified_data,unified_file)
set_played_first()
