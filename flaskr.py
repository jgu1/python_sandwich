from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify, Response
from db_classes import DAO

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return DAO()

@app.before_request
def before_request():
    g.dao = connect_db()

@app.teardown_request
def teardown_request(exception):
    dao = getattr(g, 'dao', None)
    if dao is not None:
        dao.db.close()

@app.route('/')
def show_index_page():
    dao = getattr(g, 'dao', None)
    # where the meat comes from!
    python_meat_list  = ['beef','chicken','tempura','tofu']
    bottom_bread_list = dao.get_bread_calorie()
    return render_template('index.html',python_meat_list = python_meat_list, bottom_bread_list = bottom_bread_list)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=60000,threaded=True)
