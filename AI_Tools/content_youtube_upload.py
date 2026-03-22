import os
import sys
import argparse
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
import pickle

# The CLIENT_SECRETS_FILE is the path to the JSON file you downloaded
CLIENT_SECRETS_FILE = "PDCT_Real_Estate/C Storyboarding/0. Asset/A Personal Video/credentials.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    credentials = None
    token_path = '.pass/token_youtube_v3.pickle'
    
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            credentials = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def initialize_upload(youtube, options):
    tags = None
    if options.keywords:
        tags = options.keywords.split(',')

    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category
        ),
        status=dict(
            privacyStatus=options.privacyStatus
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(options.file, chunksize=1024*1024, resumable=True)
    )

    resumable_upload(insert_request)

def resumable_upload(request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print('Uploading file... %d%%' % int(status.progress() * 100))
            if response is not None:
                if 'id' in response:
                    print('Video id "%s" was successfully uploaded.' % response['id'])
                else:
                    exit('The upload failed with an unexpected response: %s' % response)
        except Exception as e:
            print('An error occurred: %s' % e)
            exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Video file to upload')
    parser.add_argument('--title', help='Video title', default='Test Upload')
    parser.add_argument('--description', help='Video description', default='Test Description')
    parser.add_argument('--category', help='Numeric video category. See https://developers.google.com/youtube/v3/docs/videoCategories/list', default='22')
    parser.add_argument('--keywords', help='Video keywords, comma-separated', default='')
    parser.add_argument('--privacyStatus', help='Video privacy status', default='private', choices=['public', 'private', 'unlisted'])
    
    args = parser.parse_args()

    if not os.path.exists(args.file):
        exit('Please specify a valid file using the --file= parameter.')

    youtube = get_authenticated_service()
    try:
        initialize_upload(youtube, args)
    except Exception as e:
        print(e)
