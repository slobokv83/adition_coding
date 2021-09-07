from sqlalchemy import create_engine
import pandas as pd
import os

os.chdir('../')
PROJECT_ABSOLUTE_PATH = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))

mysql_name = PROJECT_ABSOLUTE_PATH + '\\' + 'csv\\mysql.csv'

df_mysql = pd.read_csv(mysql_name, sep='\t')
print(df_mysql)
engine = create_engine(f'sqlite:///{basedir}/server/app.db')
connection = engine.connect()

df_mysql.to_sql('advertisement', con=engine, index=False, if_exists='append')