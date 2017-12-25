from pymongo import MongoClient, ASCENDING
from config import *

class AppDb(object):
    def __init__(self):
        self._client = MongoClient(MONGO_URL)
        self._db = self._client[MONGO_DB]
        self._coll = self._db[MONGO_COLL]

    def getUser(self, userId, groupId):
        return self._coll.find_one({
            'userId':userId,
            'groupId':groupId
        })
        
    def hasUser(self, userId, groupId):
        return bool(self.getUser())

    def createUser(self, userId, groupId):
        if self.hasUser(userId, groupId):
            return None
        else:
            self._coll.insert_one({
                'userId': userId,
                'groupId': groupId,
                'tags': {

                }
            })
    
    def addTag(self, userId, groupId, tag):
        self.createUser(userId, groupId)
        u = self.getUser()
        if tag in u['tags']:
            update_doc = {
                "$set": {
                    "tags": {
                        tag: 1
                    }
                }
            }
        else:
            update_doc = {
                "$inc": {
                    "tags": {
                        tag: u['tags'][tag] + 1
                    }
                }
            }
        self._coll.update_one({
            "userId": userId,
            "groupId": groupId
        }, update_doc)
    
    def listTag(self, groupId, tag):
        return self._coll.find({
            "groupId": groupId
        }, limit=5).sort(['tag.' + tag, ASCENDING])
