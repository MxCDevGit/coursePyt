def task_1(text):
    dict = {}
    sentenceCounter = 0
    wordCounter = 1
    sentence = ""

    for i in text:
        if i == ".":
            sentenceCounter += 1
            dict[sentence] = wordCounter
            wordCounter = 0
            sentence = ""

        elif sentence == "" and i == " ":
            wordCounter += 1

        elif i == " ":
            wordCounter += 1
            sentence += i

        else:
            sentence += i

    return dict

def task_2(x1, y1, x2, y2):
    result = ((x2 - x1)**2+(y2-y1)**2)**(1/2)
    return result