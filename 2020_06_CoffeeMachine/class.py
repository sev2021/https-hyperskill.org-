# Given lines 2-8, 14-18 ? 

class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
    def tri_area(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            return self.a * self.b * 0.5
        return "Not right"
        
# triangle from the input

input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here

x = RightTriangle(input_c, input_a, input_b)
print(x.tri_area())
