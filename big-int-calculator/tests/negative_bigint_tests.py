import unittest
from big_calc.bigint import BigInt

class NegativeBigIntTests(unittest.TestCase):
  def test_from_string_negative_big_int(self):
    neg_num = BigInt.from_string("-987")
    self.assertEqual([-9,8,7], neg_num.digits)

    neg_num = BigInt.from_string("-09870")
    self.assertEqual([-9,8,7,0], neg_num.digits)

  def test_from_string_negative_big_int_exception(self):
    with self.assertRaises(Exception) as ex:
      neg_num = BigInt.from_string("00-1")
    self.assertEqual("Invalid format", ex.exception.args[0])

  def test_add_negative_big_int_1(self):
    neg_num = BigInt.from_string("-100")
    pos_num = BigInt.from_string("99")
    num = neg_num + pos_num
    self.assertEqual([-1], num.digits)

  def test_add_negative_big_int_2(self):
    neg_num = BigInt.from_string("99")
    pos_num = BigInt.from_string("-100")
    num = neg_num + pos_num
    self.assertEqual([-1], num.digits)

  def test_add_negative_big_int_3(self):
    neg_num = BigInt.from_string("99")
    pos_num = BigInt.from_string("-99")
    num = neg_num + pos_num
    self.assertEqual([0], num.digits)
  
  def test_add_2_negative_big_ints(self):
    neg_num = BigInt.from_string("-18")
    pos_num = BigInt.from_string("-12")
    num = neg_num + pos_num
    self.assertEqual([-3, 0], num.digits)
    
