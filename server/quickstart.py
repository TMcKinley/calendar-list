from __future__ import print_function
import datetime
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=3200)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #now = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).isoformat()+'Z'
    tzinfo = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    today = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0,tzinfo=tzinfo).isoformat()
    #tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=30)).replace(hour=0,minute=0,second=0,microsecond=0,tzinfo=tzinfo).isoformat()

    print(today)
    print(tomorrow)

    newEventArray = []

    #print(now)
    #print('Getting the upcoming 10 events')
    events_result = service.events().list(
        calendarId='n64tt3v1qmpm3eko90duvn7s2s@group.calendar.google.com',
        timeMin=today,
        timeMax=tomorrow,
        maxResults=250,
        singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    print(len(events))

    if not events:
        print('No upcoming events found.')
    for event in events:
        id = event['id']
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        description = event['summary']

        newEventArray.append({
            'id': id,
            'start_time': start,
            'end_time': end,
            'description': description,
            'completed': 0
        })

        #print(event)
        print(start, event['summary'])
    
    with open('../public/eventlist.json', 'w') as f:
        json.dump(newEventArray, f) 
    with open('../dist/eventlist.json', 'w') as f:
        json.dump(newEventArray, f) 

if __name__ == '__main__':
    main()