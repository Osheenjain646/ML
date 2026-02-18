from logger import logging

def add(a,b):
    logging.debug("Addition operation taking place")
    return a+b

logging.debug("addition function is called")
print(add(5,3))