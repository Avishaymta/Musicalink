from db_adapter import client

## Create Database
## DEMO, DEV AND QA USAGE ONLY - MUST REFACTOR FOR STAGING AND PROD
## This creates an initial user database (empty)
## App start up creates an Admin user.
## Registration possible on all envs
 
def create_musicallink_mongo_db():
    if 'ml_mdb' in client.list_database_names():
        return
    else:
        return client['ml_db']
        
