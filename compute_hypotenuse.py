import math
shorter_side1 = int(input('Enter the length of 1 of the 2 shorter sides of the right triangle: '))
shorter_side2 = int(input('Enter the length of the other shorter side of the right triangle: '))

def hypotenuse(shorter_side1, shorter_side2):
    c_sq = shorter_side1 ** 2 + shorter_side2 ** 2
    c = math.sqrt(c_sq)
    return c


print(f'The length of the hypotenuse is {hypotenuse(shorter_side1, shorter_side2)} units.')