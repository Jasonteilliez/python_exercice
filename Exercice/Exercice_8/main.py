def domain_name(url):
    a = url.split('//')
    if a[0] == "http:" or a[0] == "https:":
        a = a[1].split('.')
    else :
        a = a[0].split('.')
    if a[0] == "www":
        return a[1]
    return a[0]


def domain_name2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

def domain_name3(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]


print(domain_name('https://www.codewars.com/kata/'))