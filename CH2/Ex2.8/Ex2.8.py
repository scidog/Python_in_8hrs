#Ex2.8.py
'''
“if num==5:  break” will run the “break” command 
if num is 5, the break statement will exit from 
the while loop, runs “print (num) ”.
'''
n = 0
while n < 20:
    print("n pre break=", n)
    if n == 16:
        break
    n += 1
print("n post break=", n)
print("The 'break' command popped us right out after the loop.")