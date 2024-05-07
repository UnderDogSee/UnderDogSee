import random
cpu_random = []
cpu_random.append(random.randrange(0,3))
cpu_choice = cpu_random[0]

player_choice_list = [(0,"가위"), (1,"바위") , (2,"보")]
cpu_choice_list = [(0,"가위"), (1,"바위") , (2,"보")]
result_list = [(0,"비겼습니다"), (1,"이겼습니다") , (2,"졌습니다")]

player_choice = int(input("가위(0) 바위(1) 보(2) 중에 선택해주세요: "))
result_vs = (player_choice - cpu_choice +3) % 3

print("플레이어: %s 컴퓨터: %s" % (player_choice_list[player_choice][1], cpu_choice_list[cpu_choice][1]))
print("결과 %s" % result_list[result_vs][1])