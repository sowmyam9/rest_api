from flask import Flask, jsonify

app = Flask(__name__)

# Define the students list at the global level
students = [
    {
        'id': 1,
        'student_name': 'std1',
        'age': 21,
        'email': 'heloo@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'std2',
        'age': 22,
        'email': 'heloo@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'std3',
        'age': 23,
        'email': 'heloo@gmail.com'
    }
]

@app.route('/students-list')
def students_list():
    return jsonify(students)

@app.route('/students/get/<int:id>')
def get_student(id):
    # Use global variable students
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
