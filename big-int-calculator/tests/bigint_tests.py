import unittest
from big_calc.bigint import BigInt


class BigIntTests(unittest.TestCase):
  def test_init(self):
    big_num = BigInt()
    self.assertEqual([0], big_num.digits)

  def test_from_string(self):
    """
    Test if the init method parse the input string correctly
    """
    big_num = BigInt.from_string("00000012345678901234567890")
    digits = big_num.digits
    self.assertEqual(20, len(digits))

  def test_from_string_with_invalid_input_format(self):
    """
    Test if the init method parse the invalid input value
    """
    with self.assertRaises(Exception):
      big_num = BigInt.from_string("000a001234567890")

  def test_from_string(self):
    big_num = BigInt.from_string("123")
    self.assertEqual([1, 2, 3], big_num.digits)

  def test_equal(self):
    """
    Test eq func: equality
    """
    self.assertEqual(BigInt.from_digits([1, 0]), BigInt.from_digits([1, 0]))

  def test_not_equal(self):
    """
    Test eq func: inequality
    """
    self.assertNotEqual(BigInt.from_digits([1, 0]), BigInt.from_digits([1]))

  def test_add_2_bigint_non_remembered(self):
    """
    Test add 2 bigint, non-remembered number
    """
    num_1 = BigInt.from_string("123")
    num_2 = BigInt.from_string("111")
    total = num_1 + num_2
    self.assertEqual([2, 3, 4], total.digits)

  def test_add_2_bigint_remembered(self):
    """
    Test add 2 bigint, remembered number
    """
    num_1 = BigInt.from_string("123")
    num_2 = BigInt.from_string("117")
    total = num_1 + num_2
    self.assertEqual([2, 4, 0], total.digits)

  def test_add_2_bigint_remembered_exceed(self):
    """
    Test add 2 bigint, remembered number, exceed original length
    """
    num_1 = BigInt.from_string("123")
    num_2 = BigInt.from_string("877")
    total = num_1 + num_2
    self.assertEqual([1, 0, 0, 0], total.digits)


if __name__ == '__main__':
  unittest.main()
