import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps


# class to initialize connections to mongoDB
class Connections:
    def __init__(self, uri):
        # client
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # ssts database
        self.db = self.client['ticket_tracker']
        # ticket collection
        self.ticket_collection = self.db['tickets']
        # worker collection
        self.worker_collection = self.db['workers']
        # device collection
        self.team_collection = self.db['teams']
        # team collection
        self.device_collection = self.db['devices']
        # client collection
        self.client_collection = self.db['clients']
        # solution collection
        self.solution_collection = self.db['solutions']
        # id tracker collection
        self.id_tracker_collection = self.db['id_tracker']

# 



