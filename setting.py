# 글 발행 중 중괄호로 된 set의 정보로 파일 이름을 생성하는 함수
# 글 작성 조건 -> set.md
from datetime import datetime

def createTopic(fname, topic):
    with open(f"./test/{fname}") as f: # 여기선 파일을 로컬 경로에서 찾지만 웹상에선 inpt 값을 바로 받아와서 실행시킬 예정
        set = f.readlines()[0:5]
        set = [x.strip() for x in set]
        f.close()
        print(set)
        result = convertSet(set)
        print(result)
    
    f = open(f"./test/{result['title']}_{result['date']}.txt", "w")
    f.write(f"{result}\n{topic}")
    f.close()

    return set


def convertSet(set):
    _set = {
        "title": set[1],
        "date": set[2],
        "opt": set[3],
    }

    _set["title"] = set[1][10:-2]
    _set["opt"] = set[3][8:-1]
    print(_set["date"])
    _set["date"] = checkOpt(_set)

    return _set


def checkOpt(set):
    opt = set["opt"]
    if opt == "ymd":
        # print(str(datetime.now())[0:10])
        return str(datetime.now())[0:10]
    elif opt == "ymdhm":
        # print(str(datetime.now())[0:16].replace(" ", "(") + ")")
        return str(datetime.now())[0:16].replace(" ", "(") + ")"
    elif opt == "ymdhms":
        # print(str(datetime.now())[0:19].replace(" ", "(") + ")")
        return str(datetime.now())[0:19].replace(" ", "(") + ")"
    else:
        print(opt)
        return False

lorem = "Magna dolore sit exercitation qui eiusmod nostrud veniam adipisicing incididunt."

# createTopic('test.md', lorem)