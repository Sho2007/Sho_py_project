name_coffee = "---Welcome to Sho's Coffee---\n"  #HELLO
name_menu = """\n---Choose the menu---
1. Espresso
2. Cappucino
3. Latte
4. Green tea"""
name_type = "---Choose the type of the coffee---"
#file
ggg = ["1"]
#fuction 
def crash():
    while True:
        break
#1
print(name_coffee)
open_menu = input('Please type 1 to show menu: ')
while True:
    if open_menu in ggg:
        print("")
        break
    else:
        crash()
    
# list-----------------------------------------
menu_list = ()
type_list = ()
bath_list = ()
money = ()

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
        print('Not enough money 🙁 ')
    break
while money_pay > money:
    if money_pay > money:
        print('You recieved a change of %s baht.\n\n ---Thank you :D---' % over_paid)
    break
while money_pay == money:
    if money_pay == money:
        print('---Thank you :D---')
        break