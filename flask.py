import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        group = request.form['group']
        try:
            EP.add_group(group)
        except Exception as ex:
            print(ex)
        return redirect('/')
    elif request.method == 'GET':
        groups = [EP.group_names(i) for i in range(EP.group_count())]
        return render_template('index.html', groups=groups, is_admin=is_admin)


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['pass']
        if login == os.getenv('LOGIN') and password == os.getenv('PASSWORD'):
            globals()['is_admin'] = True
        else:
            return redirect('/reg')
        return redirect('/')
    elif request.method == 'GET':
        return render_template('reg.html')


@app.route('/groups/<int:id>', methods=['POST', 'GET'])
def groups(id):
    if request.method == 'POST':
        name = request.form['name']
        course = int(request.form['course'])
        try:
            EP.add_student(EP.group_names(id), name, course)
        except Exception as ex:
            print(ex)
        return redirect(f'/groups/{id}')
    elif request.method == 'GET':
        group_name = EP.group_names(id)
        students_count = EP.get_group(group_name)[1]
        students = []
        for i in range(students_count):
            student = EP.get_student(group_name, i)
            students.append({
                'name': student[0],
                'course': int(student[1])
            })
        return render_template('group.html', id=id, is_admin=is_admin, group_name=group_name, students=students)


if __name__ == '__main__':
    is_admin = False
    EP = api.EduPart()
    app.run(debug=True)
