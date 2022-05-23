string = input()

al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#순서대로 확인하면서 같은 것 *로 치환
for i in al:
    string = string.replace(i, '*')

print(len(string)) #치환하면 문자열의 길이가 줄어듦 -> 정답 문자열 길이
