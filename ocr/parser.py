from collections import defaultdict

NUMBERS = {
    ' _ | ||_|': '0',
    '     |  |': '1',
    ' _  _||_ ': '2',
    ' _  _| _|': '3',
    '   |_|  |': '4',
    ' _ |_  _|': '5',
    ' _ |_ |_|': '6',
    ' _   |  |': '7',
    ' _ |_||_|': '8',
    ' _ |_| _|': '9',
}

def parse_ocr(text):
    characters = defaultdict(str)
    for line in text.split('\n'):
        i = 0
        for j, character in enumerate(line):
            if j % 3 == 0:
                i += 1
            characters[i] += character

    account_num = []
    for char in characters.values():
        account_num.append(NUMBERS[char])

    return ''.join(account_num)
