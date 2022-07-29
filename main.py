from flask import Flask, request, redirect
import sqlite3
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    rows = str(db.readRow())
    return rows

@app.route('/set/')
def set():
    db.setDb()
    db.readRow(all)
    return "db is ready"

@app.route('/read/<int:id>/')
def read(id):
    rows = str(db.readRow(id))
    return f"""
    <p>{rows}</p>
    """

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="number" name="id" placeholder="id"></p>
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return content

    elif request.method == 'POST':
        id = int(request.form['id'])
        title = request.form['title']
        body = request.form['body']
        db.createRow(id, title, body)
        return redirect('/')

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