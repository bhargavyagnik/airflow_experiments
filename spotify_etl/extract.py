import pandas as pd 
import requests
from datetime import datetime
import datetime
import get_Token


# Creating an function to be used in other python files
def return_dataframe(): 
	input_variables = {
	"Accept" : "application/json",
	"Content-Type" : "application/json",
	"Authorization" : "Bearer {token}".format(token=get_Token.fetch_token())
	}

	today = datetime.datetime.now()
	yesterday = today - datetime.timedelta(days=1) #no of Days u want the data for
	yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

	# Download all songs you've listened to "after yesterday", which means in the last 24 hours      
	r = requests.get("https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02/albums", headers = input_variables)

	data = r.json()
	album_names = []
	release_dates = []
	img_urls = []
	
	timestamps = []
	
	# Extracting only the relevant bits of data from the json object      
	for album in data["items"]:
		album_names.append(album["name"])
		release_dates.append(album["release_date"])
		img_urls.append(album["images"][0]["url"])

	# Prepare a dictionary in order to turn it into a pandas dataframe below       
	album_dict = {
	"album_name" : album_names,
	"release_dates": release_dates,
	"img_urls" : img_urls,
	}
	song_df = pd.DataFrame(album_dict, columns = ["album_name", "release_dates", "img_urls"])
	return song_df
    
if __name__ =="__main__":
	print(return_dataframe())
