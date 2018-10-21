# -*- coding: utf-8 -*-
from config import * 

def diff_to_baseline(df_base, df_csv_full):
          
   df_inner_merge = pd.merge(df_base, df_csv_full, how='inner', on=['commodity', 'station1', 'station2'], suffixes=('_old', '_new'))
   df_inner_diff = df_inner_merge[df_inner_merge['baseTariff_old'] != df_inner_merge['baseTariff_new']]
   
   df_right_merge = pd.merge(df_base, df_csv_full, how='right', on=['commodity', 'station1', 'station2'], suffixes=('_old', '_new'))
   df_right_diff = df_right_merge[~df_right_merge.isin(df_inner_merge)].dropna(how='all')
   
   df_left_merge = pd.merge(df_base, df_csv_full, how='left', on=['commodity', 'station1', 'station2'], suffixes=('_old', '_new'))
   df_left_diff = df_left_merge[~df_left_merge.isin(df_inner_merge)].dropna(how='all')
   
   df_inner_diff['result'] = 'ИЗМЕНЕНИЕ'
   df_right_diff['result'] = 'ДОБАВЛЕНИЕ'
   df_left_diff['result']  = 'ПРОПАЖА'
   
   df_diff = pd.concat([df_inner_diff, df_right_diff, df_left_diff], ignore_index=True)
   df_diff.drop(columns = ['deadline_old', 'deadline_new'], inplace = True)
            
   return df_diff