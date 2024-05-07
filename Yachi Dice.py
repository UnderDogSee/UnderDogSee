import random           #랜덤 모듈 호출
#함수 적는 곳
def dice():         #dice라는 이름의 함수 선언 인자는 없음
    roll = []           #roll 이라는 빈 리스트를 생성 해서 값을 받을 수 있게 준비
    for i in range(5):      #주사위가 5개가 돼야 하기 때문에 5번 반복
        roll.append(random.randint(1,6))  #roll 빈 리스트에 1~6 중 랜덤하게 추가
    return roll     #roll 변수를 반환해줌
def game_result(dice_result):       #game_result라는 이름의 함수 선언 함수 호출시 입력받을 dice_result 라는 변수를 인자로 선언
    score = 0               #score 라는 변수를 0 으로 초기화
    if dice_result[0] == dice_result[4]:        #만약에 dice_result 의 인덱스 0에 있는 값이 4에 있는 값과 일치 할 경우
        score += 1000 + dice_result[0]          #1000점을 얻고 0번 인덱스의 값도 score 에 저장
        print("%d 야추!" % dice_result[0])                          #제일 높은 족보
    elif dice_result[0] == dice_result[3] or dice_result[1] == dice_result[4]:  #그게 아니라 0번 인덱스와 3번인덱스가 같거나 1번 인덱스와 4번 인덱스가 같다면
        score += 500               #500점 획득
        print("%d 포카드!" % dice_result[3])           #두번째로 높은 족보
        if dice_result[0] == dice_result[3]:    #만약에 0번 인덱스와 3번 인덱스가 같다면
            score += dice_result[0]*10 + dice_result[4]    #score에 0번 인덱스를 10번 곱해서 저장하고 4번 인덱스를 추가 저장
        else:           #그외는
            score += dice_result[4]*10 + dice_result[0]      #4번 인덱스를 10번 곱하고 0번 인덱스를 추가 저장
    elif dice_result[0] == dice_result[2] or dice_result[1] == dice_result[3] or dice_result[2] == dice_result[4]:  #그게 아니라 0,2번 인덱스가 같거나 1,3번 인덱스가 같거나 2,4번 인덱스가 같다면
        score += 300                #300점 획득
        if dice_result[0] == dice_result[2] and dice_result[3] == dice_result[4]:       #만약에 0,2번 인덱스 가 같고 3,4번 인덱스가 같다면
            score += 50 + dice_result[0]*10 + dice_result[3]*3       #50점 획득과 0번 인덱스를 10번 곱하고 3번 인덱스를 2번 곱한 값을 저장
            print("%d,%d 풀하우스!" % (dice_result[0],dice_result[3]))              #세번째로 높은 족보
        elif dice_result[2] == dice_result[4] and dice_result[0] == dice_result[1]:     #그게 아니라 2,4번 인덱스 가 같고 0,1번
            # 인덱스가 같다면
            score += 50 + dice_result[2]*10 + dice_result[0]*3       #50점 획득과 2번 인덱스를 10번 곱하고 0번 인덱스를 3번 곱한 값을 저장
            print("%d,%d 풀하우스!" % (dice_result[2],dice_result[0]))              #세번째로 높은 족보
        else:               #그외는
            if dice_result[2] == dice_result[4]:        #만약 2,4번 인덱스가 같다면
                score += -100 + dice_result[2]*10 + dice_result[1]*2 + dice_result[0]      #100점을 증감 하고 2번 인덱스를 10번 곱하고 1번 인덱스를 곱하고 0번 인덱스를 더한 값을 저장
                print("%d 트리플!" % dice_result[2])           #다섯번째 족보
            elif dice_result[1] == dice_result[3]:      #만약 1,3번 인덱스가 같다면
                score += -100 + dice_result[2]*10 + dice_result[4]*2 + dice_result[0]      #100점을 증감 하고 2번 인덱스를 10번 곱하고 4번 인덱스를 곱하고 0번 인덱스를 더한 값을 저장
                print("%d 트리플!" % dice_result[2])           #다섯번째 족보
            else:   #그외는
                score+= -100 + dice_result[2]*10 + dice_result[4]*2 + dice_result[3]      #100점을 증감 하고 2번 인덱스를 10번 곱하고 4번 인덱스를 2번 곱하고 3번 인덱스를 더한 값 저장
                print("%d 트리플!" % dice_result[2])           #다섯번째 족보
    elif dice_result in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:     #그게 아니라 dice_result 안에 해당 튜플 중에서 들어가있다면
        if dice_result == [1, 2, 3, 4, 5]:          #만약 dice_result 와 12345 튜플 과 같다면
            score += 277         #270점 획득
        else:       #그외는
            score += 278         #271점 획득
        print("%d 스트레이트!" % dice_result[4])         #네번째 족보
        #그게 아니라면 0과 1 그리고 3 과 4 인덱스가 같다면 그게 아니라면 0 과 1 인덱스와 2와 3 인덱스 또는 1 과 2 인덱스와 3과 4 또는 0과 1 인덱스와 3과 4인덱스가 같다면
    elif dice_result[0] == dice_result[1] and dice_result[2] == dice_result[3] or dice_result[1] == dice_result[2] and dice_result[3] == dice_result[4] or dice_result[0] == dice_result[1] and dice_result[3] == dice_result[4]:
        score += 100  # 30점 획득
        if dice_result[0] == dice_result[1] and dice_result[2] == dice_result[3]:  # 만약 0과 1 그리고 2 와 3 인덱스가 같다면
            score += dice_result[3]*10 + dice_result[1]*2 + dice_result[4]  #3번 인덱스를 10번 곱하고 1번 인덱스를 2번 곱하고 4번 인덱스를 더한 값을 저장
            print("%d 투페어!" % (dice_result[2]))  # 여섯번째 족보
        elif dice_result[1] == dice_result[2] and dice_result[3] == dice_result[4]:  # 아니라면 1과 2 그리고 3 과 4 인덱스가 같다면
            score += dice_result[4]*10 + dice_result[2]*2 + dice_result[0]   #4번 인덱스를 10번 곱하고 2번 인덱스를 2번 곱하고 0번 인덱스를 더한 값을 저장
            print("%d 투페어!" % (dice_result[3]))  # 여섯번째 족보
        else:  # 그외는
            score += dice_result[4]*10 + dice_result[1]*2 + dice_result[2]   #1번 인덱스를 10번 곱하고 1번 인덱스를 2번 곱하고 2번 인덱스를 더한 값을 저장
            print("%d 투페어!" % (dice_result[3]))  # 여섯번째 족보
        #그게 아니라면 0 과 1 또는 1 과 2 또는 2와 3 또는 3과 4의 인덱스가 같다면
    elif dice_result[0] == dice_result[1] or dice_result[1] == dice_result[2] or dice_result[2] == dice_result[3] or dice_result[3] == dice_result[4]:
        score += 10     #10점 획득
        if dice_result[0] == dice_result[1]:        #만약 0 과 1번 인덱스가 같다면
            score += dice_result[1]*10 + dice_result[4]*4 + dice_result[3]*2 + dice_result[2]      #1번 인덱스를 10번 곱하고 4번 인덱스를 4번 곱하고 3번 인덱스를 2번 곱하고 2번 인덱스를 추가로 더한 값을 저장
            print("%d 원페어!" % dice_result[1])  # 일곱번째 족보
        elif dice_result[1] == dice_result[2]:      #그게 아니라 1과 2번 인덱스가 같다면
            score += dice_result[1]*10 + dice_result[4]*4 + dice_result[3]*2 + dice_result[0]      #1번 인덱스를 10번 곱하고 4번 인덱스를 4번 곱하고 3번 인덱스를 2번 곱하고 0번 인덱스를 추가로 더한 값을 저장
            print("%d 원페어!" % dice_result[1])  # 일곱번째 족보
        elif dice_result[2] == dice_result[3]:          #그게 아니라 2번 3번 인덱스가 같다면
            score += dice_result[3]*10 + dice_result[4]*4 + dice_result[1]*2 + dice_result[0]      #3번 인덱스를 10번 곱하고 4번 인덱스를 4번 곱하고 1번 인덱스를 2번 곱하고 0번 인덱스를 추가로 더한 값을 저장
            print("%d 원페어!" % dice_result[3])  # 일곱번째 족보
        else:       #그외는
            score += dice_result[4]*10 + dice_result[2]*4 + dice_result[1]*2 + dice_result[0]      #4번 인덱스를 10번 곱하고 2번 인덱스를 4번 곱하고 1번 인덱스를 2번 곱하고 0번 인덱스를 추가로 더한 값을 저장
            print("%d 원페어!" % dice_result[4])  # 일곱번째 족보
    else:       #그외는
        score += dice_result[4] + dice_result[3]     #4번,3번 인덱스에 있는 값을 score에 저장
        print("%d 탑!" % dice_result[4])     #마지막 족보(꼴등족보)
    return score        #score 변수를 반환해줌
