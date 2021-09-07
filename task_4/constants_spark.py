import os

os.chdir('../')
PROJECT_ABSOLUTE_PATH = os.getcwd()

mysql_name = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\mysql.csv'
hadoop_name = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\hadoop.csv'
hadoop_miss = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\hadoop_miss.csv'
mysql_miss = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\mysql_miss.csv'