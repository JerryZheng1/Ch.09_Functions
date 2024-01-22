
# #1
# x = int(input("Enter a number: "))
#
#
# def increase(x):
#     return x+1
#
# print("Your number has been increased to", increase(x))

#2

# def count_to_ten():
#     for i in range(10):
#         print(i+1)
#
# count_to_ten()

#3

# def sum_list(list):
#     sum=0
#     for i in list:
#         sum += i
#     return sum
#
# list = [45, 2, 10, -5, 100]
# print(sum_list(list))

#4

# def reverse(text):
#     result = ""
#     text_length = len(text)
#     for i in range(text_length):
#         result = result + text[(i+1) * -1]
#     return result
#
#
# text = input("Enter a sentence: ")
# print(reverse(text))

#5

# def get_user_choice():
#     while True:
#         command = input("Command: ")
#         if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
#             return command
#         else:
#             print("Hey, that's not a command. Here are your options:")
#             print("f - Full speed ahead")
#             print("m - Moderate speed")
#             print("s - Status")
#             print("d - Drink")
#             print("q - Quit")
#
#
# user_command = get_user_choice()
# print("You entered:", user_command)

#6

# def mini(first,second,third):
#     small_number=0
#     if first<=second and first <=third:
#         small_number=first
#     if second<=first and second<=third:
#         small_number=second
#     else:
#         small_number=third
#     return small_number
#

#7

# def box(high,across):
#     for i in range(high):
#         boxes=print("o"*across)
#     # return boxes
#
# box(7,7)
# #8



# def find(list,key):
#     for i in range(len(list)):
#         if list[i]==key:
#             print("Found",key,"at position",i)
#
# list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
#
# find(list, 12)
# find(list, 91)
# find(list, 80)


#9

# def fizzbuzz(number):
#     for i in range(1,number+1):
#         if i%15==0:
#             print("FizzBuzz")
#         elif i%5==0:
#             print("buzz")
#         elif i%3==0:
#             print("fizz")
#         else:
#             print(i)
#
# fizzbuzz(1)
#


#10

# def fibonacci(number):
#     first_number=0
#     second_number=1
#     list=[]
#     list.append(f"{second_number:3}")
#     for i in range(number+1):
#         sum=first_number+second_number
#         if sum>=1000:
#             list.append(f"{sum:3,}")
#         else:
#             list.append(f"{sum:3}")
#         first_number=second_number
#         second_number=sum
#     print(list)
#
#
# fibonacci(20)


# def fibonacci(number):
#     first_number=0
#     second_number=1
#     print(f"{second_number:3}")
#     for i in range(number):
#         sum=first_number+second_number
#         if sum>=1000:
#             print(f"{sum:3,}")
#         else:
#             print(f"{sum:3}")
#         first_number=second_number
#         second_number=sum


# fibonacci(100)


#11
# import random
#
#
#
# def create_list(list_size):
#     list = []
#     for i in range(list_size):
#         list.append(random.randint(1,6))
#     return list
#
#
#
# def count_list(list,key):
#     count=0
#     for i in range(len(list)):
#         if list[i]==key:
#             count+=1
#     return count
#
#
# def average_list(list):
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     average=sum/(len(list))
#     return average
#
#
# def main():
#     random_number=create_list(10000)
#     for i in range(1,7):
#         count=count_list(random_number,i)
#         print("there are",count,"of",i)
#     avg=average_list(random_number)
#     print("The average is:",float(avg))
#
#
# main()
#
#12
#
# import arcade
# arcade.open_window(600, 600, "BB8")
#
# def draw_BB8(x,y,radius):
#
#     #White Circle w/ outline
#     arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
#     arcade.draw_circle_outline(x,y,radius,arcade.color.BLACK,3)
#
#     #Orange Circle w/ outline
#     arcade.draw_circle_filled(x,y,radius*.70,(255,160,0,255))
#     arcade.draw_circle_outline(x,y,radius*.70,arcade.color.BLACK,3)
#
#     #Grey Circle w/ outline
#     arcade.draw_circle_filled(x,y,radius*.4,(171,197,225,255))
#     arcade.draw_circle_outline(x,y,radius*.4,arcade.color.BLACK,3)
#
#     # Semi Circle for head
#     arcade.draw_arc_filled(x, y + (radius*.8), radius * 1.4, radius * 1.6, arcade.color.WHITE, 0, 180)
#     arcade.draw_arc_outline(x, y + (radius*.8), radius * 1.4, radius * 1.6, arcade.color.BLACK, 0, 180,5)
#     arcade.draw_line(x-((radius*1.4)/2),y+(radius*.8),x+((radius*1.4)/2),y+(radius*.8),arcade.color.BLACK,3)
#
#
#     #Blue circle Top of head
#     arcade.draw_circle_filled(x,y+(radius*1.23),radius*.27,(85,155,209,255))
#     arcade.draw_circle_outline(x,y+(radius*1.23),radius*.27,arcade.color.BLACK,3)
#
#
#
# def main():
#     arcade.set_background_color(arcade.color.WHEAT)
#     arcade.start_render()
#
#
#     draw_BB8(100,50,50)
#     draw_BB8(300, 300, 30)
#     draw_BB8(500, 100, 20)
#     draw_BB8(500, 400, 60)
#     draw_BB8(120, 500, 15)
#
#     arcade.finish_render()
#     arcade.run()
#
#
# if __name__=="__main__":
#     main()
#
# def sum_list(list):
#     sum=0 #made a variable sum = 0 to define sum and to reset the sum to 0
#     for i in list:
#         sum += i #i needed to be added to sum
#     return sum
#
# list = [45, 2, 10, -5, 100]
# print(sum_list(list))
# def reverse(text):
#     result = ""
#     text_length = len(text)
#     for i in range(text_length):
#         result = result + text[(i+1) * -1] #changed i to i+1 to make the first character -1, or else it will be at 0
#     return result
#
# text = input("Enter a sentence: ")
# print(reverse(text))


