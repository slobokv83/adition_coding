import pandas as pd
from time import time
from constants import *

start = time()

df_mysql = pd.read_csv(mysql_name, sep='\t') 
df_hadoop = pd.read_csv(hadoop_name, skiprows=1, names = hadoop_columns)#, usecols = "A:AK"

df_hadoop = df_hadoop.iloc[:, :-sufficent_cols]

df1 = df_mysql.id
df2 = df_hadoop.id

df2=df2.str.replace("(","")
df1 = df1.astype(str)

df = pd.concat([df1, df2]).drop_duplicates(keep=False)

df_int = []
[df_int.append(int(i)) for i in df]
	
missing_records_from_hadoop = df_mysql.loc[df_mysql.id.isin(df_int)]
missing_records_from_mysql = df_hadoop.loc[df_hadoop.id.str.contains(df.iloc[-1])]

missing_records_from_hadoop.to_csv(hadoop_miss)
missing_records_from_mysql.to_csv(mysql_miss)

print('missing records from hadoop:', missing_records_from_hadoop)
print('missing records from mysql:', missing_records_from_mysql)
print('time spent: ', time() - start)