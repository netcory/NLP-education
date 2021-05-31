#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = 7
b = 3
d = a/b


# In[3]:


d


# In[4]:


d = int(d)
d


# In[5]:


c = a * b
c


# In[6]:


c = float(c)
c


# In[7]:


3>1


# In[11]:


3!=3


# In[12]:


a = 0
bool(a)


# In[13]:


a   = 0.1
bool(a)


# In[14]:


a0 = 1
bool(a0)


# In[15]:


a = []
bool(a)


# In[16]:


a = ['']
bool(a)


# In[17]:


a=()
bool(a)


# In[19]:


a = 70
b = 60
c = 66

if a > 50 and b > 50 and c > 50:
    print("true")


# In[20]:


print("hi", "hello")


# In[21]:


print("\"hello\"")


# In[22]:


print("\'hello\'")


# In[23]:


print("hello\nmy frined")


# In[24]:


s = "hello world"
s[:-4:3]


# In[25]:


s[-1:-4]


# In[26]:


s[-4:-1]


# In[28]:


name = "Liam"
print ("My name is " + name)


# In[29]:


print("My name is %s" %name)


# In[30]:


print("My name is %10s" % name)


# In[31]:


print("My name is %-10s!" % name)


# In[32]:


a = 0.581929


# In[41]:


print("number {} {} {}".format("hi", 'hello', 'there'))


# In[42]:


s = "I love strawberry"
s.replace('strawberry','orange')


# In[43]:


s


# In[44]:


s.count('r)')


# In[45]:


s.count('r')


# In[1]:


s = "    hello    world    "
s.lstrip()


# In[2]:


s


# In[3]:


s.rstrip()


# In[4]:


s.strip()


# In[5]:


s = "10:20:30:40:50"
s.split(':')


# In[6]:


s.split()


# In[9]:


s = "10 20 30 40 50 "
a = s.split()


# In[10]:


''.join(a)


# In[11]:


' '.join(a)


# In[12]:


'-'.join(a)


# In[14]:


b = [1, 2, 3]
a = list(b)


# In[17]:


a + [4]


# In[18]:


b = (1, 2, 3, 4, 5)
type(b)


# In[19]:


b[0]


# In[22]:


a = list(range(5, 0, -1))


# In[23]:


a


# In[24]:


a = [1, 2, 3, 4, 5]
type(a)


# In[25]:


tuple(a)


# In[26]:


b = (1, 2, 3, 4, 5)
type(b)


# In[27]:


list(b)


# In[28]:


type(list(b))


# In[29]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[0 : 9 : 2]


# In[30]:


a = [1, 2, 3, 4, 5]
del a[1:4]


# In[31]:


a


# In[32]:


a = [1, 2, 3]
a.insert(1, 1.5)
a


# In[33]:


a.pop(1)


# In[34]:


a


# In[35]:


a.remove(100)


# In[36]:


a


# In[37]:


a.revese()


# In[38]:


a.reverse()


# In[39]:


a


# In[40]:


a.sort()


# In[41]:


a


# In[42]:


a.sort(reverse=True)
a


# In[43]:


a = [1, 2, 3, 4, 5]
b = a


# In[44]:


a is b


# In[45]:


b[0] = 10
b


# In[46]:


a


# In[47]:


a = [1, 2, 3, 4, 5]
b = a.copy()


# In[48]:


b


# In[49]:


b[0] = -1
b


# In[50]:


a


# In[51]:


a = [[1, 2], [3, 4], [5, 6]]
a


# In[52]:


a[0][1]


# In[53]:


a[2][0]


# In[54]:


a = [[1, 2], [3, 4], [5, 6]]
a


# In[55]:


b = a.copy()
b


# In[56]:


b[0][0] = -1
b


# In[57]:


a


# In[58]:


a = [[1, 2], [3, 4], [5, 6]]


# In[59]:


import copy


# In[60]:


b = copy.deepcopy(a)


# In[61]:


b


# In[62]:


b[0][0] = "짠"
b


# In[63]:


a


# In[64]:


score = {'name' : 'Liam',
        'age' : 33,
        'City' : 'Goyang'}
score


# In[65]:


