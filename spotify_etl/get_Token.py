import base64
import requests
from decouple  import config

client_id = config("client_id")
client_secret = config("client_secret")
# Encode the client ID and secret as base64
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

# Set up the request parameters
auth_url = 'https://accounts.spotify.com/api/token'
headers = {'Authorization': f'Basic {client_creds_b64.decode()}'}
data = {'grant_type': 'client_credentials'}


def fetch_token():
# Send the POST request
	response = requests.post(auth_url, headers=headers, data=data)
# Parse the response JSON to get the access token
	if response.status_code == 200:
		response_data = response.json()
		access_token = response_data.get('access_token')
		return access_token
	else:
		return None
