import time
import random

#     file 
UI = ("""www.
  ___________     ______           
 /           \\   |    ||
/   _________||  |    ||
\  ||_________   |    || _______      _________
 \           \\\\  |    |/        \\\\   /         \\\\
  \_____     ||  |      ____     ||  |   __    ||
   _____|    ||  |     /    \    ||  |  ||_|   ||
  /          ||  |    ||    |    ||  |         ||
 |__________ //  |____||    |____||  \_________// Office.com""")

MENU = ("""
__________________________________________________________
|                                                         |
|  [1]  Cafe                                              |
|                                                         |
|  [2]  Login&Register                                    |
|                                                         |
|  [3]  Look like hacker                                  |
|                                                         |
|  [4]  Stop watch                                        |
|                                                         |
|  [5]  Tic tac toe                                       |
|                                                         |                                                         
|  [6]  Rock paper scissors                               |
|                                                         |
|  [7]  Soon..                                            |
|_________________________________________________________| 
""")
#   1
def cafe():
    name_coffee = "---Welcome to Sho's Coffee---\n"
    name_menu = """\n---Choose the menu---
    1. Espresso
    2. Cappucino
    3. Latte
    4. Green tea"""
    name_type = "---Choose the type of the coffee---"
    #1
    print(name_coffee)
    open_menu = int(input('Please type 1 to show menu: '))
    # list-----------------------------------------
    menu_list = ()
    type_list = ()
    bath_list = ()
    money = ()
    # Check1 complete
    while open_menu != int(1):
        if open_menu < int(1):
            break
    while open_menu != int(1):
        if open_menu > int(1):  
            break
    #2 
    print(name_menu)
    select_menu = int(input('\nSelect coffee: '))
    #--------------------------
    # check
    zzz = 1
    while zzz == 1:
        if select_menu != 1:
            break
        elif select_menu != 2:
            break
        elif select_menu != 3:
            break
        elif select_menu != 4:
            break
    # if menu
    if select_menu == int(1):
        menu_list = ('Espresso')
    elif select_menu == int(2):
        menu_list = ('Cappucino')
    elif select_menu == int(3):
        menu_list = ('Latte')
    elif select_menu == int(4):
        menu_list = ('Green tea')
    #--------------------------
    #3
    print(name_type)
    print("""
    1. Hot 55 baht
    2. Cold 60 baht\n""")
    #4
    select_choice = int(input('Select type: '))
    # Check
    while select_choice < int(2):
        if select_choice < int(2):
            break
    while select_choice > int(2):
        if select_choice > int(2):
            break
    if select_choice == int(1):
        type_list = ('Hot')
    else:
        type_list = ('Cold')
    if select_choice == int(1):
        bath_list = ('55')
    else:
        bath_list = ('60')
    if select_choice == int(1):
        money = int(55)
    else:
        money = int(60)
    #5
    print('---You choose %s %s %s baht---' %(menu_list,type_list,bath_list))
    # pay
    money_pay = int(input('\nInput your money: '))
    # count money
    over_paid = money_pay - money
    while money_pay < money:
        if money_pay < money:
            print('Not enough money :( ')
        break
    while money_pay > money:
        if money_pay > money:
            print('You recieved a change of %s baht.\n\n ---Thank you :D---' % over_paid)
        break
    while money_pay == money:
        if money_pay == money:
            print('---Thank you :D---')
            break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#   2
def login():
    a = ['Sho']
    b = ['22072007']

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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 3

