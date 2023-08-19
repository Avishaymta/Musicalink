from flask import Flask, render_template
import pymongo
import gconfig

## Database
from db_adapter import create as db_create
user_db = db_create.create_musicallink_mongo_db()

## Create FlaskApp object
app = Flask(
    __name__,
    template_folder=gconfig.WEB_TEMPLATES,
    static_folder=gconfig.WEB_TEMPLATES_STATICS
    )

## Import Routes
from routes import main

## FlaskApp Config
from base import config
config.dev()