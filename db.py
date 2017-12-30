from pymongo import MongoClient, DESCENDING
from config import *
import datetime

class AppDb(object):
    def __init__(self):
        self._client = MongoClient(MONGO_URL)
        self._db = self._client[MONGO_DB]
        self._coll = self._db[MONGO_COLL]
        self._limit = self._db[MONGO_LIMIT]
        self._username = self._db[MONGO_USERNAME]

    def getUser(self, userId, groupId):
        return self._coll.find_one({
            'userId':userId,
            'groupId':groupId
        })
        
    def hasUser(self, userId, groupId):
        return bool(self.getUser(userId, groupId))

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
        tag = str(tag).lower()
        self.createUser(userId, groupId)
        u = self.getUser(userId, groupId)

        update_doc = {
            "$inc": {
                "tags.{0}".format(tag): 1
            }
        }
        self._coll.update_one({
            "userId": userId,
            "groupId": groupId
        }, update_doc)
    
    def listTag(self, groupId, tag):
        tag = tag.lower()
        return self._coll.find({
            "groupId": groupId
        }, limit=5).sort('tags.{0}'.format(tag), DESCENDING)

    def setUserName(self, username, userId):
        user = self._username.find_one({
            "userId": userId
        })
        if user:
            if username != user["name"]:
                self._username.update_one({
                    "userId": userId
                }, {
                    "$set": {
                        "name": username
                    }
                })
        else:
            self._username.insert_one({
                "userId": userId,
                "name": username
            })

    def getUserName(self, userId):
        user = self._username.find_one({
            "userId": userId
        })
        if user:
            return user["name"]
        else:
            return "Unknown"

    def addLimit(self, userId, groupId):
        self._limit.create_index("date", expireAfterSeconds=60)
        self._limit.insert_one({
            "userId": userId,
            "date": datetime.datetime.utcnow()
        })

    def isLimied(self, userId):
        tag_count = self._limit.count({
            "userId": userId
        })
        return tag_count > LIMIT_PRE_MIN
