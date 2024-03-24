from io import StringIO

import adbc_driver_postgresql.dbapi
import pandas as pd
import pyarrow.parquet
from sqlalchemy import create_engine


# Write a dataframe to a database table using df.to_sql
def write_to_db(df: pd.DataFrame, table_name: str, url: str) -> None:
    engine = create_engine(url)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Dataframe written to table {table_name} in the database")


# Write a dataframe to a database table using SQLAlchemy
def write_to_db_sqlalchemy(df: pd.DataFrame, table_name: str, url: str) -> None:
    engine = create_engine(url)
    connection = engine.raw_connection()
    cursor = connection.cursor()

    # create the table but first drop if it already exists
    command = f"""DROP TABLE IF EXISTS {table_name}; CREATE TABLE {table_name} ("Integers" integer,"Floats" double precision,"Strings" text);"""

    cursor.execute(command)
    connection.commit()

    # stream the data using 'to_csv' and StringIO(); then use sql's 'copy_from' function
    output = StringIO()
    # ignore the index
    df.to_csv(output, sep="\t", header=False, index=False)
    # jump to start of stream
    output.seek(0)
    contents = output.getvalue()
    cur = connection.cursor()
    # null values become ''
    cur.copy_from(output, table_name, null="")
    connection.commit()
    cur.close()
    connection.close()
    print("Dataframe written to table in the database")


# Write a dataframe to a database table using ADBC Driver
def write_to_db_adbc(
    df: pd.DataFrame,
    table_name: str,
    url: str,
    MODE: str = "create",
    BATCH_SIZE: int = 150000,
) -> None:
    df.to_parquet("random_data1.parquet")
    with adbc_driver_postgresql.dbapi.connect(url) as conn:
        with conn.cursor() as cur:
            table = pyarrow.parquet.ParquetFile("./random_data1.parquet")
            print(f"{MODE} table {table_name} in postgres...")
            cur.adbc_ingest(
                table_name, table.iter_batches(batch_size=BATCH_SIZE), mode=MODE
            )

        conn.commit()
        cur.close()
    conn.close()
    print("Dataframe written to table in the database")
