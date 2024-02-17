# import libraries
import pymongo
import sys
sys.path.insert(0, './')
import addInfo as db


# this will be the file that has all the functions for grabbing information from the
# mongo databases that can be passed back to mid

# connect collections as global variables
    # connect a tickets collection
ticket_collection = db.get_ticket_collection()

    # connect a workers collection
worker_collection = db.get_worker_collection()

    # connect a teams collection
team_collection = db.get_team_collection()

    # connect a device collection
device_collection = db.get_device_collection()

    # connect client collection
client_collection = db.get_client_collection()

# create function to find tickets with client email
def client_email_find_tickets(client_email):
    # need to go through client database first
    tickets = client_collection.find({'email' : client_email}, {'tickets' : 1})
    # return the list of ticket ids
    return tickets

# create functiont to finf ticket with ticket id
def ticket_id_find_ticket(ticket_id):
    # make a search on the database (query) to find the ticket from ticket id
    ticket = ticket_collection.find({'ticket id' : ticket_id})
    # return the ticket object
    return ticket

# create function to find tickets with worker id
def worker_id_find_tickets(worker_id):
    # find the worker and only grab the tickets list
    tickets = worker_collection.find({'worker id' : worker_id}, {'tickets' : 1})
    # return the list of tickets assigned to the worker
    return tickets

# create function to find tickets with worker email
def worker_email_find_tickets(worker_email):
    # find the worker with email and grab the tickets list
    tickets = worker_collection.find({'email' : worker_email}, {'tickets' : 1})
    # return the tickets list cursor
    return tickets

# create function to find tickets with team id
    # return ???

# create function to find a worker given id
    # return ???

# create function to find a worker given email
    # return ???

# create function to look for device given device id
    # return ???

# create function to look for device given device owner
    # return ???

# create function to look for device given devices ticket id
    # return ???

# create search function to find a client given client id
    # retrun ???

# create search function to find a client given client email
    # return ???

# create search function to find a client given client phone number
    # return ???

# create search function to find a client given client name
    # return ???


