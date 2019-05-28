import pandas as pd
from utils import *
from config import *

def get_result():
    os.chdir(unified_dir)
    unified_data = read_panda_csv(unified_file,False)
    unified_data['mun_result']=1
    unified_data['csk_result']=1
    for index,row in unified_data.iterrows():
        mun_winner = row['mun_winner']
        csk_winner = row['csk_winner']
        final_score = mun_winner.split("(")[0]
        mun_goals = final_score.split(':')[0]
        opp_goals = final_score.split(':')[1].strip()
        if mun_goals == opp_goals:
            result = 0
        elif mun_goals < opp_goals:
            result = -1
        else:
            result = 1
        unified_data.at[index,'mun_result'] = result
        if csk_winner != 'Super Kings':
            unified_data.at[index,'csk_result'] = -1
    write_panda_to_csv(unified_data,unified_file)

get_result()
