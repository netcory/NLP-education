#!/usr/bin/env python
# coding: utf-8

# In[5]:


keys = ["name", "height", "weight"]
values = ["정욱", "174", "69"]


a = list(zip(keys, values, [1, 2, 3]))
a


# In[8]:


keys = ["name", "height", "weight"]
values = ["정욱", "174", "69"]


a = dict(zip(keys, values, [1, 2, 3]))
a

# 에러. 딕셔너리는 애초에 키 : 밸류 쌍으로 이루어지므로 리스트 세개를 zip해서 dict로 만들 수 없음


# In[10]:


def func1(a, b):
    return a + b
    print("a와 b의 합: ", a + b) # 실행되지 않음. 함수는 return 만나면 종료됨


# In[12]:


def func1(a, b):
    print("a와 b의 합: ", a + b) #여기 와야함
    return a + b

func1(5, 1)


# In[21]:


def func2(a, b):
    for i in range(10):
        if i == 3:
            break
    return i
func2(10, 105)


# In[24]:


# 위와 사실상 같은 코드

def func2(a, b):
    for i in range(10):
        if i == 3:
            return i
func2(10, 105)


# In[26]:


a = 5

def func3():
    global a
    a = 1
    print(a)

func3()  # func3 함수를 호출했기 때문에 print(a) 결과가 1.
         # func3 함수 호출 라인이 빠지면 print(a) 결과가 5.
         # 즉, 함수 정의와 함수 호출은 다르다.
print(a)


# In[29]:


def func(a, b):
    print(a + b)
    return a + b
a = func(3, 1)


# In[34]:


def func(a, b):
    return print(a + b, '입니다.') # return과 print 같이 사용도 가능

a = func(3, 1)

print(a) # 단, print함수의 return 타입이 None이므로 return 결과는 None
         # 따라서 return과 print를 같이 사용하면 원하는 결과가 안 나올 가능성이 큼


# In[49]:


a = lambda x: [i * 10 for i in range(x)]
a(5)


# ## args, kwargs

# In[51]:


def concat(a, b, c, d): #a, b, c, d 는 인수
    return a + b + c + d
str1 = concat("가", "나", "다", "라") #가, 나, 다, 라는 인자

str1


# In[68]:


list1 = ['가', '나', '다', '라']
str2 = concat(list1[0], list1[1], list1[2], list1[3])


str3 = concat(*list1) # *를 입력하면 리스트, 튜플 등을 풀어서 넣음
str3


# In[54]:


def func(*args): # *args는 가변인수. 꼭 args라고 쓸 필요 없음. 관례적으로 쓸 뿐
    print(args)
    print(type(args)) # args는 튜플임을 알 수 있다.


# In[55]:


func(1, 2, 3, 4)


# In[56]:


def func(*x): # args가 아니라 x로 해도 같음
    print(x)
    print(type(x))
func(1, 2, 3, 4)


# In[63]:


def total(*args):
    a = 0
    for arg in args:
        a += arg
    return a
total(3, 5, 10, 2, 7, 7)


# In[73]:


def func(a, *args):
    print(a, end = " ")
    for arg in args:
        print(arg, end = " ")
func(100, 1, 2, 3, 4, 5)


# In[85]:


def total(*args):
    print(args)
    print(type(args))
    
total(*{1, 2, 3})


# ## 가변인수와 고정인수 함께 사용

# In[107]:


def func(a, b, *args): # a, b는 고정, *args는 가변.
    print(a)
    print(b)
    print('---')
    print(args)
func(1, 2, 3, 4, 5)


# In[110]:


def func(*args, a, b): # 보통 이렇게는 안쓰지만
    print(a)
    print(b)
    print('---')
    print(args)
func(1, 2, 3, a = 4, b = 5) # 이렇게 지정해주면 가능


# In[131]:


