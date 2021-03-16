#!/usr/bin/env python
# coding: utf-8

# In[1]:


ver=0
while(ver==0):
    player =int(input("1-камень,2-ножницы,3-бумага.*"))
    player2=int(input("1-камень,2-ножницы,3-бумага.*"))
    if(player==1 or player ==2 or player==3):
        ver=1
if player==1:
    print("Камень")
if player==2:
    print("ножницы")
if player==3:
    print("бумага")
while(ver==0):
    player2 =int(input("1-камень,2-ножницы,3-бумага.*"))
    if(player2==1 or player2 ==2 or player2==3):
        ver=1
if player2==1:
    print("Камень")
if player2==2:
    print("ножницы")
if player2==3:
    print("бумага")
if player==1 and player2==2:
    win=1
if win==0:
    print("ничья")
if win==1:
    print("победил 1")
if win==2:
    print("победил 2")

