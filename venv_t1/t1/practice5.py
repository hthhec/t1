#리스트 []
# 순서를 갖고있는 객체의 집합

#지하철 칸별로 10명, 20명, 30명

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호가 몇번째 칸?
print(subway.index("조세호"))

#하하가 다음 정류장에 탐
subway.append("하하")
print(subway)

#정형돈 유재석 / 조세호 사이에 탐
subway.insert(1,"정형돈" )
print(subway)

# 지하철 사람을 뒤에서 한명씩 꺼냄
# print(subway.pop())
# print(subway)

# print((subway.pop())*3)
# print(subway)

# print(subway.pop())
# print(subway)

# cntrl + / 여러 줄 주석

subway.append("유재석")
print(subway)

print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
#print(num_list.clear())

num_list.clear()
print(num_list)


#다양한 자료형 함께사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

#list 확장
num_list = [5,2,4,3,1]

num_list.extend(mix_list)
print(num_list)

print("\n\n")


#사전

cabinet = {3:"유재석" , 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])

print(cabinet.get(5))
print(cabinet.get(5 , "사용가능"))
print("HI")

print(3 in cabinet) # true
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석" , "B-100" : "김태호"}
print(cabinet["A-3"])

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)


# 튜플 - 리스트와 다르게 내용 변경이나 추가가 불가능 
# 속도가 리스트 보다 빠름

menu = ("돈까스" , "치즈가스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")

name = "김종국"
age = 20
hobby = "codding"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# set (집합)
# 중복 안됨, 순서가 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호" , "양세형"}
python = set(["유재석" , "박명수"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java 까먹음
java.remove("김태호")
print(java)



#자료구조의 변경
menu = {"커피" , "우유" , "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# quiz

from random import *

# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)

# print(sample(lst,1))

users = range(1,21)
print(type(users))
users= list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("당첨자발표")
print("치킨 : {0}" .format(winners[0]))
print("커피 : {0}" .format(winners[1:]))
