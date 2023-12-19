from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import os


driver = "{SQL Server Native Client 11.0}"
server = "localhost"
database = "sara-nsrdb-dni;"

uid="sara"
pwd= "nrel"

def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/sara-nsrdb-dni')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

for ...:
    load(df, name)