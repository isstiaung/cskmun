from config import *
from utils import *
from pull_csk_data import *
from pull_utd_data import *
from combine_files import *
from clean_csvs import *
from unify import *
from get_result import *
from played_first import *
from analysis import *


pull_csk_data()
pull_utd_data()
combine_files()
clean_csvs()
unify_data()
get_match_result()
set_played_first()
analysis()
