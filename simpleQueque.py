#! /usr/bin/env python3 

from collections import deque

stack= deque(maxlen=100)
ext=False
while(ext==False):
    cmd=input()
    if(cmd[:4]=='push'):
        stack.append(cmd[5:])
        print('ok')
    elif(cmd=='pop' or cmd=='front'):
        if(len(stack)>=1 and cmd=='pop'):
            print(stack.popleft())
        elif(len(stack)>=1 and cmd=='front'):
            print(stack[0])
        else: print('error')
    elif(cmd=='size'):
        print(len(stack))
    elif(cmd=='clear'):
        stack.clear()
        print('ok')
    elif(cmd=='exit'):
        print('bye')
        ext=True
