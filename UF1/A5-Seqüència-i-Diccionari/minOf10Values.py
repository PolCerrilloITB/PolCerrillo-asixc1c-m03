# Prompt the user to enter 10 values
values = []
for i in range(10):
    num = float(input("Enter value " + str(i+1) + ": "))
    values.append(num)

# Find and print the smallest value
smallest = min(values)
print("The smallest value is: ", smallest)