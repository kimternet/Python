
#문자열에 변수 넣기

my_name = "kim"
my_age = 12
my_color_eyes ="black"

print(f"hello I'm {my_name}, I have {my_age} years in te earth, {my_color_eyes} is my eye color")

# !!! Important
# *   f 필수   *


# 주스 기계 만들기


def make_juice(fruit):
    return f"{fruit}+juice"

def add_ice(juice):
    return f"{juice}+ice"

def add_sugar(iced_juice):
    return f"{iced_juice}+sugar"


juice = make_juice("apple")           # 1. 먼저 과일을 넣은 주스를 만든다.

cold_juice = add_ice(juice)           # 2. 과일 넣어 만든 주스에 얼음을 넣는다
perfect_juice = add_sugar(cold_juice) # 3. 주스와 얼음을 넣은 음료에 설탕을 넣는다

print(perfect_juice)    # 주스가 완성이 된다.



