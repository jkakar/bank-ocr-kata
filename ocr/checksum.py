import operator
from re import compile


ACCOUNT_REGEXP = compile(r'^[0-9]{9}$')


def check_account(account):
    if not ACCOUNT_REGEXP.match(account):
        return False
    checksum = []
    for i, character in enumerate(reversed(account)):
        number = int(character)
        checksum.append(number + i + 2 if i < 8 else number)
    checksum = reduce(operator.mul, checksum)
    return checksum % 11 == 0
