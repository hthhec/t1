#문자열

sentence = '나는 소년'
print(sentence)

sentence2 = "파이썬 !~!"
print(sentence2)

sentence3 = """오오
오이
이이"""
print(sentence3 , "\n")


#슬라이싱
jumin = "940228-1023456"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0이상 2미만
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6] ) #처음부터 6미만까지
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤에부터 count) : " + jumin[-7:])


#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # lower, upper
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n") #몇번쨰에 글자가 위치하고 있는지
print(index)

index = python.index("n", index +1)
print(index)

print(python.find("Java")) #값이 없을때는 -1 을 반환
#print(python.index("Java")) # 오류 나면서 안됨

print(python.count("n"))
print()


#문자열 포맷
print("a"+"b")
print("a","b")

#방법1
print("나는 %d 살입니다." %24)
print("나는 %s 살입니다." %24)

print("나는 %s이 좋아." %"파이썬")
print("Apple 은 %c 로 시작"  %"A")

print("나는 %s, %s색이 좋아." %("빨","파 "))

#방법2
print("나는 {}살 이다." .format(20))
print("나는 {}, {}색이 좋아." .format("파","빨"))

print("나는 {0}, {1}색이 좋아." .format("0파","1빨"))
print("나는 {1}, {0}색이 좋아." .format("0파","1빨"))


#방법3
print("나는 {age}, {color}색이 좋아." .format(age = 20, color="빨깡"))
print("나는 {age}, {color}색이 좋아." .format(color="빨깡", age = 20))

#방법4
age = 20
color = "red"
print(f"나는 {age}, {color}색이 좋아.")

#탈출문자
print("호로 줄바꿈\n 뿅 ! ")
print("저는 \"나도코딩\" 입니다")
print("저는 '나도코딩' 입니다")
print('저는 나도코딩 입니다')

# \\ : 문장내에서 \
#print("D:\회사\스터디\python\py6\t1")
print("D:\\회사\\스터디\\python\\py6\\t1")

# \r : 커서를 맨앞으로 -> ??? 덮어쓰끼까지 하는듯
print("RED APPLE\rPine")

# \b 백스페이스(한글자삭제)
print("redd\b apple")

# \t (tab)
print("red \t ap")
print("")

#퀴즈

domain = "http://naver.com"
r1 = domain[7:]
r2 = r1[:5]
r3 = len(r2)
r4 = r2.count("e")

#print("r2[:3]"+"r3"+"r4"+"!")
print(str(r2[:3])+str(r3)+str(r4)+"!")

#답
url = "http://naver.com"

my_str = url.replace("http://" , "") #규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] #규칙 2
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다. " .format(url, password))


