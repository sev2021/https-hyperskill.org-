# Write your code here
ml_water = 400
ml_milk = 540
gr_beans = 120
no_cups = 9
no_cash = 550

# Setting predefined openeing values:
supplies_list = [400, 540, 120, 9, 550]
supplies_name = ["water", "milk", "coffee beans", "disposable cups", "money"]
fill_name = ["Write how many ml of water do you want to add:", 
            "Write how many ml of milk do you want to add:", 
            "Write how many grams of coffee beans do you want to add:", 
            "Write how many disposable cups of coffee do you want to add:"]
# Supplies required for coffee
make_usage = [[250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]

def action_show(supplies_list): # This ONLY shows values, no return needed
    print("The coffee machine has:")
    for i in range(5):
        print(str(supplies_list[i]) + " of " + supplies_name[i])
    
def action_buy(make_list): # This checks if supplies level, do coffee and returns new supplies level 
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    string = input()
    if string in "123":
        make_select = int(string) - 1
        if [i for i in make_list] >= [i for i in make_usage[make_select]]:
            for i in range(4):
                make_list[i] -= make_usage[make_select][i]
            make_list[4] += make_usage[make_select][4]
        else:
            print("Can't make coffee. Need refill.")
    return make_list

def action_fill(fill_list): # This displays predefined commments and get new supplies values + return
    for i in range(4):
        print(fill_name[i])
        fill_list[i] += int(input())
    return fill_list
    
def action_take(take_list):  # Takes all money off machine, returns nwa value
    print("I gave you $" + str(take_list[4]))
    take_list[4] = 0
    return take_list

# Program starts here
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        supplies_list = action_buy(supplies_list)
    if action == "fill":
        supplies_list = action_fill(supplies_list)
    if action == "take":
        supplies_list = action_take(supplies_list)
    if action == "remaining":
        action_show(supplies_list) # THIS IS NOT RETURNING NEW VALUE
    if action== "exit":
        break;
