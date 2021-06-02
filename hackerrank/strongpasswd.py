import re
def minimumNumber(n, password):
    p=["[\d]", "[A-Z]", "[a-z]", "[!@#$%^&*()+-]"]
    return max(6-n,sum([1 for i in p if not re.search(i, password)]))
print(minimumNumber(11,"Abc1"))