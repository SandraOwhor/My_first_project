'''
author: Sandra Owhor
date : March 19, 2022
contact: owhorsandra@gmail.com
'''

# import libraries
import pandas as pd
import sqlite3

# create dataframe from excel file
wiki_df = pd.read_excel('flatten_data_table-main/wikipedia_dataset_flat.xlsx',index_col=False,header=0)
print(wiki_df)

# create database and connection
db_conn = sqlite3.connect("flatten_data_table-main/wikipedia.db")

cur = db_conn.cursor()

# create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS wikiproject(
        date TEXT,
        page TEXT, 
        visits INTEGER)
    """
)
cur.execute("insert into wikiproject values ('date','page','visits')")
cur.execute("insert into wikiproject values ('2016-01-01','.xxx_en.wikipedia.org_all-access_all-agents','7089')")

# populate database table
wiki_df.to_sql('wikiproject', db_conn, if_exists='replace', index=False)

db_conn.commit()
db_conn.close()