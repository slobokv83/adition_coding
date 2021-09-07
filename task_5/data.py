import pandas as pd
from utils.constants import mysql_name


df_mysql = pd.read_csv(mysql_name, sep='\t')
dict_mysql = df_mysql.to_dict('records')
