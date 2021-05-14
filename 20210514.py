#!/usr/bin/env python
# coding: utf-8

# ## 5장

# #연습문제 1
# Car 클래스를 만드세요
# 객체 생성시 차이름, 배기량, 생산년도 입력받으세요
# 객체 생성시 등록된 차이름, 배기량, 생산년도는 직접 변경하지 못합니다
# 
# 차 이름을 변경하는 함수를 만드세요
# 
# 배기량에 따라 1000CC 이하 소형
#                       1000CC 초과 2000CC 이하 중형
#                       2000CC 초과 대형을 출력하는 함수를 만드세요
#                       
# 객체 생성시마다 등록된 차량 갯수를 기록해주세요
# 
# 총 등록된 차량개수를 출력하는 클래스 함수를 만드세요. (= 클래스 메소드를 만드세요)
# 
# ** 조건 추가:
# 1. 객체의 name과 배기량, 생산년도를 반환하는 get 함수를 만드세요.   ex) def get_name(self)//def get_cc(self) // def get_prod_year(self)
# 
# 2. speed라는 인스턴스 속성 만드시고, excel이라는 메소드가 speed를 증가시키고, break_라는 메소드는 speed를 감소시키도록 하세요.

# In[58]:


#나 혼자 시도

class Car:
    
    car_count = 0
    
    def __init__(self, name, cc, year):
        self.__name = name
        self.__cc = cc
        self.__year = year
        Car.car_count += 1
    
    def name_change(self, new_name):
        self.__name = new_name
        
    def size(self):
        if __cc < 1000:
            print("소형입니다.")
        elif 1000 <= __cc < 2000:
            print("중형입니다.")
        else:
            print("대형입니다.")
    
    def Carcount(self):
        print("총 등록된 차량개수는 {}대 입니다.".format(Car.car_count))
            

sm3 = Car("sm3", 2000, 2011)
g80 = Car("g80", 3500, 2018)

sm3.name_change("sm5")


# In[173]:


#강사님 버젼
#클래스메소드는 self가 아니라 cls ==> 모든 객체에 적용됨
#인스턴스메소드는 self ==> 각각의 객체 하나하나에 적용


class Car:
    
    count = 0
    
    def __init__(self, name, cc, year):
        self.__name = name
        self.__cc = cc
        self.__year = year
        self.__speed = 0
        Car.count += 1
    
    @classmethod
    def get_car_count(cls):
        print("{}개의 차 등록".format(cls.count))
        return cls.count
            
    def update_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_cc(self):
        return self.__cc
    
    def get_prod_year(self):
        return self.__year
    
    def get_size(self):
        if self.__cc <= 1000:
            size = "소형"
        elif self.__cc <= 2000:
            size = "중형"
        else:
            size = "대형"
        print("{}은 {}".format(self.__name, size))
        return size
    
    def excel(self):
        self.__speed += 10
        if self.__speed > 200:
            self.__speed = 200 #임의로 최고속도 제한
        print("가속", self.__speed)
        return True
        
        
    def break_(self):
        self.__speed -= 10
        if self.__speed <0:
            self.__speed = 0 #속도는 0이 최저
        print("감속", self.__speed)
        return True
        

car = Car("소나타", 2000, 2012)


# In[174]:


Car.get_car_count() #get_car_count는 클래스 메소드이기 때문에 클래스(Car)로 호출


# In[175]:


car.update_name("붕붕이")


# In[176]:


car.get_name()


# In[177]:


car.get_size()


# In[178]:


car.get_prod_year()


# In[179]:


car.get_cc()


# In[180]:


car.get_name()


# In[185]:


car.break_()


# In[190]:


car.excel()


# In[200]:


car.break_()


# ## 부록. 변수이름, 클래스이름 (파이썬 유저들의 암묵적인 룰)

# In[62]:


car_list = []


# In[63]:


class Car:
    pass


# In[64]:


class SportsCar(Car):
    pass


# In[ ]:


def set_car_name(name):
    pass


# In[34]:


#결론
#클래스 이름은 맨 앞을 대문자, 여러 단어인 경우 단어 첫글자마다 대문자 (카멜 케이스)
#변수, 함수 이름은 다 소문자로 하고 띄어쓰기는 언더바로 대신하자 (스네이크 케이스)


# ## 상속 (객체지향 언어의 핵심 개념)
# ## 부모 클래스로부터 속성(과 함수)를 물려받음

