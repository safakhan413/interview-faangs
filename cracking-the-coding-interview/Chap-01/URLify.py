import re

def URLify(s1):
    return re.sub(' ', '%20',s1)

s1 = 'Mr John Smith'
print(URLify(s1))
