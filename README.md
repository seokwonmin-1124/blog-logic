# setting.py 사용방법
```md
<!-- ./test/test.md -->
{
    "title": "first",
    "date": date.today(),
    "opt": "default"
}
<!-- 한칸 띄고 -->
topic
```
위와 같은 형태로 작성하면 됨<br>
형식을 지키지 않으면 에러가 남<br>
저런 형태라면 파일명은 `first_yyyy-mm-dd(hh:mm:ss)` 로 자동적으로 세팅됨

## options

### title
별 다른 옵션 없이 자신이 원하는 파일 이름을 입력하면 됨.<br>
ex) vuejs 컴포넌트 사용법<br>
이때 띄어쓰기는 다 하이폰(-) 으로 자동교체됨<br>
-> vuejs-컴포넌트-사용방법

### date
수동으로 날짜를 입력할 땐 아래의 형식을 지켜주는게 좋음(형식 표준화를 위해)<br>
`yyyy-mm-dd` or `yyyy-mm-dd(hh:mm)` or `yyyy-mm-dd(hh:mm:ss)`<br>
개인적으로 2번째 y-m-d(h:m) 형식을 추천함

### opt
이 opt는 날짜 설정으로써 총 세가지 속성이 있음

1. ymdhm(추천기능)
`yyyy-mm-dd(hh:mm)` 형식으로 날짜가 입력됨.<br>
이 형식을 추천하는 이유는 시:분 형식으로 파일명이 이루어져 있어 같은날에 올라오는 글의 중복을 막을 수 있음<br>
개인적인 블로그에 추천하는 기능

2. ymdhms
`yyyy-mm-dd(hh:mm:ss)` 형식으로 날짜가 입력됨.<Br>
매 초마다 새로운 글이 발행되는 게시판과 같은 사이트에 추천하는 기능

3. ymd
`yyyy-mm-dd` 형식으로 날짜가 입력됨<br>
TIL에 추천하는 기능<br>

추가적으로 setting.py에 있는 코드를 수정해 유저가 날짜형식을 커스텀할 수 있음
