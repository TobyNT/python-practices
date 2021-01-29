import unittest

from big_calc.math_util import DigitsUtility

class DigitsUtilityTests(unittest.TestCase):
  def test_prepare_operands(self):
    d1, d2 = DigitsUtility.prepare_operands([1, 0, 0], [1, 2])
    self.assertEqual([1, 0, 0], d1)
    self.assertEqual([0, 1, 2], d2)
