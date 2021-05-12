#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2장 연습문제 6 가위바위보 게임

import random

total = 0
win_count = 0
draw_count = 0

r_dict = {
    1: "가위", 2: "바위", 3: "보"
}

user = int(input("가위(1), 바위(2), 보(3)을 입력해주세요!"))


while user in [1, 2, 3]:
    com = random.randint(1, 3)
    print("유저: {}, 컴퓨터: {}".format(r_dict[user], r_dict[com]))
    
    total +=1
    if user == com:  # draw case
        draw_count += 1
    elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com ==2): # win case
        win_count += 1
    
    user = int(input("가위(1), 바위(2), 보(3)을 입력해주세요!"))

print("게임종료 (전체: {}, 승리: {}, 무승부: {}, 패배: {})".format(total, win_count, draw_count, total-win_count-draw_count))


# In[19]:


# 2장 연습문제 7

import random

a = []
maximum = 0

for i in range(1,101):
    a.append(random.randint(1, 1000))
    
for j in a:
    if j > maximum:
        maximum = j
    
print(a)
print(maximum)


# In[21]:


# 2장 연습문제 7 강사님

import random

a = []

for i in range(100):
    num = random.randint(1, 1000)
    a. append(num)
    
    if maximum < num:
        maximum = num
        
print(a)
print(maximum)


# In[ ]:


# 2장 연습문제 8

import random

a = []

total = 0

for i in range(1,100):
    a.append(random.randint(1, 1000))

for j in a:
    total += j

print(a)
print(total)


# In[24]:


# 2장 연습문제 9 (1)

word = ["school", "game", "piano", "science", "hotel", "mountain"]

new_word = [i for i in word if len(i) >= 6]

new_word


# In[25]:


# 2장 연습문제 9 (2)

word = ["school", "game", "piano", "science", "hotel", "mountain"]

new_word2 = [len(j) for j in word]

new_word2


# In[28]:


a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

a[0].append(-10)
a[1].append(-20)
a[2].append(-30)
a.append([70,80,90])
a


# In[29]:


#2장 연습문제 9 (10인데 오타인듯)

a = [[10, 20], [30, 40], [50, 60]]
b = [[2, 3], [4, 5], [6, 7]]
c = []

for (i, j), (k, l) in zip(a, b):
    c.append([i * k, j * l])

c
    
    


# In[31]:


#2장 연습문제 9 (10인데 오타인듯) 심화 ==> 문제를 위한 문제라 따로 안해주심


# In[39]:


#2장 연습문제 10

a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(i * 2 + j + 1)
        
    
    a.append(line)
    
print(a)


# In[41]:


#2장 연습문제 10 강사님

a = []

p = 3

for i in range(3):
    line = []
    for j in range(p):
        line.append(p * i + j + 1)
            
    a.append(line)
    
print(a)


# In[ ]:


#break, continue는 필연적으로 if문과 같이 쓰일 수 밖에 없음


# In[42]:


for i in range(5):
    
    if i == 3:
        break
    print(i)


# In[43]:


for i in range(5):
    print(i)
    
    if i == 3:
        break


# In[44]:


for i in range(5):
    if i == 3:
        continue
        
    print(i)


# In[ ]:


#2장 연습문제 11 (1)
#while 문과 break 문을 사용하여 사용자가 입력한 숫자만큼 반복하여 ‘hi’ 출력하기

i = 0
a = int(input("숫자를 입력해주세요: "))

while i < a:
    print("hi")
    i += 1
    if i == a:
        break


# In[50]:


#2장 연습문제 11 (2)
#for 문과 continue 문을 사용하여 사용자가 입력한 숫자까지의 짝수를 출력하기

b = int(input("숫자를 입력해주세요: "))

for i in range(1, b):
    if i % 2 != 0:
        continue
    print(i)


# In[51]:


file = open("write_practice.txt", 'w') #w 는 wt인데 t가 생략된 것
file.write("파일에 글 쓰기 실습.")
file.close()