# 4장 연습문제 3
# 가변인수와 고정인수를 사용해 모든값을 더하거나 빼거나 곱하는 함수 작성
# ex)
# >>> calc("+", 1, 2, 3, 4, 5) # 1 + 2 + 3 + 4 + 5
# 15
# >>> calc("-", 1, 2, 3, 4, 5) # 1 - 2 - 3 - 4 - 5
# -13
# >>> calc("*", 1, 2, 3, 4, 5) # 1 * 2 * 3 * 4 * 5
# 120

def calc(a, *args):
    if a == '+':
        sum_ = 0
        for arg in args:
            sum_ += arg
        return (sum_)
        
    elif a == '*':
        mul_ = 1
        for arg in args:
            mul_ *= arg
        return (mul_)
        
    elif a == '-':
        sub_ = 2*args[0]
        for arg in args:
            sub_ -= arg
        return (sub_)
        
    elif a == '/':
        div_ = 1
        for arg in args:
            div_ /= arg
        return (div_)
    else:
        return
        

calc("-", 1, 2, 3, 4, 5)


# In[140]:


# 4장 연습문제 3 강사님 버젼
# 가변인수와 고정인수를 사용해 모든값을 더하거나 빼거나 곱하는 함수 작성
# ex)
# >>> calc("+", 1, 2, 3, 4, 5) # 1 + 2 + 3 + 4 + 5
# 15
# >>> calc("-", 1, 2, 3, 4, 5) # 1 - 2 - 3 - 4 - 5
# -13
# >>> calc("*", 1, 2, 3, 4, 5) # 1 * 2 * 3 * 4 * 5
# 120


def calc(oper, *args):
    initial = args[0]
    if oper == '+':
        for i in args[1:]:  #[:] 같은 인덱스 슬라이싱은 꼭 기억할 것. 자주 씀.
            initial += i
        
    elif oper == '-':
        for i in args[1:]:
            initial -= i
        
    elif oper == '*':
        for i in args[1:]:
            initial *= i
        
    elif oper == '/':
        for i in args[1:]:
            initial /= i
        
    else:
        print("연산자 오류")
        return
    return initial
    
calc("-", 1,0)


# In[130]:


def calc(*x):
    maximum = x[0]
    minimum = x[0]
    total = 0
    average = 0
    for i in x[1:]:
        if i > maximum:
            maximum = i
    for j in x[1:]:
        if j < minimum:
            minimum = j
    for k in x:
        total += k
        average = total/len(x)
    print ("최대값: {}, 최소값: {}, 평균값: {}".format(maximum, minimum, average))
    
calc(-1, 3, 17, 0, 2)


# In[143]:


def func(name, city, height):
    print("이름은 {} 도시는 {} 키는 {}".format(name, city, height))
    return {
        "name": name,
        "city": city,
        "height": height
    }
          
profile = func("최정욱", "고양", 174)
profile


# In[145]:


my_profile = {
    'city' : '고양',
    'name' : '최정욱',
    'height' : 170
    }

func(**my_profile) # 딕셔너리를 별표 하나로 풀면 리스트가 되고
                   # 그 리스트를 다시 별표 하나로 풀면 하나 하나의 인자가 됨
                   # 따라서 별표 두개를 붙여 입력해야 함


# In[148]:


def func2(**kwargs): # kwargs(키워드 아규먼츠)는 관례적으로 많이 쓰는 표현.
    print(kwargs)
    print(type(kwargs))

func2(name = '최정욱', hometown =  '서울')
# 딕셔너리를 별표 두번으로 받음. 즉 키워드로 나눠서 받음


# ## quiz: kwargs로 인자를 입력받아 본인의 profile을 출력하는 함수 작성
# ## ==> 이름은 {} 도시는 {} 고향은 {}
# 
# ## (name, city, hometown) + name이 입력받지 않으면 Tom, City가 입력받지않으면 Seoul, hometown이 입력받지 않으면 "Busan"
# 
# ## def create_profile(**kwargs):
# ##       ~~~
# ## create_profile(name='최정욱', city='Goyang', hometown = 'Seoul') ==> 결과: "이름은 최정욱 도시는 Goyang 고향은 Seoul

