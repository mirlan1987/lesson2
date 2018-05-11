import re
s = "The;longest;word;here"
string = re.findall(r'[^;]+',s)
print (string)
maxlen = max(len(word) for word in string)
print (maxlen)
print ([word for word in string if len(word) == maxlen])
