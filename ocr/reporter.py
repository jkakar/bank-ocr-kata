from parser import parse_ocr
from checksum import check_account


CODES = {None: 'ILL',
         True: '',
         False: 'ERR'}

def generate_report(directory):
    results = []
    for ocr in directory:
        account_num = parse_ocr(ocr)
        valid = None
        if "?" not in account_num:
            valid = check_account(account_num)
        results.append((CODES[valid], account_num))

    return results
