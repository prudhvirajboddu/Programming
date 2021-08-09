import re
# from typing import Protocol
# from typing import Pattern
text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCabc
mabcbac
'''

pattern=re.compile('abc')

matches=pattern.finditer(text_to_search)

print(*(matches))

print(text_to_search[1:4])

print(text_to_search[2:5])
