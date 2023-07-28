D = '999999999'
d = '99999'
# D = '222399293923493'
# d = '323939'
# D = '2332323239492394'
# d = '2332'

print('{} |{}'.format(D, d))

n = len(d)
m = len(D)

i = 0
d = int(d)
spaces = 0
partDiff = '0' 
quotient = ''
while i < m:
    # take digits from Dividend
    for j in range(1, m):
        partD = int(partDiff + D[i:i + j])
        if partD >= d or i + j >= m:
            break
        quotient += '0'
    i += j 
    if int(partDiff) == 0 and spaces != 0: spaces += 1
    print('{}{}'.format(spaces*' ', partD))
    # since we take at maximum n + 1 digits from D
    # and our divisor d has n digits, after
    # multiplying by 10, the divisor will have at 
    # most n + 1 digits (the appended 0 to d), so 
    # multiplying up to 9, will not provide more
    # than n digits
    for j in range(1, 11):
        if j*d > int(partD):
            q = j - 1
            part = d*q
            break
    quotient += str(q)
    spaces += len(str(partD)) - len(str(part))
    print('{}{}'.format(spaces*' ', part))
    # note that the diference has n or less digits, since
    # r < d, so we always indent one left
    partDiff = str(partD - part);
    spaces += len(str(part)) - len(str(partDiff))
    print('{}{}'.format(spaces*' ', partDiff))
        

print('\n{} == {}*{} + {}'.format(D, int(quotient), d, partDiff))
assert(int(D) == int(quotient)*d + int(partDiff))
