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
    def __init__(self):
        # connection to ticket collection
        database = Database()
        self.collection = database.db['tickets']
    # method to add ticket to database collection
    # method to update worker
    # method to update progress level
    # method to update work progress
    def add_ticket(self, tick_cnt, desc, title, type,  worker, device, client, team):
        ticket_collection = self.collection
        # create ticket id
        ticket_id = 't' + str(tick_cnt)
        # create document dictionary to add to the collection
            # the id is made by pymongo so we dont have to do that
        new_ticket = {
            'ticket id' : ticket_id,
            'description': desc,
            'title' : title,
            'type' : type,
            'worker' : worker,
            'device' : device,
            'client' : client,
            'team' : team,
            
        }
        # return the document inserted into the ticket collection
        return ticket_collection.insert_one(new_ticket)

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
        # solution info
        # method to add solution
    def add_solution(self, team, work_progress, keywords, device_os):
        # set up connection to solution collection
        solutions = self.collection
        # create solution id
        solution_count = self.id_count
        soulution_id = 's' + str(solution_count)
        # add solution to collection of solutions
        new_solution = {
            'team' : team,
            'work progress' : work_progress,
            'keywords' : keywords,
            'operating system': device_os
        }
        # return document pymongo id of new solution
        return solutions.insert_one(new_solution)
            # add team, work progress, keywords, device operating system
        
    
# create subclass of users for clients
class Client:
    # create init function 
    def __init__(self):
        database = Database()
        self.collection = database.db['client']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('clients')
    # add client method
    def add_client(self, email, name, phone_num, contact_method):
        # set up client collection connection
        clients = self.collection
        # create client id
        id_num = self.id_count
        client_id = 'c' + str(id_num)
        # create a new document for the new client
        new_client = {
            'client id' : client_id,
            'email' : email,
            'name': name,
            'phone number' : phone_num,
            'contact method' : contact_method
        }
        # return the new added client pymongo id
        return clients.insert_one(new_client)
        
        
# create subclass of users for workers
class Worker:
    def __init__(self, name, email, team):
    # collection connection
        database = Database()
        self.collection = database.db['workers']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('workers')
    # add worker to collection
    def add_worker(self, name, email, team):
        worker_collection = self.collection
        # create worker id
        worker_id = 'w' + str(self.id_count)
        # create new document for the new worker
        new_worker = {
            'worker id' : worker_id,
            'name' : name,
            'email' : email,
            'team' : team
        }
        # return the new worker added to the collection
        return worker_collection.insert_one(new_worker)
            
# create class for teams
class Team:
    def __init__(self):
        # collection connection
        database = Database()
        self.collection = database.db['teams']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('teams')
    # create init function 
    def add_team(self, name, workers):
        # connection to team collection
        team_collection = self.collection
        # create id for team
        team_id = 'g' + str(self.id_count)
        # create new document for the new team
        new_team = {
            'team id' : team_id,
            'name' : name,
            'workers' : workers
        }
        # return the new team inserted into the team collection
        return team_collection.insert_one(new_team)

        
# create class for devices
class Device:
    def __init__(self):
        database = Database()
        self.collection = database.db['devices']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('teams')
    # method to add device to collection
    def add_device(self, worker, os_type, problems):
        device_collection = self.collection
        # create device count
        dev_id = 'd' + str(self.id_count)
        new_device = {
            'device id' : dev_id,
            'worker' : worker,
            'device type' : os_type,
            'problems' : problems
        }
        # return pymongo id of new document in collection
        return device_collection.insert_one(new_device)

        
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