score['name']


# In[66]:


score['age']


# In[67]:


score['city']


# In[68]:


score['City']


# In[69]:


type(score)


# In[1]:


score = {'name' : 'Liam',
        'math' : 99,
        'english' : 100}


# In[2]:


score['math'] = 100


# In[3]:


score


# In[5]:


score.setdefault("age", 25)
score


# In[6]:


score.update({'math' : 99})


# In[7]:


score


# In[8]:


score.pop('age')


# In[9]:


score


# In[10]:


score.clear()


# In[11]:


score


# In[12]:


list(score)


# In[13]:


score


# In[14]:


score = list(score)


# In[15]:


score


# In[16]:


type(score)


# In[18]:


score = {'name' : 'Liam',
        'math' : 100,
        'english' : 100}
score.keys()


# In[19]:


score.values()


# In[20]:


score.items()


# In[21]:


animal = {'dog','cat', 'monkey','horse'}
animal


# In[22]:


type(animal)


# In[23]:


"cat" in animal


# In[24]:


"cat " in animal


# In[25]:


a = set("animal")


# In[26]:


a


# In[27]:


b=set(range(5))


# In[28]:


b


# In[29]:


b = set(range(0, 15, 2))


# In[30]:


b


# In[31]:


a = {1, 2, 3}
b = {3, 4, 5}


# In[32]:


a|b


# In[33]:


set.union(a, b)


# In[34]:


a & b


# In[35]:


set.intersection(a, b)


# In[36]:


a


# In[37]:


a.add(4)


# In[38]:


a


# In[39]:


a.remove(1)


# In[40]:


a


# In[41]:


a.discard(2)


# In[42]:


a


# In[43]:


a.discard(2)


# In[44]:


a


# In[45]:


a.add(1, 2)


# In[46]:


a


# In[47]:


a.add({1,2})


# In[48]:


a.add((1,2))


# In[49]:


a


# In[50]:


x = 10
if x == 10:
    pass


# In[57]:


n = int(input("정수를 입력하세요: "))

if n % 2 == 0:
    print("입력하신 %d는 짝수입니다." %n)
else:
    print("입력하신 {}는 홀수입니다.".format(n)) 


# In[68]:


for i in range(10):
    print("현재값은 {} 입니다.".format(i))


# In[69]:


for i in range(0, 10, 2):
    print(i)


# In[72]:


for i in "Orange":
    print(i, end = "")


# In[73]:


a = {'name': 'Liam',
    'math': 100,
    'english': 100}
a


# In[79]:


for i in a:
    print(i, end ='\n')
    print(a[i])   


# In[88]:


n = int(input("정수를 입력하세요: "))
for i in range(n+1):
    print('*' * (n-i))


# In[90]:


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for idx, val in enumerate(a):
    print(idx, val, sep=",", end = " ")


# In[93]:


for i in range(2, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i * j))


# In[94]:


count = int(input("반복횟수?"))
i = 0
while i < count:
    print("입력한 횟수만큼 반복")
    i += 1


# In[102]:


while i != 5:
    i = int(input("5를 입력하면 반복이 중단됩니다"))
print ("중단!")


# In[6]:


n = 0
total = 0

while n != 's' and n !='S':
    
    total += int(n)
    n = input("값을 입력해주세요: ")
    
print("합계는 {}입니다.".format(total))


# In[7]:


import random


# In[18]:


a = []

for i in range(100):
    
    r = random.randint(1, 1000)
    a.append(r)
    
maximum = 0
for j in a:
    if j > maximum:
        maximum = j
        
print(a)
print(maximum)


# In[19]:


min(a), max(a)


# In[20]:


min(a)


# In[21]:


a.sort()


# In[23]:


a.sort(reverse = True)


# In[24]:


a


# In[25]:


a[0]


# In[26]:


a[-1]


# In[27]:


sum(a)


# In[28]:


a = [i for i in range(10)]


# In[29]:


a


# In[30]:


a = [i for i in range(10) if i%2 == 1]


# In[31]:


a


# In[39]:


c = [i * j for j in range(2, 10) for i in range(1, 10)]


# In[41]:


print(c)


# In[42]:


