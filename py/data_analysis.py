import pandas as pd
from utils import *
from config import *
from pull_utd_data import *
from pull_csk_data import *
from combine_files import *
from clean_csvs import *

def setup():
    pull_utd_data()
    pull_csk_data()
    combine_files()
    clean_csvs()

def unify_data():
    combined_mun_frame = get_combined_file(mun_dir,combined_mun_file)
    combined_csk_frame = get_combined_file(csk_dir,combined_csk_file)

    unified_frame = pd.merge(combined_mun_frame,combined_csk_frame, on=unified_date_column)
    unified_frame[new_column]=default_column_value
    os.chdir(unified_dir)
    write_panda_to_csv(unified_frame,unified_file)
    print "Done unifying data"
    print read_panda_csv(unified_file,True)

if data_unification:
    setup()
    unify_data()
else:
    print "Get to work"
