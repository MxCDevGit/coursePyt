def task_1(N):
    answer = 1
    for i in range (1, N + 1, 1):
        answer *= i
    return answer


def task_2(N):
    temp = 0
    answer = 1
    for i in range(3, N + 1, 1):
        answer += temp
        temp = answer - temp
    return answer


def task_3(N):
    numberList = []
    for i in range(1, N + 1, 1):
        if N % i == 0:
            numberList.append(i)
    return numberList