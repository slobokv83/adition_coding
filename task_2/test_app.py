from app import jumps
import traceback


def test_jumps():
  assert jumps(A=10 , B=85 , D=30) == 3
  assert jumps(A=10 , B=280 , D=30) == 9
  assert jumps(A=10 , B=280 , D=1000) == 1
  assert jumps(A=20 , B=50 , D=30) == 1
  assert jumps(A=50 , B=50 , D=30) == 0
  assert jumps(A=50 , B=50 , D=50) == 0
  assert jumps(A=60 , B=50 , D=30) == -1
  assert jumps(A=10 , B=20 , D=0) == -1
  assert jumps(A=30 , B=20 , D=0) == -1

if __name__ == '__main__':
  try:
    test_jumps()
    print('PASS')
  except:
    print('FAIL')
    traceback.print_exc()