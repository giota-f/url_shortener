from restapi import app

### Endpoints ###
@app.route('/')
def hello_world():
    return 'Hello from application', 200