# In[53]:


file = open("write_practice.txt", "r") #r 은 rt인데 t가 생략된 것
content = file.read()
file.close()


# In[54]:


content


# In[ ]:


# r 읽기 모드
# w 쓰기 모드
# a append 모드
# x
# t
# b binary 혹은 byte 모드
# + +가 붙냐 안붙냐


# In[55]:


with open("sample1.txt", "w") as f:
    f.write("글쓰기 실습 \n")
    f.write("글이 써졌습니다.")
#with 절 끝나면 자동으로 close 호출해서 파일 닫아줌


# In[56]:


with open("sample1.txt", "r") as f:
    content = f.read()


# In[59]:


print(content)


# In[62]:


with open("sample1.txt", "r") as f:
    line = f.readline()
    print(line)
    print("-" * 10)
    line = f.readline()
    print(line)


# In[63]:


with open("sample1.txt", "r") as f:
    lines = f.readlines()
    print(lines)


# In[64]:


lines


# In[67]:


with open("sample2.txt", "w") as f:
    f.writelines(lines)
    
lines


# In[68]:


## rt+(r+), wt+(w+)

with open("no_exist.txt", "r") as f:
    content = f.read()
print (content)

# 없는 파일을 read 모드로 열면 당연히 에러 발생

with open("no_exist.txt", "r+") as f:
    content = f.read()
print (content)

# 마찬가지


# In[69]:


## rt+(r+), wt+(w+)

with open("no_exist2.txt", 'w') as f:
    f.write("w모드 실습")


# In[70]:


with open("no_exist3.txt", 'w+') as f:
    f.write("w+모드 실습")


# In[ ]:


# r+, w+ 쓰기모드 비교


# In[71]:


with open("no_exist2.txt", "r+") as f:
    # 
    f.write("r+")


# In[73]:


with open("no_exist3.txt", "w+") as f:
    # 기존 파일의 내용이 삭제됨.
    f.write("w+")


# In[74]:


# r+, w+ 읽기모드 비교


# In[77]:


with open("no_exist2.txt", "r+") as f:
    content = f.read()
print(content)


# In[76]:


with open("no_exist2.txt", "w+") as f:
    content = f.read()
print(content)


# In[ ]:


# a모드 - 덮어쓰지 않고 뒤에 붙여쓰는 기능


# In[78]:


with open("no_exist3.txt", "a") as f:
    f.write("\n a mode open")


# In[81]:


# a+ - 붙여 쓰면서 읽을 수도 있는 모드

with open("no_exist3.txt", "a+") as f:
    content = f.read()
print(content)


# In[85]:


with open("nex_w+.txt", "w+") as f:
    f.write("w+모드 실습입니다. \n w+ 모드")
    print(f.tell())
    #tell은 현재 커서의 위치를 알려줌. 
    f.seek(0)
    #seek은 커서 위치를 바꿔줌 (0번째로 감)
    print(f.tell())
    content = f.read()
    print(content)
    #커서를 0 위치로 바꿔주고 읽었기 때문에 내용을 읽어줌
    print(f.tell())
    #다 읽고 커서가 다시 끝으로 감


# In[86]:


#3장 연습문제 1
#14-1-12.txt 텍스트파일을 리스트로 읽어 단어 길이가 5보다 큰 단어만 나열하세요
#패스함


# In[ ]:


#3장 연습문제 2
#가위바위보 게임 업그레이드
#이전에 만든 가위바위보 게임을 총 게임횟수와 승률을 게임을 다시 실행하도 유지되도록 수정하세요
#심화 이름을 입력받아 이름별로 게임횟수와 승률을 저장해주세요
#패스함


# In[ ]:


#3장 연습문제 3
#성적관리 프로그램 개발
#패스함


# # 4장 함수

# In[92]:


#1 인자 O, 반환값 X

