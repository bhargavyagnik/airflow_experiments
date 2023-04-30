import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
import sqlite3
import extract

DATABASE_LOCATION = "sqlite:///album_tracks.sqlite"

if __name__ == "__main__":
	load_df=extract.return_dataframe()
	print(load_df)
#Loading into Database
	engine = sqlalchemy.create_engine(DATABASE_LOCATION)
	conn = sqlite3.connect('album_tracks.sqlite')
	cursor = conn.cursor()

	#SQL Query to Create Played Songs
	sql_query_1 = """
	CREATE TABLE IF NOT EXISTS album_track(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	album_name VARCHAR(200),
	release_dates VARCHAR(200),
	img_urls VARCHAR(200)
	)
	"""

	cursor.execute(sql_query_1)
	print("Opened database successfully")

    #We need to only Append New Data to avoid duplicates
	try:
		load_df.to_sql("album_track", engine, index=False, if_exists='append')
	except:
		print("Data already exists in the database")

	conn.close()
	print("Close database successfully")
