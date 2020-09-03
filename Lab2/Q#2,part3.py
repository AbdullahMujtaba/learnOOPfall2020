initial_range = int(input(" Please Enter the Minimum Value : "))
final_range = int(input(" Please Enter the Maximum Value : "))

number = 1
final_range = number

while number <= initial_range:

    if (number % 2 != 0):
        print(number,"IS ODD")

    number = number + 1

initial_range = int(input(" Please Enter the Minimum Value : "))
final_range= int(input(" Please Enter the Maximum Value : "))

number = 1

final_range = number

while number <= initial_range:
    if (number % 2 == 0):
        print(number,"IS EVEN")
    number = number + 1