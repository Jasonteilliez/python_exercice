def valid_braces(string):
    b = ""

    for c in string:
        if c == "(" or c == "{" or c == "[":
            b += c
        elif c == ")" and len(b)> 0 and b[-1] == "(":
            b= b[:-1]
        elif c == "]" and len(b)> 0 and b[-1] == "[":
            b= b[:-1]
        elif c == "}" and len(b)> 0 and b[-1] == "{":
            b= b[:-1]
        else :
            return False

    return b==''
    
def valid_braces2(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0 

def valid_braces3(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


braces = "([{}])"
print(valid_braces(braces))