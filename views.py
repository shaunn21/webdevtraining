import psycopg2
from flask import render_template, Blueprint, Flask, request
from flask import current_app as app

views = Blueprint("views", __name__)

#! view in this instance is a blueprint

task_list = []

def dbconnection():
    conn = psycopg2.connect(host=app.config['db_host'], database=app.config['db_name'], user=app.config['db_username'], password=app.config['db_password'])
    return conn

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/about")
def about():
    conn=dbconnection()
    cur=conn.cursor()
    cur.execute('SELECT * FROM test')
    results=cur.fetchall()
    cur.close()
    conn.close()
    return render_template("about.html", results=results)

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method == "POST":
        task = request.form.get ("task-input")
        task_list.append(task)
        print(task_list)
        return render_template("todos.html", task_list=task_list)
    return render_template("todos.html")