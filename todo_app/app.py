from flask import Flask
from flask.templating import render_template
from flask import session
from todo_app.data.session_items import get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()   
    return render_template('index.html', items=items)
    


