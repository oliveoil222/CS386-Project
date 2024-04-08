import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps

uri = input('mongoDB database connection uri: ')

# create database class
class Database:
    # create init function
    def __init__(self):
        # add client to database class
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # add ssts database to database class
        self.db = self.client['ticket_tracker']

# create class for user
class User:
    # create init function
    def __init__(self, email, username, password):
        # connect to user database
        database = Database()
        self.collection = database.db['users']
        # create other user attricbutes
        self.username = username
        self.password = password
        self.email = email
    # function to add user to database collection
    def add_user(self):
        return None
    # create sign in function
    def sign_in(self):
        return None

# create a class for tickets
class Ticket:
    # create init function 
    def __init__(self, desc, title,  worker, device,  progress_level, work_progress):
        # connection to ticket collection
        database = Database()
        self.collection = database.db['tickets']
        self.description = desc
        self.title = title
        self.worker = worker
        self.device = device
        self.progress_level = progress_level
        self.work_progress = work_progress
    # method to add ticket to database collection
    # method to update worker
    # method to update progress level
    # method to update work progress
    def add_document(self):
        return None

# create subclass of tickets for solutions
class Solution:
    # create init function
    def __init__(self, team, work_progress, keywords, device_os):
        # connect to solution collection
        database = Database()
        self.collection = database.db['solutions']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('solutions')
        self.team = team
        self.work_progress = work_progress
        self.keywords = keywords
        self.device_os = device_os
        # solution info
        # method to add solution
    
# create subclass of users for clients
class Client:
    # create init function 
    def __init__(self, email, name, phone_num, contact_method):
        database = Database()
        self.collection = database.db['client']
        self.email = email
        self.name = name
        self.phone_number = phone_num
        self.contact_method = contact_method
        # method to get tickets
        # method to get devices
        # connection to client collection
        # client 
        
        
# create subclass of users for workers
class Worker:
    def __init__(self, name, email, team):
    # collection connection
        database = Database()
        self.collection = database.db['workers']
        self.name = name 
        self.email = email
        self.team = team
    # create init function 
        # connection to worker collection
        
# create class for teams
class Team:
    def __init__(self, name, workers):
        # collection connection
        database = Database()
        self.collection = database.db['teams']
        self.name = name
        self.workers = workers
    # create init function 
        # connection to team collection

        
# create class for devices
class Device:
    def __init__(self, worker, os_type, problems):
        database = Database()
        self.collection = database.db['devices']
        self.worker = worker
        self.os = os_type
        self.problems = problems
    # create init function 
        # connection to device collection

        
# add class for id trackers
class ID:
    def __init__(self):
        # get database collection
        database = Database()
        self.collection = database.db['id_tracker']
    def grab_info(self, collection_name):
        # get collection
        collection = self.collection
        # go through id tracker collection and only get ticket id count
        id_count = collection.find_one({'collection' : collection_name}, {'count' : 1})
        # convert the str to an int
        id_count = int(id_count['count'])
        # return the id count integer value
        return id_count
    def inc_id_count(self, collection_name):
        # get id tracker collection
        collection = self.collection
        # get current id count pymongo cursor 
        id_count = self.get_current_id(collection_name)
        # incriment id count
        new_id_count = id_count + 1
        id_to_update = {'collection' : collection_name}
        new_count = {'$set' : {'count' : new_id_count}}
        # return new collection id count pymongo cursor
        return collection.update_one(id_to_update, new_count)
        
    # create init function 
        # connection to id collection



