# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
import os
import time

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

path_to_excel_files = "C:\\Python_progs\\ТД\\"
output_file_suffix = "nlk"

# Мэппинг колонок из Excel-файла на колонки в csv. Первая колонка имеет нулевой номер. Имя товара и расстояние будет заменено
cols_dict = {6:'commodity_name',2:'station1',4:'station2',7:'baseTariff',5:'distance'}
# Мэппинг кодов товара на название
commodity_dict = {'пшеница':402, 'ячмень':452, 'кукуруза':453, 'сахар':454, 'соя':455}
# Целевой порядок колонок в csv-файле
target_cols = ['commodity','station1','station2','baseTariff','deadline']
# Тип строк в diff-файле
diff_type_dict = {'both':'ИЗМЕНЕНИЕ', 'right_only':'ДОБАВЛЕНИЕ', 'left_only':'УДАЛЕНИЕ'}