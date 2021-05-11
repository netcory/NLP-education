#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1,2,3,4,5]
sum(a0)


# In[2]:


sum(a)


# In[3]:


sum


# In[4]:


sum(a)


# In[6]:


import random

a = 1 # 유저
b = 0 # 컴퓨터
total = 0 # 전체
win = 0 # 승리
draw = 0 # 무승부
lose = 0 # 패배

while a == 1 or a == 2 or a == 3:
    b = random.randint(1,3)
    a = int(input("가위(1), 바위(2), 보(3)을 입력해주세요!: "))
    if a == 1:
        if b == 1:
            print("유저: 가위, 컴퓨터: 가위")
            draw += 1
        elif b == 2:
            print("유저: 가위, 컴퓨터: 바위")
            lose += 1
        else:
            print("유저: 가위, 컴퓨터: 보")
            win += 1

    if a == 2:
        if b == 1:
            print("유저: 바위, 컴퓨터: 가위")
            win += 1
        elif b == 2:
            print("유저: 바위, 컴퓨터: 바위")
            draw += 1
        else:
            print("유저: 바위, 컴퓨터: 보")
            lose += 1

    if a == 3:
        if b == 1:
            print("유저: 보, 컴퓨터: 가위")
            lose += 1
        elif b == 2:
            print("유저: 보, 컴퓨터: 바위")
            win += 1
        else:
            print("유저: 보, 컴퓨터: 보")
            draw += 1

    total += 1
    
print("게임종료(전체: {}, 승리: {}, 무승부: {}, 패배: {} )".format(total, win, draw, lose))

