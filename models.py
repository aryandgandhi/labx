from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    results = db.Column(db.JSON)  # Store test results as JSON

class DecisionTree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tree_name = db.Column(db.String(100))
    tree_data = db.Column(db.JSON)  # Store the decision tree as JSON
