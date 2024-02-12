# import libraries
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://root:<password for uri in figma>@cluster0.zusbpwn.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['ticket_tracker']

# connect to help desk ticket database
#db = client['ticket_tracker']
# create collections
    # create a tickets collection
ticket_collection = db['tickets']
    # add to collections list
        
    # create a workers collection
worker_collection = db['workers']

    # create a teams collection
team_collection = db['teams']

    # create a device collection
device_collection = db['devices']

    # create client collection
client_collection = db['clients']

def add_ticket(tick_cnt, desc, title, type,  worker, device, client, team):
    '''
    Adds in a row into the ticket collection for a new ticket being input.

    PARAMETERS:
    > tick_cnt (required) int: the current total of ticket rows that will
            be input after this ticket
    > desc (required) string: a string of the description of the ticket
            issue.
    > title (required) string: a title for the ticket
    > type (required) int: the enumerated value of the type the ticket's
            category falls under
    > worker (required) string: the worker email who is assigned the ticket
    > device (required) int: enumerated value of the device's type
    > client (required) string: the email of the client who submitted the 
            ticket.
    > team (required) int: the enumerated value for the team assigned the
            ticket
    '''
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
        'team' : team
    }
    # return the document inserted into the ticket collection
    return ticket_collection.insert_one(new_ticket)


def add_client(cli_cnt, email,phone_num, ticket_id, device_id, pref_contact):
    # create client id
    client_id = 'c' + str(cli_cnt)
    # create a new document for the new client
    new_client = {
        'client id' : client_id,
        'email' : email,
        'phone number' : phone_num,
        'tickets' : [ticket_id],
        'devices' : [device_id],
        'contact method' : pref_contact
    }
    # return the new inserted document in the collection
    return client_collection.insert_one(new_client)

def add_worker(worker_count, name, email, team, ticket):
    # create worker id
    worker_id = 'w' + str(worker_count)
    # create new document for the new worker
    new_worker = {
        'worker id' : worker_id,
        'name' : name,
        'email' : email,
        'team' : team,
        'tickets' : [ticket]
    }
    # return the new worker added to the collection
    return worker_collection.insert_one(new_worker)

def add_team(team_count, worker_ids, tickets, name):
    team_id = 't' + str(team_count)
    # create new document for the new team
    new_team = {
        'team id' : team_id,
        'name' : name,
        'workers' : [worker_ids],
        'tickets': [tickets]
    }
    # return the new team inserted into the team collection
    return team_collection.insert_one(new_team)

def add_device(dev_count, worker, dev_type, tickets, has_problems):
    # create device count
    dev_id = 'd' + dev_count
    new_device = {
       'device id' : dev_id,
       'worker' : worker,
       'device type' : dev_type,
       'tickets' : [tickets],
       'has problems' : has_problems
    }
    return device_collection.insert_one(new_device)

