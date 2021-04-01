#class

# m_name = '마린'
# m_hp = 40
# m_damage = 5

# print("{0} 유닛이 생성" .format(m_name))
# print("체력 {0}, 공격력 {1}".format(m_hp,m_damage))

# t_name = '탱크'
# t_hp = 140
# t_damage = 35

# print("{0} 유닛이 생성" .format(t_name))
# print("체력 {0}, 공격력 {1}".format(t_hp,t_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적을 공격. 공격력 {2}" .format(name,location, damage))

# attack(m_name, "1시" , m_damage)
# attack(t_name, "1시" , t_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성" .format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

m1 = Unit("마린1", 40 , 5)
m2 = Unit("마린2", 40 , 5)
t1 = Unit("탱크1", 150 , 35)



# __init__

# 멤버변수


wraith1 = Unit("레이스1" , 80 ,5 )
print("유닛이름 : {0}, damage : {1}" .format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스2" , 80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹상태" .format(wraith2.name))



#메소드

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성" .format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 공격 [공격력 {2}]" 
        .format(self.name , location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 받음" .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} " .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 파괴됨" .format(self.name))


firebat1 = AttackUnit("파이어뱃", 50,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)



#상속

#class AttackUnit(Unit):



# 다중상속

#class flyable:

#class FlyableAttackunit(AttackUnit, Flyable):



#메소드 오버라이딩
