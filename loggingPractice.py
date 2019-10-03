import logging
logging.basicConfig(level=logging.WARNING, filename='operation.log', format='%(asctime)s: %(levelname)s: %(message)s')
def add(num1, num2):
	logging.info('Added {} and {} together'.format(num1, num2))
	return num1 + num2		

sum = add(5, 4)