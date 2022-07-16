import logging as lp
lp.basicConfig(filename="oops.log",level=lp.INFO, format='%(levelname)s %(asctime)s %(message)s')
lp.info("Logging is enabled")