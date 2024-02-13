from models import db, Cupcake
from app import app
#################################################################
with app.app_context():
    db.drop_all()#wipe out all existing data
    db.create_all()#recreate 
    #############################################################
    cupcakes=[
        Cupcake(flavor="cherry",   size="large",rating=5),
        Cupcake(flavor="chocolate",size="small",rating=9,image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg")
    ]
    db.session.add_all(cupcakes)
    db.session.commit()
    ###############################################################################################
    print("Data seeded successfully")