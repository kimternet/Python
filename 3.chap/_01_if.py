# name = input("What's your name ? ")


# print("안녕하세요 ", name,"씨")

# age = int(input("How old Are you? "))

# print("오 나이가 ", age,"이군요")


# print(name,"씨 올해 나이는 ", age," 입니다")


    
print(" 안녕하세요 유아반 접수처 입니다.")
print(" 귀하의 자녀 나이를 입력해주세요.")

age = int(input("자녀의 나이가 몇 세인가요?"))

if age >= 8 :
    print("유아반 가입이 불가능한 나이입니다.")
elif age >= 3 and age < 8:
    print("유아반 가입이 가능합니다.")
else:
    print("자세한 문의 사항은 01로 연락주세요")
    

print("1번 가입 나이, 2번 위치 , 3번 자세한 문의, 4번 상담원 연결을 눌러주세요")    
Info = int(input("궁금한 사항이 있으시면 숫자를 눌러주세요?"))


if Info == 1:
    print("3세 이상 부터 8세 미만입니다.")
elif Info == 2:
    print("오시는 길은 문자로 보내드렸습니다.")
elif Info == 3:
    print("자세한 문의사항은 전화주세요.")
else:
    Info == 4
    print("전화 드리겠습니다..")
    
    # And 연산 양쪽 모두 True여야 함
    
    True and True == True
    False and True == False
    True and False == False
    False and False == False
    
    # Or 연산자 한쪽만 True여도 괜찮음
    
    True or True == True
    True or False == True
    False or True == True
    False or False == False
    
    