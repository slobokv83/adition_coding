from app import fibonacci
import traceback


def test_fibonacci():
  assert fibonacci(n=1) == 0
  assert fibonacci(n=2) == 7
  assert fibonacci(n=3) == 12
  assert fibonacci(n=4) == 17
  assert fibonacci(n=5) == 21
  assert fibonacci(n=6) == 26
  assert fibonacci(n=7) == 31
  assert fibonacci(n=8) == 36
  assert fibonacci(n=9) == 40
  assert fibonacci(n=10) == 45
  assert fibonacci(n=1000) == 4782

if __name__ == '__main__':
  try:
    test_fibonacci()
    print('PASS')
  except:
    print('FAIL')
    traceback.print_exc()