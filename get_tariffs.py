# -*- coding: utf-8 -*-
from parse_excel import *

df_csv_list = []

for item in os.listdir(path_to_excel_files):
    item_path = os.path.join(path_to_excel_files, item)
    if os.path.isfile(item_path):
        if item_path.endswith(".xlsx") or item_path.endswith(".xls"):
            print(item_path)
            df_csv = parse_excel_file(item_path)
            if df_csv.empty is False:
                df_csv_list.append(df_csv)
            else:
                print("Устраните ошибки в Excel-файлах!")
                exit()      
if len(df_csv_list) > 0:
    # concatenate all sheets in one DataFrame
    df_csv_full = pd.concat(df_csv_list, ignore_index=True)
    df_csv_full.sort_values(by=target_cols, inplace=True)
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    csv_file_name = csv_file_suffix + "_" + timestr + ".csv"
    df_csv_full.to_csv(csv_file_name, index=False)
    print("Добавлено записей в файл " + csv_file_name + " : " + str(df_csv_full.shape[0]))
else:
    print("Не найдено Excel-файлов в директории: " + path_to_excel_files)
