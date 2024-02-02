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
        return render_template("auth/login.html", page_name=page_name)

    @app.route('/sp')
    def service_portal(page_name="Service Portal"):
        return render_template("service_portal/portal.html", page_name=page_name)

    @app.route('/sp/schedule')
    def service_portal_schedule(page_name="Service Portal Scheduler"):
        return render_template("service_portal/schedule.html", page_name=page_name)

    @app.route('/new/ticket')
    def new_ticket(page_name="New Ticket"):
        return render_template("new/ticket.html", page_name=page_name)

    @app.route('/view/ticket/[ID_NUMBER]')
    def new_ticket(page_name="View Ticket"):
        return render_template("view/ticket/[ID_NUMBER].html", page_name=page_name)

    return app
