print('''
welcome
1.search
2.insert
3.delete
4.exit
''')
addressBook={}
while 1:
    temp = int(input('num:'))
    if temp <1 or temp > 4:
        print('error,try again')
        continue
    if temp == 4:
        print('阿里嘎多')
        break
    name = input('enter name:')
    if temp == 1:
        if name in addressBook:
            print(name,",",addressBook[name])
            continue
        else:
            print('none')
    if temp == 2:
        if name in addressBook:
            print('exist',name,addressBook[name])
            isEdit = input('edit?(N/Y')
            if isEdit=='Y'or isEdit == 'y':
                userPhone = input('enter phone number')
                addressBook[name] = userPhone
                print('success')
                continue
            else:continue
        else:
            userPhone = input('enter phone number')
            addressBook[name] = userPhone
            print('success')
            continue
    if temp ==3:
        if name in addressBook:
            del addressBook[name]
            continue
        else:
            print('not exist')