def look():
    import time
    #----------
    word = "  -- Welcome to www.Sho_Office.com  -- \n"
    a = (0)
    w1 = (0)
    # start
    print(word)
    yn = input("Do you want to hack?  (yes/no): ") 

    #----------check------

    while w1 == 0:
        if yn == "yes":
            print('\n   --   Dowloading information...   --   ')
            w1 = w1 + 1
            if yn == "no":
                break
                

    # loading -------
    while a < 10:
        print('[]', end = '')
        time.sleep(0.5)
        print('[]', end = '')
        time.sleep(0.5)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.5)
        print('[]', end = '')
        time.sleep(0.5)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.4)
        print('[]', end = '')
        time.sleep(0.4)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.4)
        print('[]', end = '')
        time.sleep(0.3)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.2)
        print('[]', end = '')
        time.sleep(0.2)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.2)
        print('[]', end = '')
        time.sleep(0.2)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.1)
        print('[]', end = '')
        time.sleep(0.1)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.1)
        print('[]', end = '')
        time.sleep(0.1)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.1)
        print('[]', end = '')
        time.sleep(0.1)
        a = a + 1
        print('[]', end = '')
        time.sleep(0.1)
        print('[]', end = '')
        time.sleep(0.1)
        a = a + 1

        if a == 10:
            print('', end = '       [ -- dowloading 100% -- ]\n\n')

    #show
    time.sleep(0.5)
    print("""
    ----- IP -----

    city: Roi-et
    regoin_name: -
    area_code: -
    longitude: -
    country_code2: TH
    latitude: -
    postal_code: 4500
    dma_code: -""")
    time.sleep(0.2)
    print("""
    ----- User profile -----
        All User Profile    : Sho
        <None>""")
    time.sleep(0.5)
    print("""
    =======================================================================

    Applied: All User Profile

    Profile information""")
    time.sleep(0.2)
    print("""
    -------------------
        Version                : 1
        Type                   : Wireless LAN
        Name                   : Shota
        Control options        : <None>
            Connection mode    : Connect automatically
            Network broadcast  : Connect only if this network is broadcasting
            AutoSwitch         : Do not switch to other networks
            MAC Randomization  : Disabled""")
    time.sleep(0.4)
    print("""
    Connectivity settings
    ---------------------""")
    time.sleep(0.2)
    print("""
    Number of SSIDs            : 1
        SSID name              : "Sho"
        Network type           : Infrastructure
        Radio type             : [ Any Radio Type ]
        Vendor extension       : Not present
    """)
    time.sleep(0.4)
    print("""Security settings
    -----------------
        Authentication         : WPA2-Personal
        Cipher                 : CCMP
        Authentication         : WPA2-Personal
        Cipher                 : GCMP
        Security key           : Present
        Key Content            : <None>""")
    time.sleep(0.2)
    print("""Cost settings
    -------------
        Cost                   : Unrestricted
        Congested              : No
        Approaching Data Limit : No
        Over Data Limit        : No
        Roaming                : No
        Cost Source            : Default""")
# - - - - - - - -- - - -- - - - - - - - - - - - - - - - - - -

