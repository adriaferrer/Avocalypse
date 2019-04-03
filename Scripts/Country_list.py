import pandas as pd
from sqlalchemy import create_engine


price_table = pd.read_csv('/Users/adriaferrer/Avocalypse_data/FAOSTAT_pricing.csv')
countries = price_table.groupby(['Area', 'Area Code']).sum()
countries = countries.reset_index()[['Area', 'Area Code']]

driver = 'mysql+pymysql:'
user = 'root'
password = '17028854'
ip = '35.195.111.11'
database = 'Avocalypse'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)

countries.to_sql('countries', con=engine, if_exists='replace')