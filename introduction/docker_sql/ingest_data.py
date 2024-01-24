import os
import argparse
import gzip
import shutil
from time import time
import pandas as pd
from sqlalchemy import create_engine

def unzip_csv_gz(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url
    csv_name = 'output.csv'
    input_file = 'your_file.csv.gz'
    
    os.system(f"wget {url} -O {input_file}")
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
    
    print(f"Unzipping {input_file} to {csv_name}...")
    unzip_csv_gz(input_file, csv_name)
    print("Unzip complete.")
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table, con=engine, if_exists='replace')
    df.to_sql(name=table, con=engine, if_exists='append')
    
    while True:
        t_start = time()
        
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table, con=engine, if_exists='append')

        t_end = time()

        print(f"Inserted another chunk..., and it took {t_end - t_start}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Inest data by downloading CSV files, processing the data and uploading the data into any provided postgres database.')
    
    parser.add_argument('--user',  help='username of the postgres database')
    parser.add_argument('--password',  help='Password to the postgres database')
    parser.add_argument('--host',  help='host of the postgres database', default='localhost')
    parser.add_argument('--port', default=5432, help='port of the postgres database')
    parser.add_argument('--db', help='Database name to connect to')
    parser.add_argument('--table', help='table name to connect to')
    parser.add_argument('--url', help='url to the csv data')

    args = parser.parse_args()
    
    main(args)
