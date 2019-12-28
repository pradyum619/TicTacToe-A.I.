#computer symbol is "o"
#pass inputs as a list of 9 elements
#empty boxes must be stored as " "(space)
#this function returns position number of computer's input in game
#pos = [0, 1, 2,
#       3, 4, 5,
#       6, 7, 8]

def inputsai(pos):
        
    # calculate number of inputs
    nulls = 0
    for i in pos:
        if( i == " "):
            nulls = nulls +1
    inputItem = 9-nulls

    #for zero inputs
    if(inputItem == 0):
        return 4

    #for one input
    if(inputItem == 1):
        if( pos[4] != " " ):
            return 0
        else:
            return 4

    #for two inputs
    if(inputItem == 2):
        if(pos[1] or pos[3] == "x"):
            return 0
        elif(pos[5] or pos[7] == "x"):
            return 8
        elif(pos[0] == "x"):
            return 8
        elif(pos[8] == "x"):
            return 0
        elif(pos[2] == "x"):
            return 6
        elif(pos[6] == "x"):
            return 2

    #for three inputs
    if(inputItem == 3):
        if( pos[4] == "x"):
            if( pos[2] or pos[8]  == "x"):
                return 6
            elif( pos[6] == "x"):
                return 2
            elif( pos [1] == "x"):
                return 7
            elif( pos [7] == "x"):
                return 1
            elif( pos [3] == "x"):
                return 5
            elif( pos [5] == "x"):
                return 3
        
        if( pos[4] == "o"):
            if( pos[0] == "x"):
                if( pos[1] == "x"):
                    return 2
                elif( pos[2] == "x"):
                    return 1
                elif( pos[3] == "x"):
                    return 6
                elif( pos[6] == "x"):
                    return 3
                elif( pos[5] or pos[7] == "x" ):
                    return 8
                elif( pos[8] == "x"):
                    return 7
            
            if( pos[1] == "x"):
                if( pos[2] or pos[3] or pos[6] or pos[7] == "x"):
                    return 0
                elif( pos[5] or pos[8] == "x"):
                    return 2
            
            if( pos[2] == "x"):
                if( pos[3] == "x"):
                    return 0
                elif( pos[5] or pos[7] == "x"):
                    return 8
                elif( pos[6] == "x"):
                    return 7
                elif( pos[8] == "x"):
                    return 5
            
            if( pos[3] == "x"):
                if( pos[5] or pos[6] == "x"):
                    return 0
                elif( pos[7] or pos[8] == "x"):
                    return 6
            
            if( pos[5] == "x"):
                if( pos[6] or pos[7] == "x"):
                    return 8
                elif( pos[8] == "x"):
                    return 2
            
            if( pos[6] == "x"):
                if( pos[7] == "x"):
                    return 8
                elif( pos[8] == "x"):
                    return 7
            
            if( pos[7] and pos[8] == "x"):
                return 6
                
    
    #for four inputs
    if(inputItem == 4):
        if(pos[0] == "o" and pos[8] == " "):
            return 8
        if(pos[8] == "o" and pos[0] == " "):
            return 0
        
        if(pos[8] == "o" and pos[0] == "x" and pos[5] == "x"):
            return 7
        if(pos[8] == "o" and pos[0] == "x" and pos[7] == "x"):
            return 5
        if(pos[8] == "o" and pos[0] == "x" and pos[1] == "x"):
            return 2
        if(pos[8] == "o" and pos[0] == "x" and pos[2] == "x"):
            return 1
        if(pos[8] == "o" and pos[0] == "x" and pos[6] == "x"):
            return 3
        if(pos[8] == "o" and pos[0] == "x" and pos[3] == "x"):
            return 6
        
        if(pos[6] == "o" and pos[2] == "x" and pos[3] == "x"):
            return 7
        if(pos[6] == "o" and pos[2] == "x" and pos[7] == "x"):
            return 3
        if(pos[6] == "o" and pos[2] == "x" and pos[0] == "x"):
            return 1
        if(pos[6] == "o" and pos[2] == "x" and pos[1] == "x"):
            return 0
        if(pos[6] == "o" and pos[2] == "x" and pos[5] == "x"):
            return 8
        if(pos[6] == "o" and pos[2] == "x" and pos[8] == "x"):
            return 5
        
        if(pos[0] == "o" and pos[8] == "x" and pos[1] == "x"):
            return 3
        if(pos[0] == "o" and pos[8] == "x" and pos[3] == "x"):
            return 1
        if(pos[0] == "o" and pos[8] == "x" and pos[6] == "x"):
            return 7
        if(pos[0] == "o" and pos[8] == "x" and pos[7] == "x"):
            return 6
        if(pos[0] == "o" and pos[8] == "x" and pos[2] == "x"):
            return 5
        if(pos[0] == "o" and pos[8] == "x" and pos[5] == "x"):
            return 2

        if(pos[2] == "o" and pos[6] == "x" and pos[1] == "x"):
            return 5
        if(pos[2] == "o" and pos[6] == "x" and pos[5] == "x"):
            return 1
        if(pos[2] == "o" and pos[6] == "x" and pos[3] == "x"):
            return 0
        if(pos[2] == "o" and pos[6] == "x" and pos[0] == "x"):
            return 3
        if(pos[2] == "o" and pos[6] == "x" and pos[7] == "x"):
            return 8
        if(pos[2] == "o" and pos[6] == "x" and pos[8] == "x"):
            return 7

    #for five inputs
    if(inputItem == 5):
        #chec if comp. is winning
        #0 1 2
        if(pos[0] == pos[1] == "o" and pos[2] == " "):
            return 2
        elif(pos[0] == pos[2] == "o" and pos[1] == " "):
            return 1
        elif(pos[1] == pos[2] == "o" and pos[0] == " "):
            return 0

        #3 4 5 
        if(pos[3] == pos[4] == "o" and pos[5] == " "):
            return 5
        elif(pos[3] == pos[5] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[5] == "o" and pos[3] == " "):
            return 3

        #6 7 8
        if(pos[6] == pos[7] == "o" and pos[8] == " "):
            return 8
        elif(pos[6] == pos[8] == "o" and pos[7] == " "):
            return 7
        elif(pos[7] == pos[8] == "o" and pos[6] == " "):
            return 6

        #0 3 6
        if(pos[0] == pos[3] == "o" and pos[6] == " "):
            return 6
        elif(pos[0] == pos[6] == "o" and pos[3] == " "):
            return 3
        elif(pos[3] == pos[6] == "o" and pos[0] == " "):
            return 0

        #1 4 7
        if(pos[1] == pos[4] == "o" and pos[7] == " "):
            return 7
        elif(pos[1] == pos[7] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[7] == "o" and pos[1] == " "):
            return 1

        #2 5 8
        if(pos[2] == pos[5] == "o" and pos[8] == " "):
            return 8
        elif(pos[2] == pos[8] == "o" and pos[5] == " "):
            return 5
        elif(pos[5] == pos[8] == "o" and pos[2] == " "):
            return 2

        #0 4 8
        if(pos[0] == pos[4] == "o" and pos[8] == " "):
            return 8
        elif(pos[0] == pos[8] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[8] == "o" and pos[0] == " "):
            return 0

        #2 4 6
        if(pos[2] == pos[4] == "o" and pos[6] == " "):
            return 6
        elif(pos[2] == pos[6] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[6] == "o" and pos[2] == " "):
            return 2

        #check if user is winning
        #0 1 2
        if(pos[0] == pos[1] == "x" and pos[2] == " "):
            return 2
        elif(pos[0] == pos[2] == "x" and pos[1] == " "):
            return 1
        elif(pos[1] == pos[2] == "x" and pos[0] == " "):
            return 0

        #3 4 5 
        if(pos[3] == pos[4] == "x" and pos[5] == " "):
            return 5
        elif(pos[3] == pos[5] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[5] == "x" and pos[3] == " "):
            return 3

        #6 7 8
        if(pos[6] == pos[7] == "x" and pos[8] == " "):
            return 8
        elif(pos[6] == pos[8] == "x" and pos[7] == " "):
            return 7
        elif(pos[7] == pos[8] == "x" and pos[6] == " "):
            return 6

        #0 3 6
        if(pos[0] == pos[3] == "x" and pos[6] == " "):
            return 6
        elif(pos[0] == pos[6] == "x" and pos[3] == " "):
            return 3
        elif(pos[3] == pos[6] == "x" and pos[0] == " "):
            return 0

        #1 4 7
        if(pos[1] == pos[4] == "x" and pos[7] == " "):
            return 7
        elif(pos[1] == pos[7] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[7] == "x" and pos[1] == " "):
            return 1

        #2 5 8
        if(pos[2] == pos[5] == "x" and pos[8] == " "):
            return 8
        elif(pos[2] == pos[8] == "x" and pos[5] == " "):
            return 5
        elif(pos[5] == pos[8] == "x" and pos[2] == " "):
            return 2

        #0 4 8
        if(pos[0] == pos[4] == "x" and pos[8] == " "):
            return 8
        elif(pos[0] == pos[8] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[8] == "x" and pos[0] == " "):
            return 0

        #2 4 6
        if(pos[2] == pos[4] == "x" and pos[6] == " "):
            return 6
        elif(pos[2] == pos[6] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[6] == "x" and pos[2] == " "):
            return 2
        
        #exceptional cases
        if(pos[4] == "o"):
            if((pos[1] == "o" and pos[7] == "x") or (pos[1] == "x" and pos[7] == "o")):
                return 3
            elif((pos[8] == "o" and pos[0] == "x") or (pos[8] == "x" and pos[0] == "o")):
                return 6
            elif((pos[6] == "x" and pos[2] == "o") or (pos[6] == "o" and pos[2] == "x")):
                return 0
            elif((pos[3] == "x" and pos[5] == "o") or (pos[3] == "o" and pos[5] == "x")):
                return 1
        elif(pos[4] == "x"):
            if(pos[3] == "x" and pos[5] == "o"):
                return 1
            elif(pos[1] == "x" and pos[7] == "o"):
                return 3

    #for six inputs
    if(inputItem == 6):
        #type 1
        if( pos[0] == "x" and pos[8] == "o"):
            if( pos[7] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 6
            
            if( pos[5] == "o"):
                if(pos[3] == " "):
                    return 3
                else:
                    return 2
            
            if( pos[2] == "o"):
                if(pos[5] == " "):
                    return 5
                else:
                    return 6
            
            if( pos[6] == "o"):
                if( pos[2] == " "):
                    return 2
                else:
                    return 7
            
            if( pos[1] == "o"):
                if( pos[7] == " "):
                    return 7
                else:
                    return 5
            
            if( pos[3] == "o"):
                if( pos[5] == " "):
                    return 5
                else:
                    return 7
        
        #type 2
        if( pos[2] == "x" and pos[6] == "o"):
            if( pos[7] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 8
            
            if( pos[3] == "o"):
                if( pos[5] == " "):
                    return 5
                else:
                    return 0
            
            if( pos[0] == "o"):
                if( pos[8] == " "):
                    return 8
                else:
                    return 3
            
            if( pos[8] == "o"):
                if( pos[0] == " "):
                    return 0
                else:
                    return 7
            
            if( pos[1] == "o"):
                if(pos[7] == " "):
                    return 7
                else:
                    return 3
            
            if( pos[5] == "o"):
                if( pos[3] == " "):
                    return 3
                else:
                    return 7
        
        #type 3
        if( pos[0] == "o" and pos[8] == "x"):
            if( pos[1] == "o"):
                if( pos[7] == " "):
                    return 7
                else:
                    return 2
            
            if( pos[3] == "o"):
                if( pos[5] == " "):
                    return 5
                else:
                    return 6
            
            if( pos[7] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 3
            
            if( pos[5] == "o"):
                if( pos[3] == " "):
                    return 3
                else:
                    return 1
            
            if( pos[6] == "o"):
                if(pos[2] == " "):
                    return 2
                else:
                    return 3
            
            if( pos[2] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 6
        
        #type 4
        if( pos[2] == "o" and pos[6] == "x"):
            if( pos[5] == "o"):
                if( pos[3] == " "):
                    return 3
                else:
                    return 8
            
            if( pos[1] == "o"):
                if( pos[0] == " "):
                    return 0
                else:
                    return 7
            
            if( pos[3] == "o"):
                if( pos[5] == " "):
                    return 5
                else:
                    return 1
            
            if( pos[7] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 5
            
            if( pos[8] == "o"):
                if(pos[0] == " "):
                    return 0
                else:
                    return 5
            
            if( pos[0] == "o"):
                if( pos[1] == " "):
                    return 1
                else:
                    return 8

    #for seven inputs
    if(inputItem == 7):
        #chec if comp. is winning
        #0 1 2
        if(pos[0] == pos[1] == "o" and pos[2] == " "):
            return 2
        elif(pos[0] == pos[2] == "o" and pos[1] == " "):
            return 1
        elif(pos[1] == pos[2] == "o" and pos[0] == " "):
            return 0

        #3 4 5 
        if(pos[3] == pos[4] == "o" and pos[5] == " "):
            return 5
        elif(pos[3] == pos[5] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[5] == "o" and pos[3] == " "):
            return 3

        #6 7 8
        if(pos[6] == pos[7] == "o" and pos[8] == " "):
            return 8
        elif(pos[6] == pos[8] == "o" and pos[7] == " "):
            return 7
        elif(pos[7] == pos[8] == "o" and pos[6] == " "):
            return 6

        #0 3 6
        if(pos[0] == pos[3] == "o" and pos[6] == " "):
            return 6
        elif(pos[0] == pos[6] == "o" and pos[3] == " "):
            return 3
        elif(pos[3] == pos[6] == "o" and pos[0] == " "):
            return 0

        #1 4 7
        if(pos[1] == pos[4] == "o" and pos[7] == " "):
            return 7
        elif(pos[1] == pos[7] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[7] == "o" and pos[1] == " "):
            return 1

        #2 5 8
        if(pos[2] == pos[5] == "o" and pos[8] == " "):
            return 8
        elif(pos[2] == pos[8] == "o" and pos[5] == " "):
            return 5
        elif(pos[5] == pos[8] == "o" and pos[2] == " "):
            return 2

        #0 4 8
        if(pos[0] == pos[4] == "o" and pos[8] == " "):
            return 8
        elif(pos[0] == pos[8] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[8] == "o" and pos[0] == " "):
            return 0

        #2 4 6
        if(pos[2] == pos[4] == "o" and pos[6] == " "):
            return 6
        elif(pos[2] == pos[6] == "o" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[6] == "o" and pos[2] == " "):
            return 2

        #check if user is winning
        #0 1 2
        if(pos[0] == pos[1] == "x" and pos[2] == " "):
            return 2
        elif(pos[0] == pos[2] == "x" and pos[1] == " "):
            return 1
        elif(pos[1] == pos[2] == "x" and pos[0] == " "):
            return 0

        #3 4 5 
        if(pos[3] == pos[4] == "x" and pos[5] == " "):
            return 5
        elif(pos[3] == pos[5] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[5] == "x" and pos[3] == " "):
            return 3

        #6 7 8
        if(pos[6] == pos[7] == "x" and pos[8] == " "):
            return 8
        elif(pos[6] == pos[8] == "x" and pos[7] == " "):
            return 7
        elif(pos[7] == pos[8] == "x" and pos[6] == " "):
            return 6

        #0 3 6
        if(pos[0] == pos[3] == "x" and pos[6] == " "):
            return 6
        elif(pos[0] == pos[6] == "x" and pos[3] == " "):
            return 3
        elif(pos[3] == pos[6] == "x" and pos[0] == " "):
            return 0

        #1 4 7
        if(pos[1] == pos[4] == "x" and pos[7] == " "):
            return 7
        elif(pos[1] == pos[7] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[7] == "x" and pos[1] == " "):
            return 1

        #2 5 8
        if(pos[2] == pos[5] == "x" and pos[8] == " "):
            return 8
        elif(pos[2] == pos[8] == "x" and pos[5] == " "):
            return 5
        elif(pos[5] == pos[8] == "x" and pos[2] == " "):
            return 2

        #0 4 8
        if(pos[0] == pos[4] == "x" and pos[8] == " "):
            return 8
        elif(pos[0] == pos[8] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[8] == "x" and pos[0] == " "):
            return 0

        #2 4 6
        if(pos[2] == pos[4] == "x" and pos[6] == " "):
            return 6
        elif(pos[2] == pos[6] == "x" and pos[4] == " "):
            return 4
        elif(pos[4] == pos[6] == "x" and pos[2] == " "):
            return 2
        
        #exceptional
        if(pos[4] == "x" and pos[8] =="x" and pos[0] == "o" and pos[2] == "x"):
            return 1

    #for eight inputs
    if(inputItem == 8):
        for i in range(0,len(pos)):
            if(pos[i] == " "):
                return i