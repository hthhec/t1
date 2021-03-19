#연산자
print(1+1)
print(6/3)
print(2**3)
print(5%3) #나머지
print(10//3 , "\n") #몫

print(10 >3) #true
print(4 <= 5)
print(3 == 3)
print(3 != 2,  "\n")

print((3>0) and (3<5))
print((3>0) & (3<5))
print((3>0) or (3 >=5))
print((3>0) | (3 >=5))
print(5>4>3 , "\n")

#수식
number = 2+3*4
print(number)
number += 2
print(number)

#숫자 처리 함수
#abs, pow, max, min, round 
print(abs(-5)) #절대값
print(pow(4,2)) #제곱
print(round(3.1))
print(round(4.6))

from math import *
print("\n", floor(4.9)) #내림
print(ceil(3.1)) #올림
print(sqrt(16) , "\n")


#랜덤함수
from random import *

print(random()) # 0~1 사이 랜덤
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) +1 )


print(int(random() * 45) +1 )
print(randrange(1,46)) # 1부터 46 미만의 값
print(randint(1,45) , "\n") # 1이상, 45 이하의 값


#quiz
from random import *
date = randrange(4,32)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
