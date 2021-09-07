from constants_spark import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from constants_spark import *
# spark = SparkSession.builder.getOrCreate()

'''
Create pyspark session
'''
spark = SparkSession.builder.appName('Missing_records').getOrCreate()

'''
Read csv files to dataframes; mysql dataframe needs tab delimiter
'''
df_mysql = spark.read.csv(mysql_name, header=True, sep="\t")
df_hadoop = spark.read.csv(hadoop_name, header=True)

'''
Rename column '(id' from hadoop.csv just to be compared with the 'id column 
from mysql.csv
'''
df_hadoop = df_hadoop.withColumnRenamed('(id', 'id')

'''
Replace all values from the hadoop 'id' column to be compared with the mysql
'id column' - e.g. replace '(6221540456511701567' with '6221540456511701567'
'''
df_hadoop = df_hadoop.withColumn('id', regexp_replace('id', '\\(', ''))

'''
find missing values in column 'id' and return dataframe which contains values:
1. comparing mysql to hadoop
2. comparing hadoop to mysql
'''
df_m = df_mysql.select('id').subtract(df_hadoop.select('id'))
df_h = df_hadoop.select('id').subtract(df_mysql.select('id'))

'''
from dataframes 'id' missing values, find all records which contain the values
from 'id' columns
'''
missing_records_from_hadoop = df_mysql.join(df_m, ['id'])
missing_records_from_mysql = df_hadoop.join(df_h, ['id'])

'''
show all records missing from
1. mysql
2. hadoop
'''
missing_records_from_hadoop.show()
missing_records_from_mysql.show()

# left_join = mysql.join(hadoop, hadoop['id'] == mysql['id'], how='left')
# left_join.filter(left_join['id'].isNull()).show()

# list_m = list(df_m.toPandas()['id'])
# list_h = list(df_h.toPandas()['id'])

# print('LISTA****:',list_m)

# df_mysql.filter(df_mysql['id'].isin(df_m)).show()

# print(spark)
# mysql = spark.read.format("csv").option("header", "true").load("..\\csv\\mysql.csv")

# df_mysql.join(df_hadoop.select('id'), on=['id'], how='right').show() 