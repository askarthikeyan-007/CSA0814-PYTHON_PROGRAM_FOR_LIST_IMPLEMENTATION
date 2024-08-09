from collections import defaultdict
words = ["listen", "silent", "enlist", "hello",  "drowl"]
ag = defaultdict(list)
for word in words:
    ssorted = ''.join(sorted(word))
    ag ssorted.append(word)
ag = dict(ag)
print(ag)