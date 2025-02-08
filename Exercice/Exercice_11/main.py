def alphanumeric(password):
    for x in password:
        if x not in "1234568790AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn":
            return False
    return password != ""

def alphanumeric2(string):
    return string.isalnum()

print(alphanumeric(""))