# -*- coding: utf-8 -*-
from config import * 

def select_max_tariff (df, station):
    # Choose one of the two rows with the higher tariff
    df_station = df[df['station1'] == station]
    df_merge = pd.merge(df_station, df_station, how='inner', on=['commodity', 'station1', 'station2'], suffixes=('_1', '_2'))
    df_max = df_merge[df_merge['baseTariff_1'] > df_merge['baseTariff_2']]
    df_max = df_max.drop(columns = ['baseTariff_2', 'deadline_2'], axis=1)
    df_max.rename(index=str, columns = {'baseTariff_1':'baseTariff', 'deadline_1': 'deadline'}, inplace = True)

    # Prepare matrix with no station
    df_no_station = df[df['station1'] != station]
    # Combine larger tariffs with no station    
    df_filtered = pd.concat([df_max, df_no_station], ignore_index=True)
    
    return df_filtered