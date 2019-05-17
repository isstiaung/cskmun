import pandas as pd
import glob,os
from config import *
from utils import read_panda_csv,write_panda_to_csv,concat_panda

def combine_files():
    _combine_files(csk_dir,unified_date_column,combined_csk_file)
    _combine_files(mun_dir,unified_date_column,combined_mun_file)
    print "Done combining files"
def _combine_files(dir,date_column,combined_file):
    os.chdir(dir)
    files = glob.glob(csvs)
    combined_csv = [read_panda_csv(file,True) for file in files ]
    combined_frame = concat_panda(combined_csv)
    sorted_frame = combined_frame.sort_values([date_column])
    write_panda_to_csv(sorted_frame,combined_file)

combine_files()
