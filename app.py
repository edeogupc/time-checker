from flask import FLASK
app = FLASK(__name__)
app.route('/')
def hello_world():
    return "This is my app world developed by peter chuma edeogu"
if "__name" == "__name__":
    app.run(host='0.0.0.0', port=5000)