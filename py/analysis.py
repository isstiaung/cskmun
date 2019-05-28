import pandas as pd
import os
from config import unified_dir,unified_file
from utils import read_panda_csv
# did analysis using panda table pivots in interpreter
#tables and pivots derived can be found below

def analysis():
    os.chdir(unified_dir)
    df = read_panda_csv(unified_file,False)
    played_first = '1'
    #data_cleanup
    df.replace(['H','A','N'],[1,-1,0],inplace=True)
    df.drop('Opponent',axis=1,inplace=True)
    df.drop('Team 1',axis=1,inplace=True)
    df.drop('Team 2',axis=1,inplace=True)
    df.drop('mun_winner',axis=1,inplace=True)
    df.drop('csk_winner',axis=1,inplace=True)
    df.drop('date',axis=1,inplace=True)
    df.drop('newdate',axis=1,inplace=True)
    df.drop('time_x',axis=1,inplace=True)
    df.drop('time_y',axis=1,inplace=True)
    df.loc[df['Ground'] != 'Chennai','Ground'] = -1
    df.loc[df['Ground'] == 'Chennai','Ground'] = 1

    mun_table=df.query("played_first==1")
    csk_table = df.query("played_first==0")

    mun_pivot = pd.pivot_table(mun_table,values='place',index=["mun_result","csk_result"],aggfunc='count')
    csk_pivot = pd.pivot_table(csk_table,values='place',index=["csk_result","mun_result"],aggfunc='count')

    both_wins = df.query("csk_result==1 & mun_result == 1")
    both_lose = df.query("csk_result==-1 & mun_result == -1")
    draws = df.query("mun_result == 0")

    print "Original Table"
    print df

    print "Table when utd plays first"
    print mun_table
    print "Table when csk plays first"
    print csk_table

    print "Table when both win"
    print both_wins

    print "Table when both lose"
    print both_lose

    print "Table when utd draws"
    print draws

    print "mun pivot table"
    print mun_pivot

    print "csk pivot table"
    print csk_pivot
