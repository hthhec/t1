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