# In[205]:


class Animal:
    
    def __init__(self):
        self.hungry = 0
    
    def eat(self):
        self.hungry -= 10
        print("밥먹음", self.hungry)
    
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)
        
        
class Dog(Animal):
    
    def __init__(self):
        super().__init__()  # 부모 클래스의 init 메소드를 호출
                            # 즉 self.hungry = 0 으로 시작
    def sound(self):
        print("멍멍")
        
class Cat(Animal):
    
    def __init__(self):
        super().__init__()
    
    def sound(self):
        print("야옹")


# In[206]:


dog = Dog()
cat = Cat()


# In[207]:


dog.walk()


# In[208]:


dog.sound()


# In[209]:


dog.eat()


# In[210]:


cat.sound()


# In[211]:


cat.eat()


# In[213]:


animal = Animal()
animal.sound()  # Animal 클래스에는 sound 속성이 없으므로 에러


# ## 추상클래스 (abstract class) 1 (최신 방법)

# In[227]:


from abc import *
# abc 는 abstract class 의 약자
# abc 라는 패키지(모듈)에서 import 뒤에 있는 ? 라는 모듈(함수, 클래스, 변수)를 불러온다 사용한다.
# * 를 쓴 건 abc 안의 모든 모듈을 부르는 것


# In[228]:


class Animal(metaclass = ABCMeta):
    #Animal 클래스는 metaclass = ABCMeta 로부터 상속 받음
    #ABCMeta는 abc라는 패키지 안에 있는 모듈 중 하나
    
    def __init__(self):
        self.hungry = 0
    
    def eat(self):
        self.hungry -= 10
        print("밥먹음", self.hungry)
    
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)
    
    @abstractmethod
    def sound(self):
        pass


# In[231]:


a = Animal()


# In[234]:


class Dog(Animal):
    pass


# In[240]:


dog = Dog() #실행하면 sound 함수 재정의 안돼있다고 에러 떠야함 (뭐가 잘못됐지?)


# In[237]:


class Dog(Animal):
    def sound(self):
        print("왈왈")


# In[238]:


dog = Dog()


# In[239]:


dog.sound()


# ## 부록.decorator

# In[250]:


def generate_something(f):
    def wrap():
        print("wrap 호출")
        f()
        print("wrap 종료")
    return wrap


# In[251]:


def func1():
    print("func1 start")
    print("func1 end")


# In[252]:


a = generate_something(func1)
a()

#def wrap():
#        print("Wrap 호출")
#        func1()
#        print("Wrap 종료")


# ## 추상클래스 (abstract class) 2 (옛날 방법)

# In[217]:


class Animal:
    
    def __init__(self):
        self.hungry = 0
    
    def eat(self):
        self.hungry -= 10
        print("밥먹음", self.hungry)
    
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)
        
    def sound(self):
        raise NotimplementedError("sound 함수를 재정의하셔야 합니다.")
        # 객체에서 sound 쓰려면 재정의해라


# In[218]:


class Dog(Animal):
    pass


# In[219]:


dog = Dog()


# In[223]:


dog.sound()


# In[224]:


class Dog(Animal):
    def sound(self):
        print("왈왈")


# In[226]:


dog = Dog()
dog.sound()


# ## 다중상속. (원래 교육 내용은 아닌데 질문 받아서)

# In[254]:


class Animal(object):
    
    def __init__(self):
        self.hungry = 0
        
    def eat(self):
        print("음식을 먹습니다.")
        self.hungry += 10
        


# In[255]:


class Fliable(object):
    def fly(self):
        print("비행하다.")


# In[256]:


class Vehicle(object):
    def __init__(self, speed):
        self.speed = speed


# In[257]:


class Bird(Animal, Fliable): #파이썬은 두 클래스 상속 받을 수 있음
    def __init__(self):
        super().__init__()


# In[262]:


# 1. 다중상속이 되나요?
bird = Bird()
bird.eat() #Animal 상속받아서 eat 가능


# In[263]:


bird.fly() #Fliable도 상속받아서 fly 가능


# In[ ]:


class Fliable(object):
    def fly(self):
        print("비행하다.")
        
    def eat(self): # Animal 에도 eat 이 있는데 Fliable에도 추가해 봄(파이썬은 가능)
        print("날 수 있는 에너지 공급")


# In[266]:


bird.eat() # Bird(Animal, Fliable) 에서 먼저 나온 Animal을 상속함


