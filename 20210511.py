#!/usr/bin/env python
# coding: utf-8

# In[1]:


l2 = [10, 20, 30, 40, 50]
for i in enumerate(l2):
    print(i)
    print(type(i))


# In[2]:


for i in enumerate(l2):
    # i[0] index
    # i[1] value
    l2[i[0]] = i[1] + 1
print(l2)


# In[3]:


for idx, value in enumerate(l2):
    l2[idx] = value + 1
print(l2)


# In[4]:


enumerate(l2)


# In[5]:


print(enumerate(l2))


# In[7]:


l2 = [[1, 2], [3, 4], [5, 6]]
for idx, value in enumerate(l2):
    for idx2, value2 in enumerate(value):
        l2[idx][idx2] = value2 + 10
print(l2)


# In[46]:


x = [3, 6, 9, 20, -5, 5]

for idx, value in enumerate(x):
    print(value*10)
    x[idx] = x[idx] * 10
x


# In[75]:


y = {
    "math":70,
    "science":80,
    "english":20
}

for key in y:
    print(y[key] + 10)
    y[key] = y[key] + 10
y


# In[38]:


num = int(input("정수를 입력해주세요: "))

for i in range(1,10):
    print(num, "*", i, "=", num * i)


# In[100]:


for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
    print("-----------------")


# In[95]:


words = ["school", "game", "piano", "science", "hotel", "mountain", "abcd", "abcdefg", "abcdefgh", "abcdefghijk"]
words2 = []

for ind, value in enumerate(words):
    if len(words[ind]) >= 6:
        words2.append(words[ind])
words2


# In[97]:


words = ["school", "game", "piano", "science", "hotel", "mountain", "abcd", "abcdefg", "abcdefgh", "abcdefghijk"]

new_word = []
for w in words:
    if len(w) >= 6:
        new_word.append(w)
new_word


# In[99]:


words = ["school", "game", "piano", "science", "hotel", "mountain", "abcd", "abcdefg", "abcdefgh", "abcdefghijk"]

new_word = words.copy()
for w in words:
    if len(w) < 6:
        new_word.remove(w)
new_word


# In[85]:


for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        print(i,"는 3과 5의 공배수")
    elif i%3 == 0:
        print(i, '는 3의 배수')
    elif i%5 == 0:
        print(i, '는 5의 배수')
    else:
        print(i, '는 그냥 숫자')


# In[87]:


num = int(input("정수를 입력해주세요: "))

for i in range (1, num+1):
    if i%3 == 0 and i%5 == 0:
        print(i,"는 3과 5의 공배수")
    elif i%3 == 0:
        print(i, '는 3의 배수')
    elif i%5 == 0:
        print(i, '는 5의 배수')
    else:
        print(i, '는 그냥 숫자')


# sum = 0
# i = input("값을 입력해주세요: ")
# 
# while i.upper() != "S":
#     sum += int(i)
#     i = input("값을 입력해주세요: ")
# if i.upper() == 'S':
#     print("합계는 {}".format(sum))

# In[140]:


sum = 0

i = input("값을 입력해주세요: ")

while i.upper() != "S":
    sum += int(i)
    i = input("값을 입력해주세요: ")
if i.upper() == "S":
    print("합계는 {}".format(sum))


# In[144]:


# 강사님 코드

i = 0
total = 0

while i != "s" and i != "S":
    total += int(i)
    i = input("값을 입력해주세요: ")
print("합계: ", total)    


# In[145]:


import random
random.random()


# In[146]:


random()


# In[172]:


random.random()


# In[175]:


get_ipython().run_line_magic('pinfo', 'random.random')


# In[206]:


random.randint(1,1000000)


# a = 1 # 유저
# b = 0 # 컴퓨터
# total = 0 # 전체
# win = 0 # 승리
# draw = 0 # 무승부
# lose = 0 # 패배
# 
# while a == 1 or a == 2 or a == 3:
#     b = random.randint(1,3)
#     a = int(input("가위(1), 바위(2), 보(3)을 입력해주세요!: "))
#     if a == 1:
#         if b == 1:
#             print("유저: 가위, 컴퓨터: 가위")
#             draw += draw
#         elif b == 2:
#             print("유저: 가위, 컴퓨터: 바위")
#             lose += lose
#         else:
#             print("유저: 가위, 컴퓨터: 보")
#             win += win
#     
#     if a == 2:
#         if b == 1:
#             print("유저: 바위, 컴퓨터: 가위")
#             win += win
#         elif b == 2:
#             print("유저: 바위, 컴퓨터: 바위")
#             darw += draw
#         else:
#             print("유저: 바위, 컴퓨터: 보")
#             lose += lose
#     
#     if a == 3:
#         if b == 1:
#             print("유저: 보, 컴퓨터: 가위")
#             lose += lose
#         elif b == 2:
#             print("유저: 보, 컴퓨터: 바위")
#             win += win
#         else:
#             print("유저: 보, 컴퓨터: 보")
#             draw += draw
#             
#     total += total
#                
#             
# print("게임종료(전체: {}, 승리: {}, 무승부: {}, 패배: {} )".format(total, win, draw, lose))

# ## import random
# 
# a = 1 # 유저
# b = 0 # 컴퓨터
# total = 0 # 전체
# win = 0 # 승리
# draw = 0 # 무승부
# lose = 0 # 패배
# 
# while a == 1 or a == 2 or a == 3:
#     b = random.randint(1,3)
#     a = int(input("가위(1), 바위(2), 보(3)을 입력해주세요!: "))
#     if a == 1:
#         if b == 1:
#             print("유저: 가위, 컴퓨터: 가위")
#             draw += 1
#         elif b == 2:
#             print("유저: 가위, 컴퓨터: 바위")
#             lose += 1
#         else:
#             print("유저: 가위, 컴퓨터: 보")
#             win += 1
# 
#     if a == 2:
#         if b == 1:
#             print("유저: 바위, 컴퓨터: 가위")
#             win += 1
#         elif b == 2:
#             print("유저: 바위, 컴퓨터: 바위")
#             draw += 1
#         else:
#             print("유저: 바위, 컴퓨터: 보")
#             lose += 1
# 
#     if a == 3:
#         if b == 1:
#             print("유저: 보, 컴퓨터: 가위")
#             lose += 1
#         elif b == 2:
#             print("유저: 보, 컴퓨터: 바위")
#             win += 1
#         else:
#             print("유저: 보, 컴퓨터: 보")
#             draw += 1
# 
#     total += 1
#     
# print("게임종료(전체: {}, 승리: {}, 무승부: {}, 패배: {} )".format(total, win, draw, lose))
