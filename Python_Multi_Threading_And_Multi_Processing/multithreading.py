## Multi Threading

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(letter)

## create two thread 
t1=threading.Thread(target=print_letter)
t2=threading.Thread(target=print_number)


t=time.time()

## Start the thraed 
t1.start()
t2.start()

##join the thread 


finished_time=time.time()-t
print(finished_time)
