#create: db,connect_db
#Cupcake,cupcakes(id,flavor,size,rating,image),to_dict
##################################################################################
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
##################################################################################
def connect_db(app):
    db.app = app
    db.init_app(app)
###################################################################################
DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"
class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    def serialize(self):#Serialize cupcake to a dict of cupcake info."""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }