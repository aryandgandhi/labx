from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

postgres = os.getenv('POSTGRES')
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgres
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "LabSense API Running"

@app.route('/create_patient', methods=['POST'])
def create_patient():
    data = request.json
    new_patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient created", "patient_id": new_patient.id})

@app.route('/add_results/<patient_id>', methods=['POST'])
def add_results(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404
    
    results = request.json['results']
    patient.results = results
    db.session.commit()
    return jsonify({"message": "Results added"})

@app.route('/traverse_tree/<patient_id>/<tree_id>', methods=['POST'])
def traverse_tree(patient_id, tree_id):
    # Load patient and tree data
    patient = Patient.query.get(patient_id)
    tree = DecisionTree.query.get(tree_id)

    if not patient or not tree:
        return jsonify({"message": "Invalid patient or tree"}), 404

    # Get the current results to make a decision in the tree
    results = patient.results
    tree_data = tree.tree_data

    # Traverse the tree based on inputs (simplified for now)
    next_node = tree_data.get('next_step')  # Simplified example
    return jsonify({"next_step": next_node})


if __name__ == "__main__":
    app.run(debug=True)