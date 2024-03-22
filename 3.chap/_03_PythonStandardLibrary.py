# 파이썬으로 카지노 만들기

# 컴퓨터 숫자 하나 선택 , 유저  숫자 하나 선택
# 유저가 컴퓨터 숫자 맞추면 이기는 게임


from random import randint # 랜덤 모듈에서 랜드인트를 불러주세요.

user_choice = int(input("Choose Number")) 

pc_choice = randint(1,10)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Higher!", pc_choice)
elif user_choice < pc_choice:
    print("Lower!", pc_choice)

print("수고하셨습니다.")

