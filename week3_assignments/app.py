from flask import Flask, jsonify, request
from person_dao import Person, Db_operations

db = Db_operations()
db.create_db()
db.create_table()

app = Flask(__name__)

@app.route('/people', methods=['POST'])
def create_person():
    body = request.get_json()
    new_person = Person(body['name'], body['gender'], body['dob'], body['location'])
    id = db.insert_row(new_person)
    person = db.search_row(id)
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people/<id>', methods=['GET'])
def get_person(id):
    person = db.search_row(id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people', methods=['GET'])
def list_people():
    people = db.list_all_rows()
    people_list = [{'id': p[0], 'name': p[1], 'gender': p[2], 'dob': p[3], 'location': p[4]} for p in people]
    return jsonify(people_list)

@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
    person = db.search_row(id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404

    body = request.get_json()
    updated_person = (body['name'], body['gender'], body['dob'], body['location'], id)
    db.update_row(updated_person)

    person = db.search_row(id)
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people/<id>', methods=['DELETE'])
def delete_person(id):
    person = db.search_row(id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    db.delete_row(id)
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)