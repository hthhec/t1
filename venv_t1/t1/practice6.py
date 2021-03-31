#if

weather = "비"
#weather = input("오늘날씨는?")
if weather == "비" or weather == "눈":
    print("우산챙겨")
elif weather == "미세먼지":
    print("마스크챙겨")
else:
    print("필요X")


#temp = int(input("기온은?"))
temp = -50000
if 30<= temp:
    print("덥누")
elif 10<=temp and temp <30:
    print("외투")
else:
    print("영도절대영도최영도")

#반복문

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}" .format(waiting_no))

#randrange()
for waiting_no in range(5):
    print("대기번호 : {0}" .format(waiting_no))

for waiting_no in range(1,6):
    print("대기번호 : {0}" .format(waiting_no))



starbucks = ["아이언맨" , "토르" , "그루트"]

for customer in starbucks:
    print("{0}, 커피 준완".format(customer))

#while
customer = "토리"
index = 5
while index >=1:
    print("{0}, 커피 준완, {1}번 남았어요" .format(customer,index))
    index -= 1
    if index==0:
        print("커피버림")

customer = "언맨"
index = 1
# while True:
#     print("{0}, 커피 준완, {1}번 째 말하는 중" .format(customer,index))
#    index += 1


customer = "토르"
person = "unknown"

# while person != customer:
#     print("{0}, 커피 준완" .format(customer))
#     person = input("이름이?")

#contunue, break

#한줄 for
#students = [i+100 for i in students]


# quiz

from random import *
cnt = 0 # 총 탑승 승객

for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분" .format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분" .format(i,time))

print("총 승객 {0}" .format(cnt))

