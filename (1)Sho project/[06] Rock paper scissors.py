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