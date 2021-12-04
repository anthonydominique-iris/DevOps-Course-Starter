from flask import Flask
from flask.templating import render_template
from flask import session
from todo_app.data.session_items import get_items
from todo_app.flask_config import Config
from flask import request
from werkzeug.utils import redirect


app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()   
    return render_template('index.html', items=items)
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    add_item(request.form.get('title'))
    #return render_template('index.html', items=items)
    return redirect('/')

def add_item(title):
    #kept getting session_items is not defined error - so just added it to the main app
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item
