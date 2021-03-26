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

