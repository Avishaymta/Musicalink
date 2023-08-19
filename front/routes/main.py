import json
from base import app, gconfig
from flask import render_template, request, send_file

# DEMO INVENTORY LOAD
d = open('inventory/demo/dummycards.json')
tlc_dummies = json.load(d)
del d

## DEMONSTRATION ONLY - NOT DYNAMIC
## Todo:
## User system module
## Proper DB population
## Proper integration with frontend

@app.route('/')
def index():
    ## Loads up 10 most relevant posts from DB
    ## DEMO: Only 5 static cards
    return render_template(
        'timeline.html', 
        WEB_TEMPLATES_COMPONENTS_REL=gconfig.WEB_TEMPLATES_COMPONENTS_REL,
        tlc_payload=tlc_dummies
    )

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/get-img')
def return_img():
    return send_file(f'{gconfig.WEB_TEMPLATES_STATICS}/timeline_card/img/{request.query_string.decode("utf-8")}'
            ,mimetype='image/jpg'             
        )