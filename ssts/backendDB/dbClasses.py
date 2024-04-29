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
    def __init__(self):
        # connect to user database
        database = Database()
        self.collection = database.db['users']
    # function to add user to database collection
    # the user variable to input is a Worker/Client object
    def add_user(self, user):
        collection = self.collection
        user.set_id_num()
        new_user = {
            'id' : user.id_num,
            'name' : user.name,
            'email': user.email,
            'type' : user.user_type
        }
        return collection.insert_one(new_user)
    # the user variable to input is a Worker/Client object
    def find_user(self, user):
        email = user.email
        name = user.name
        collection = self.collection
        found_user = collection.find_one({'email': email, 'name': name})
        found_user = User(found_user['id'],
                          found_user['name'],
                          found_user['email'],
                          found_user['type'])
        # query to find a user in the user collection
        return found_user

class User:
    def __init__(self, name, email, type):
        self.collection_name = 'users'
        self.name = name
        self.user_type = type
        self.email = email
        self.id_num = None
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the user
        id_num = ids.grab_id_count(self.collection_name)
        # set the users id number
        self.id_num = 'user-' + id_num
        # return the id number
        return self.id_num

# create a class for tickets
class TicketCollection:
    # create init function 
    def __init__(self):
        # connection to ticket collection
        database = Database()
        self.collection = database.db['tickets']
    # method to add ticket to database collection
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
            'type' : ticket.operating_sys,
            'worker' : ticket.worker,
            'device' : ticket.device,
            'status': ticket.status
        }
        # return the document inserted into the ticket collection
        return collection.insert_one(new_ticket)
    def update_ticket_status(self, ticket, status):
        collection = self.collection
        # update ticket object status
        ticket.update_status(status)
        # get the ticket_id
        ticket_id = ticket.id_num
         # set query variable to find unique ticket to update
        ticket_to_update = {'ticket id' : ticket_id}
        # set up new value for ticket
        new_status = {'$set' : {'status' : status}}
        return collection.update_one(ticket_to_update, new_status)
    
    def update_ticket_worker(self, ticket, worker_email):
        collection = self.collection
        # update the ticket objects worker email
        ticket.update_worker(worker_email)
        # set query variable to find unique ticket to update
        ticket_to_update = {'ticket id' : ticket.id_num}
        # set up new value for ticket
        new_ticket_worker = {'$set' : {'worker' : worker_email}}
        # return updated ticket
        return collection.update_one(ticket_to_update, new_ticket_worker)
    
    def get_tickets(self, worker_email = None, device_id = None):
        collection = self.collection
        tickets = []
        # check if theres a worker email inputted
        if worker_email != None and device_id != None:
            # get query with both attributes
            for ticket in collection.find({'worker': worker_email, 'decide': device_id}):
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
            for ticket in collection.find({'worker': worker_email}):
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
            for ticket in collection.find({'decide': device_id}):
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
    def __init__(self, desc, title, worker, device, status = 'open'):
        self.description = desc
        self.title = title
        self.operating_sys = device.operating_sys
        self.worker = worker.email
        self.device = device.id_num
        self.id_num = None
        self.collection_name = 'tickets'
        self.status = status
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the ticket
        id_num = ids.grab_id_count(self.collection_name)
        # set the tickets id number
        self.id_num = 'ticket-' + id_num
        # return the id number
        return self.id_num
    def update_status(self, new_status):
        # udpate status and return new status
        self.status = new_status
        return self.status
    
    def update_worker(self, worker_email):
        self.worker = worker_email
        return self.worker

    


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
    def __init__(self, worker_email, work_progress, keywords, device):
        self.worker = worker_email
        self.work_progress = work_progress
        self.keywords = keywords
        self.device = device.id_num
        self.id_num = None
        self.collection_name = 'solutions'
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the solution
        id_num = ids.grab_id_count(self.collection_name)
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
    
    def get_workers():
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
        ids = ID()
        # use the ID class to set the id number for the client
        id_num = ids.grab_id_count(self.collection_name)
        # set the clients id number
        self.id_num = 'client-' + id_num
        # return the id number
        return self.id_num

