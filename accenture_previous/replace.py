from collections import Counter
s="abbceww"
q=dict(Counter(s))
d=sorted(q.items(),key=lambda x:ord(x[0]),reverse=False)
d=dict(d)
print(d.get('a'))
for i,j in enumerate(d):
    if d[j]>2:
        pass
        # s.replace(d[i],'t')
        # break

print(s)