# In[153]:


def create_profile(**kwargs):
    # 방법1
   # kwargs.setdefault("name", "Tom")
   # kwargs.setdefault("city", "Seoul")
   # kwargs.setdefault("hometown", "Busan")
   # name = kwargs['name']
   # city = kwargs['city']
   # hometown = kwargs['hometown']

    # 방법2
    #if 'name' not in kwargs:
    #    kwargs['name'] = 'Tom'
    # if 'city' not in kwargs:
    #    kwargs['city'] = 'Seoul'
    # if 'hometown' not in kwargs:
    #    kwargs['hometown'] = 'Busan'
    # name = kwargs['name']
    # city = kwargs['city']
    # hometown = kwargs['hometown']
    
    # 방법 3
    # name = kwargs.get('name', 'Tom')
    # city = kwargs.get('city', 'Seoul')
    # hometown = kwargs.get('hometown', 'Busan')
    
        
    print("이름: {}, 도시: {}, 고향: {}".format(name, city, hometown))
    return {
        'name': name,
        'city': city,
        'hometown' : hometown
    }
p = create_profile(name="최정욱", city="고양", hometown="서울")


# ## default value

# In[161]:


def create_profile(name, city, email):
    return {
        'name' : name,
        'city' : city,
        'email' : email
    }

profile = create_profile('정욱', 'Seoul', 'netcory@gmail.com')
profile


# In[164]:


def create_profile(name, city, email='netcory@gmail.com'):
    #예를 들어 자료가 너무 많은 경우 인자 입력할 때부터 기본값을 미리 설정해줌
    return {
        'name' : name,
        'city' : city,
        'email' : email
    }

profile = create_profile('정욱', 'Seoul')
#이메일을 입력하지 않아도 기본값을 설정해줬기 때문에 출력됨
#기본값과 다른 이메일을 입력해주면 입력한 그 이메일로 바뀌어서 출력


# In[169]:


def create_profile(name, city = "Busan", email = 'netcory@gmail.com'):
    return {
        'name' : name,
        'city' : city,
        'email' : email
    }
create_profile("정욱", city ="고양") # 됨


# In[170]:


def create_profile(name, city = "고양", email):
    return {
        'name' : name,
        'city' : city,
        'email' : email
    }
create_profile("정욱", 'netcory@gmail.com') # 안됨


# In[181]:


def last_func(name, email, addr = None, age = 20, *args, **kwargs):
    print("name : ", name)
    print("email: ", email)
    print("age: ", age)
          
    if addr is None:
          addr = "서울"
    print('addr: ', addr)
          
    print('-'*10, 'args 시작')
    for arg in args:
          print(arg)
          
    print('-'*0, 'kwargs 시작')
    for key in kwargs:
          print(key, kwargs[key])
          
last_func("정욱", "netcory@gmail.com", age = 20, 1, 2, 3, 4, 5, 'hi', language = 'python', birth = '0102', is_korean=True)


# In[183]:


# 4장 연습문제 4

def calc(*x):
    maximum = x[0]
    minimum = x[0]
    average = 0
    total = 0
    for i in x:
        if i > maximum:
            maximum = i
    for j in range(len(x)):
        if x[j] < minimum:
            minimum = x[j]
    for k in x:
        total += k
        average = total/len(x)
    print ("최대값: {}, 최소값: {}, 평균값: {}".format(maximum, minimum, average))
    
calc(-1, -2, -3, -4, -5)


# In[187]:


# 4장 연습문제 4

def calc(*x):
    maximum = x[0]
    minimum = x[0]
    average = 0
    total = 0
    for i in x:
        if i > maximum:
            maximum = i
    for j in x:
        if j < minimum:
            minimum = j
    for k in x:
        total += k
        average = total/len(x)
    print ("최대값: {}, 최소값: {}, 평균값: {}".format(maximum, minimum, average))
    
