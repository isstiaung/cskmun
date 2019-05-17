import pandas as pd
from config import *
from utils import *
import os

def clean_csvs():
    _clean_csvs(mun_dir,combined_mun_file,True,mun_to_drop)
    _clean_csvs(csk_dir,combined_csk_file,False,csk_to_drop)

def _clean_csvs(dir,file,is_united,columns_to_drop):
    combined_frame = get_combined_file(dir,file,is_united)
    combined_frame.drop(columns_to_drop,axis=1,inplace=True)
    write_combined_file(combined_frame,dir,file)

def get_combined_file(dir,file,is_united):
    os.chdir(dir)
    return read_panda_csv(file,is_united)

def write_combined_file(combined_frame,dir,file):
    os.chdir(dir)
    write_panda_to_csv(combined_frame,file)

clean_csvs()
