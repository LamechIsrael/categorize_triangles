###############################################
# CS 1110A - Programming in Python            #
# Module 4 - Program 4 - Categorize Triangles #
# Author: Lamech Israel                       #
# Date:   01/31/2023                          #
###############################################


def kind(a, b, c):
    
    # Sort the numbers into ascending order, guarenteeing c is the hypotenuse.
    sides = [a, b, c]
    sides.sort()
    print(sides)
    
    # Turn the array into variables again to make th code more readable
    x = sides[0]
    y = sides[1]
    z = sides[2]
    
    
    # This math determines whether a triangle can be made.
    # The sum of the hypotenuse is the longest distance two sides can cover without being a straight line.
    if z >= (x + y):
        triangle_kind = 0
    
    # If the sides are equalateral
    elif x == y and y == z:
        triangle_kind = 1
    
    # If the triangle is isosceles (two sides are the same length, but not all three)
    elif x == y or y == z or x == z:
        triangle_kind = 2
    
    # If the triangle is a right triangle
    elif x**2 + y**2 == z**2:
        triangle_kind = 3
    
    # If the triangle is acute
    # If a^2 + b^2 = c^2 makes a right triangle, any smaller hypotenuse shrings the angle
    elif x**2 + y**2 >  z**2:
        triangle_kind = 4
    
    #If the triangle is obtuse(none of the others apply)
    else:
        triangle_kind = 5
        
    # Output to the user the result
    triangle_name = name(triangle_kind)
    print(' {}, {}, {}     {}    {}'.format(a,b,c,triangle_kind, triangle_name))
    
def name(k):
    
    # Switch case to return the name of the triangle
    match k:
        case 0:
            return 'No triangle'
        case 1:
            return 'Equilateral'
        case 2:
            return 'Isosceles'
        case 3:
            return 'Right'
        case 4:
            return 'Acute'
        case 5:
            return 'Obtuse'
        

# Start the program
print('Categorize Triangles')

print('\n  Sides    Kind    Triangle Name')
print('---------  ----    -------------')
print('1,  2, 33    0     no triangle')
print('5,  5,  5    1     equilateral')
print('6,  6,  4    2     isosceles')
print('3,  4,  5    3     right')
print('7,  8,  9    4     acute')
print('4,  5,  8    5     obtuse')

# Will continue while true
while True:
    

    # Take in inputs
    a = int(input('\nFirst side:  '))
    # Exit the loop if a is 0
    if a == 0:
        break  
    # Get the other inputs
    b = int(input('Second side: '))
    c = int(input('Third side:  '))

    # Get the triangle type
    kind(a, b, c)

# Finish when the code is done
print('\nDone!')
exit()