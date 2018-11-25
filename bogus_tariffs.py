# -*- coding: utf-8 -*-
from config import * 

def select_max_tariff (df, station):
    print(df.shape)
    df_station = df[df['station1'] == station]
    df_merge = pd.merge(df_station, df_station, how='inner', on=['commodity', 'station1', 'station2'], suffixes=('_1', '_2'))
    df_max = df_merge[df_merge['baseTariff_1'] > df_merge['baseTariff_2']]
    df_max.drop(columns = ['baseTariff_2', 'deadline_2'], inplace = True)
    df_max.rename(index=str, columns = {'baseTariff_1':'baseTariff', 'deadline_1': 'deadline'}, inplace = True)
#            df_error = df_csv[~df_csv[column].apply(np.isreal)]
    print(df[~df['station1'] == station])
#    print(df_max)

def calc_zero_tariffs(df_full):
    station_list = df_full['station1'].unique()
    # find a station2
    arbitr_station = df_full.iloc[0, 2]
    # replace the arbitrary station2 by station1
    df_zero = df_full[df_full['station2'] == arbitr_station]
    df_zero['station2'] = df_zero['station1']
    df_zero['baseTariff'] = zero_tariff
    df_zero['deadline'] = zero_deadline   
    print(df_zero)
    return df_zero

def calc_FO_tariffs(df_full):
    # find a station2
    arbitr_station = df_full.iloc[0, 2]
    # replace the arbitrary station2 by FO one for non-sugar commodities
    df_FO = df_full[(df_full['station2'] == arbitr_station) & (df_full['commodity'] != commodity_dict['сахар'])]
    df_FO['station2'] = FO_station
    df_FO['baseTariff'] = FO_tariff
    df_FO['deadline'] = sugar_deadline    
    return df_FO