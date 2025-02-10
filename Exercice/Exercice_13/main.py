# 1
def prime_factors(num):
    factors = dict()
    factor = 3
    z=""

    while num % 2 == 0 :
        if 2 in factors:
            factors[2] +=1
        else :
            factors[2] = 1
        num = num // 2

    while abs(num) >= 3:
        if (num % factor == 0) :
            if factor in factors:
                factors[factor] +=1
            else :
                factors[factor] = 1
            num = num / factor
        else :
            factor += 2 

    for key, value in factors.items():
        if value > 1:
            z+= "({}**{})".format(key,value)
        else:
            z+="({})".format(key)

    return z

# 3
def prime_factors2(num):
    factor = 3
    z=""
    k=0

    while num % 2 == 0 :
        k+=1
        num = num // 2
    if k==1:
        z+="({})".format(2)
    elif k>1:
        z+= "({}**{})".format(2,k)

    while abs(num) >= 3:
        k=0
        while (num % factor == 0) :
            k+=1
            num = num / factor
        if k==1:
            z+="({})".format(factor)
        elif k>1:
            z+= "({}**{})".format(factor,k)
        factor += 2 
        
    return z

# 4
def prime_factors3(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r
        
# 2   
def prime_factors4(n):
  result = ''
  fac = 2
  while fac <= n:
    count = 0
    while n % fac == 0:
      n /= fac
      count += 1
    if count:
      result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
    fac += 1
  return result



print(prime_factors(86240))