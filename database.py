import sqlite3

db = 'topic.db'

def setDb():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS topic (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title text, body text)")
    conn.commit()
    conn.close()
    return print("DB 초기 세팅 완료")

def createRow(title, body):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO topic(title, body) VALUES(?,?)''',
        (title, body)
    )
    conn.commit()
    conn.close()
    lastId = cursor.lastrowid
    return lastId

def readRow(opt=all):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    if opt == all:
        cursor.execute("SELECT * FROM topic")
    else:
        cursor.execute(f"SELECT * FROM topic WHERE id = '{opt}'")

    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def updateRow(id, title, body):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE topic SET title = '{title}', body = '{body}' WHERE id = '{id}'")
    conn.commit()
    conn.close()
    return print("수정 완료")

def delRow(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    if id == all:
        cursor.execute("DELETE FROM topic")
    else:
        cursor.execute(f"DELETE FROM topic WHERE id = '{id}'")

    conn.commit()
    conn.close()
    return print("삭제 완료")

def lastRowId():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    id = cursor.lastrowid
    return id

# setDb()