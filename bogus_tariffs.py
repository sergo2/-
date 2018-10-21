# -*- coding: utf-8 -*-
from config import * 

def calc_FO_tariffs(df_full):
    # find a station2
    arbitr_station = df_full.iloc[0, 2]
    # replace the arbitrary station2 by FO one for non-sugar commodities
    df_FO = df_full[(df_full['station2'] == arbitr_station) & (df_full['commodity'] != commodity_dict['сахар'])]
    df_FO['station2'] = FO_station
    df_FO['baseTariff'] = FO_tariff
    df_FO['deadline'] = sugar_deadline    
    return df_FO

def calc_zero_tariffs(df_full):
    station_list = df_full['station1'].unique()
    # find a station2
    arbitr_station = df_full.iloc[0, 2]
    # replace the arbitrary station2 by station1
    df_zero = df_full[df_full['station2'] == arbitr_station]
    df_zero['station2'] = df_zero['station1']
    df_zero['baseTariff'] = zero_tariff
    df_zero['deadline'] = zero_deadline   
    return df_zero
