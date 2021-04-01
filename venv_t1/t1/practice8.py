#표준입출력

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))


#다양한 출력 포맷
print("{0:_<+10}".format(500))
print("{0:,}".format(197430312974398701))

#파일입출력
# score_file = open("score.txt", "w" , encoding="utf") #쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a" , encoding="utf") #덮어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
#score_file.close()


score_file = open("score.txt", "r" , encoding="utf") 
#print(score_file.read())
#score_file.close()

# print(score_file.readline()) #줄별로 읽기
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
#score_file.close()

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()


#pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "취미" : ["축구","농구","골프"]}
# print(profile)
# pickle.dump(profile, profile_file) 
# profile_file.close()

#with
# #close 할 필요 없다
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있댜")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#quiz

for i in range(1,51):
    with open(str(i)+"주차.txt" , "w" , encoding="utf8") as report_file:
        report_file.write(" {0}주차 주간보고 \n".format(i))
        report_file.write("이름 : ")