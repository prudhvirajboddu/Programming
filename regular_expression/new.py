import re
sentence="randomized text to search in using regular expressions . period a interstenda 123964.sajf"
p=re.compile(r'sa')
m=p.finditer(sentence)
for ma in m:
    print(ma)
