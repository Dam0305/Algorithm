def solution(s):
    answer = []
    eng = {"zero" : "0","one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    num = '1234567890'

    start = 0
    end = 1
    while end <= len(s):
        if s[start:end] in num:
            answer.append(s[start:end])
            start+= 1
            end+=1
        elif s[start:end] in eng.keys():
            answer.append(eng[s[start:end]])
            start = end
            end += 1
        else:
            end += 1
    print(answer)
    return int(''.join(answer))
