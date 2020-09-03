even_num, odd_num = 0, 0
initial_range = int(input("Enter start range of table: "))
final_rang = int(input("Enter end range of table: "))

while initial_range <= final_rang:
    if initial_range % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    initial_range +=1
print("total even numbers are ",even_num)
print("total even numbers are ",odd_num)