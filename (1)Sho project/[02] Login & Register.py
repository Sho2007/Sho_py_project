a = ['s']  #    This is not update !!!
b = ['s']

login = ("""\n--       login       --""")
question = ("""Do you want to login or register ?
1. login
2. register\n""")
register = ("""--       Register       --""")

print(question)
ans = int(input('(1 or 2): '))

while ans == 1:
    print(login)
    put_user = input('Username: ')
    put_password = input('password: ')
    print("\n")

    if put_user in a:
        if put_password in b:
            print('Welcome to www.Sho_Office.com')
        else:
            print('Wrong password.')
    else:
        print('Not have this user in our server.')
    break


while ans == 2:
    print(register)
    put_user = input('Username: ')
    a.append(put_user)
    put_password = input('password: ')
    b.append(put_password)

    g1 = put_user
    g2 = put_password
    
    print(login)
    g1 = input('Username: ')
    g2 = input('password: ')
    print("\n")

    if g1 in a:
        if g2 in b:
            print('Welcome to www.Sho_Office.com')
        else:
            print('Wrong password.')
    else:
        print('Not have this user in our server.')
    break
