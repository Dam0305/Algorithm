def solution(n, t, m, timetable):
    #셔틀버스 운행횟수만큼 리스트 초기화
    answer = [[] for _ in range(n)]
    #시간은 9시로 초기화
    #(60*9) -> 배차 시간 계산 편리하게 하기 위함
    time = 540

    #크루 도착 시간 오름차순 정렬
    timetable.sort()

    #크루 도착시간 정수로 변경
    for i in range(len(timetable)):
        H, M = timetable[i].split(':')
        H = int(H) * 60
        M = int(M)
        timetable[i] = H + M

    #배차시간 계산
    def trans(t):
        #시작 시간부터 배차간격만큼 더해줌
        return 60 * 9 + t

    idx = 0
    #운행 횟수만큼 반복
    for i in range(n):
        #함수 인자로 배차 시간 * 현재 운행 횟수
        time = trans(t * i)

        #현재 출발 셔틀보다 먼저 도착하거나 같은 시간에 도착한 크루가 있을 때까지 반복
        while timetable[idx] <= time:
            #배차 순서에 맞게 리스트에 출발한 크루 저장
            answer[i].append(timetable[idx])
            idx += 1
            #만약 셔틀에 탄 크루가 정원보다 많으면
            if len(answer[i]) >= m:
                #반복문 탈출
                break
            #만약 모든 크루가 셔틀에 다 탔다면 반복문 탈출
            elif idx >= len(timetable):
                break

    #마지막 셔틀에 탄 크루가 정원보다 많으면
    if len(answer[-1]) >= m:
        #콘은 마지막 셔틀에 탄 마지막 크루보다 1분 빨리 도착해야 셔틀에 탈 수 있음
        return str((answer[-1][-1] - 1) // 60).rjust(2, '0') + ':' + str((answer[-1][-1] - 1) % 60).rjust(2, '0')
    #마지막 셔틀에 탄 크루가 없거나 정원보다 적으면
    elif len(answer[-1]) == 0 or len(answer[-1]) < m:
        #콘은 마지막 셔틀 출발시간에 도착해도 셔틀을 탈 수 있음
        return str(time // 60).rjust(2, '0') + ':' + str(time % 60).rjust(2, '0')