keys = ['name', 'math', 'english']
values = ['Liam', '100', '100']
dicdic = {keys[i]: values[i] for i in range(3)}


# In[43]:


dicdic


# In[47]:


dict(zip(keys, values))


# In[48]:


list(zip(keys,values))


# In[49]:


print(zip(keys, values))


# In[50]:


word = ['school', 'game', 'piano', 'science', 'hotel', 'mountain']


# In[51]:


new_list = [i for i in word if len(i) >= 6]


# In[52]:


new_list


# In[53]:


word


# In[54]:


len_list = [len(i) for i in word ]


# In[55]:


len_list


# In[56]:


for w, l in zip(word, len_list):
    print("{}의 길이는 {}".format(w, l))


# In[57]:


a = [[10, 20], [30, 40], [50, 60]]
a


# In[58]:


print(a)


# In[59]:


a = [[10, 20],
    [30, 40],
    [50, 60]]
a


# In[60]:


print(a, end = "")


# In[61]:


a[0]


# In[62]:


a[0][1]


# In[63]:


a[0].append[10]


# In[64]:


a[0].append(10)


# In[65]:


a


# In[66]:


a[2].extend([1, 2])


# In[67]:


a


# In[68]:


pprint(a)


# In[69]:


import pprint


# In[70]:


pprint(a)


# In[71]:


from pprint import pprint


# In[72]:


pprint(a)


# In[73]:


print(a)


# In[74]:


a = [[10, 20],
    [30, 40],
    [50, 60]]
a


# In[76]:


for x, y in a:
    print(x, y)


# In[77]:


a


# In[80]:


for i in a:
    for j in i:
        print(j, end = ' ')


# In[81]:


a = [[10, 20], [30, 40], [50, 60]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')


# In[83]:


for idx, val in enumerate(a):
    for idx2, val2 in enumerate(val):
        print(idx, idx2, val2)


# In[86]:


i = 0
while i < len(a):
    x, y = a[i]
    i += 1
    print(x, y)


# In[89]:


i = 0
while i < len(a):
    j = 0
    while j < len([i]):
        print(a[i][j], end = ' ')
        j += 1
        
    i += 1


# In[90]:


a = [[10, 20], [30, 40], [50, 60]]
b = [[2, 3], [4, 5], [6, 7]]


# In[92]:


c = []
for i in range(len(a)):
    for j in range(len(a[i])):
        c.append(a[i][j] * b[i][j])
        
c


# In[93]:


a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
        
    a.append(line)
    
print(a)


# In[94]:


a


# In[95]:


a.append([1,2])


# In[96]:


a


# In[97]:


a.extend([1,2])


# In[98]:


a


# In[99]:


d = {
    1 : 'Liam',
    2 : 'Choi'
}
d


# In[100]:


enumerate(d)


# In[101]:


a = enumerate(d)


# In[102]:


a


# In[103]:


a[0]


# In[107]:


a = []
for i in range(3):
    line = []
    for j in range(2):
        
        
        line.append(2*i + j+1)
    a.append(line)
    
print(a)


# In[108]:


## break : for, while 을 완전히 중단
## continue : 처음으로 돌아가 다음 반복 수행


# In[109]:


for i in range(5):
    if i ==3:
        break
    print (i)


# In[110]:


for i in range(5):
    if i == 3:
        continue
    print(i)


# In[111]:


i = 0
while i < 30:
    if i == 20:
        break
    print(i)
    i += 1


# In[113]:


i = 0
while i < 30:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end = " ")


# In[115]:


n = int(input("숫자를 입력하세요: "))
i = 0

while True:
    print('hi')
    i += 1
    if i ==n:
        break
        


# In[116]:


print("출력할 문자를 입력하세요")


# In[121]:


print('hello', 'my', 'name', 'is', '%s' %"정욱")


# In[122]:


file = open("file.txt", 'w')


# In[123]:


a = open('file', 'w')


# In[124]:


ㅁ


# In[125]:


a


# In[126]:


a.write("First Line \n")


# In[127]:


a


# In[128]:


a = open('file.txt', 'w')


# In[129]:


a


# In[130]:


a.write('first line \n')
a.write('second line \n')


