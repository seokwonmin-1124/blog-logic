from re import template
from flask import Flask, request, redirect
import sqlite3
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    rows = db.readRow()
    print(rows)
    li = ''
    for row in rows:
        li += f"<li><a href='/read/{row[0]}/'>{row[1]}</a></li>"
    li += f"<p><a href='/create/'>create</a></p>"
    return li

@app.route('/read/<int:id>/')
def read(id):
    row = db.readRow(id)
    title = row[0][1]
    body = row[0][2]
    return f"<h2>{title}</h2><p>{body}</p><a href='/'>home</a> <a href='/update/{id}/'>update</a> <a href='/delete/{id}/'>delete</a></p>"

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

@app.errorhandler(IndexError)
def indexError(error):
    return "없는 글입니다"

@app.errorhandler(404)
def notFound(error):
    return "404 Not Found, 없는 페이지입니다."

app.run(debug=True, port=2020)