import json
from sys import argv
import requests

username = argv[1]

#This is the method to get a user's ID.
def getUserID(user):
    URL_GET_User = 'https://kitsu.io/api/edge/users?filter[name]=' + user
    resp = requests.get(URL_GET_User)
    if resp.status_code != 200:
        print ("API Error" + resp)
    print (resp)
    userID = resp.json()['data'][0]['id']
    print(userID)
    return userID

def getUserLibrary(user):
    userID = getUserID(user)
    URL_GET_Library = 'https://kitsu.io/api/edge/users/'+ userID + '/library-entries'
    resp = requests.get(URL_GET_Library)
    if resp.status_code != 200:
        print ("API Error getUserLibrary " + resp)
    print(resp)
    userLibrary = (resp.json()['data'])
    print (userLibrary)
    return userLibrary

getUserLibrary(username)