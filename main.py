from flask import Flask, request, redirect
import sqlite3
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    rows = str(db.readRow())
    return rows

@app.route('/read/<int:id>/')
def read(id):
    row = str(db.readRow(id))
    return f"id값이 {id}인 데이터의 값은 {row} 입니다"

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return content

    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        id = db.createRow(title, body)
        url = f'/read/{id}/'
        return redirect(url)

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        row = db.readRow(id)
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{row[0][1]}"></p>
                <p><textarea name="body" placeholder="body">{row[0][2]}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return content

    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        db.updateRow(id, title, body)
        url = f'/read/{id}/'
        return redirect(url)

@app.route('/delete/<int:id>/')
def delete(id):
    db.delRow(id)
    return redirect('/')

app.run(debug=True, port=2020)