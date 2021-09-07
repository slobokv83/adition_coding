"""
A rabbit wants to jump from one side of the road to the other. The rabbit starts at position A and wants to get to B.
For simplicity the rabbit can only jump a fixed distance D. Write an efficient function int jumps(int A, int B, int D)
that returns the minimal number of jumps required to get from A to B (or further in case the last jump makes the rabbit
jump over B).For example: givenA=10, B=85, D=30, the function should return 3. The first jump takes the rabbit to
10+30=40. The second jump to 40+30=70. The third jump to 70+30=100
"""

import logging

def jumps(A:int = 10, B:int = 85, D:int = 30) -> int:
  num_jumps = 0
  if A <= B and D > 0:
    while A < B:
      A = A + D
      num_jumps += 1
  else:
    num_jumps = -1
    
  return num_jumps

if __name__ == '__main__':
  logger = logging.getLogger(__name__)
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s %(levelname)-8s %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
  logger.info(f'Minimum number of rabbit\'s jumps = {jumps()}')