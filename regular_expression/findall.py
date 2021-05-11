import re
# from datetime import datetime
i="is one of the 02-03-1945 and me is 31-04-1945"
s=set()
l=re.findall(r'[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]',i) #Matchin the pattern of the date to lookup in the string 
for i in l:
    s.add(i[6:]) #Finding the dates  and adding to sets to find only unique years
print(s)
print(len(s))
"""
Find the distinct years in a string where the format is DD-MM-YYYY
"""