# In[131]:


a


# In[132]:


a.close()


# In[133]:


a


# In[134]:


file = open('file.txt', 'r')


# In[135]:


file


# In[137]:


text = file.read()


# In[138]:


print(text)


# In[139]:


file.close()


# In[140]:


with open('file.txt', 'r') as file:
    text = file.read()
    print(text)


# In[141]:


with open('file.txt', 'r') as file:
    line = file.readline()
    while line:
        line = file.readline()
        print(line)


# In[142]:


with open('file.txt', 'r') as file:
    text = None
    lines = file.readlines()
    print(lines)


# In[143]:


text = ['first file\n', 'second line']

with open('file.txt', 'w') as file:
    file.writelines(text)


# In[147]:


file


# In[148]:


file = open('write_practice.txt', 'w')

file.write('파일에 글 쓰기 실습')
file.close


# In[149]:


content = file.read()


# In[158]:


file = open('write_practice.txt', 'wt')
file.write('파일에 글 쓰기 실습')


# In[159]:


file.read()


# In[160]:


file = open('write_practice.txt', 'r')


# In[161]:


file.read()


# In[162]:


content = file.read()


# In[163]:


content


# In[164]:


file.read()


# In[166]:


file = open('write_practice.txt', 'r')
content = file.read()
content


# In[167]:


with open ('sample1.txt', 'w') as f:
    f.write("글쓰기 실습 \n")
    f.write("글이 써졌습니다.")


# In[168]:


f


# In[169]:


f.read()


# In[171]:


with open('sample1.txt', 'r') as fr:
    content = fr.read()
    
print(content)


# In[172]:


content


# In[174]:


with open('sample1.txt', 'r') as f:
    line = f.readline()
    print(line)
    print("-" * 10)
    line = f.readline()
    print(line)


# In[175]:


with open('sample1.txt', 'r') as f:
    lines = f.readlines()
    print(lines)


# In[176]:


lines


# In[177]:


with open('no_exist.txt', 'r') as f:
    content = f.read()
    print(content)


# In[178]:


with open('no_exist.txt', 'r+') as f:
    content = f.read()


# In[186]:


with open('no_exist2.txt', 'w+') as f:
    f.write('w 모드 실습')
    content = f.read()
print(content)


# In[187]:


with open('no_exist3.txt', 'w+') as f:
    f.write('w모드 실습')


# In[192]:


with open('no_exist3.txt', 'w+') as f:
    f.write('w+')
    content = f.read()


# In[193]:


with open('new_w+.txt', 'w+') as f:
    f.write('w+모드 실습입니다. \n w+모드')
    print(f.tell())
    f.seek(0)
    print(f.tell())
    content = f.read()
    print(content)
    print(f.tell())


# In[196]:


def func(a, b):
    print('덧셈 함수입니다.')
    return a + b
          
func(1, 2)


# In[198]:


def func():
    print("hello, function")
    
func()


# In[199]:


func(1234)


# In[201]:


def func(name):
    print("hello, " + name)
func('Liam')


# In[202]:


def func():
    return 3, 5


# In[203]:


func()


# In[204]:


a = 1
b = 2
c = 5

def func1():
    a = 3
    b = 4
    print(a, b, c)
    return


# In[205]:


func1()


# In[206]:


def func2():
    a = 5
    b = 6
    
    func1()
    
    print(a, b)


# In[208]:


func2()


# In[1]:


a = [1, 2, 3, 4]
b = a


# In[2]:


b[0] = 3


# In[3]:


b


# In[4]:


a


# In[5]:


a = [1, 2, 3, 4]
b.copy(a)


# In[6]:


b = copy(a)


# In[7]:


b = a.copy()


# In[8]:


b


# In[9]:


b[0] = 5


# In[10]:


a


# In[11]:


b


# In[18]:


lis = [2, 2, 3, 1, 4, 2, 1]


# In[19]:


lis


# In[22]:


def allindex(a, b):
    index_list = []
    for i, v in enumerate(a):
        if v == b:
            index_list.append(i)
            
    return index_list
            
allindex(lis, 1)


# In[23]:


(lambda x : x**2)(3)


