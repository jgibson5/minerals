from app import app
# from app import app, db

@app.route('/')
def hello_world():
    return 'Hello, World!'