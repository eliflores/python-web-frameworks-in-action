from wut4lunch import app
from wut4lunch import db
db.create_all()  # make our sqlalchemy tables
app.run(debug=True)