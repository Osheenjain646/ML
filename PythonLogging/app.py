import logging 

## logging setting 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmaticAPP")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"Subtract {a}-{b} = {result}")
    return result
def multiply(a,b):
    result=a*b
    logger.debug(f"Multiply {a}*{b} = {result}")
    return result
def div(a,b):
    try:
        result=a/b
        logger.debug(f"Division {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

print(div(45,0))
print(multiply(45,56))
print(sub(56,66))
print(add(465,46545))

