"""
Module for load info in diferent types
"""
from sqlalchemy import create_engine




def add_to_db(df):
    try:
        engine = create_engine("postgresql+psycopg2://postgres:1111@localhost:5432/hh_db")
    except:
        print("Error with db. Pls check the db admin")

    df.to_sql(
        name="vacancies", 
        con=engine,
        if_exists="replace",  
        index=False, 
    )

def add_to_csv(df):
    df.to_csv('data.csv')

