def solution(m, n, board):
    answer = 0
    block = [] #삭제한 블럭 좌표
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #수정하기 쉽게 리스트로 변환
    for i in range(m):
        board[i] = list(board[i])
    
    #블록 삭제 후 내리기
    def rep(row):
        s = [] #스택

        for i in range(m):
            #삭제한 블록이 아닌 경우
            if board[i][row] != '.':
                s.append(board[i][row]) #스택에 블록 저장
            board[i][row] = '0' #모든 블록 0으로 초기화
            
        #보드 제일 아래에서부터 스택의 길이만큼만 블럭 채워 넣음
        for i in range(m - 1, m - len(s) - 1, -1):
            board[i][row] = s.pop()


    while True:
        
        for i in range(m - 1):
            for j in range(n - 1):
                #블럭 4개가 같으면 리스트에 좌표 저장
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] in char:
                    block.extend([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
        
        #삭제한 블럭 없으면 종료
        if len(block) == 0:
            break
        #삭제한 블록 .으로 변경 
        for i in block:
            board[i[0]][i[1]] = '.'
        
        answer += len(set(block)) #삭제한 블럭 개수 더해주고 블럭 초기화
        block.clear()
        
        for i in range(m):
            for j in range(n):
                #삭제한 블럭 있으면 블럭 아래로 내리기
                if board[i][j] == '.':
                    rep(j)

    for i in range(m):
        board[i] = ''.join(board[i]) #블럭 다시 string으로

    return answer
