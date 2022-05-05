def solution(places):
    answer = [1 for i in range(5)]

    #상하좌우 확인 함수
    def check_dir(p, x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        #상좌하우 순서로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #확인하려는 좌표가 주어진 좌표에서 벗어나면 탐색하지 않음
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
            #상하좌우에 사람이 있다면 False 반환
            elif p[nx][ny] == 'P': return False
            #파티션 있으면 다른 곳 탐색
            elif p[nx][ny] == 'X': continue
            #빈 자리라면 맨해튼 2이하에 또 사람이 있나 확인하기 위하여 재탐색
            #맨해튼 2초과하려면 상하좌우에 2칸씩 사람이 없어야함
            elif p[nx][ny] == 'O':
                #탐색 인덱스에 상하좌우 인덱스를 한번씩 더 증가
                nx += dx[i]
                ny += dy[i]

                #탐색하려는 곳이 벗어난 곳인지 확인
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:continue
                #사람이 있으면 맨해튼 2 이하이므로 False
                elif p[nx][ny] == 'P':return False
                else:continue

        #끝까지 함수가 종료되지 않았다면 거리두기가 지켜진 것이므로 True 반환
        return True

    #대각선 방향 탐색
    def check_dia(p, x, y):
        dx = [-1, -1, 1, 1]
        dy = [-1, 1, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #탐색하려는 곳이 주어진 좌표 안인지 확인
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
            #대각선에 사람이 있으면 대각선이 아닌 곳에 파티션이 있나 확인
            elif p[nx][ny] == 'P':
                #좌측 상향에 사람이 있다면 상, 좌 확인 후 두 곳 다 파티션이 존재하면 True
                if p[x][ny] == 'X' and p[nx][y] == 'X': return True
                #그렇지 않으면 False
                else: return False
            elif p[nx][ny] == 'X' or p[nx][ny] == 'O': continue

        return True

    for i in range(5):
        for j in range(5):
            for k in range(5):
                #대기실에 사람이 존재하면
                if places[i][j][k] == 'P':
                    #상하좌우에 사람이 있는지 확인 후 맨해튼 2 이하에 사람이 있다면
                    if check_dir(places[i], j, k) == False:
                        #거리두기가 지켜지지 않은 것으로 0 저장후 반복문 탈출
                        answer[i] = 0
                        break
                    #상하좌우 사람 없다면 대각선에 사람이 있나 확인
                    elif check_dia(places[i], j, k) == False:
                        answer[i] = 0
                        break
            if answer[i] == 0 :
                break

    return answer