# def get_user_choice():
#     while True:
#         command = input("Command: ")
#         if command == "f" or command == "m" or command == "s" or command == "d" or command == "q": #changed = to == to show that the command is equal to a variable
#             return command
#         else: #add a else statement so if the user didn't enter any options above, it would return this.
#             print("Hey, that's not a command. Here are your options:")
#             print("f - Full speed ahead")
#             print("m - Moderate speed")
#             print("s - Status")
#             print("d - Drink")
#             print("q - Quit")
#
#
# user_command = get_user_choice()
# print("You entered:", user_command)

# def mini(first,second,third):
#     small_number=0
#     if first<=second and first <=third:
#         small_number=first
#     if second<=first and second<=third:
#         small_number=second
#     else:
#         small_number=third
#     return small_number
#
# print(mini(7, 3, 5))
# print(mini(5, 5, 4))
# print(mini(2, 2, 3))
# print(mini(-2, -6, -100))
# print(mini("Z", "B", "A"))
# def box(high,across):
#     for i in range(high):
#         boxes=print("o"*across)
# box(7,5) # Print a box 7 high, 5 across
# print() # Blank line
# box(3,2) # Print a box 3 high, 2 across
# print() # Blank line
# box(3,10) # Print a box 3 high, 10 across
#
# def find(list,key):
#     for i in range(len(list)):
#         if list[i]==key:
#             print("Found",key,"at position",i)
#
# list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
#
# find(list, 12)
# find(list, 91)
# find(list, 80)

# def fibonacci(number):
#     first_number=0
#     second_number=1
#     print(f"{second_number:27,}")
#     for i in range(number):
#         sum=first_number+second_number
#         print(f"{sum:27,}")
#         first_number=second_number
#         second_number=sum
# fibonacci(100)

# import random
#
#
# def create_list(list_size):
#     list = []
#     for i in range(list_size):
#         list.append(random.randint(1, 6))
#     return list
#
#
# my_list = create_list(5)
# print(my_list)
# def count_list(list, key):
#     count = 0
#     for i in range(len(list)):
#         if list[i] == key:
#             count += 1
#     return count
#
#
# my_list = [1, 2, 3, 3, 3, 4, 2, 1]
# count = count_list(my_list, 3)
# print(count)
# def average_list(list):
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     average=sum/(len(list))
#     return average
#
# my_list = [1,2,3]
# avg = average_list(my_list)
# print(avg)

# import random
# def create_list(list_size):
#     list = []
#     for i in range(list_size):
#         list.append(random.randint(1,6))
#     return list
#
#
#
# def count_list(list,key):
#     count=0
#     for i in range(len(list)):
#         if list[i]==key:
#             count+=1
#     return count
#
#
# def average_list(list):
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     average=sum/(len(list))
#     return average
#
#
# def main():
#     random_number=create_list(10000)
#     for i in range(1,7):
#         count=count_list(random_number,i)
#         print("there are",count,"of",i)
#     avg=average_list(random_number)
#     print("The average is:",float(avg))
#
#
# main()
# import random
#
#
#
# def create_list(list_size):
#     list = []
#     for i in range(list_size):
#         list.append(random.randint(1,6))
#     return list
#
#
#
# def count_list(list,key):
#     count=0
#     for i in range(len(list)):
#         if list[i]==key:
#             count+=1
#     return count
#
#
# def average_list(list):
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     average=sum/(len(list))
#     return average
#
#
# def main():
#     random_number=create_list(10000)
#     for i in range(1,7):
#         count=count_list(random_number,i)
#         print(f"there are {count:,} of {i}s")
#     avg=average_list(random_number)
#     print("The average is:",float(avg))
#
#
# main()
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