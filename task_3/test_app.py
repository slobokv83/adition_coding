from app import zeroes
import traceback

def test_zeroes():
  assert zeroes(number=168000) == 5
  assert zeroes(number=0) == 0
  assert zeroes(number=-100) == 2
  assert zeroes(number=1) == 0
  assert zeroes(number=513) == 8

if __name__ == '__main__':
  try:
    test_zeroes()
    print('PASS')
  except:
    print('FAIL')
    traceback.print_exc()  