import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True   ## to do the time and date format 
)
## log meassages with different severity levels

logging.debug("This is a debug meassage")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")