calc(-50, 0, 1020, -305, 50, 1.5, -1000.33, 5215.27)


# In[190]:


# 4장 연습문제 4 강사님 버젼

def calc(*args):
    
    minimum = args[0]
    maximum = args[0]
    total = args[0]
    
    for i in args:
        if i < minimum :
            minimum = i
        if i > maximum:
            maximum = i
        total += i
    average = total / len(args)
    
    print("최대값: {}, 최소값: {}, 평균값: {}".format(maximum, minimum, average))
    
calc(-1, -2, -3, -4, 5)


# # 5장. 객체와 클래스

# In[199]:


class Dog:  # Dog라는 클래스 생성
    def __init__(self, name, color):  # __init__ : Constructor 생성자,
                                      # 객체가 생성될 때 호출되어야 하는 함수
                                      # self 는 instance 자기 자신. 무조건 써 줘야 함
        self.name = name
        self.color = color            # name, color를 입력 받아 초기화
        self.hungry = 0
            
    def eat(self):
        self.hungry -= 10
        print("밥먹음 ", self.hungry)
        
    def walk(self):
        self.hungry += 10
        print("산책 ", self.hungry)
        
choco = Dog("choco", "black")  # choco라는 객체 생성
                               # Dog 의 __init__ 호출, 호출하는데 choco, black 두 개 인자를 넣음
print(choco.name)
print(choco.color)
print(choco.walk())
print(choco.eat())


# ## 접근지정자 private attribute

# In[276]:


class Dog:
    def __init__(self, name, color):  
                                      
        self.name = name
        self.color = color           
        self.__hungry = 0   # 언더바 두개를 붙임. 외부에서 접근 못하게 함.
                            # 클래스 외부에서 self.__hungry를 접근 못함
            
    def eat(self):
        self.__hungry -= 10
        print("밥먹음 ", self.__hungry)
        
    def walk(self):
        self.__hungry += 10
        print("산책 ", self.__hungry)
        
        
jjong = Dog('jjong', 'white')
choco = Dog('choco', 'black')


# In[320]:


choco.walk()


# ## 클래스 속성

# In[321]:


class Dog:
    
    count = 0 # 클래스 속성. 모든 객체가 공유하는 속성
    
    def __init__(self, name, color):
        self.name = name
        self.color = color           
        self.__hungry = 0
        Dog.count += 1  # 객체 강아지를 만들 때마다 하나씩 세겠다
                                        
    def eat(self):
        self.__hungry -= 10
        print("밥먹음 ", self.__hungry)
        
    def walk(self):
        self.__hungry += 10
        print("산책 ", self.__hungry)
        
        


# In[322]:


jjong = Dog('jjong', 'white')
choco = Dog('choco', 'black')


# In[327]:


Dog.count # Dog 몇 마리 만들었는지


# ## 정적 메서드 (static method) & 클래스 메서드 (class method)

# In[337]:


class Dog:
    count = 0
    dog_list = []
    
    @staticmethod
    def intro(name):
        print("{}님 동물의 숲에 오신 것을 환영합니다.".format(name))
        
    @classmethod
    def create_dog(cls, name, color):
        cls.count += 1
        dog = cls(name, color)
        cls.dog_list.append(dog)
        return cls(name, color)
    
    def __init__(self, name, color):  
        self.name = name
        self.color = color           
        self.__hungry = 0
            
    def eat(self):
        self.__hungry -= 10
        print("밥먹음 ", self.__hungry)
        
    def walk(self):
        self.__hungry += 10
        print("산책 ", self.__hungry)


# In[338]:


jjong = Dog.create_dog("jjong", "white")
choco = Dog.create_dog("choco", "black")


# In[339]:


Dog.intro("최정욱")


# In[340]:


Dog.dog_list


# In[ ]:





# In[330]:




