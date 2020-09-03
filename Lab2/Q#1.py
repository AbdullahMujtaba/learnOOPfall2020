num = int(input("Enter a number To Print The Table :"))

start_range = int(input("Enter a Starting range: "))
end_range = int(input("Enter an Ending range: "))
print("\n")

for i in range(start_range,end_range + 1):
    print(num, " * ", i , " = ", num * i)