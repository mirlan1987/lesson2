import re
 
for s in re.findall('e[qazxsweryuijjgfdcvbno]*?[awedcvgyuj]', 'Everyone underwent something that changed him.', re.I):
    print(s)
