import pandas as pd
from sqlalchemy import create_engine

data_1 = pd.read_excel('/Users/adriaferrer/Desktop/inflation_raw.xlsx')

driver = 'mysql+pymysql:'
user = 'root'
password = '17028854'
ip = '35.195.111.11'
database = 'Avocalypse'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)

data_1.to_sql('inflation',con=engine)