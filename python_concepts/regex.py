import re
# from typing import Protocol
# from typing import Pattern
text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCabc
mabcbac
.123-1234

'''

pattern=re.compile('[0-9][0-9][0-9]')

matches=pattern.finditer(text_to_search)

print(*(matches))

print(text_to_search[48:51])

