import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('./employee_data.csv')

# Update the connection URL with your PostgreSQL configuration
URL = "postgresql://postgres:jjm123@localhost:5432/postgres"

engine = create_engine(URL, echo=True)
df.to_sql('employee', engine, if_exists='replace')