#    4
def watch():
    import time

    output = float(0.00) #วิและนาที
    hour = int(0) #ตัวบอกชม.
    t_m = int(0) #ตัวบอกจำนวนวิเพื่อเปลี่ยนเป็นนาที
    t_h = int(0) #ตัวบอกจำนวนนาทีเพื่อเปลี่ยนเป็นชม.

    start = int(0)
    while start != 1:
        time.sleep(1)
        output = output + float(0.01)
        t_m = t_m + int(1)
        print('[%d hour] %.2f min' %(hour,output))
        if t_m == int(60): #func change in to min
            output = output - float(0.60)#เปลี่ยนเป็นนาที
            output = output + float(1.00)
            t_h = t_h + int(1)
            t_m = t_m - t_m #close
        elif t_h == int(60):#print the hour
            hour = hour + int(1)
            output = output - float(60.00)
            print('[%d hour] %.2f min' %(hour,output))
            t_h = t_h - t_h#close
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#    5
def ttt():
    #                         ----- File -----
    op_xo = (
    "_"+'a1'+"_|_"+'a2'+"_|_"+'a3\n'+
    "_"+'a4'+"_|_"+'a5'+"_|_"+'a6\n'+
    "_"+'a7'+"_|_"+'a8'+"_|_"+'a9')

    conx = 'Congratulation player X win!!!'
    cono = 'Congratulation player O win!!!'
    #show
    print(op_xo)
    #1111-------------------------------------------------------------------

    ch1 = input('Type your charactor (x/o): ')
    where1 = input('Where do you want to put: ')
    a = 1

    while a == 1:
        if ch1 == "x" or"o" :
            if where1 == ('a1'):
                v1 = op_xo.replace('a1',str(ch1))
                print(v1)
                break
            if where1 == ('a2'):
                v1 = op_xo.replace('a2',str(ch1))
                print(v1)
                break
            if where1 == ('a3'):
                v1 = op_xo.replace('a3',str(ch1))
                print(v1)
                break
            if where1 == ('a4'):
                v1 = op_xo.replace('a4',str(ch1))
                print(v1)
                break
            if where1 == ('a5'):
                v1 = op_xo.replace('a5',str(ch1))
                print(v1)
                break
            if where1 == ('a6'):
                v1 = op_xo.replace('a6',str(ch1))
                print(v1)
                break
            if where1 == ('a7'):
                v1 = op_xo.replace('a7',str(ch1))
                print(v1)
                break
            if where1 == ('a8'):
                v1 = op_xo.replace('a8',str(ch1))
                print(v1)
                break
            if where1 == ('a9'):
                v1 = op_xo.replace('a9',str(ch1))
                print(v1)
                break
    #22222----------------------------------------------------------
    ch2 = input('Type your charactor (x/o): ')
    where2 = input('Where do you want to put: ')
    a = a + 1

    while a == 2:
        if ch2 == "x" or"o" :
            if where2 == ('a1'):
                v2 = v1.replace('a1',str(ch2))
                print(v2)
                break
            if where2 == ('a2'):
                v2 = v1.replace('a2',str(ch2))
                print(v2)
                break
            if where2 == ('a3'):
                v2 = v1.replace('a3',str(ch2))
                print(v2)
                break
            if where2 == ('a4'):
                v2 = v1.replace('a4',str(ch2))
                print(v2)
                break
            if where2 == ('a5'):
                v2 = v1.replace('a5',str(ch2))
                print(v2)
                break
            if where2 == ('a6'):
                v2 = v1.replace('a6',str(ch2))
                print(v2)
                break
            if where2 == ('a7'):
                v2 = v1.replace('a7',str(ch2))
                print(v2)
                break
            if where2 == ('a8'):
                v2 = v1.replace('a8',str(ch2))
                print(v2)
                break
            if where2 == ('a9'):
                v2 = v1.replace('a9',str(ch2))
                print(v2)
                break
    #33333333-----------------------------------------------
    ch3 = input('Type your charactor (x/o): ')
    where3 = input('Where do you want to put: ')
    a = a + 1

    while a == 3:
        if ch3 == "x" or"o" :
            if where3 == ('a1'):
                v3 = v2.replace('a1',str(ch3))
                print(v3)
                break
            if where3 == ('a2'):
                v3 = v2.replace('a2',str(ch3))
                print(v3)
                break
            if where3 == ('a3'):
                v3 = v2.replace('a3',str(ch3))
                print(v3)
                break
            if where3 == ('a4'):
                v3 = v2.replace('a4',str(ch3))
                print(v3)
                break
            if where3 == ('a5'):
                v3 = v2.replace('a5',str(ch3))
                print(v3)
                break
            if where3 == ('a6'):
                v3 = v2.replace('a6',str(ch3))
                print(v3)
                break
            if where3 == ('a7'):
                v3 = v2.replace('a7',str(ch3))
                print(v3)
                break
            if where3 == ('a8'):
                v3 = v2.replace('a8',str(ch3))
                print(v3)
                break
            if where3 == ('a9'):
                v3 = v2.replace('a9',str(ch3))
                print(v3)
                break

    #4444444----------------------------
    ch4 = input('Type your charactor (x/o): ')
    where4 = input('Where do you want to put: ')
    a = a + 1

    while a == 4:
        if ch4 == "x" or"o" :
            if where4 == ('a1'):
                v4 = v3.replace('a1',str(ch4))
                print(v4)
                break
            if where4 == ('a2'):
                v4 = v3.replace('a2',str(ch4))
                print(v4)
                break
            if where4 == ('a3'):
                v4 = v3.replace('a3',str(ch4))
                print(v4)
                break
            if where4 == ('a4'):
                v4 = v3.replace('a4',str(ch4))
                print(v4)
                break
            if where4 == ('a5'):
                v4 = v3.replace('a5',str(ch4))
                print(v4)
                break
            if where4 == ('a6'):
                v4 = v3.replace('a6',str(ch4))
                print(v4)
                break
            if where4 == ('a7'):
                v4 = v3.replace('a7',str(ch4))
                print(v4)
                break
            if where4 == ('a8'):
                v4 = v3.replace('a8',str(ch4))
                print(v4)
                break
            if where4 == ('a9'):
                v4 = v3.replace('a9',str(ch4))
                print(v4)
                break

    #5555555--------------------------------

    ch5 = input('Type your charactor (x/o): ')
    where5 = input('Where do you want to put: ')
    a = a + 1

    while a == 5:
        if ch5 == "x" or"o" :
            if where5 == ('a1'):
                v5 = v4.replace('a1',str(ch5))
                print(v5)
                break
            if where5 == ('a2'):
                v5 = v4.replace('a2',str(ch5))
                print(v5)
                break
            if where5 == ('a3'):
                v5 = v4.replace('a3',str(ch5))
                print(v5)
                break
            if where5 == ('a4'):
                v5 = v4.replace('a4',str(ch5))
                print(v5)
                break
            if where5 == ('a5'):
                v5 = v4.replace('a5',str(ch5))
                print(v5)
                break
            if where5 == ('a6'):
                v5 = v4.replace('a6',str(ch5))
                print(v5)
                break
            if where5 == ('a7'):
                v5 = v4.replace('a7',str(ch5))
                print(v5)
                break
            if where5 == ('a8'):
                v5 = v4.replace('a8',str(ch5))
                print(v5)
                break
            if where5 == ('a9'):
                v5 = v4.replace('a9',str(ch5))
                print(v5)
                break

    #66666-------------------------------------------
    ch6 = input('Type your charactor (x/o): ')
    where6 = input('Where do you want to put: ')
    a = a + 1

    while a == 6:
        if ch6 == "x" or"o" :
            if where6 == ('a1'):
                v6 = v5.replace('a1',str(ch6))
                print(v6)
                break
            if where6 == ('a2'):
                v6 = v5.replace('a2',str(ch6))
                print(v6)
                break
            if where6 == ('a3'):
                v6 = v5.replace('a3',str(ch6))
                print(v6)
                break
            if where6 == ('a4'):
                v6 = v5.replace('a4',str(ch6))
                print(v6)
                break
            if where6 == ('a5'):
                v6 = v5.replace('a5',str(ch6))
                print(v6)
                break
            if where6 == ('a6'):
                v6 = v5.replace('a6',str(ch6))
                print(v6)
                break
            if where6 == ('a7'):
                v6 = v5.replace('a7',str(ch6))
                print(v6)
                break
            if where6 == ('a8'):
                v6 = v5.replace('a8',str(ch6))
                print(v6)
                break
            if where6 == ('a9'):
                v6 = v5.replace('a9',str(ch6))
                print(v6)
                break

    #777777-------------------------------------------

    ch7 = input('Type your charactor (x/o): ')
    where7 = input('Where do you want to put: ')
    a = a + 1

    while a == 7:
        if ch7 == "x" or"o" :
            if where7 == ('a1'):
                v7 = v6.replace('a1',str(ch7))
                print(v7)
                break
            if where7 == ('a2'):
                v7 = v6.replace('a2',str(ch7))
                print(v7)
                break
            if where7 == ('a3'):
                v7 = v6.replace('a3',str(ch7))
                print(v7)
                break
            if where7 == ('a4'):
                v7 = v6.replace('a4',str(ch7))
                print(v7)
                break
            if where7 == ('a5'):
                v7 = v6.replace('a5',str(ch7))
                print(v7)
                break
            if where7 == ('a6'):
                v7 = v6.replace('a6',str(ch7))
                print(v7)
                break
            if where7 == ('a7'):
                v7 = v6.replace('a7',str(ch7))
                print(v7)
                break
            if where7 == ('a8'):
                v7 = v6.replace('a8',str(ch7))
                print(v7)
                break
            if where7 == ('a9'):
                v7 = v6.replace('a9',str(ch7))
                print(v7)
                break
    #8888888---------------------------------------------------

    ch8 = input('Type your charactor (x/o): ')
    where8 = input('Where do you want to put: ')
    a = a + 1

    while a == 8:
        if ch8 == "x" or"o" :
            if where8 == ('a1'):
                v8 = v7.replace('a1',str(ch8))
                print(v8)
                break
            if where8 == ('a2'):
                v8 = v7.replace('a2',str(ch8))
                print(v8)
                break
            if where8 == ('a3'):
                v8 = v7.replace('a3',str(ch8))
                print(v8)
                break
            if where8 == ('a4'):
                v8 = v7.replace('a4',str(ch8))
                print(v8)
                break
            if where8 == ('a5'):
                v8 = v7.replace('a5',str(ch8))
                print(v8)
                break
            if where8 == ('a6'):
                v8 = v7.replace('a6',str(ch8))
                print(v8)
                break
            if where8 == ('a7'):
                v8 = v7.replace('a7',str(ch8))
                print(v8)
                break
            if where8 == ('a8'):
                v8 = v7.replace('a8',str(ch8))
                print(v8)
                break
            if where8 == ('a9'):
                v8 = v7.replace('a9',str(ch8))
                print(v8)
                break

    #999999----------------------------------

    ch9 = input('Type your charactor (x/o): ')
    where9 = input('Where do you want to put: ')
    a = a + 1

    while a == 9:
        if ch9 == "x" or"o" :
            if where9 == ('a1'):
                v9 = v8.replace('a1',str(ch9))
                print(v9)
                break
            if where9 == ('a2'):
                v9 = v8.replace('a2',str(ch9))
                print(v9)
                break
            if where9 == ('a3'):
                v9 = v8.replace('a3',str(ch9))
                print(v9)
                break
            if where9 == ('a4'):
                v9 = v8.replace('a4',str(ch9))
                print(v9)
                break
            if where9 == ('a5'):
                v9 = v8.replace('a5',str(ch9))
                print(v9)
                break
            if where9 == ('a6'):
                v9 = v8.replace('a6',str(ch9))
                print(v9)
                break
            if where9 == ('a7'):
                v9 = v8.replace('a7',str(ch9))
                print(v9)
                break
            if where9 == ('a8'):
                v9 = v8.replace('a8',str(ch9))
                print(v9)
                break
            if where9 == ('a9'):
                v9 = v8.replace('a9',str(ch9))
                print(v9)
                break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#   6
