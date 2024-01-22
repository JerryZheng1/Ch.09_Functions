# 9.0 Jedi Training (45pts)  Name:________________

#make comments

#1.) Correct the following code: (The user's number should be increased by 1 and printed.) (2pts)


x = int(input("Enter a number: ")) #set the input to equal to x, as we use this in our function.

def increase(x):
    return x+1

print("Your number has been increased to", increase(x))

#we can recall our function with the copy value rather than just global x.


#2.) Correct the following code to print 1-10:  (2pts)

def count_to_ten():
    for i in range(10): #changed [] to ()
        print(i+1) #print i+1 to make it start at 1 rather than 0

count_to_ten()



#3.) Correct the following code to sum the list:  (2pts)
def sum_list(list):
    sum=0 #made a variable sum = 0 to define sum and to reset the sum to 0
    for i in list:
        sum += i #i needed to be added to sum
    return sum

list = [45, 2, 10, -5, 100]

print(sum_list(list))



#4.) Correct the following code which should reverse the sentence that is entered.  (2pts)

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[(i+1) * -1] #changed i to i+1 to make the first character -1, or else it will be at 0
    return result


text = input("Enter a sentence: ")
print(reverse(text))



#5.) Correct the following code: (if one of the options is not entered it should print the statements)  (2pts)


def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q": #changed = to == to show that the command is equal to a variable
            return command
        else: #add a else statement so if the user didn't enter any options above, it would return this.
            print("Hey, that's not a command. Here are your options:")
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")


user_command = get_user_choice()
print("You entered:", user_command)



'''
#6.) MINI FUNCTION (5pts)
-------------------------------
Write a function called mini that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))

OUTPUT
------
3
4
2
-100
A

The function should return the value, not print the value. 
Also, while there is a min function built into Python, don't use it. 
Please use if statements and practice creating it yourself.

def mini(first,second,third):
    small_number=0
    if first<=second and first <=third:
        small_number=first
    if second<=first and second<=third:
        small_number=second
    else:
        small_number=third
    return small_number

print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))
'''



'''
7.) BOX_FUNCTION (5pts)
-------------------------------
Write a function called box that will output boxes (made of lower case o's) 
given a height and width. Once you've finished writing your function, copy 
and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
box(7,5) # Print a box 7 high, 5 across
print() # Blank line
box(3,2) # Print a box 3 high, 2 across
print() # Blank line
box(3,10) # Print a box 3 high, 10 across

OUTPUT
------
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo

oo
oo
oo

oooooooooo
oooooooooo
oooooooooo


def box(high,across):
    for i in range(high):
        boxes=print("o"*across)

box(7,5) # Print a box 7 high, 5 across
print() # Blank line
box(3,2) # Print a box 3 high, 2 across
print() # Blank line
box(3,10) # Print a box 3 high, 10 across
    
'''



'''
8.) FIND FUNCTION (5pts)
-------------------------------
Write a function called FIND that will take a list of numbers, "list", 
along with one other number, "key". Have it search the list for the value
contained in key. Each time your function finds the key value, 
print the list position of the key. You will need to juggle three variables,
one for the list, one for the key, and one for the position of where you are 
in the list. You may want to review your notes for the code to iterate though
a list using the range and len functions. Start with that code and modify the 
print to show each element and its position. Then instead of just printing 
each number, add an if statement to only print the ones we care about. 
Once you've finished writing your function, copy and paste the following code 
after it and make sure it works with the function you wrote:

INPUT
-----
list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(list, 12)
find(list, 91)
find(list, 80)

OUTPUT
------
Found 12 at position 11
Found 12 at position 13
Found 91 at position 5

Use a for loop with an index variable and a range. 
Inside the loop use an if statement. This function 
can be written in about four lines of code.


def find(list,key):
    for i in range(len(list)):
        if list[i]==key:
            print("Found",key,"at position",i)

list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(list, 12)
find(list, 91)
find(list, 80)
'''

'''
9.) FIZZBUZZ (5pts)
-------------------------------
The "Fizz-Buzz test" is an interview question designed to help filter out the 99.5% 
of programming job candidates who can't seem to program their way out of a wet paper bag.
Write a function called fizzbuzz that prints the numbers from 1 to "endpoint", where 
endpoint is your final number. But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz". Once you've finished writing your function, 
copy and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
fizzbuzz(15)

OUTPUT
------
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz


def fizzbuzz(number):
    for i in range(1,number+1):
        if i%15==0:
            print("FizzBuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)

fizzbuzz(15)


The classic test is to use the numbers 1-100 so make sure you test that with your function.
'''



'''
10.) FIBONACCI (5pts)
-------------------------------
In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, 
called the Fibonacci sequence, and characterized by the fact that every number after the
first two is the sum of the two preceding ones:1,1,2,3,5,8,13,21,34,55,89,144
Write a function called fibonacci() that will print up to a maximum of the first 100 numbers
in the Fibonacci sequence. Pass the number into the function.

Just to do a quick review of text formatting in the last chapter, make the list of numbers
right-justified with commas.

def fibonacci(number):
    first_number=0
    second_number=1
    print(f"{second_number:27,}")
    for i in range(number):
        sum=first_number+second_number
        print(f"{sum:27,}")
        first_number=second_number
        second_number=sum
        
fibonacci(100)
'''




