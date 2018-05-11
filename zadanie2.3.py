import re
s = "I reject your reality and substitute my own!"
words = re.sub("[^\w]", " ",  s).split()
t = [v for v in words if len(v) == len(min(words))]
from itertools import groupby
t1 = {k:list(v) for k,v in groupby(sorted(words, key=len), len)}

print(t1[min(t1)], t)