# ## 6장. 예외처리

# In[267]:


10 / 0 #zerodivisionerror


# In[270]:


profile = {
    'name': "정욱"
}


# In[276]:


profile['city'] #keyerror


# In[280]:


try:
    #코드
    a = 10 / 0
    print("try 문 실행 종료")
    
    # 만약 에러 발생하면 다 무시하고 except문으로 가라
    # 만약 에러 아니면 except 문은 무시해
    
except:
    #예외 처리
    a = 10 /1
    print("except문 실행 종료")

print(a)


# ## try, except [Exception]

# In[285]:


a = [1, 2, 3]

profile = {
    'name': "정욱",
    'city': "고양"
}

try:
    10 / 0
  
    
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")


# In[291]:


a = [1, 2, 3]

profile = {
    'name': "정욱",
    'city': "고양"
}

try:
    print(a[4])
    
except IndexError:
    print("a의 len은 {}입니다.".format(len(a)))


# In[292]:


a = [1, 2, 3]

profile = {
    'name': "정욱",
    'city': "고양"
}

try:
    profile['hometown']
  
    
except KeyError:
    print("hometown not in profile.")


# In[295]:


a = [1, 2, 3]

profile = {
    'name': "정욱",
    'city': "고양"
}

try:
    10 / 0
    
except IndexError:
    print("a의 len은 {}입니다.".format(len(a)))
  
except KeyError:
    print("hometown not in profile.")
    
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    
except E


# ## 예외 발생시키기 (raise) ***중요함***

# In[297]:


raise IndexError("index 메시지")


# In[298]:


raise Exception ("예외 발생")


# In[300]:


# Error class 정의
# 모든 에러는 Exception을 상속 받음

class CustomError(Exception): #Exception을 상속 받음
    pass


# In[302]:


raise CustomError("메시지") #에러도 클래스로 관리함을 알 수 있다.


# In[303]:


try:
    raise CustomError("메시지")
    
except CustomError:
    print("예외처리")


# ## 7장. 모듈과 패키지

# In[304]:


#모듈은 일종의 파이썬 파일


# In[308]:


import calc #스파이더로 쥬피터 있는 폴더(CJW)에 내가 calc.py 파일 저장했음


# In[310]:


calc.name


# In[311]:


calc.add(3, 5)


# In[312]:


calc.sub(3, 5)


# In[313]:


#모듈이 여러개 있다면 폴더로 존재할 것이고 그 폴더를 패키지라고 함
#모든 모듈, 패키지를 포함하는 단어를 라이브러리 라고 하는 것


# In[314]:


import practice


# In[2]:


import calc


# In[1]:


import calc


# In[1]:


import calc


# In[1]:


import mylib


# In[2]:


mylib.calc.add(3, 5)


# In[1]:


__name__ = '__main__'


# In[2]:


__name__


# ## 이렇게 파이썬 기초 강의는 마무리
# ## 가장 중요한 건 if, for 문 사용하는 것과 논리를 세우는 것이니
# ## 그 연습 많이 할 것

# ## 파이썬 최종 점검 연습문제 1
# **피보나치 수열 
# 사용자로부터 숫자 n을 입력 받아서
# 피보나치 수열의 n번째 값을 출력하여라.
# 
# 피보나치 수열: A_n 
# 
# 예) 입력: 7 => 13이 출력

# In[5]:


a = [1, 1]

def A_n(n):
    
    for i in range(2, n):
        a.append(a[i-1] + a[i-2])

    return(a[n-1])

A_n(5)


# In[16]:


# 피보나치 수열 강사님 버젼

def fibonacci(n):
    n1 = 1
    n2 = 1
    result = n2
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    for i in range(n-2):
        result = n1 + n2
        n1 = n2
        n2 = result
    return result

fibonacci(7)
        


# In[22]:


# 피보나치 재귀적으로 푸는 방법. 단점 느리다. for문이 계속 돌기 때문.

def fibonacci2(n):
    
    if n == 1 or n == 2:
        return 1
    
    return fibonacci2(n-1) + fibonacci2(n-2) #자기 자신을 호출. 재귀함수
    
fibonacci2(7)


# ## 파이썬 최종 점검 연습문제 2
# **오른쪽 수열은 ‘개미수열’이라고 불립니다.
# 사용자로부터 n값을 입력받아서 n번째 위치에 있는 수열을 출력하시오.
# 

# In[ ]:




