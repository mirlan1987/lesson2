s = "Everyone underwent something that changed him"
d = s.split(" ")
[x for x in d if len(x)==max(map(len, d))]
['underwent', 'something']
