import loadingInfos
import emailSender
from sys import argv
import time


username = argv[1]

mediaDictionary = loadingInfos.getStarted(username)

animeURL = 'https://kitsu.io/anime/'

while(True):
    newMediaDict = loadingInfos.getStarted(username)
    for x in mediaDictionary:
        if x in newMediaDict:
            if mediaDictionary[x] is None or newMediaDict[x] is None:
                continue
            if mediaDictionary[x] < newMediaDict[x]:
                emailSender.send_email(x,animeURL + x)
    time.sleep(60 * 10)