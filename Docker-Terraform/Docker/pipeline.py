import pandas as pd
import wget
import gzip
import shutil
import os
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name_1 = params.table_name_1
    url_1 = params.url_1
    csv_name_1 = 'output1.csv'
    table_name_2 = params.table_name_2
    url_2 = params.url_2
    csv_name_2 = 'output2.csv'
    

    # Descargar los archivos
    file = wget.download(url_1)
    file2 = wget.download(url_2)
    
    # Ruta donde se descomprimirá el archivo
    output_file = file.replace('.gz', '')

    # Descomprimimos el archivo csv.gz
    with gzip.open(file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Eliminamos el archivo .gz
    os.remove(file)

    # Creamos los dataframes
    df1 = pd.read_csv(output_file)
    df2 = pd.read_csv(file2)

    # Pasamos a tipo datetime los campos de fecha
    df1.lpep_pickup_datetime = pd.to_datetime(df1.lpep_pickup_datetime)
    df1.lpep_dropoff_datetime = pd.to_datetime(df1.lpep_dropoff_datetime)
    
    # Conectarse a la base de datos
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    
    # Insertamos la tabla green_tripdata
    df1.head(n=0).to_sql(name = table_name_1, con=engine, if_exists='replace')
    t_start = time()
    df1.to_sql(name = table_name_1, con=engine, if_exists='append', index=False)
    t_end = time()
    print(f'Inserted csv_1 ... took {t_end - t_start:.3f} seconds')
    
    # Insertamos la tabla zones
    df2.head(n=0).to_sql(name = table_name_2, con=engine, if_exists='replace')
    t_start = time()
    df2.to_sql(name = table_name_2, con=engine, if_exists='append', index=False)
    t_end = time()
    print(f'Inserted csv_2 ... took {t_end - t_start:.3f} seconds')

if __name__ == '__main__':  
    
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name_1', help='name of the first table where we will write the resolts to')
    parser.add_argument('--url_1', help='url of the first csv file')
    parser.add_argument('--table_name_2', help='name of the second table where we will write the resolts to')
    parser.add_argument('--url_2', help='url of the second csv file')

    args = parser.parse_args()
    
    main(args)