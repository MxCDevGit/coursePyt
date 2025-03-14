# todo: replace this with an actual task
def task_1(str):
    counter = 0
    for i in str:
        counter += 1
        if i == ' ':
            counter = 0
    return counter


def task_2(str):
    strTemp = ""
    strResult = ""
    flag = 1
    for i in str:
        if flag % 2 == 1:
            strTemp += i
        if flag % 2 == 0:
            strResult += i

        if i == " ":
            flag += 1
            if flag % 2 == 1:
                strResult += strTemp
                strTemp = ""

    if flag % 2 == 1:
        strResult += strTemp

    return strResult


def task_3(str):
    temp = ""
    counter = 0
    flag = 0

    for i in str:
        if flag == 1 and temp == i:
            counter += 1
        if i == ' ':
            flag = 1
        else:
            temp = i
            flag = 0

    return counter