# create subclass of users for workers
class WorkerCollection:
    def __init__(self):
    # collection connection
        database = Database()
        self.collection = database.db['workers']
    # add worker to collection
    def add_worker(self, worker):
        worker_collection = self.collection
        worker.set_id_num()
        # create new document for the new worker
        new_worker = {
            'id' : worker.id_num,
            'name' : worker.name,
            'email' : worker.email,
            'team' : worker.team
        }
        # return the new worker added to the collection
        return worker_collection.insert_one(new_worker)
    
    def get_team_workers(self, name):
        collection = self.collection
        workers = []
        for worker in collection.find({'team': name}):
            team_worker = Worker(worker['name'], worker['email'], worker['team'])
            workers.append(team_worker)
        return workers
    
    def get_worker(self, worker_email):
        collection = self.collection
        worker = collection.find_one({'email': worker_email})
        worker = Worker(worker['name'],
                        worker['email'], 
                        worker['team'], 
                        worker['id'])
        return worker
    
    def update_worker_team(self, team):
        return None


class Worker:
    def __init__(self, name, email, team, id_num = None):
        self.name = name
        self.email = email
        self.team = team
        self.collection_name = 'workers'
        self.id_num = id_num
        self.user_type = 'worker'
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the worker
        id_num = ids.grab_id_count(self.collection_name)
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
    # create init function 
    def add_team(self, team):
        # connection to team collection
        team_collection = self.collection
        # create new document for the new team
        team.set_id_num()
        new_team = {
            'id' : team.id_num,
            'name' : team.name
        }
        # return the new team inserted into the team collection
        return team_collection.insert_one(new_team)
    def get_workers(self, team):
        # query the workers collection to get workers on specific team
        workers_collection = WorkerCollection()
        workers = workers_collection.get_team_workers(team.name)
        return workers
    def get_tickets(self, team):
        # create tickets list 
        tickets = []
        ticket_collection = TicketCollection()
        # get the list of workers within the team
        workers = self.get_workers(team)
        for worker in workers:
            worker_tickets = ticket_collection.get_tickets(worker.email, None)
            # add worker tickets list to team tickets list
            tickets += worker_tickets
        # return list of tickets
        return tickets
    
class Team:
    def __init__(self, name):
        self.name = name
        self.collection_name = 'teams'
        self.id_num = None
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the team
        id_num = ids.grab_id_count(self.collection_name)
        # set the teams id number
        self.id_num = 'team-' + id_num
        # return the id number
        return self.id_num
    
    def get_workers(self):
        workers_collection = WorkerCollection()
        # use worker collection class to find workers in team
        workers = workers_collection.get_team_workers(self.name)
        # return list of worker objects of workers in the team
        return workers
    
    def get_tickets(self):
        # create tickets list
        tickets = []
        # get team workers
        workers = self.get_workers()
        ticket_collection = TicketCollection()
        # use ticket collection to get list of ticket objects
        for worker in workers:
            
            worker_tickets = ticket_collection.get_tickets(worker.email, None)
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
    def add_device(self, device):
        device_collection = self.collection
        # create device count
        device.set_id_num
        new_device = {
            'device id' : device.id_num,
            'client': device.client,
            'device type' : device.operating_sys,
            'problems' : device.problems
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
        self.client = client.email
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
        ids = ID()
        # use the ID class to set the id number for the device
        id_num = ids.grab_id_count(self.collection_name)
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
        while len(id_num) < 4:
            id_num = '0' + id_num

        self.inc_id_count(collection_name)
        # return the id count integer value
        return id_num
    
    def add_collection_id(self, collection_name):
        id_tracker = self.collection
        # add new id tracked collection 
        new_collection_tracker = {
        'collection' : collection_name,
        'count' : 1
        }
        return id_tracker.insert_one(new_collection_tracker)
    
    def get_current_id(self, collection_name):
        collection = self.collection
        # go through id tracker collection and only get ticket id count
        id_count = collection.find_one({'collection' : collection_name}, {'count' : 1})
        # get the str version of the id count
        id_count = dumps(id_count['count'])
        # convert the str to an int
        id_count = int(id_count)
        # return the id count integer value
        return id_count    

'''

users = UserCollection()
user = User('start', 'start@email.com', 'worker')
print(users.add_user(user))
solutions = SolutionCollection()
solution = Solution('test worker', 'progress', 'keywords', 'device')
print(solutions.add_solution(solution))
'''
