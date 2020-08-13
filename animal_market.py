anim = {-1: ["None", "None"], 23: ["chicken","chickens"], 678: ["goat", "goats"],
1296: ["pig", "pigs"], 3848: ["cow", "cows"], 6769: ["sheep", "sheep"]}

inp = int(input())

top_price = [i for i in anim if i < (inp + 1)][-1]
if inp >= 23:
    print(inp // top_price, end=" ")
if (inp // top_price) == 1:
    print(anim[top_price][0])
else:
    print(anim[top_price][1])
