# -*- coding: utf-8 -*-
from config import * 

def diff_to_baseline(df_base, df_csv_full):
   
   df = pd.merge(df_base, df_csv_full, how='outer', on=['commodity', 'station1', 'station2'], suffixes=('_old', '_new'), indicator=True, sort=True)

   # drop unchanged tariffs
   df = df.drop(df[(df._merge == 'both') & (df.baseTariff_old == df.baseTariff_new)].index)
   
   # mapping diff reason to its Russian name
   df_diff_type = pd.DataFrame.from_dict(diff_type_dict, orient='index', columns = ['diff_type'])
   df = pd.merge(df, df_diff_type, left_on='_merge', right_index=True)
   
   df.drop(columns = ['deadline_old', 'deadline_new', '_merge'], inplace = True)

   return df