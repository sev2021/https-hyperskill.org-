# Write your code here
ml_water = 400
ml_milk = 540
gr_beans = 120
no_cups = 9
no_cash = 550

# Current level of suplies
supplies_list = [400, 540, 120, 9, 550]
# Supplies required for coffee
make_usage = [[250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]

def action_show(all_list):
    print("The coffee machine has:")
    print(str(all_list[0]) + "of water")
    print(str(all_list[1]) + "of milk")
    print(str(all_list[2]) + "of coffee beans")
    print(str(all_list[3]) + "of disposable cups")
    print(str(all_list[4]) + "of money")
    
def action_buy(make_list):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    make_select = int(input()-1)

    if ((make_list[0] >= make_usage[make_select][0]) 
        and (make_list[1] >= make_usage[make_select][1])
        and (make_list[2] >= make_usage[make_select][2])
        and (make_list[3] >= make_usage[make_select][3])):
            make_list[0] -= make_usage[make_select][0]
            make_list[1] -= make_usage[make_select][1]
            make_list[2] -= make_usage[make_select][2]
            make_list[3] -= make_usage[make_select][3]
            make_list[4] += make_usage[make_select][4]
    else:
        print("Can't make coffee. Need refill.")
    return make_list

def action_fill(fill_list):
    print("Write how many ml of water do you want to add:")
    fill_list[0] += input()
    print("Write how many ml of milk do you want to add:")
    fill_list[1] += input()    
    print("Write how many grams of coffee beans do you want to add:")
    fill_list[2] += input()
    print("Write how many disposable cups of coffee do you want to add:")
    fill_list[3] += input()
    return fill_list
    
def action_take(take_list):
    print("I gave you $" + str(take_list[4]))
    take_list[4] = 0
    return take_list

# Program starts here
action = ""
action_show(supplies_list)

while action != "exit":
    print("Write action (buy, fill, take):")
    action = input()
    if input == "buy":
        supplies_list = action_buy(supplies_list)
    if input == "fill":
        supplies_list = action_fill(supplies_list)
    if input == "take":
        supplies_list = action_take(supplies_list)
