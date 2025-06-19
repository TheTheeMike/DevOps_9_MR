from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)
CSV_FILE = 'Students.csv'
FIELDS = {'first_name', 'last_name', 'age'}

def read_students():
    students = []
    if not os.path.exists(CSV_FILE):
        return students
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])
            students.append(row)
    return students

def write_students(students):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['id', 'first_name', 'last_name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s)

@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    students = read_students()
    for s in students:
        if s['id'] == id:
            return jsonify(s)
    return jsonify(error="Student not found"), 404

@app.route('/students', methods=['GET'])
def get_students_by_ln():
    last_name = request.args.get('last_name')
    students = read_students()
    if last_name:
        matched = [s for s in students if s['last_name'] == last_name]
        if not matched:
            return jsonify(error="No student found with that last name"), 404
        return jsonify(matched)
    return jsonify(students)


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data:
        return jsonify(error="No data provided"), 400
    if set(data.keys()) != FIELDS:
        return jsonify(error="Invalid or missing fields"), 400

    students = read_students()
    new_id = max([s['id'] for s in students], default=0) + 1
    new_student = {
        'id': new_id,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'age': int(data['age']),
    }
    students.append(new_student)
    write_students(students)
    return jsonify(new_student), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if not data:
        return jsonify(error="No data provided"), 400
    if set(data.keys()) != FIELDS:
        return jsonify(error="Invalid or missing fields"), 400

    students = read_students()
    for s in students:
        if s['id'] == id:
            s['first_name'] = data['first_name']
            s['last_name'] = data['last_name']
            s['age'] = int(data['age'])
            write_students(students)
            return jsonify(s)
    return jsonify(error="Student not found"), 404

@app.route('/students/<int:id>', methods=['PATCH'])
def patch_student(id):
    data = request.get_json()
    if not data or 'age' not in data:
        return jsonify(error="Missing age field"), 400
    students = read_students()
    for s in students:
        if s['id'] == id:
            s['age'] = int(data['age'])
            write_students(students)
            return jsonify(s)
    return jsonify(error="Student not found"), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    students = read_students()
    for i, s in enumerate(students):
        if s['id'] == id:
            students.pop(i)
            write_students(students)
            return jsonify(message=f"Student deleted successfully")
    return jsonify(error="Student not found"), 404

if __name__ == '__main__':
   app.run(debug=True)