def intro(name):
    print("안녕하세요. {}입니다.".format(name))
    
intro("정욱")

a = intro("정욱")
print(a)
#return이 없기 때문에 None


# In[93]:


#2 인자 O, 반환값 O

def func_sum(num1, num2):
    return num1 + num2

func_sum(3,5)


# In[95]:


#3 인자 X, 반환값 X

def welcome():
    print("welcome to my service!")
    
welcome()
print(a)


# In[97]:


#4 인자 X, 반환값 O

__version__ = 3.5
def func_4():
    return __version__

func_4()


# In[109]:


# 로또 번호 추첨기

import random
def lotto_number():
    result = []
    while True:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
        if len(result) == 6:
            break
    return result
lotto_number()


# ## 전역변수 vs 지역변수

# In[112]:


a, b, c = 1, 2, 5

def func1():
    a = 3
    b = 4
    print(a)
    print(b)
    print(c)
    
func1()
print(a, b, c)


# In[116]:


def func2():
    a = 5
    b = 6
    
    func1()
    
    print("=" *10)
    print(a)
    print(b)
    print(c)
    
func2()


# In[120]:


# global 키워드

a = 1
b = 2
c = 5

def func3():
    a = 3
    b = 4
    
        
    global c #전역변수 c 를 불러
    c = 10 #전역변수 변경
    
    print(a, b, c)
    
func3()
print (a, b, c)


# In[122]:


a = 3
b = 4
c = 5

def func1():
    a = 1
    b = 2
    print(a, b)
    
def func2():
    a = 6
    b = 7
    
    func1()
    
    print(a, b)
    
print(a, b, c)
func1()
func2()


# ## decorator

# In[140]:


a = 10
b = 11
c = 12

def something():
    a = 1
    b = 2
    c = 5
    
    def sample():
        a = 3
        b = 4
        print (a, b, c) # 아래 print 다음에 출력
        
    print(a, b, c)  #먼저 만남
    sample()
    
something()


# In[148]:


a = 10
b = 11
c = 12

def something(x1, x2): 
    
    def sample(a, b):
        # print (a, b, c)
        return [a + x1, b + x2]
    
    return sample
    
new_func = something(1, 2) #x1에 1, x2에 2
#new_func (a, b) return [a +1, b + 2]

something(1, 2)

new_func(-8, 10)


# In[150]:


def func_loop(data, func):
    result = []
    for i in range(3):
        result.append(func(data))
    return result


# In[152]:


def move_pos(origin_pos):
    return [i + 10 for i in origin_pos]

origin_pos = [2, 5]

func_loop(origin_pos, move_pos)


# In[167]:


#4장 연습문제 1
#사칙연산 함수만들기
#ex) calc(5, 6)
#덧셈: 11, 뺄셈: -1, 곱셈: 30, 나눗셈: 0.8333333333333334
#a= calc(5,6)
# return Type: (덧셈결과, 뺄셈결과, 곱셈결과, 나눗셈결과)

def calc(a, b):
    print("덧셈: {}, 뺄셈: {}, 곱셈: {}, 나눗셈: {}".format(a + b, a - b, a * b, a / b))
    return (a+b, a-b, a*b, a/b)

a = calc(1,3)

type(a)


# In[176]:


#4장 연습문제 2
#해당값을 모두 찾아 위치를 리턴해주는 함수만들기
# ex)
# >>> lis = [1, 2, 3, 1, 4, 2, 1]
# >>> allindex(lis, 1)
# [0, 3, 6]
# def allinedx(a, b):

lis = [1, 2, 3, 1, 4, 2, 1]

def allindex(a, b):
    index = []
    idx = 0
        
    for i in a:
        if i == b:
            index.append(idx)
        idx += 1
                
    return index
            
    
allindex(lis, 1)


# In[181]:


