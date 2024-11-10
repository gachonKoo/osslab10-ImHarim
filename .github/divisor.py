# tests/test_example.py
import unittest
from main import find_divisors  # 'main'이 테스트할 파일의 이름인 경우

class TestFindDivisors(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual(find_divisors(10), [1, 2, 5, 10])
        self.assertEqual(find_divisors(15), [1, 3, 5, 15])

if __name__ == "__main__":
    unittest.main()
