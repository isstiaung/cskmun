import pandas as pd
import glob,os
import config


os.chdir(config.csk_dir)
csk_files = glob.glob("./*.csv")
combined_csk = pd.concat( [ pd.read_csv(f) for f in csk_files ] )
combined_csk.to_csv( "combined_csk.csv", index=False )

os.chdir(config.mun_dir)
mun_files = glob.glob("./*.csv")
combined_mun = pd.concat( [ pd.read_csv(f) for f in mun_files ] )
combined_mun.to_csv( "combined_mun.csv", index=False )
