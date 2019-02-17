# -*- coding: utf-8 -*-
from parse_excel import *
from select_max_tariff import *
from diff_to_baseline import *

df_excel_list = []
df_base = pd.DataFrame

for item in os.listdir(path_to_excel_files):
    item_path = os.path.join(path_to_excel_files, item)
    if os.path.isfile(item_path):
        if item_path.endswith(".xlsx") or item_path.endswith(".xls"):
            print("Загружаю файл ТД: " + item_path)
            df_excel = parse_excel_file(item_path)
            if df_excel.empty is False:
                df_excel_list.append(df_excel)
                print("Успешно")
            else:
                print("Устраните ошибки в Excel-файлах!")
                exit() 
        elif item.startswith("bt_") and item.endswith(".csv"):
            print("Загружаю файл для сверки: " + item_path)
            df_base = pd.read_csv(item_path, sep = ';', engine="python")
            print("Успешно")    
if df_base.empty:
    print("Поместите файл для сверки bt_xxx.csv в папку с Excel-файлами " + path_to_excel_files + " !")
    exit() 
         
if len(df_excel_list) > 0:
    # concatenate all sheets in one DataFrame
    df_csv_full = pd.concat(df_excel_list, ignore_index=True)
    
    # delete same-station invisible tariffs
    df_csv_full = df_csv_full[df_csv_full['station1'] != df_csv_full['station2']]
    
    # add sugar tariffs from bt_xxx.csv
    df_sugar = df_base[df_base['commodity'] == commodity_dict['сахар']]
    df_csv_full = pd.concat([df_csv_full, df_sugar], ignore_index=True)
  
    # select route from 527101 with max tariff
    df_csv_full = select_max_tariff(df_csv_full, 527101)
    
    df_csv_full.sort_values(by=target_cols, inplace=True) 
    df_base.sort_values(by=target_cols, inplace=True) 

    # comparing to the base file
    df_diff = diff_to_baseline(df_base, df_csv_full)
    diff_file_name = path_to_excel_files + "diff.csv"
    df_diff.to_csv(diff_file_name, index=False, sep = ';', encoding='cp1251')
    print("Добавлено записей в файл сверки " + diff_file_name + " : " + str(df_diff.shape[0]))
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    csv_file_name = path_to_excel_files + output_file_suffix + "_" + timestr + ".csv"
    df_csv_full.to_csv(csv_file_name, index=False, sep = ';', encoding='cp1251')
    print("Добавлено записей в файл тарифов " + csv_file_name + " : " + str(df_csv_full.shape[0]))
    print("Добавьте маршруты для сахара вручную")
else:
    print("Не найдено Excel-файлов в директории: " + path_to_excel_files)
