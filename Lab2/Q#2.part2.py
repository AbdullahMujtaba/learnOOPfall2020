initial_range = int(input("Enter a Starting range: "))
final_range = int(input("Enter an Ending range: "))

for i in range(initial_range, final_range + 1):
    evenNumber = i % 2

    if evenNumber == 0:
        print (i, "is an even")
    else:
        print (i, "is an odd")