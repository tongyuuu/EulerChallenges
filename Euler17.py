

ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}



def saynumber(i):
    if i < 0:
        return _join('negative', _say_number_pos(-i))
    if i == 0:
        return 'zero'
    return _say_number_pos(i)
def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i//10],ones[i % 10])
    if i == 100:
        return 'one hundred'
    if i == 200:
        return 'two hundred'
    if i == 300:
        return 'three hundred'
    if i == 400:
        return 'four hundred'
    if i == 500:
        return 'five hundred'
    if i == 600:
        return 'six hundred'
    if i == 700:
        return 'seven hundred'
    if i == 800:
        return 'eight hundred'
    if i == 900:
        return 'nine hundred'
    if i < 1000:
        return _divide(i, 100, 'hundredand')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )


def _join(*args):
    return ' '.join(filter(bool, args))

y = 1
g = 0
while y <= 1000:
    a = saynumber(y)
    m = sum(len(x) for x in a.split())
    g = g + m
    y = y+1
print(g)

    
