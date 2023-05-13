import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler1(event, context):

    cilent_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id= "fd7aa42654254f01a930ab6a2726a981", client_secret= "b77a127b882a42aa9cbee7af0fa5642d")
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXbVhgADFy3im?si=0007c08d346a4bc6"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    spotify_data = sp.playlist_tracks(playlist_URI)   
    
    cilent = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    cilent.put_object(
        Bucket="warepam-airflow-bucket",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
        )