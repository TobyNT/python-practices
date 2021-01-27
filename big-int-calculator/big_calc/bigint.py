class BigInt:
  __digits: list[int]

  def __init__(self, digits: list[int]):
    super().__init__()
    self.__digits = digits.copy()

  @classmethod
  def fromStr(cls, value: str):
    validValue = cls.validate_input_value(value)
    return cls(cls.create_digits_from_str(validValue))

  @property
  def digits(self) -> list[int]:
    return self.__digits.copy()
  
  @staticmethod
  def validate_input_value(value: str ) -> str:
    if not isinstance(value, str):
      raise Exception("Not a string")

    for c in value:
      if not c.isdigit():
        raise Exception("Not a number")

    return value.strip()

  @staticmethod
  def create_digits_from_str(value: str) -> list[int]:
    non_zero = False
    result = []

    for c in value:
      if non_zero:
        result.append(int(c))
      else:
        if c != '0':
          non_zero = True
          result.append(int(c))
    
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
    o1_digits, o2_digits = BigInt.prepare_operands(self.__digits, another.__digits)
    result = []
    length = len(o1_digits)
    rem_num = 0

    for i in  reversed(range(length)):
      subtotal = o1_digits[i] + o2_digits[i] + rem_num

      if (subtotal > 9):
        rem_num = 1
        subtotal = subtotal % 10
      else:
        rem_num = 0
      result.insert(0, subtotal)
    
    if rem_num > 0:
      result.insert(0, 1)
    
    return BigInt(result)

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
      second_operand_digits = [0] * distance + o2_digits
    elif distance < 0:
      max = second_operand_len
      second_operand_digits = o2_digits.copy()
      first_operand_digits = [0] * distance + o1_digits
    else:
      first_operand_digits = o1_digits.copy()
      second_operand_digits = o2_digits.copy()

    return first_operand_digits, second_operand_digits


