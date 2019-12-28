from ticTacToeAI import *

pos = [" ", " ", " ",
       " ", " ", " ",
       " ", " ", " "]
if(str(input("do you want to start(y/n): ")) == "y"):
    turn = 0
else:
    turn = 1
flag = -1
count = 0
newInput = -1


while(flag < 0 and count < 9):
    print("*" * 20)
    print(" " + str(pos[0]) + " | " + str(pos[1]) + " | " + str(pos[2]) + "\n")
    print("-----------\n")
    print(" " + str(pos[3]) + " | " + str(pos[4]) + " | " + str(pos[5]) + "\n")
    print("-----------\n")
    print(" " + str(pos[6]) + " | " + str(pos[7]) + " | " + str(pos[8]) + "\n")
    if(turn == 0):
        newInput = int(input("Enter your position Player (x): "))
        pos[newInput - 1] = "x"
        turn = 1
    else:
        newInput = inputsai(pos)
        pos[newInput] = "o"
        turn = 0

    #check current state
    if(pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] ):
        if(pos[0] == pos[3] == pos[6] == "x" 
        or pos[1] == pos[4] == pos[7] == "x" 
        or pos[2] == pos[5] == pos[8] == "x" ):
            flag = 0
        elif(pos[0] == pos[3] == pos[6] == "o"
          or pos[1] == pos[4] == pos[7] == "o"
          or pos[2] == pos[5] == pos[8] == "o" ):
            flag = 1
    
    elif(pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] ):
        if(pos[0] == pos[1] == pos[2] == "x"
        or pos[3] == pos[4] == pos[5] == "x"
        or pos[6] == pos[7] == pos[8] == "x"):
            flag = 0
        elif(pos[0] == pos[1] == pos[2] == "o"
          or pos[3] == pos[4] == pos[5] == "o"
          or pos[6] == pos[7] == pos[8] == "o"):
            flag = 1
    
    elif(pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6]):
        if(pos[0] == pos[4] == pos[8] == "x"
        or pos[2] == pos[4] == pos[6] == "x"):
            flag = 0
        elif(pos[0] == pos[4] == pos[8] == "o"
          or pos[2] == pos[4] == pos[6] == "o"):
            flag = 1

    count = count + 1

print("*" * 20)
print(" " + str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]) + "\n")
print(" " + str(pos[3]) + " " + str(pos[4]) + " " + str(pos[5]) + "\n")
print(" " + str(pos[6]) + " " + str(pos[7]) + " " + str(pos[8]) + "\n")

#RESULTS after loop terminate
if(flag == 0):
    print("Player x Winner")
elif(flag == 1):
    print("Player o Winner")
else:
    print("DRAW")


        
    
