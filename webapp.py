import logging
from flask import Flask
from helpers.db import load_db

def create_app():
    # loading db
    logging.info("Creating DB")
    load_db()
    # run migrations
    logging.info("Running Migrations")


    app = Flask(__name__)

    # ...

    from views.catalogue import bp
    app.register_blueprint(bp)

    return app