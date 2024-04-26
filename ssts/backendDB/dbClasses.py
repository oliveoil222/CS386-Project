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
class UserCollection:
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
    def add_user(self, user):
        return None


class User:
    def __init__(self, user):
        self.name = user.name
        self.email = user.email



# create a class for tickets
class TicketCollection:
    # create init function 
    def __init__(self):
        # connection to ticket collection
        database = Database()
        self.collection = database.db['tickets']
    # method to add ticket to database collection
    # method to update worker
    # method to update progress level
    # method to update work progress
    def add_ticket(self, ticket):
        collection = self.collection
        # create document dictionary to add to the collection
            # the id is made by pymongo so we dont have to do that
        new_ticket = {
            'description': ticket.description,
            'title' : ticket.title,
            'type' : ticket.device_type,
            'worker' : ticket.worker,
            'device' : ticket.device
        }
        # return the document inserted into the ticket collection
        return collection.insert_one(new_ticket)
    def get_ticket(worker_email, device_id):
        return None

class Ticket:
    def __init__(self, desc, title, type, worker, device):
        self.description = desc
        self.title = title
        self.device_tyep = type
        self.worker = worker.email
        self.device = device.id_num
    


# create subclass of tickets for solutions
class SolutionCollection:
    # create init function
    def __init__(self):
        # connect to solution collection
        database = Database()
        self.collection = database.db['solutions']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('solutions')
        # solution info
        # method to add solution
    def add_solution(self, worker, work_progress, keywords, device):
        # set up connection to solution collection
        solutions = self.collection
        # create solution id
        solution_count = self.id_count
        soulution_id = 's' + str(solution_count)
        # add solution to collection of solutions
        new_solution = {
            'worker': worker,
            'work progress' : work_progress,
            'keywords' : keywords,
            'device': device.id_num
        }
        # return document pymongo id of new solution
        return solutions.insert_one(new_solution)
            # add team, work progress, keywords, device operating system
    def get_solutions(self, keywords, worker):
        return None
    
    
# create subclass of users for clients
class ClientCollection:
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
    def get_devices():
        return None
    
    def get_tickets():
        return None
    
    def get_worker():
        return None
        
        
# create subclass of users for workers
class WorkerCollection:
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
    
    def get_team_workers(self, team):
        name = team.name
        collection = self.collection
        workers = []
        for worker in collection.find({}, {'team': name}):
            team_worker = Worker(worker['name'], worker['email'], worker['team'])
            workers.append(team_worker)
        return workers

class Worker:
    def __init__(self, name, email, team):
        self.name = name
        self.email = email
        self.team = team

# create class for teams
class TeamCollection:
    def __init__(self):
        # collection connection
        database = Database()
        self.collection = database.db['teams']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('teams')
    # create init function 
    def add_team(self, name):
        # connection to team collection
        team_collection = self.collection
        # create id for team
        team_id = 'g' + str(self.id_count)
        # create new document for the new team
        new_team = {
            'team id' : team_id,
            'name' : name
        }
        # return the new team inserted into the team collection
        return team_collection.insert_one(new_team)
    def get_workers():
        # query the workers collection to get workers on specific team
        # 
        return None
    def get_tickets():
        # get the list of workers within the team
        # go through
        return None
    
class Team:
    def __init__(self, name):
        self.name = name
    def get_workers():
        return None
    def get_tickets():
        return None
    

        
# create class for devices
class DeviceCollection:
    def __init__(self):
        database = Database()
        self.collection = database.db['devices']
        # create id attribute
        id_collection = ID()
        self.id_count = id_collection.grab_info('teams')
    # method to add device to collection
    def add_device(self, client, os_type, problems):
        device_collection = self.collection
        # create device count
        dev_id = 'd' + str(self.id_count)
        new_device = {
            'device id' : dev_id,
            'client': client,
            'device type' : os_type,
            'problems' : problems
        }
        # return pymongo id of new document in collection
        return device_collection.insert_one(new_device)
    def get_device():
        # should retunr a Device type after finding query
        return None
    
    def get_worker():
        return None
    
    def get_tickets():
        return None
    
    def get_client(self, device):
        return None
    
class Device:
    def __init__(self, client, os_type, problems = False):
        self.client = client
        self.operating_sys = os_type
        self.problems = problems

    def get_worker(self):
        return None
    
    def get_client(self):
        return self.client
    
    def get_tickets():
        return None

# add class for id trackers
class ID:
    def __init__(self):
        # get database collection
        database = Database()
        self.collection = database.db['id_tracker']
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
    def grab_info(self, collection_name):
        # get collection
        collection = self.collection
        # go through id tracker collection and only get ticket id count
        id_count = collection.find_one({'collection' : collection_name}, {'count' : 1})
        # convert the str to an int
        id_count = int(id_count['count'])
        self.inc_id_count(collection_name)
        # return the id count integer value
        return id_count

        
    # create init function 
        # connection to id collection



