def task_1(str):
    dict = {}
    for i in str:
        if i.isalpha():
            dict[i] = 0
    for i in str:
        if i in dict:
            dict[i] += 1
    return dict


def task_2(list):
    myList = set(list)
    result = 0

    for i in myList:
        result += i

    return result


def task_3(cities):
    myStr = ""
    counter = 0

    for i in cities:
        if counter + 1 == len(cities):
            myStr += i + '.'
        else:
            myStr += i + ',' + ' '
            counter += 1
    return myStr


def task_4(a, b):
    c = set(a) & set(b)
    return list(c)
