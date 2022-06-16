from flask import Flask
from views import views
import psycopg2

#! we import out view from the views file

app = Flask(__name__)
app.config['db_name'] = 'flask'
app.config['db_username'] = 'postgres'
app.config['db_password'] = 'password'
app.config['db_host'] = 'localhost'

#! connection to database


#! we instantiate the app 

app.register_blueprint(views)
#! we register the views blueprint

if __name__ == "__main__":
    app.run(debug=True, port=8000)

#! running the application