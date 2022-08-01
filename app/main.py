from flask import Flask, request, redirect, render_template
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    rows = db.readRow()
    print(rows)
    return render_template('index.html', rows=rows)

@app.route('/read/<int:id>/')
def read(id):
    row = db.readRow(id)
    id = row[0][0]
    title = row[0][1]
    body = row[0][2]
    return render_template('read.html', id=id, title=title, body=body)

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