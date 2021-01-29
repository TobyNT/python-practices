import re

from big_calc.math_util import DigitsUtility


class BigInt:
  __digits: list[int]

  """
    Python has no constructor overloading. Therefore use classmethod instead.
  """
  def __init__(self):
    super().__init__()
    self.__digits = [0]

  @classmethod
  def from_string(cls, value: str):
    valid_value = cls.validate_input_str(value)
    instance = cls()
    instance.__digits = cls.__create_digits_from_str(valid_value)
    return instance

  @classmethod
  def from_digits(cls, digits: list[int]):
    valid_digits = cls.validate_input_value(digits)
    instance = cls()
    instance.__digits = valid_digits
    return instance

  @property
  def digits(self) -> list[int]:
    return self.__digits.copy()

  @staticmethod
  def validate_input_str(value: str) -> str:
    if not isinstance(value, str):
      raise Exception("Not a string")

    stripped = value.strip()
    pattern = re.compile("^(\+|-)?(0*)([0-9]+)$")
    if not pattern.match(stripped):
      raise Exception("Invalid format")

    on = False
    refined = []
    for i in range(len(stripped)):
      c = stripped[i]
      if on:
        refined.append(c)
      elif c != '0':
        on = True
        refined.append(c)

    if len(refined) == 0:
      return [0]

    return refined

  @staticmethod
  def validate_input_value(digits: list[int]) -> list[int]:
    if not isinstance(digits, list):
      raise Exception("Not a list of int")

    def reverse_enumerate(l): return zip(
      range(len(l) - 1, -1, -1), reversed(l))

    for i, digit in reverse_enumerate(digits):
      if digit < 0 and i > 0:
        raise Exception("Invalid position of negative digit in list")

    on = False
    refined = []
    for i in range(len(digits)):
      digit = digits[i]
      if on:
        refined.append(digit)
      elif digit != 0:
        on = True
        refined.append(digit)

    if len(refined) == 0:
      return [0]

    return refined

  @staticmethod
  def __create_digits_from_str(value: str) -> list[int]:
    non_zero = False
    negative = False
    result = []

    for i in range(len(value)):
      c = value[i]
      if non_zero:
        result.append(int(c))
      else:
        if c == '-':
          negative = True
        elif c == '+' or c == '0':
          continue
        else:
          non_zero = True
          result.append(int(c))

    if negative:
      result[0] = result[0] * (-1)

    return result

  def __eq__(self, obj):
    if isinstance(obj, self.__class__):
      if len(self.__digits) != len(obj.__digits):
        return False

      for i in range(len(self.__digits)):
        if (self.__digits[i] != obj.__digits[i]):
          return False

      return True

    return False

  def __hash__(self):
    return super().__hash__()

  def __add__(self, another):
    negpos_1 = -1 if BigInt.__is_negative(self) else 1
    negpos_2 = -1 if BigInt.__is_negative(another) else 1

    negpos = negpos_1 * negpos_2
    if negpos < 0:
      if negpos_1 < 0:
        return BigInt.__sub_ignore_sign(another, self.negate())
      else:
        return BigInt.__sub_ignore_sign(self, another.negate())
    else:
      big_num = BigInt.__add_ignore_sign(self, another)
      if negpos_1 < 0:
        return big_num.negate()
      return big_num

  def __sub__(self, another):

    return BigInt()

  @staticmethod
  def __add_ignore_sign(first_operand, second_operand):
    unsigned_digits_1 = first_operand.digits
    unsigned_digits_1[0] = abs(unsigned_digits_1[0])

    unsigned_digits_2 = second_operand.digits
    unsigned_digits_2[0] = abs(unsigned_digits_2[0])

    o1_digits, o2_digits = DigitsUtility.prepare_operands(
      unsigned_digits_1, unsigned_digits_2)

    final_digits = []
    length = len(o1_digits)
    carry = 0

    for i in reversed(range(length)):
      subtotal = o1_digits[i] + o2_digits[i] + carry

      if (subtotal > 9):
        carry = 1
        subtotal = subtotal % 10
      else:
        carry = 0
      final_digits.insert(0, subtotal)

    if carry > 0:
      final_digits.insert(0, 1)

    return BigInt.from_digits(final_digits)

  @staticmethod
  def __sub_ignore_sign(first_operand, second_operand):
    unsigned_digits_1 = first_operand.digits
    unsigned_digits_1[0] = abs(unsigned_digits_1[0])

    unsigned_digits_2 = second_operand.digits
    unsigned_digits_2[0] = abs(unsigned_digits_2[0])

    o1_digits, o2_digits = DigitsUtility.prepare_operands(
      unsigned_digits_1, unsigned_digits_2)

    length = len(o1_digits)
    bigger_num_digits, smaller_num_digits, sign = DigitsUtility.max(
      o1_digits, o2_digits, length)
    if bigger_num_digits == None or smaller_num_digits == None:
      return BigInt()

    final_digits = []
    carry = 0
    for i in reversed(range(length)):
      subtotal = bigger_num_digits[i] - smaller_num_digits[i] - carry

      if (subtotal < 0):
        carry = 1
        subtotal = 10 + subtotal
      else:
        carry = 0
      final_digits.insert(0, subtotal)

    big_num = BigInt.from_digits(final_digits)
    big_num.__digits[0] *= sign
    return big_num

  @staticmethod
  def __is_negative(big_num):
    return big_num.__digits[0] < 0

  def negate(self):
    final_digits = self.digits
    final_digits[0] *= -1

    return BigInt.from_digits(final_digits)