#족보 조건 코드 칸이 난잡해서 요약도 적겠습니다. 해당 함수는
#족보가 완성이 되면 족보점수 + 족보에 해당하는 숫자 * 10 + 나머지 숫자중 높은 수 를 기준으로 계산해서
#score 라는 변수를 내보내는 함수 입니다.

#유저 주사위 굴리는 자리
user_dice_result = []           #유저 주사위 결과 빈 리스트 생성
com_dice_result = []         #컴퓨터 주사위 결과 빈 리스트 생성
for i in range(3):          #주사위를 3개를 뽑을 것이기 때문에 3번 반복
    print("당신의 %d번째 주사위 입니다" % (i+1))       #몇 번째 주사위 인지 알려줌
    user_dice = dice()                          #user_dice 라는 변수에 함수 dice 를 불러옴 인자는 없으므로 () 공백
    print(user_dice)        #주사위를 출력
    while True:             #무한루프 실행
        select_user = int(input("다시 굴리실 주사위 갯수를 적어주세요: "))      #몇개를 굴릴지 입력 받음
        if 5 >= select_user:        #5이하의 입력을 받으면
            break       #while문을 종료
        else:               #그 외는
            print("잘못 입력하셨습니다")  # 잘못 입력했다는 메세지
    selected_dice = []           #선택했던 주사위를 확인하기 위한 빈 리스트 생성
    for k in range(select_user):                #다시 굴릴 주사위 갯수 만큼 반복
        while True:                 #무한 루프 선언
            select_dice = int(input("%d번째 굴리실 주사위 위치를 적어주세요: " % (k + 1)))  #다시 굴릴 위치 입력 받음
            if select_dice in selected_dice:             #만약에 다시굴릴 위치 입력이 selected_dice 리스트 안에 있는 정수와 일치하는 게 있을 시
                print("이전에 선택했던 주사위는 다시 굴릴 수 없습니다")     #다시 입력 받을 수 없다고 출력
                print("현재 주사위 상태 %s" % user_dice)                #현재 주사위 상태를 알려줌
            elif 5 >= select_dice:                #5이하의 입력을 받으면
                user_dice[select_dice - 1] = random.randint(1, 6)       #user_dice 리스트 안에있는 select_dice -1 인덱스를 새롭게 1~6 중 하나로 변경
                print("현재 주사위 상태 %s" % user_dice)                #현재 주사위 상태를 알려줌
                selected_dice.append(select_dice)        #selected_dice 리스트에 select_dice 로 입력받은 정수를 저장
                break                       #while문을 종료
            else:                   #그외 에는
                print("잘못 입력하셨습니다")             #잘못 입력했다는 메세지
    user_dice.sort()            #user_dice 리스트 정렬
    print("당신의 %d번째 주사위 결과: %s" % (i+1,user_dice))          #컴퓨터의 주사위 결과 확인
    print("")                               #출력이 더러워져서 공백 메세지
    user_dice_result.append(user_dice)      #user_dice_result 리스트에 user_dice 의 결과를 추가

