from base import app

## Development Settings
## Allows auto-refresh per code change
## Allows compilation errors to appear on webpage
## NOT SECURE FOR PROD
def dev():
    app.config["TESTING"] = True
    app.config["DEBUG"] = True