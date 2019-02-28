import config
import difflib 
import pandas as pd
import pyodbc
import re 
import sqlalchemy

from datetime import datetime

def create_connection(): 
    conn_str = "mssql+pyodbc://{}:{}@{}/{}?driver={}".format(
        config.DB_USERNAME, 
        config.DB_PASSWORD, 
        config.SERVER_ADDRESS, 
        config.DB_NAME, 
        config.ODBC_DRIVER
    )

    engine = engine = sqlalchemy.create_engine(conn_str)
    return engine.connect()


def test_connection():
    try:
        print("Establishing connection to database...")

        with create_connection() as conn:
            print("Connection established")

            result = conn.execute('SELECT TOP 3 [_BMI_] FROM dbo.train')
            for row in result:
                print(row)
        
        return True
    except Exception as ex:
        print(ex)
        return False


def clean_data():
    with create_connection() as conn:
        print()
        print("Cleaning data started...")

        print("Step 1 - reading data from SQL database...")
        df = pd.read_sql("SELECT TOP 10 [_Id_], [_Ins_Age_], [_BMI_] FROM dbo.train", conn)
        df.columns = ['ID', 'Age', 'BMI']

        print("Step 2 - data cleaning, feature engineering etc.")
        df['Magic_Coefficient'] = df['Age'] * df['BMI']

        print("Step 3 - saving changes to SQL database ")
        values = str([ (row['ID'], row['Magic_Coefficient']) for _, row in df.iterrows() ])
        values = values.replace('[', '')
        values = values.replace(']', '')
        query = """
            UPDATE t
            SET t.[_Magic_Coefficient_] = x.MagicCoefficient
            FROM dbo.train t
            INNER JOIN 
                ( VALUES
                    {}
                ) AS x(Id, MagicCoefficient) 
                ON x.Id = t._Id_
            WHERE [_Id_] = x.ID;""".format(values)

        conn.execute(query)
        print("Done!")


connection_ok = test_connection()
if connection_ok == True:
    clean_data()