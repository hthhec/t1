#함수

def open_account():
    print("새로운 계좌 생성")

open_account()

def deposit(balance, money): #압금
    print("입금이 완료 잔액은 {0}원" .format(balance + money))
    return balance+ money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료 잔액은 {0}원" .format(balance - money))
        return balance - money
    else:
        print("출금X 잔액은 {0}원" .format(balance))
        return balance


def withdraw_night(balance,money): #저녁출금
    commision = 100 #수수료 
    return commision, balance-money - commision

balance = 0
balance = deposit(balance,1000)
print(balance)


balance = withdraw(balance,1100)
print(balance)

commision , balance = withdraw_night(balance, 500)
print("수수료 {0}won , 잔액 {1} 원" .format(commision,balance))


#기본값

#키워드값

#가변인자
#def profile(name,age,*language)

#지역변수, 전역변수


#quiz

def std_weight(height, gender):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*22

height = 175
gender = "남자"

weight = round(std_weight(height /100,gender),2)
print("키{0}, {1}, 표준몸무게{2}" .format(height,gender,weight))