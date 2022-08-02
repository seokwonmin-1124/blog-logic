# blog-logic
flask를 이용한 동적 블로그
### 사용법
1. /app/database.py 에서 사용할 db명을 `db = "이름"` 에 입력합니다.<br>
2. /app/database.py 에서 `setDb()`함수를 호출해 데이터베이스 세팅을 마칩니다.<br>
3. /app/main.py 를 실행시킵니다. 이때 필요한 모듈들은 `flask`, `python markdown` 입니다.<br>