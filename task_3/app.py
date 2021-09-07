'''
Integers in their binary representation contain 1s and 0s. For example 1001 in binary is 9 in decimal.
Write a function int zeroes(int i) that returns the largest number of consecutive 0s surrounded by 1s.
For example given i = 168000 (which is binary 101001000001000000) return 5. The last 6 zeroes are not
surrounded by 1s, since there is only a 1 to the left
'''
import logging

def zeroes(number:int = 168000) -> int:
  result = bin(number)[2:] # the same is without [2:]

  cnt = 0
  container = 0
  flag = False

  for i in range(len(result)):
    if i > 0:
      if result[i - 1] == '1' and result[i] == '0':
        flag = True
      elif result[i - 1] == '0' and result[i] == '1':
        flag = False
    
    if flag:
      cnt += 1
    else:
      if cnt > container:
        container = cnt
      cnt = 0
  return container

if __name__ == '__main__':
  logger = logging.getLogger(__name__)
  logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
  logger.info(f'Number of zeros = {zeroes()}')