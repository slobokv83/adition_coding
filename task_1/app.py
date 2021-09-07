'''
Write an efficient function that returns the index i for the first Fibonacci number that has more than 1000 digits i.e.
F(i) has 1000 or more decimal digits and F(i-1) has less than 1000 digits. Note that the number 1000 only has 4 digits
'''
import logging


def fibonacci(n:int = 1000) -> int:
  a , b = 0, 1

  i = 0
  while True:
    if len(str(a)) == n:
      break
    i += 1
    a, b = b, a + b
  return i

if __name__ == '__main__':
  logger = logging.getLogger(__name__)
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s %(levelname)-8s %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
  logger.info(f'The index of the first number with 1000 digits = {fibonacci()}')