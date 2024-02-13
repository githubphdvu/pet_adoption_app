#########################################################################################
from flask import Flask,request,render_template,jsonify
from flask_debugtoolbar import DebugToolbarExtension#put raise where to inspect with debugtool
from models import db, connect_db, Cupcake
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.debug = True #for auto reload(with command:$python3 app.py, not $flask run)
connect_db(app)#establish connection to database
with app.app_context():#within app context,create tables
    db.create_all()
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False#no intercept redirect
toolbar = DebugToolbarExtension(app)
########################################################################################
@app.route("/")
def root():
    return render_template("index.html")
#####################################################################
# RESTFUL JSON API (all data transmitted in JSON)
########################################################################################
@app.route("/api/cupcakes")
def list_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    data = request.json
    cupcake = Cupcake(flavor=data['flavor'],rating=data['rating'],size=data['size'],image=data['image'] or None)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
#########################################################################
if __name__ == '__main__':# Run Flask app
    app.run(host='127.0.0.1', port=5000)

