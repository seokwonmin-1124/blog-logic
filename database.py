import sqlite3

def setDb():
    conn = sqlite3.connect('_test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS topic (id INTEGER PREMENT KEY, title text, body text)")
    conn.commit()
    conn.close()
    return print("DB 초기 세팅 완료")

def createRow(id, title, body):
    conn = sqlite3.connect('_test.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO topic(id, title, body) VALUES(?,?,?)''',
        (id, title, body)
    )
    conn.commit()
    conn.close()
    return print("Row 생성 완료")

def readRow(opt=all):
    conn = sqlite3.connect('_test.db')
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
    conn = sqlite3.connect('_test.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE topic SET title = '{title}', body = '{body}' WHERE id = '{id}'")
    conn.commit()
    conn.close()
    return print("수정 완료")

def delRow(id):
    conn = sqlite3.connect('_test.db')
    cursor = conn.cursor()

    if id == all:
        cursor.execute("DELETE FROM topic")
    else:
        cursor.execute(f"DELETE FROM topic WHERE id = '{id}'")

    conn.commit()
    conn.close()
    return print("삭제 완료")