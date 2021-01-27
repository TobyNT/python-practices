import unittest
from big_calc.bigint import BigInt

class BigIntTest(unittest.TestCase):
  def test_init(self):
    """
    Test if the init method parse the input string correctly
    """
    big_num = BigInt.fromStr("00000012345678901234567890")
    digits = big_num.digits
    self.assertEqual(20, len(digits))

  def test_init_with_invalid_input_format(self):
    """
    Test if the init method parse the invalid input value
    """
    with self.assertRaises(Exception):
      big_num = BigInt.fromStr("000a001234567890")

  def test_createDigitArray(self):
    """
    Test if createDigitArray returns a list of int
    """
    digits = BigInt.create_digits_from_str("123")
    self.assertEqual([1,2,3], digits)
  
  def test_prepare_operands(self):
    d1, d2 = BigInt.prepare_operands([1,0,0], [1,2])
    self.assertEqual([1,0,0], d1)
    self.assertEqual([0,1,2], d2)

  def test_equal(self):
    """
    Test eq func: equality
    """
    self.assertEqual(BigInt([1,0]), BigInt([1,0]))

  def test_not_equal(self):
    """
    Test eq func: inequality
    """
    self.assertNotEqual(BigInt([1,0]), BigInt([1]))

  def test_add_2_bigint_non_remembered(self):
    """
    Test add 2 bigint, non-remembered number
    """
    num_1 = BigInt.fromStr("123")
    num_2 = BigInt.fromStr("111")
    total = num_1 + num_2
    self.assertEqual([2,3,4], total.digits)

  def test_add_2_bigint_remembered(self):
    """
    Test add 2 bigint, remembered number
    """
    num_1 = BigInt.fromStr("123")
    num_2 = BigInt.fromStr("117")
    total = num_1 + num_2
    self.assertEqual([2,4,0], total.digits)

  def test_add_2_bigint_remembered_exceed(self):
    """
    Test add 2 bigint, remembered number, exceed original length
    """
    num_1 = BigInt.fromStr("123")
    num_2 = BigInt.fromStr("877")
    total = num_1 + num_2
    self.assertEqual([1,0,0,0], total.digits)


if __name__ == '__main__':
    unittest.main()