# In[24]:


def sqr(x):
    return x**2

sqr(3)


# In[25]:


type(lambda)


# In[26]:


def func(a, b, c):
    print(a, b, c)
    
x = [1, 2, 3]
func(*x)


# In[27]:


x = [1, 2]
func(*x)


# In[28]:


def func(*args):
    for arg in args:
        print(arg)
func(1)


# In[29]:


func(1, 2, 3, 4, 5)


# In[32]:


def func(a, *args):
    print(a, end ="")
    for arg in args:
        print(arg, end= "")
func(100, 1, 2, 3,4, 5)


# In[ ]:


def func(email, name):
    print


# In[1]:


def func(a, *args):
    print (a, end = " ")
    for arg in args:
        print(arg, end = " ")
func(100, 1, 2, 3, 4, 5)


# In[3]:


def func(email, name):
    print("이메일 : ", email)
    print("이름 : ", name)
    
func('netcory@gmail.com', 'Liam Choi')


# In[6]:


func(email = 'netcory@gmail.com', name = 'Liam Choi')


# In[8]:


x = {'email': 'netcory@gmail.com', 'name': 'Liam Choi'}


# In[9]:


func(**x)


# In[10]:


def func(**kwargs):
    print('이메일:', kwargs['email'])
    print("이름: ", kwargs['name'])
    
func(email = 'netcory@gmail.com', name = 'Liam Choi')


# In[11]:


func(**x)


# In[12]:


def func(email, name, age = 20):
    print('이메일: ', email)
    print('이름: ', name)
    print('나이: ', age)
    
func('netcory@gmail.com', 'Liam Choi')


# In[13]:


func('netcory@gmail.com', 'Liam Choi', 33)


# In[27]:


def calc(a, *args):
    initial = args[0]
    
    if a == '+':
        for arg in args[1:]:
            initial += arg
        
        
    if a == '-':
        for arg in args[1:]:
            initial -= arg
            
    if a == '*':
        for arg in args[1:]:
            initial *= arg
            
    return initial

calc('-', 1, 2, 3,4 , 5)
            


# In[41]:


def calc(*args):
    minimum = args[0]
    maximum = args[0]
    total = 0
    count = 0
    
    for arg in args:
        if minimum > arg:
            minimum = arg
    
        if maximum < arg:
            maximum = arg
            
        total += arg
        count += 1
        
        average = total / count
        
            
    print("최대값 : {}".format(maximum), "최소값 : {}".format(minimum), '평균값 : {}'.format(average))


# In[42]:


calc(1, 2, 3, 4, 5)


# In[21]:


class Dog:
    def __init__(self, name, color):
        self.hungry = 0
        self.name = name
        self.color = color
    
    def eat(self):
        if self.hungry <= 0:
            print("배가 너무 불러요!")
        else:
            self.hungry -= 10
            print("밥먹음 ", self.hungry)
    
    def walk(self):
        if self.hungry >= 50:
            print("배고파요!")
        else:
            self.hungry += 10
            print("산책함 ", self.hungry)


# In[24]:


choco = Dog('choco', 'black')
jjong = Dog('jjong', 'white')


# In[56]:


choco.eat()


# In[49]:


choco.walk()


# In[74]:


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.__hungry = 0
    
    def eat(self):
        if self.__hungry <=0:
            print('배가 너무 불러요!')
        else:
            self.__hungry -= 10
            print('밥먹음', self.__hungry)
            
    def walk(self):
        self.__hungry += 10
        print('산책', self.__hungry)
        
    def condition(self):
        print('{} 배고픔 : {}'.format(self.name, self.__hungry))


# In[75]:


mery = Dog('mery', 'black')
mery.eat()


# In[79]:


mery.walk()


# In[80]:


mery.condition()


# In[81]:


class Dog:
    dog_count = 0
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Dog.dog_count += 1
        
    def dogCount(self):
        print("총 강아지는: ", Dog.dog_count)


# In[82]:


hello = Dog('hello', 'black')


# In[83]:


hello.dogCount()


# In[84]:


happy = Dog('happy', 'black')


# In[85]:


hello.dogCount()


# In[88]:


hello.dogCount()

