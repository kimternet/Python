def tax_cal(money):
    return money  * 0.35  #  함수안에서 return으로 받은 인자를 계산하고
    
def pay_tax(tax):         #  두번째 함수에 출력을 해준다.
    print("감사합니다",tax)





to_pay = tax_cal(10000)  # 첫번째 함수에 인자 입력
pay_tax(to_pay)  # return으로 계산된 값이 두번째 함수를 통해 출력


#  == 실습 ==

def me(money):
    return money * 1.13

def you(money2):
    print("감사합니다",money2,"잘 전달 받았습니다.")


to_pay = me(100000)
you(to_pay)

# 궁금한점
# 이렇게 함수를 두개로 분할해서 사용하는 이유?

# 1. 재사용성   -> 예로 me 라는 함수를 다른 곳에 가져다 쓸 수 도 있다
# 2. 유지 보수  -> 계산이 수정되거나 값의 조절이 필요할 때 me 함수만 수정하거나 you함수만 수정하면 된다.
# 3. 가독성 -> 함수들의 각 기능을 보기 편하게 함으로써 가독성을 높일 수 있다.