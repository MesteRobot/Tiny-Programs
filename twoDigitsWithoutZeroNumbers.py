def digits(num):
    digits = set()
    while num>0:
        digits.add(num%10)
        num//=10
    return digits


def is_two_digits(x: set) -> bool:
    if len(x)!=2:
        return False
    return True

def contain_zero(x: set) -> bool:
    zero = {0}
    if x.issuperset(zero):
        return False
    return True


count = 0
for i in range(100,1000):
    digit = digits(i)
    if contain_zero(digit):
        if is_two_digits(digit):
            count+=1
    
print(count)
