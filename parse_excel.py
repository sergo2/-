# -*- coding: utf-8 -*-
from config import * 

def parse_excel_file(excel_file_name):
    # read one Excel file
    sheet_dict = pd.read_excel(excel_file_name, sheet_name=None, header=None, skiprows=4)
    # concatenate all sheets in one DataFrame
    df_excel = pd.concat(sheet_dict, ignore_index=True)
    # select useful columns
    df_csv = df_excel.iloc[:, list(cols_dict.keys())]
    df_csv = df_csv.rename(columns=cols_dict, copy = True)
    # mapping commodity to its code
    df_commodity = pd.DataFrame.from_dict(commodity_dict, orient='index', columns = ['commodity'])
    df_csv = pd.merge(df_csv, df_commodity, left_on='commodity_name', right_index=True)
    # check that all numbers are numbers
    for column in df_csv.columns[1:]:
        df_error = df_csv[~df_csv[column].apply(np.isreal)]
        if df_error.empty is False:
            print("Нечисловое значение в поле: " + column + " файла: " + excel_file_name + "\n")
            print(df_error)
            return pd.DataFrame()
    # check that all cells are not empty
    for column in df_csv.columns[1:]:
        df_error_nan = df_csv[df_csv[column].apply(np.isnan)]
        if df_error_nan.empty is False:
            print("Пустое значение в поле: " + column + " файла: " + excel_file_name + "\n")
            print(df_error_nan)
            return pd.DataFrame()
    # calculate delivery time
    df_csv['deadline'] = df_csv['distance'].apply(lambda x: math.ceil(x/300))
    # arrange columns for flushing
    df_csv.drop(['commodity_name'], axis = 1, inplace = True)
    df_csv.drop(['distance'], axis = 1, inplace = True)
    df_csv['station1'] = df_csv['station1'].apply(lambda x: int(x))
    df_csv['station2'] = df_csv['station2'].apply(lambda x: int(x))
    df_csv = df_csv[target_cols]

    return df_csv

# print(parse_excel_file("C:\\Python_progs\\ТД\\Расчет ТД кукурузы-2018-2019 (тариф 2018) 30082018 для загрузки.xlsx"))