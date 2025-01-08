from flask import render_template, request
from models import Student

def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            students = Student.query.all()
            return render_template('index.html', students=students)
        elif request.method == 'POST':
            first_name = request.form.get('firstname')
            last_name = request.form.get('lastname')
            age = int(request.form.get('age'))

            student = Student(
                first_name=first_name,
                last_name=last_name,
                age=age
            )

            db.session.add(student)
            db.session.commit()

            students = Student.query.all()
            return render_template('index.html', students=students)
        
    @app.route('/delete/<id>', methods=['DELETE'])
    def delete(id):
        Student.query.filter(Student.id == id).delete()

        db.session.commit()

        students = Student.query.all()
        return render_template('index.html', students=students)
    
    @app.route('/details/<id>')
    def details(id):
        student = Student.query.filter(Student.id == id).first()
        return render_template('details.html', student=student)