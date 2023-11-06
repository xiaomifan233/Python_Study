import re

list1 = []
pwds = input('请输入密码')
for pwd in pwds.split(','):
    if len(pwd) < 6 or len(pwd) > 12:
        continue
    if not re.search("[a-z]", pwd):
        continue
    if not re.search("[A-Z]", pwd):
        continue
    if not re.search("[0-9]", pwd):
        continue
    if not re.search("[@#$]", pwd):
        continue
    else:
        list1.append(pwd)
print(list1)
# ABd1234@1,a E1#，2w3E*，2We3345