#컴퓨터 주사위 굴리는 자리
for i in range(3):              #주사위 3개를 만들거기 때문에 3번 반복
    com_dice = dice()           #com_dice 변수에 dice 함수의 반환 변수를 입력받음
    print("컴퓨터의 %d번째 주사위 입니다" % (i+1))       #컴퓨터가 던진게 몇 번째 주사위 인지 알려줌
    print(com_dice)        #주사위를 출력

#컴퓨터 주사위 다시 굴리는 자리
    dice_save_list = [0,0,0,0,0,0]  #1부터 6까지 카운터를 셀 리스트를 생성
    for k in range(5):              #주사위 5개라서 5번 반복
        dice_save_list[com_dice[k]-1] += 1  #dice_save_list 리스트안에 com_dice의 인덱스에 있는 정수의 -1에 해당하는 인덱스를 1씩 증가 (com_dice의 0번 인덱스의 정수가 4면 인덱스4에 1 증가)
    com_count = 0  #비교를 하기 위해서 com_count 라는 변수 생성 후 0 저장
    for k in range(6):  #dice_save_list 리스트가 6개 라서 6번 반복
        if dice_save_list[k] > com_count:  #만약에 dice_save_list의 리스트의 [k]인덱스가 com_count 보다 높다면
            com_count = dice_save_list[k]  #com_count 에 dice_save_list 의 k에 해당하는 값을 저장
            com_dice_bigyo = k + 1  #com_dice_bigyo 에 k+1 을 저장
        elif dice_save_list[k] == com_count:  #그게 아니라면 dice_save_list[k] 와 com_count가 같다면 예)3번 인덱스가 6이고 5번 인덱스가 똑같이 6이라면
            com_dice_bigyo = k + 1  #com_dice_bigyo 에 k+1 을 저장                                위 예시 이어서 설명) com_dice_bigyo 는 6이 된다
    com_save = []               #제일 높은 값 or 중복으로 많이 나온 값을 저장하기 위한 빈 리스트 생성
    for k in range(com_count):  #com_count 만큼 반복
        if com_count == 1:      #만약에 com_count가 하나 밖에 오르지 않아서 1과 같다면
            com_save = [com_dice[3]]+[com_dice[4]]      #com_dice 리스트의 3번 인덱스와 4번 인덱스르 com_save에 리스트 형식으로 저장한다 예) 3번 인덱스 4 4번 인덱스 5 일 경우 com_save는 [4,5]
        else:       #그외는
            com_save.append(com_dice_bigyo)  #com_dice_bigyo에 저장되있는 정수를 com_save에 저장
    print("컴퓨터가 %s을(를) 세이브 하고 다시 굴립니다" % com_save)  # 컴퓨터가 주사위를 다시 굴림을 알려줌
    for k in range(5-len(com_save)):    #com_save에 부족한 리스트 5칸이 만들어질때까지 반복
        com_save.append(random.randint(1,6))    #com_save 에 랜덤하게 1~6중 하나 생성해서 저장
        com_save.sort()         #com_save 리스트를 정렬
    print("컴퓨터의 %d번째 주사위 결과: %s" % (i+1,com_save))          #컴퓨터의 주사위 결과 확인
    print("")                       #출력이 더러워져서 공백 메세지
    com_dice_result.append(com_save)      #com_dice_result 리스트에 com_save 리스트를 저장

