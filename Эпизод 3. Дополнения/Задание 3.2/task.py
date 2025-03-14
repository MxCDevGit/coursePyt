def task_1(list, x):
    index = 0

    for i in list:
        if i == x:

            return str(index)
        index += 1

def task_2(x):
    flag = 0
    i = 1
    while(i <= x):
        if x % i == 0:
            flag += 1
        i += 1

    if flag == 2:
        return True
    else:
        return False