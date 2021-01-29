
class DigitsUtility:
  @staticmethod
  def prepare_operands(o1_digits: list[int], o2_digits: list[int]):
    first_operand_len = len(o1_digits)
    second_operand_len = len(o2_digits)
    max = first_operand_len

    first_operand_digits = []
    second_operand_digits = []

    distance = first_operand_len - second_operand_len

    if distance > 0:
      max = first_operand_len
      first_operand_digits = o1_digits.copy()
      second_operand_digits = [0] * abs(distance) + o2_digits
    elif distance < 0:
      max = second_operand_len
      second_operand_digits = o2_digits.copy()
      first_operand_digits = [0] * abs(distance) + o1_digits
    else:
      first_operand_digits = o1_digits.copy()
      second_operand_digits = o2_digits.copy()

    return first_operand_digits, second_operand_digits

  @staticmethod
  def max(first_digits: list[int], second_digits: list[int], length: int = 0):
    bigger_num_digits = None
    smaller_num_digits = None
    sign = 1

    for i in range(length):
      if first_digits[i] > second_digits[i]:
        bigger_num_digits = first_digits
        smaller_num_digits = second_digits
        break
      elif first_digits[i] < second_digits[i]:
        bigger_num_digits = second_digits
        smaller_num_digits = first_digits
        sign = -1
        break
    return bigger_num_digits, smaller_num_digits,sign
