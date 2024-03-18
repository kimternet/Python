
def plus(a , b):     # a = 0 , # b =0  초기값을 0으로 설정해주면 오류를 방지해 줄 수 있다.
    print(a + b)

def minus(a , b):
    print(a - b)
    
def multiple(a , b):
    print(a * b)

def division(a , b):
    print(a / b)


plus(1,1)
min(5,2)
multiple(2,4)
division(4,2)

# 두 코드 사이의 주요 차이점은 함수 매개변수의 기본값 설정에 있다. 
# 첫 번째 plus 함수는 매개변수 a와 b에 기본값 0을 할당 
# 이렇게 하면 함수가 인자 없이 호출될 때 오류를 방지하고, 
# a와 b가 제공되지 않았을 경우에도 함수가 정상적으로 0 + 0 = 0을 출력할 수 있게 한다. 
# 반면, 두 번째 plus 함수는 매개변수에 기본값을 설정하지 않았기 때문에, 
# 이 함수는 반드시 두 개의 인자를 필요로 한다. 
# 인자가 누락되면 파이썬은 오류를 발생시킬 것