from main_app import db
from user import User

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# create all tables
db.create_all() 