#4장 연습문제 1 강사님
#사칙연산 함수만들기
#ex) calc(5, 6)
#덧셈: 11, 뺄셈: -1, 곱셈: 30, 나눗셈: 0.8333333333333334
#a= calc(5,6)
# return Type: (덧셈결과, 뺄셈결과, 곱셈결과, 나눗셈결과)


def calc(a, b):
    # :a int
    # :b int
    
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    
    print("덧셈: {}, 뺄셈: {}, 곱셈: {}, 나눗셈: {}".format(add, sub, mul, div))
    
    return add, sub, mul, div # 괄호 안씌워도 튜플로 리턴함

calc(20, 4)
    


# In[183]:


#4장 연습문제 2 강사님
#해당값을 모두 찾아 위치를 리턴해주는 함수만들기
# ex)
# >>> lis = [1, 2, 3, 1, 4, 2, 1]
# >>> allindex(lis, 1)
# [0, 3, 6]
# def allinedx(a, b):

def allindex(_list, target_value):
    result = []
    for idx, v in enumerate(_list):
        if v == target_value:
            result.append(idx)
    return result

lis = [1, 2, 3, 1, 4, 2, 1]

allindex(lis, 1)


# In[188]:


#더 짧게

def allindex(_list, target_value):
    return [idx for idx, v in enumerate(_list) if v == target_value]
    
    lis = [1, 2, 3, 1, 4, 2, 1]

allindex(lis, 1)


# ## 즉석 연습문제. 유클리디언 거리 구하기
# ## v1, v2는 리스트이다. v1과 v2가 같은 길이를 가졌다고 가정하고 리스트 사이의 거리를 구하라.
# ## [a, b] 와 [c, d] 사이 거리는 sqrt((a-c)**2 + (b-d)**2)
# ## [a, b, c] 와 [d, e, f] 사이 거리는 sqrt((a-d)**2 + (b-e)**2 + (c-f)**2)
# ## import math 후 math.sqrt(x)하면 루트 값 구할 수 있음
# 
#     

# In[194]:


import math

def euclidean_distance(v1, v2):
    distance = 0
    for i in range(len(v1)):
        distance += (v1[i]-v2[i])**2
    return math.sqrt(total)

euclidean_distance([1,5], [2,6])


# In[214]:


# 강사님 버젼

import math

def euclidean_distance(v1, v2):
    total = 0
    for i, j in zip(v1, v2):
        total += (i - j)**2
    return math.sqrt(total)
    # return total ** 0.5 해도 같은 결과

a = [1, 2, 3, 4]
b = [4, 3, 2, 1]

euclidean_distance(a, b)


# ## 즉석 연습문제
# ## n개의 랜덤한 실수를 가진 리스트를 만드는 함수.
# ## 범위는 (0 ~ 100)

# In[207]:


import random

def random_list(n):
    lis = []
    for i in range (n):
        lis.append(random.uniform(0, 100))
    return lis

random_list(5)


# In[217]:


# 강사님 버젼
# radnom.uniform 사용하지 않고

import random

def random_list(n):
    return [random.random() * 100 for i in range(n)]
    
random_list(5)
        


# ## 즉석 연습문제
# ## n개의 랜덤한 실수를 가진 리스트를 만드는 함수.
# ## 범위는 (-100 ~ 100)

# In[213]:


import random

def random_list(n):
    lis = []
    for i in range (n):
        lis.append(random.uniform(-100, 100))
    return lis

print(random_list(5))


# In[219]:


# 강사님 버젼

import random

def random_list(n):
    result = []
    for i in range(n):
        f = random.randint(0, 1)
        num = random.random() * 100
        if f == 1:
            num = num * -1
        result.append(num)
    return result

random_list(5)


# ## lambda 함수

# In[220]:


lambda x:x + 2 #lambda 인자: return value


# In[223]:


print((lambda x:x + 2)(3))

a = lambda x:x + 2

a(3)


# In[225]:


f2 = lambda x, y : x + y
f2(3,5)


# In[ ]:




