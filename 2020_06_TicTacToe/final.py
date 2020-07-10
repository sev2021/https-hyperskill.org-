# write your code here
string = "_________"

while True:
    print("---------")
    print("| " + string[0] + " " + string[1] + " " + string[2] + " |")
    print("| " + string[3] + " " + string[4] + " " + string[5] + " |")
    print("| " + string[6] + " " + string[7] + " " + string[8] + " |")
    print("---------")
    
    # generate all winning results:
    res = [string[0:3], string[3:6], string[6:9], string[0:7:3], string[1:8:3], string[2:9:3], string[0:9:4], string[2:7:2]]
     
    if "OOO" in res:               # results check:
        print("O wins")
        break
    if "XXX" in res:
        print("X wins")
        break
    if string.count("_") == 0:
        print("Draw")
        break
        
    old_string = string               # player move
    while old_string == string:                      
        change = input("Enter the coordinates:") 
        if change[0::2].isdecimal() and len(change) > 2: 
            if (change[0] in "123") and (change[2] in "123"): 
                change_int = (int(change[0]) + (3 - int(change[2])) * 3) - 1
                if string[change_int] == "_": 
                    string = string[:change_int] + "XO"[string.count("X") - string.count("O")] + string[(change_int + 1):]               
                    done = 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")       
