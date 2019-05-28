import pandas as pd
from utils import *
from config import *

def set_played_first():
    os.chdir(unified_dir)
    unified_data = read_panda_csv(unified_file,False)
    for index,row in unified_data.iterrows():
        mun_time = row['time_x']
        csk_time = row['time_y']
        played_first = 0 #csk
        if mun_time<csk_time:
            played_first = 1
        unified_data.at[index,'played_first'] = played_first
    write_panda_to_csv(unified_data,unified_file)
set_played_first()
