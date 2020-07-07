# write your code here
def action_show(string):
    res = [string[0:3], string[3:6], string[6:9], string[0:7:3], string[1:8:3], string[2:9:3], string[0:9:4], string[2:7:2]]
    print("---------")
    print("| " + string[0] + " " + string[1] + " " + string[2] + " |")
    print("| " + string[3] + " " + string[4] + " " + string[5] + " |")
    print("| " + string[6] + " " + string[7] + " " + string[8] + " |")
    print("---------")

    if("OOO" in res and "XXX" in res) or (abs(string.count("O") - string.count("X")) > 1):
        print("Impossible")
    elif "OOO" in res:
        print("O wins")
    elif "XXX" in res:
        print("X wins")
    elif string.count("_") == 0:
        print("Draw")
    else:
        print("Game not finished")
        
string = input("Enter cells: ") # input string like: _OOOO_X_X
action_show(string)

while string.count("_") > 0:
    XOmove = "X"  # check whay is nex move (X start, and O when X>O)
    if string.count("X") > string.count("O"):
        XOmove = "O"

    change = input("Enter the coordinates:")                # input string like: 2 3
    if change[0::2].isdecimal():                            # check if input is all numbers
        if change[0] and change[2] in "123":                # check if input in "123"
            # calculate position in string and (-1) to go from "123" to array "012"
            change_int = (int(change[0]) + (3 - int(change[2])) * 3) - 1
            if string[change_int] == "_":                   # check if input field is empty "_"
                # replacing input position with correct move "x" or "O"
                string = string[:change_int] + XOmove + string[(change_int + 1):]
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

    action_show(string)
print("GAME OVER")
