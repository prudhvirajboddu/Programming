from collections import Counter
from typing import Container

base="give me one grand today night"

adjust="give one grand today"

print(Counter(adjust))

print(Counter(base))

print(Counter(base)-Counter(adjust))
