def narcissistic( value ):
    r = 0
    for n in str(value) :
        r += int(n)**len(str(value))
    return r == value

def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


value = 153
print(narcissistic( value ))