'''
11.) 10,000 NUMBERS (5pts)
-------------------------------

In this program we will write three different functions.

Function #1: Write a function named create_list that takes
in a list size and returns a list of random numbers from 1-6.
i.e., calling create_list(5) should return 5 random numbers from 1-6.
Once you've finished writing your function, copy and paste the
following code after it and make sure it works with the function you wrote:

INPUT
-----
my_list = create_list(5)
print(my_list)

OUTPUT
------
[2,5,1,6,3] #something like this 



import random
def create_list(list_size):
    list = []
    for i in range(list_size):
        list.append(random.randint(1,6))
    return list
    
my_list = create_list(5)
print(my_list)
'''




'''
Function #2: Write a function called count_list that takes
in a list and a number. Have the function return the number
of times the specified number appears in the list. Once you've
finished writing your function, copy and paste the following code
after it and make sure it works with the function you wrote:

INPUT
-----

def count_list(list,key):
    count=0
    for i in range(len(list)):
        if list[i]==key:
            count+=1
    return count
    
my_list = [1,2,3,3,3,4,2,1]
count = count_list(my_list,3)
print(count)

OUTPUT
------
3 
'''



'''
Function #3: Write a function called average_list that returns the 
average of the list passed into it. Once you've finished writing your
function, copy and paste the following code after it and make sure it
works with the function you wrote:

INPUT
-----

def average_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    average=sum/(len(list))
    return average

my_list = [1,2,3]
avg = average_list(my_list)
print(avg)

OUTPUT
------
2.0
'''




'''
Now that the functions have been created, use them all in a main program that will:
1.) Create a list of 10,000 random numbers from 1 to 6. (1 line of code)
2.) Print the count of 1 through 6. (For example, "There are 1361 amount of 2s") (3 lines of code)
3.) Print the average of all 10,000 random numbers. (Make sure it's a float) (2 lines of code)


import random



def create_list(list_size):
    list = []
    for i in range(list_size):
        list.append(random.randint(1,6))
    return list



def count_list(list,key):
    count=0
    for i in range(len(list)):
        if list[i]==key:
            count+=1
    return count


def average_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    average=sum/(len(list))
    return average


def main():
    random_number=create_list(10000)
    for i in range(1,7):
        count=count_list(random_number,i)
        print(f"there are {count:,} of {i}s")
    avg=average_list(random_number)
    print("The average is:",float(avg))


main()
'''






'''
12.) BB8 DRAWING PROGRAM (5pts)
-------------------------------
Back to the drawing board! Get it? Let's say we want to draw many BB8 robots
of varying sizes at various locations. We can make a function called draw_BB8().
We've made some basic changes to our original drawing program. We still have the
first two lines as importing arcade and opening an arcade window. We actually took 
all of the other drawing code and put it in a function called main(). At the bottom
we call the main() function. In the main() function we call the draw_BB8() function
multiple times. We pass three parameters to it: x, y and radius. Write the code for 
the draw_BB8() function so that the resulting picture looks as close as you can get
it to the one on the website.
'''

import arcade
arcade.open_window(600, 600, "BB8")

def draw_BB8(x,y,radius):

    #White Circle w/ outline
    arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
    arcade.draw_circle_outline(x,y,radius,arcade.color.BLACK,3)

    #Orange Circle w/ outline
    arcade.draw_circle_filled(x,y,radius*.70,(255,160,0,255))
    arcade.draw_circle_outline(x,y,radius*.70,arcade.color.BLACK,3)

    #Grey Circle w/ outline
    arcade.draw_circle_filled(x,y,radius*.4,(171,197,225,255))
    arcade.draw_circle_outline(x,y,radius*.4,arcade.color.BLACK,3)

    # Semi Circle for head
    arcade.draw_arc_filled(x, y + (radius*.8), radius * 1.4, radius * 1.6, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_outline(x, y + (radius*.8), radius * 1.4, radius * 1.6, arcade.color.BLACK, 0, 180,5)
    arcade.draw_line(x-((radius*1.4)/2),y+(radius*.8),x+((radius*1.4)/2),y+(radius*.8),arcade.color.BLACK,3)


    #Blue circle Top of head
    arcade.draw_circle_filled(x,y+(radius*1.23),radius*.27,(85,155,209,255))
    arcade.draw_circle_outline(x,y+(radius*1.23),radius*.27,arcade.color.BLACK,3)



def main():
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()


    draw_BB8(100,50,50)
    draw_BB8(300, 300, 30)
    draw_BB8(500, 100, 20)
    draw_BB8(500, 400, 60)
    draw_BB8(120, 500, 15)

    arcade.finish_render()
    arcade.run()


if __name__=="__main__":
    main()