import sys
sys.path.insert(0, './')
from bson.json_util import dumps
import dbClasses as db
import grabInfo as grab

# set connection variable
connector = db.Connections()

# create ticket collection connection variable
ticket_collection = connector.ticket_collection

# create worker collection connection variable
worker_collection = connector.worker_collection

# create team collection connection variable
team_collection = connector.team_collection

# create device collection connection variable
device_collection = connector.device_collection

# create client collection connection variable
client_collection = connector.client_collection

# create solution collection connection variable
solution_collection = connector.solution_collection

# create id tracker collection connection variable
id_tracker_collection = connector.id_tracker_collection

# function to update id counter collection
def inc_id_count(collection_name):
    # get current id count pymongo cursor 
    id_count = grab.get_current_id(collection_name)
    # incriment id count
    new_id_count = id_count + 1
    id_to_update = {'collection' : collection_name}
    new_count = {'$set' : {'count' : new_id_count}}
    # return new collection id count pymongo cursor
    return id_tracker_collection.update_one(id_to_update, new_count)
    




# functions to update ticket collection
    # update ticket's assigned worker
def update_ticket_worker(new_worker_email, ticket_id):
    
    # set query variable to find unique ticket to update
    ticket_to_update = {'ticket id' : ticket_id}
    # set up new value for ticket
    new_ticket_worker = {'$set' : {'worker' : new_worker_email}}
    # return updated ticket
    return ticket_collection.update_one(ticket_to_update, new_ticket_worker)


    # update ticket status
    # update ticket work done


    # update ticket's assigned team
def update_ticket_team(new_team_id, ticket_id):
    # set query variable tp find unique ticket to update
    ticket_to_update = {'ticket id' : ticket_id}
    # set up new team value for the ticket
    ticket_new_team = {'$set' : {'team' : new_team_id}}
    # retrun the updated ticket
    return ticket_collection.update_one(ticket_to_update, ticket_new_team)

    # update ticket last worked on timestamp



# functions to update client collection
    # update client tickets
    # update client preferred contact method
    # upadte client devices


# functions to update worker collection
    # update worker name
    # update worker team
    # update worker tickets assigned

# function to update team collection
    # update team name
    # update team workers
    # update team assigned tickets

# functions to update device collection
    # update device tickets assigned
    # update decice worker
    # update device has problems
