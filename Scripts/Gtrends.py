import pandas as pd
from sqlalchemy import create_engine


trends = pd.read_csv('/Users/adriaferrer/Avocalypse_data/GTrends/multiTimeline.csv')
trends = trends.reset_index().drop(index=0)
trends = trends.rename(columns={'index': 'year', 'Categoría: Todas las categorías': 'popularity'})

trends['month'] = trends['year'].apply(lambda x: x[5:])

trends['year'] = trends['year'].apply(lambda x: x[:4])

trends = trends[['year', 'month', 'popularity']]

driver = 'mysql+pymysql:'
user = 'root'
password = '17028854'
ip = '35.195.111.11'
database = 'Avocalypse'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)
trends = trends.reset_index().drop(columns='index')

trends.to_sql('gtrend', con=engine)