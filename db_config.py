from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'demouser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'demopassword'
app.config['MYSQL_DATABASE_DB'] = 'demodb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
