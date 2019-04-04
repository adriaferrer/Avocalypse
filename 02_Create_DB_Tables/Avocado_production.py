import pandas as pd
from sqlalchemy import create_engine


production_table = pd.read_csv('/Users/adriaferrer/Avocalypse_data/FAOSTAT_production.csv')
production_table = production_table[['Area Code', 'Year Code', 'Value']]
production_table.rename(columns={'Value':'Total_protuction_t'}, inplace = True)

harvest_table = pd.read_csv('/Users/adriaferrer/Avocalypse_data/FAOSTAT_area_harvested.csv')
harvest_table = harvest_table[['Area Code', 'Year Code', 'Value']]
harvest_table.rename(columns={'Value':'Area harvested'}, inplace = True)

total_production_data = production_table.merge(harvest_table, on=['Area Code', 'Year Code'])


driver = 'mysql+pymysql:'
user = 'root'
password = ''#password goes here
ip = '35.195.111.11'
database = 'Avocalypse'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)

total_production_data.to_sql('production', con=engine)