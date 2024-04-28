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
    # the user variable to input is a Worker/Client object
    def add_user(self, user):
        return None
    # the user variable to input is a Worker/Client object
    def find_user(self, user):
        # query to find a user in the user collection
        return None


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
        # create new ticket id for the ticket
        ticket.set_id_num()
        new_ticket = {
            'id' : ticket.id_num,
            'description': ticket.description,
            'title' : ticket.title,
            'type' : ticket.device_type,
            'worker' : ticket.worker,
            'device' : ticket.device,
            'status': ticket.status
        }
        # return the document inserted into the ticket collection
        return collection.insert_one(new_ticket)
    def update_ticket_status(self, ticket):
        return None
    
    def update_ticket_worker(self, ticket):
        return None
    
    def get_tickets(self, worker_email = None, device_id = None):
        collection = self.collection
        tickets = []
        # check if theres a worker email inputted
        if worker_email != None and device_id != None:
            # get query with both attributes
            for ticket in collection.find({}, {'worker': worker_email, 'decide': device_id}):
                ticket = Ticket(ticket['id'], 
                                       ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'])
                tickets.append(ticket)
        elif worker_email != None:
            # get query with only worker email
            for ticket in collection.find({}, {'worker': worker_email}):
                ticket = Ticket(ticket['id'], 
                                       ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'])
                tickets.append(ticket)
            
        # check if theres a device inputted
        elif device_id != None:
            # get query with only device id
            for ticket in collection.find({}, {'decide': device_id}):
                ticket = Ticket(ticket['id'], 
                                       ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'])
                tickets.append(ticket)
            
            # return list of tickets with device id
        return tickets

class Ticket:
    def __init__(self, desc, title, type, worker, device, status = 'open'):
        self.description = desc
        self.title = title
        self.device_tyep = type
        self.worker = worker.email
        self.device = device.id_num
        self.id_num = None
        self.collection_name = 'tickets'
        self.status
    def set_id_num(self):
        # use the ID class to set the id number for the ticket
        id_num = ID.grab_id_count(self.collection_name)
        # set the tickets id number
        self.id_num = 'ticket-' + id_num
        # return the id number
        return self.id_num
    


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
    def add_solution(self, solution):
        # set up connection to solution collection
        solutions = self.collection
        # get solution device object
        device = solution.device
        # add solution to collection of solutions
        new_solution = {
            'id' : solution.id_num,
            'worker': solution.worker,
            'work progress' : solution.work_progress,
            'keywords' : solution.keywords,
            'device': device.id_num
        }
        # return document pymongo id of new solution
        return solutions.insert_one(new_solution)
            # add team, work progress, keywords, device operating system
    def get_solutions(self, keywords, worker):
        return None
    
class Solution:
    def __init__(self, worker, work_progress, keywords, device):
        self.worker = worker
        self.work_progress = work_progress
        self.keywords = keywords
        self.device = device
        self.id_num = None
        self.collection_name = 'solutions'
    def set_id_num(self):
        # use the ID class to set the id number for the solution
        id_num = ID.grab_id_count(self.collection_name)
        # set the solution id number
        self.id_num = 'solution-' + id_num
        # return id num
        return self.id_num
    

# create subclass of users for clients
class ClientCollection:
    # create init function 
    def __init__(self):
        database = Database()
        # connect to client collection
        self.collection = database.db['client']
    # add client method
    def add_client(self, client):
        # set up client collection connection
        clients = self.collection
        # create client id

        # create a new document for the new client
        new_client = {
            'id' : client.id_num,
            'email' : client.email,
            'name': client.name,
            'phone number' : client.phone_num,
            'contact method' : client.contact_method
        }
        # return the new added client pymongo id
        return clients.insert_one(new_client)
    def get_devices():
        return None
    
    def get_tickets():
        return None
    
    def get_worker():
        return None
        
class Client:
    def __init__(self, email, name, phone_num, contact_method):
        self.email = email
        self.name = name
        self.phone_num = phone_num
        self.contact_method = contact_method
        self.collection_name = 'clients'
        self.user_type = 'client'
        self.id_num = None
    
    def set_id_num(self):
        # use the ID class to set the id number for the client
        id_num = ID.grab_id_count(self.collection_name)
        # set the clients id number
        self.id_num = 'client-' + id_num
        # return the id number
        return self.id_num

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
            'id' : worker_id,
            'name' : name,
            'email' : email,
            'team' : team
        }
        # return the new worker added to the collection
        return worker_collection.insert_one(new_worker)
    
    def get_team_workers(self, name):
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
        self.collection_name = 'workers'
        self.id_num = None
        self.user_type = 'worker'
    def set_id_num(self):
        # use the ID class to set the id number for the worker
        id_num = ID.grab_id_count(self.collection_name)
        # set the workers id number
        self.id_num = 'worker-' + id_num
        # return the id number
        return self.id_num


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
    def add_team(self, team):
        # connection to team collection
        team_collection = self.collection
        # create new document for the new team
        new_team = {
            'id' : team.id_num,
            'name' : team.name
        }
        # return the new team inserted into the team collection
        return team_collection.insert_one(new_team)
    def get_workers(self, team):
        # query the workers collection to get workers on specific team
        # 
        return None
    def get_tickets(self, team):
        # get the list of workers within the team
        # go through
        return None
    
class Team:
    def __init__(self, name):
        self.name = name
        self.collection_name = 'teams'
        self.id_num = None
    def set_id_num(self):
        # use the ID class to set the id number for the team
        id_num = ID.grab_id_count(self.collection_name)
        # set the teams id number
        self.id_num = 'team-' + id_num
        # return the id number
        return self.id_num
    
    def get_workers(self):
        # use worker collection class to find workers in team
        workers = WorkerCollection.get_team_workers(self.name)
        # return list of worker objects of workers in the team
        return workers
    
    def get_tickets(self):
        # create tickets list
        tickets = []
        # get team workers
        workers = self.get_workers()
        # use ticket collection to get list of ticket objects
        for worker in workers:
            worker_tickets = TicketCollection.get_tickets(worker.email, None)
            # add the worker tickets to the tickets list
            tickets += worker_tickets
        return tickets
    

        
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
        self.id_num = None
        self.collection_name = 'devices'

    def get_client(self):
        return self.client
    
    def get_tickets():
        #return list of tickets will all attributes in a dictionary format
        return None
    
    def set_id_num(self):
        # use the ID class to set the id number for the device
        id_num = ID.grab_id_count(self.collection_name)
        # set the devices id number
        self.id_num = 'device-' + id_num
        # return the id number
        return self.id_num

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
    
    def grab_id_count(self, collection_name):
        # get collection
        collection = self.collection
        # go through id tracker collection and only get ticket id count
        id_count = collection.find_one({'collection' : collection_name}, {'count' : 1})
        # convert the str to an int
        id_count = int(id_count['count'])
        id_num = str(id_count)
        len_id_num = len(id_num)
        id_str = '0000'
        # replace the last digits of id str with the id num
        # which should allow buffer zeros in front of the
        # id num so the id is 4 digits long no matter what
        id_str[-len_id_num:] = id_num
        self.inc_id_count(collection_name)
        # return the id count integer value
        return id_str
    
    def add_collection_id(self, collection_name):
        id_tracker = self.collection
        # add new id tracked collection 
        new_collection_tracker = {
        'collection' : collection_name,
        'count' : 1
        }
        return id_tracker.insert_one(new_collection_tracker)

        
    # create init function 
        # connection to id collection



