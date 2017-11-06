#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Based on an example script from Google's API documentation. 
#
#
#
#
from __future__ import print_function
import httplib2
import os
import alarmFunc
from time import sleep
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Cavemanalarm'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    if not os.path.exists(CLIENT_SECRET_FILE) :
        print('The Credential File is not available please create or place it in this folder. More information can be found in the ReadMe file.')
        sys.exit()
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-calendarUpdate.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
def getcalendar():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.now().isoformat() + '+01:00' # 'Z' indicates UTC time +01:00 is GMT etc. 
    print('Getting the upcoming 5 events')
    try :
        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=5, singleEvents=True,
            orderBy='startTime').execute()
    except httplib2.ServerNotFoundError:
        print("Could not access server")
        return False           
    events = eventsResult.get('items', [])
    return events

def main():
    start = True
    recurence = 4449
    failOver = 60
    now = datetime.datetime.now().isoformat() + '+01:00' # 'Z' indicates UTC time
    while 1 == 1:
        events = getcalendar()
        if not events:
            print("No Events Found")
            if start != True :
                alarmFunc.run(oldevents,recurence)
            else:
                sleep(failOver)
        else :
            alarmFunc.run(events, recurence)
            oldevents = events
            start = False

if __name__ == '__main__':
    main()
