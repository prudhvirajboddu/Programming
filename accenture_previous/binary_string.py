s="0C1A1B1C1C1B0A0"
ans=int(s[0])
for i in range(1,len(s)-1):
    if s[i]=='A':
        ans=ans&int(s[i+1])
    elif s[i]=='B':
        ans=ans|int(s[i+1])
    elif s[i]=='C':
        ans=ans^int(s[i+1])

print(ans)