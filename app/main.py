from flask import Flask, request, redirect, render_template, session
import database as db
from flaskext.markdown import Markdown

app = Flask(__name__)
app.secret_key = 'super secret key'
Markdown(app, extensions=['nl2br', 'fenced_code'])

ID = "lesh"
PW = "fptnldlqslek"

login = False

@app.route('/printit')
def printloginTF():
    return str(login)

@app.route('/login')
def login():
    global login
    if "userId" in session:
        login = True
        return render_template("login.html", userName=session["userId"], login=login)
    else:
        login = False
        return render_template("login.html", login=login)

@app.route('/dologin', methods=['POST'])
def dologin():
    _id = request.form['loginId']
    _pw = request.form['loginPw']

    if ID == _id and PW == _pw:
        session["userId"] = _id
        return redirect("/login")

@app.route('/dologout')
def dologout():
    session.pop("userId")
    return redirect("/login")

@app.route('/')
def index():
    global login
    rows = db.readRow()
    print(rows)
    if "userId" in session:
        login = True
    return render_template('index.html', rows=rows, login=login)

@app.route('/read/<int:id>/')
def read(id):
    row = db.readRow(id)
    id = row[0][0]
    title = row[0][1]
    body = row[0][2]
    return render_template('read.html', id=id, title=title, body=body)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    global login
    if login == True:
        if request.method == 'GET':
            return render_template('create.html')

        elif request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            id = db.createRow(title, body)
            url = f'/read/{id}/'
            return redirect(url)

    else:
        return redirect("/login")

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    global login
    if login == True:
        if request.method == 'GET':
            row = db.readRow(id)
            return render_template('update.html', id=id, title=row[0][1], body=row[0][2])

        elif request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            db.updateRow(id, title, body)
            url = f'/read/{id}/'
            return redirect(url)

    else:
        return redirect("/login")

@app.route('/delete/<int:id>/')
def delete(id):
    global login
    if login == True:
        db.delRow(id)
        return redirect('/')
    
    else:
        return redirect("/login")

@app.errorhandler(IndexError)
def indexError(error):
    return "없는 글입니다"

@app.errorhandler(404)
def notFound(error):
    return "404 Not Found, 없는 페이지입니다."

app.run(debug=True, port=2020)