def RPS():
    import random
    import time

    #     add  R.P.S
    if_rock = ()
    if_paper = ()
    if_scissors = ()

    #    file 

    RPS1 = ["Rock","Paper","Scissors"]
    RPS2 = ["Rock","Paper","Scissors"]

    q1 = "What your name: "
    q2 = "and another player: "

    r = "Rock"
    p = "Paper"
    s = "Scrissors"

    #   start
    p1 = input(q1)
    p2 = input(q2)

    print("""

    """)
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    print("""

    """)
    random.shuffle(RPS1)
    random.shuffle(RPS2)

    print(str(p1) + ":" + str(RPS1[0]))
    print(""" """)
    print(str(p2) + ":" + str(RPS2[0]))

    #  Check
    print("""
    ---------------------------""")
    if RPS1[0] == "Rock":
        if RPS2[0] == "Scissors":
            print(str(p1) + " won!!")

    if RPS1[0] == "Rock":
        if RPS2[0] == "Paper":
            print(str(p2) + " won!!")

    if RPS1[0] == "Scissors":
        if RPS2[0] == "Rock":
            print(str(p2) + " won!!")

    if RPS1[0] == "Scissors":
        if RPS2[0] == "Paper":
            print(str(p1) + " won!!")


    if RPS1[0] == "Paper":
        if RPS2[0] == "Scissors":
            print(str(p2) + " won!!")

    if RPS1[0] == "Paper":
        if RPS2[0] == "Rock":
            print(str(p1) + " won!!")




    # Check draw

    if RPS1[0] == "Rock":
        if RPS2[0] == "Rock":
            print("Draw")

    if RPS1[0] == "Scissors":
        if RPS2[0] == "Scissors":
            print("Draw")

    if RPS1[0] == "Paper":
        if RPS2[0] == "Paper":
            print("Draw")

# - - - - - - - - - - - - - - - - - - - - - - - -  - -
#   end


#   start 
print(UI)
print(MENU)
MENU_Q = int(input("What number menu do you want?: "))
print(""" """)
open1 = int(1)

#  CHECK MENU
while open1 == 1:
    if MENU_Q == int(1):
        cafe()
        break
    elif MENU_Q == 2:
        login()
        break
    elif MENU_Q == 3:
        look()
        break
    elif MENU_Q == 4:
        watch()
        break
    elif MENU_Q == 5:
        ttt()
        break
    elif MENU_Q == 6:
        RPS()
        break
    else:
        print("We don't have this menu.")
        break