#유저와 컴퓨터가 대결하는 자리
win_count = 0                    #승패를 계산하기 위해 win_count 를 0으로 초기화
for i in range(3):                  #3판을 진행 했기 때문에 3번 반복
    print("%d번째 대결 - 유저: %s  컴퓨터: %s" % (i+1,user_dice_result[i],com_dice_result[i]))     #유저와 컴퓨터가 만들어낸 주사위를 하나씩 출력
    user = game_result(user_dice_result[i])          #user_dice_result 리스트의 [i]인덱스에 해당하는 값을 game_result 함수를 호출해 계산후 user에 저장
    com = game_result(com_dice_result[i])        #com_dice_result 리스트의 [i]인덱스에 해당하는 값을 game_result 함수를 호출해 계산후 com에 저장
    if user > com:                      #만약 com 점수보다 user 점수가 클 경우
        print("%d번째 대결 결과 - 승" % (i+1))         #승리 메세지
        win_count += 1                      #승리 카운터 1 증가
    elif com > user:                    #만약 user 점수보다 com 점수가 클 경우
        print("%d번째 대결 결과 - 패" % (i+1))         #패배 메세지
        win_count -= 1                      #승리 카운터 1 증감
    else:                               #그외는
        print("%d번째 대결 결과 - 무" % (i+1))         #무승부 메세지
    print("")                       #출력이 더러워져서 공백 메세지
if win_count > 0:                       #승리 카운터가 0 보다 클경우
    print("총게임 결과: 당신이 이겼습니다")      #승리
elif win_count < 0:                     #승리 카운터가 0 보다 작을경우
    print("총게임 결과: 당신이 졌습니다")        #패배
else:                                   #그외는
    print("총게임 결과: 당신은 비겼습니다")  #    #무승부