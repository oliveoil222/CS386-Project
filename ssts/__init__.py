# This is the essentially package that holds the project together. the routes and relevant configuration information is held in here.
import os

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ssts.mongodb'),
    )



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

    @app.route('/login')
    def agent_login_page(page_name="Agent Login"):
        # low priority TODO, will use Wertzeug's libraries to
        # implement a login.
        return render_template("auth/login.html", page_name=page_name)

    @app.route('/sp')
    def service_portal(page_name="Service Portal"):
        return render_template("service_portal/portal.html", page_name=page_name)

    @app.route('/sp/schedule')
    def service_portal_schedule(page_name="Service Portal Scheduler"):
        # medium priority TODO, will have a scheduler on this page.
        return render_template("service_portal/schedule.html", page_name=page_name)

    @app.route('/new/ticket')
    def new_ticket(page_name="New Ticket"):
        # will need to save the DB information from the webpage
        # probably using an API request template once the submit button was hit.
        # will need to get the information from front-end about what information
        # was on the page.
        # this function may also need to generate the ID Number of the ticket
        # and render it with the page as immutable.
        return render_template("new/ticket.html", page_name=page_name)

    @app.route('/view/ticket/<int:id_number>')
    def view_ticket(page_name="View Ticket {id_number}", ticket_id=id_number):
        # may need to be modifed, flask might do something with this
        # that may be unforeseeable without a bit of testing...
        # will need a template base for ticket displaying from the frontend.
        # the rest of the function will take DB functions to get the information.
        return render_template("view/ticket/{ticket_id}.html", page_name=page_name)

    return app
