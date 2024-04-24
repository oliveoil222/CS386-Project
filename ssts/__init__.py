# This is the essentially package that holds the project together. the routes and relevant configuration information is held in here.
import os

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
from markupsafe import escape
#import grabInfo
#import addInfo

id_number = "000"

# Sample incident data
incidents = [
    {'id': '001', 'title': 'Incident 1', 'description': 'This is incident 1 and I wonder if I will wreap text correctly or not???', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
    {'id': '002', 'title': 'Incident 2', 'description': 'This is incident 2', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
    {'id': '003', 'title': 'Incident 3', 'description': 'This is incident 2', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
    {'id': '004', 'title': 'Incident 4', 'description': 'This is incident 2', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
]

calls = [
    {'id': '001', 'title': 'Call 1', 'description': 'This is call 1', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
    {'id': '002', 'title': 'Call 2', 'description': 'This is call 2', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
    {'id': '003', 'title': 'Call 3', 'description': 'This is call 3', 'worker': 'Dallon', 'device': 'Laptop', 'client': 'John Doe', 'team': 'IT'},
]

def create_app(test_config=None):
    global id_number
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ssts.mongodb'),
    )
    # pull out the ID number of ticket
    # check database for last number used, if any
    try:
        # do database stuff we expect to work here
        # like pulling last ID number
        # if this errors, then move to except
        raise ValueError()
        print("working database stuff here")
        
        # use the get_ticket_collection function
        # if empty, throw error
        # otherwise, get the last ticket from the list.
    except:
        id_number = "001"
        # then this is where we set the first ID number for initialization
        # note to programmer: use str.zfill(3) to get three digit integer numbers

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # all application routes
    @app.route('/')
    def homepage(page_name="Homepage"):
        return render_template("base.html", page_name=page_name)

    @app.route('/login', methods=['GET','POST'])
    def agent_login_page(page_name="Agent Login"):

        if request.method == 'POST':
            email = str(request.form.get('email'))
            password = str(request.form.get('password'))
            
            if (email == "testing@ssts.app") & (password == "password"):
                return redirect('/')
            else:
                return redirect('/login')

        return render_template("auth/login.html", page_name=page_name)
    
    @app.route('/signup', methods=['GET','POST'])
    def agent_signup_page(page_name="Agent Signup"):

        if request.method == 'POST':
            username = str( request.form.get('username') )
            firstname = str( request.form.get('firstname') )
            lastname = str( request.form.get('lastname') )
            phone = str( request.form.get('phone') )
            email = str( request.form.get('email') )
            password = str( request.form.get('password') )
            password1 = str( request.form.get('password1') )

            email_found = False #records.find_one({"email": email})

            if password != password1:
                message = "Passwords do not match"
                return redirect('/signup', message=message) 
            if email_found:
                message = "Email already exists"
                return redirect('/signup', message=message)

        return render_template("auth/signup.html", page_name=page_name)

    @app.route('/sp')
    def service_portal(page_name="Service Portal"):
        return render_template("service_portal/portal.html", page_name=page_name)

    @app.route('/sp/schedule')
    def service_portal_schedule(page_name="Service Portal Scheduler"):
        return render_template("service_portal/schedule.html", page_name=page_name)

    @app.route('/new/ticket', methods=['GET','POST'])

    def new_ticket(id_number=id_number, page_name="New Ticket {id_number}"):

        # will need to save the DB information from the webpage
        # probably using an API request template once the submit button was hit.
        # will need to get the information from front-end about what information
        # was on the page.
        # this function will need to increment the ID Number of the ticket
        # and render it with the page as immutable.

        # if POST is used, then grab the information from the webpage and then
        # use DB functions to then make and store the information.
        if request.method == 'POST':
            # grab information given by frontend, like

            # type
            ticket_type = str(request.form.get('issueType'))

             # title
            ticket_title = str(request.form.get('title'))

            # description
            ticket_descript = str(request.form.get('description'))
           
            # worker
            ticket_worker = str(request.form.get('worker'))
            # device
            ticket_device = str(request.form.get('device'))
            # client
            ticket_client = str(request.form.get('client'))
            # team
            ticket_team = str(request.form.get('team'))
            print(f"POST Request completed here! {ticket_descript, ticket_title, ticket_type, ticket_worker, ticket_device, ticket_client, ticket_team}")
            # use the add_ticket function with all the referenced parameters
            # add_ticket(id_number, description, title, type, worker, device, client, team)
            # increment ID number
            id_number = str(int(id_number) + 1).zfill(3)

            return redirect('/view/ticket')

        # otherwise, when GET is used, just render the new ticket html template

        if request.method == 'POST':
        # Process form data and save the ticket to the database
        # Increment the current page number by one
            id_number = str(int(id_number) + 1)
        return render_template("new/ticket.html", page_name=page_name, id_number=id_number)

    
    @app.route('/view/ticket', methods=['GET'])
    def view_ticket_list(page_name="View Tickets"):
        return render_template("view/ticket.html", page_name=page_name, incidents=incidents)
    
    @app.route('/view/call', methods=['GET'])
    def view_call_list(page_name="View Calls"):
        return render_template("view/call.html", page_name=page_name, calls=calls)
    

    @app.route('/settings')
    def setting(page_name="Settings"):
        return render_template("/settings/settings.html", page_name=page_name)
    
    @app.route('/view/kb')
    def knowledgebase(page_name="Knowledge Base"):
        return render_template("view/knowledgebase.html", page_name=page_name)

    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('/error/404.html'), 404

    return app
