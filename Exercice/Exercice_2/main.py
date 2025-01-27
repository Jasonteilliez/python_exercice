def filter_list(l):
    return [x for x in l if isinstance(x, int)]

def filter_list2(l):
  return [x for x in l if type(x) is not str]

def filter_list3(l):
  return list(filter(lambda x: isinstance(x, int), l))

def filter_list4(l):
    new_list = []
    for x in l:
        if type(x) == str:
            new_list.append(x)
    return new_list
             
    

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))