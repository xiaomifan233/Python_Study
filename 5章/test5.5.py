import re

x = 'This is is a desk'
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(x)
x = x.replace(matchResult.group(0),matchResult.group(1))
print(x)