
from flask import Flask, jsonify, Response, request, abort

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/students/<int:StudentID>", methods=['GET', 'PUT'])
def students(StudentID, **kwargs):
    if request.method == 'GET':
        student = Student(StudentID, 'Female', 23, 'hmh@gmail.com', 'Seattle', 'Fall 2016', 'Aug 2018', 'Information System', 'Master', 'No') # Result example
        response = jsonify(student.serialize())
        response.status_code = 200
    else:
        params = request.get_json()
        student = Student(StudentID,
                          params['Gender'],
                          int(params['Age']),
                          params['Email'],
                          params['Campus'],
                          params['StartTerm'],
                          params['ExpectedGraduation'],
                          params['Major'],
                          params['Degree'],
                          params['Enrollment'])
        response = jsonify(student.serialize())
        response.status_code = 200
        print(student)
    return response


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


class Student(object):
    def __init__(self, StudentID, Gender, Age, Email, Campus, StartTerm, ExpectedGraduation, Major,Degree, Enrollment):
        self.StudentID = StudentID
        self.Gender = Gender
        self.Age = Age
        self.Email = Email
        self.Campus = Campus
        self.StartTerm = StartTerm
        self.ExpectedGraduation = ExpectedGraduation
        self.Major = Major
        self.Degree = Degree
        self.Enrollment = Enrollment

    def __repr__(self):
        return "Student({:d}, {}, {:d}, {}, {}, {}, {}, {}, {}, {})"\
            .format(self.StudentID, self.Gender, self.Age, self.Email, self.Campus, self.StartTerm, self.ExpectedGraduation, self.Major, self.Degree, self.Enrollment)

    def serialize(self):
        return {
            'StudentID': self.StudentID,
            'Gender': self.Gender,
            'Age': self.Age,
            'Email': self.Email,
            'Campus': self.Campus,
            'StartTerm': self.StartTerm,
            'ExpectedGraduation': self.ExpectedGraduation,
            'Major': self.Major,
            'Degree': self.Degree,
            'Enrollment': self.Enrollment,
        }
