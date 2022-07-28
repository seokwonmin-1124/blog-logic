import sqlite3

def setDb(id, title, body):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS topic (id text PREMENT KEY, title text, body text)")
    createRow(id, title, body)
    conn.commit()
    conn.close()
    return print("DB 초기 세팅 완료")

def createRow(id, title, body):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO topic(id, title, body) VALUES(?,?,?)''',
        (id, title, body)
    )
    conn.commit()
    conn.close()
    return print("Row 생성 완료")

def readRow(id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT body FROM topic WHERE id = '{id}'")
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def updateRow(id, title, body):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE topic SET title = '{title}', body = '{body}' WHERE id = '{id}'")
    conn.commit()
    conn.close()
    return print("수정 완료")

def delRow(id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM topic WHERE id = '{id}'")
    conn.commit()
    conn.close()
    return print("삭제 완료")

def delAll():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM topic")
    conn.commit()
    conn.close()
    return print("전체 삭제 완료")

def showRows():
    connn = sqlite3.connect('test.db')
    cursor = connn.cursor()
    cursor.execute("SELECT * FROM topic")
    rows = cursor.fetchall()
    print(rows)
    connn.close()
    return rows

setDb(1, "hello world", "lorem ipsum is dummy text for web page development testing and more dummy text")
showRows()
updateRow(1, "hello world", "updated")
showRows()
createRow(2, "this is a test", "test is..")
showRows()