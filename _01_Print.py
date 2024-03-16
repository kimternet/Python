# chapter 02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : www.python-course.eu/python3_formatted_output.php

# 기본 출력
print('python Start!')
print("Python Start!")
print('''python start!''')
print("""python start""")
print()



# separator 옵션

print('P', 'Y', 'T','H', 'O', 'N', sep = '|') # 원하는 옵션으로 출력시 sep
print('010', '7777', '1234', sep='-')
print('python','google.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web site')
print()

#file 옵션

import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용 (d, s, f)  # 숫자, 문자열, 소수

print('%s %s'% ('one','two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one','two'))

print()

# %s

print('%10s' % ('nice')) # 10개의자릿수  , 양수는 오른쪽부터
print('{:>10}'.format('nice'))

print('%10s' % ('nice')) # 음수의 경우 왼쪽부터
print('{:10}'.format('nice'))  


print('{:_>10}'.format('nice')) # 공백을 원하는 문자로 채움
print('{:^10}'.format('nice')) # 중앙 정렬

print('%.5s' % ('pythonstudy')) # . <- 절삭
print('%5s' % ('pythonstudy'))  # . <- 절삭없으니 문자 전체가 출력
print('{:10.5}'.format('pythonstudy'))





