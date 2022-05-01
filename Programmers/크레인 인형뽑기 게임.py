def solution(board, moves):
    answer = 0
    basket = [0]

    #for문 중첩으로 풀어도 됐었음
    #이동 수 만큼 반복
    for move in moves:
        idx = 0
        move -= 1

        #현재 좌표가 0이면
        if board[idx][move] == 0:
            #인형 만날 때까지, 0 아닐 때까지 idx 증가
            while board[idx][move] == 0:
                idx += 1
                #board의 길이만큼 index가 커지면 반복문 탈출
                #해당 줄에 인형 없는 것
                if idx >= len(board):
                    #이미 인덱스가 크기를 넘어갔으므로 하나 줄여서 탈출
                    idx -= 1
                    break

        #인형 만나면
        if board[idx][move] != 0:
            #바구니에 있는 인형이랑 비교해서 같으면
            if basket[-1] == board[idx][move]:
                #두 개 삭제
                answer += 2
                #기존에 있던 인형 pop
                basket.pop()
            #바구니에 있는 인형이랑 비교해서 다르면
            elif basket[-1] != board[idx][move]:
                #인형 바구니에 넣기
                basket.append(board[idx][move])
            #바구니에 인형 넣었으니까 0으로 치환
            board[idx][move] = 0

    return answer

'''
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]) == 4)'''
