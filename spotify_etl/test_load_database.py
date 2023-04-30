import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
import sqlite3


DATABASE_LOCATION = "sqlite:///album_tracks.sqlite"

if __name__ == "__main__":
	engine = sqlalchemy.create_engine(DATABASE_LOCATION)
	conn = sqlite3.connect('album_tracks.sqlite')
	cursor = conn.cursor()

	#SQL Query to Create Played Songs
	sql_query_1 = """
	SELECT * FROM album_track
	"""
	cursor.execute(sql_query_1)
	rows = cursor.fetchall()
	print(rows)
	conn.close()
	print()
