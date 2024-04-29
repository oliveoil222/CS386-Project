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
    def find_user(self, email):
        collection = self.collection
        found_user = collection.find_one({'email': email})
        found_user = User(found_user['name'],
                          found_user['email'],
                          found_user['type'],
                          found_user['id'])
        # query to find a user in the user collection
        return found_user

class User:
    def __init__(self, name, email, type, id_num = None):
        self.collection_name = 'users'
        self.name = name
        self.user_type = type
        self.email = email
        self.id_num = id_num
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
        ticket_to_update = {'id' : ticket.id_num}
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
                ticket = Ticket(ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'],
                                       ticket['id'])
                tickets.append(ticket)
        elif worker_email != None:
            # get query with only worker email
            for ticket in collection.find({'worker': worker_email}):
                ticket = Ticket(ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'],
                                       ticket['id'])
                tickets.append(ticket)
            
        # check if theres a device inputted
        elif device_id != None:
            # get query with only device id
            for ticket in collection.find({'decide': device_id}):
                ticket = Ticket(ticket['description'], 
                                       ticket['title'], 
                                       ticket['type'],
                                       ticket['worker'],
                                       ticket['device'], 
                                       ticket['status'],
                                       ticket['id'])
                tickets.append(ticket)
            
            # return list of tickets with device id
        return tickets

class Ticket:
    def __init__(self, desc, title, worker_email, operate_sys, device_id, status = 'open', id_num = None):
        self.description = desc
        self.title = title
        self.operating_sys = operate_sys
        self.worker = worker_email
        self.device = device_id
        self.id_num = id_num
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
            'device': solution.device
        }
        # return document pymongo id of new solution
        return solutions.insert_one(new_solution)
            # add team, work progress, keywords, device operating system
    def get_solutions(self, keywords = None, worker_email = None):
        collection = self.collection
        solutions = []
        if keywords != None and worker_email != None:
            for solution in collection.find({'worker': worker_email},{'keywords': keywords}):
                solution = Solution(solution['worker'], 
                                    solution['work progress'],
                                    solution['keywords'],
                                    solution['device'],
                                    solution['id'])
                solutions.append(solution)
        elif worker_email != None:        
            for solution in collection.find({'worker': worker_email}):
                solution = Solution(solution['worker'], 
                                    solution['work progress'],
                                    solution['keywords'],
                                    solution['device'],
                                    solution['id'])
                solutions.append(solution)
        elif keywords != None:
            for solution in collection.find({'keywords': keywords}):
                solution = Solution(solution['worker'], 
                                    solution['work progress'],
                                    solution['keywords'],
                                    solution['device'],
                                    solution['id'])
                solutions.append(solution)
        return solutions
    
class Solution:
    def __init__(self, worker_email, work_progress, keywords, device, id_num = None):
        self.worker = worker_email
        self.work_progress = work_progress
        self.keywords = keywords
        self.device = device.id_num
        self.id_num = id_num
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
    
    def get_devices(self, client):
        device_collection = DeviceCollection()
        devices = device_collection.get_devices(client.email)
        return devices
    
    def get_client(self, email):
        collection = self.collection
        client = collection.find_one({'email':email})
        client = Client(client['email'],
                        client['name'],
                        client['phone number'],
                        client['contact method'],
                        client['id'])
        return client

    def get_tickets(self, client):
        devices = self.get_devices(client)
        device_collection = DeviceCollection()
        tickets = []
        for device in devices:
            device_tickets = device_collection.get_tickets(device)
            tickets += device_tickets
        return tickets
    
    def get_workers(self, client):
        devices = self.get_devices(client)
        device_collection = DeviceCollection()
        workers = []
        for device in devices:
            device_workers = device_collection.get_workers(device)
            workers += device_workers
        return workers
        
class Client:
    def __init__(self, email, name, phone_num, contact_method, id_num = None):
        self.email = email
        self.name = name
        self.phone_num = phone_num
        self.contact_method = contact_method
        self.collection_name = 'clients'
        self.user_type = 'client'
        self.id_num = id_num
    
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
    
    def update_worker_team(self, worker, team):
        collection = self.collection
        worker.update_team(team)
        update_worker = {'id': worker.id_num}
        new_team = {'$set': {'team': worker.team}}
        return collection.update_one(update_worker, new_team)


class Worker:
    def __init__(self, name, email, team_name, id_num = None):
        self.name = name
        self.email = email
        self.team = team_name
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
    def update_team(self, new_team):
        self.team = new_team.name
        return self.team


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
    def get_team(self, name):
        collection = self.collection
        team = collection.find_one({'name': name})
        team = Team(team['name'], team['id'])
        return team
    
    def update_team_name(self, team, new_name):
        collection = self.collection
        team.update_name(new_name)
        update_team = {'id': team.id_num}
        new_team_name = {'$set': {'name': new_name}}
        return collection.update_one(update_team, new_team_name)
    
class Team:
    def __init__(self, name, id_num = None):
        self.name = name
        self.collection_name = 'teams'
        self.id_num = id_num
    def set_id_num(self):
        ids = ID()
        # use the ID class to set the id number for the team
        id_num = ids.grab_id_count(self.collection_name)
        # set the teams id number
        self.id_num = 'team-' + id_num
        # return the id number
        return self.id_num
    def update_name(self, new_name):
        self.name = new_name
        return new_name
    
    

        
# create class for devices
class DeviceCollection:
    def __init__(self):
        database = Database()
        self.collection = database.db['devices']
    # method to add device to collection
    def add_device(self, device):
        device_collection = self.collection
        # create device count
        device.set_id_num()
        new_device = {
            'id' : device.id_num,
            'client': device.client,
            'operating system' : device.operating_sys,
            'problems' : device.problems
        }
        # return pymongo id of new document in collection
        return device_collection.insert_one(new_device)
    def get_devices(self, email):
        # should retunr a Device type after finding query
        collection = self.collection
        devices = []
        for device in collection.find({'client': email}):
            device = Device(device['client'],
                            device['operating system'], 
                            device['problems'],
                            device['id'])
            devices.append(device)
        return devices
    
    def get_tickets(self, device):
        ticket_collection = TicketCollection()
        tickets = ticket_collection.get_tickets(None, device.id_num)
        return tickets
    
    def get_workers(self, device):
        worker_collection = WorkerCollection()
        # return list of ticket objects under device
        tickets = self.get_tickets(device)
        workers = []
        for ticket in tickets:
            if ticket.status != 'closed':
                worker = worker_collection.get_worker(ticket.worker)
                worker = Worker(worker['name'],
                                worker['email'],
                                worker['team'],
                                worker['id_num'])
                workers.append(worker)
        return workers
                
    def get_client(self, device):
        clients = ClientCollection()
        client = clients.get_client(device.client)
        return client
    
    def update_problems(self, device, problems):
        collection = self.collection
        device.update_problems(problems)
        device_to_update = {'id': device.id_num}
        new_problems = {'$set': {'problems': problems}}
        return collection.update_one(device_to_update, new_problems)
    
class Device:
    def __init__(self, client_email, os_type, problems = False, id_num = None):
        self.client = client_email
        self.operating_sys = os_type
        self.problems = problems
        self.id_num = id_num
        self.collection_name = 'devices'

    def update_problems(self, problems):
        self.problems = problems
        return self.problems
    
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

