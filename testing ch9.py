import random
import math


#TEST: 2 options for funciton,
#PRINT IN FUNCTION
#OR RETURN THIS VARIABLE TO THE MAIN PROGRAM
###########################################
#printing is calling a function
#returning it is return + use in main program



# def volume_sphere(radius):
#     pie=math.pi
#     vol=(4/3)*pie*radius**3
#     return vol
#     # print(f"The volume is {vol:.2f}")
# #
# #
# # volume = volume_sphere(5)
# # print(volume)
#
#
# def volume_cylinder(r,h):
#     '''This function deteremines the volume of a cylinder'''
#     pie=math.pi
#     vol=pie*h*r**2
#     return vol
#
# def main():
#     print(volume_cylinder(1,5))
#     print(volume_sphere(5))
#     print(__name__)
#
#
#
#
# #name space, able to import it FROM another file, running it from the main one
# if __name__== "__main__":
#     main()

#created in function, stays in function
#encapsulated so it wont interfere with another function
#can only read the variable outside the function

def hyp(leg1,leg2):
    '''This function finds the hypotenuse of the right triangle'''
    hyp=(leg1**2+leg2**2)**(1/2)
    return hyp

print(hyp(2,2))


def mean(a,b,c):
    '''This function finds the mean of 3 numbers'''
    mean=(a+b+c)/3.0
    return mean

print(mean(2,2,2))

def perimeter(base,height):
    '''This functio finds the perimeter of a rectangle'''
    perimeter=(base*2)+(height*2)
    return perimeter

print(perimeter(2,2))