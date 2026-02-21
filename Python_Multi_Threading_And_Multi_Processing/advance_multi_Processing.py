## MultiProcessing with ProcessPoolExecutor 

from concurrent.futures import ProcessPoolExecutor
import time 

def squares_number(number):
    time.sleep(1)
    return f"Square: {number*number}"

numbers=[1,2,3,4,5,6,7,8,9]

with ProcessPoolExecutor(max_workers=3) as executor:
    results=executor.map(squares_number,numbers)
    
for result in results:
    print(result)
    
