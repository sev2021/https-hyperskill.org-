#  Conversion to boolean  Unknown operation
#  by Daniel Tomas profile/52375764

def solve():
    some_truthy = [1, 2, 3, 4]
    some_falsy = []
    truthy_result = hidden_operation(some_truthy)
    falsy_result = hidden_operation(some_falsy)
    oper = "not"
    if id(truthy_result) == id(some_truthy):
        oper = "or"
    elif id(falsy_result) == id(some_falsy):
        oper = "and"
    
    print(oper)
    
    if oper != "not":
        hidden_operand = falsy_result if oper == 'or' else truthy_result
        print(hidden_operand)
