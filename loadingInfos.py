import json
from sys import argv
import requests


counter = 0
medias = ['anime']

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

#This is the method to get a user's Library.
def getStarted(user):
    userID = getUserID(user)
    URL_GET_Library = 'https://kitsu.io/api/edge/library-entries?filter[userId]=' + userID
    resp = requests.get(URL_GET_Library)
    if resp.status_code != 200:
        print ("API Error getStarted ")
        print (resp)
        exit()
    print(resp)
    userInfos = (resp.json())


    return getUserMedia(userInfos, 'anime')


def getMediaEpisodes(mediaAttributes):
    return mediaAttributes['episodeCount']

def getUserMedia(userInfos, media):
    mediaDictionary = {}
    userLinks = userInfos['links']
    userLibrary = userInfos['data']
    while ('next' in userLinks):
        for i in range( 0,len(userLibrary) ):
            mediaURL = userLibrary[i]['relationships'][media]['links']['related']
            mediaReq = requests.get(mediaURL)
            if mediaReq.status_code != 200 : 
                print ('ERROR MEDIAREQ !!!')
                exit()
            mediaData = mediaReq.json()['data']
            if(mediaData is None):
                continue
            #mediaID = mediaData['id']
            mediaAttributes = mediaData['attributes']
            mediaSlug = mediaAttributes['slug']
            if mediaAttributes['status'] != 'finished':
                mediaEpisodes = getMediaEpisodes(mediaAttributes)
                mediaDictionary[mediaSlug] = mediaEpisodes
                #counter += 1 
            mediaTitle = mediaAttributes['canonicalTitle']
            print(mediaTitle)
        nextRequest = requests.get(userLinks['next'])
        userInfos = nextRequest.json()
        userLinks = userInfos['links']
        userLibrary = userInfos['data']
        print(len(userLibrary))
    print ('Length of mediaDictionary : ')
    print(len(mediaDictionary))
    for x in mediaDictionary:
        print(mediaDictionary[x])
    return mediaDictionary