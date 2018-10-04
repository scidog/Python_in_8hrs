#Ex2.7.py
'''
“continue” can SKIP the next command and 
continue the next iteration of the loop.
'''
n = 0
while n < 26:
    n += 1
    if n%5 == 0:
        continue
    print("n =", n)