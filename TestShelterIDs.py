#!/usr/bin/python3

# Checks petfinder.com shelter IDs to see if their 
# pets are accessible via the API

from time import sleep
from json import loads
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError

base_url = 'http://api.petfinder.com/pet.getRandom?'
key = 'redacted'
ids = ['AL58', 'AL348', 'AL123', 'AL05', 'AL28', 'AL367', 'AL242', 'AL56', 'AL289', 'AL244', 'AL377', 'AL280', 'AL179']

def main():
    print('Checking ' + str(len(ids)) + ' pet shelters for API access.')
    for shelter_id in ids:
        good = checkShelter(shelter_id)
        print(shelter_id + ' has a ' + ('WORKING' if good else 'NON-WORKING') + ' API')

def checkShelter(shelter_id):
    print('Checking ' + shelter_id + '...')
    params = {'key': key, 'format': 'json', 'shelterid': shelter_id, 'output': 'full'}
    url = base_url + urlencode(params)
    try:
        response = urlopen(url)
    except URLError as e:
        print('URL Error encountered: ' + str(e))
        return False
    sleep(1)
    rawReply = response.read()
    reply = loads(rawReply.decode('utf-8'))
    if len(reply['petfinder']['header']['status']['message']) == 0:
        return True
    else:
        status = reply['petfinder']['header']['status']['message']['$t']
        print('Petfinder API Error: ' + status)
        return False

if __name__=='__main__':
    main()
