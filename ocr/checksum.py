import operator
from re import compile


ACCOUNT_REGEXP = compile(r'^[0-9]{9}$')


def check_account(account):
    """Determine whether an account number is valid.

    A checksum is calculated using the following rules::

      account number:  3  4  5  8  8  2  8  6  5
      position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1

      checksum calculation:
      (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0
    """
    if not ACCOUNT_REGEXP.match(account):
        return False
    checksum = []
    for i, character in enumerate(reversed(account)):
        number = int(character)
        checksum.append(number + i + 2 if i < 8 else number)
    checksum = reduce(operator.mul, checksum)
    return checksum % 11 == 0
