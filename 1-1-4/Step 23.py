i = int(input("enter number:"))
while (i <= 0):
    # Add a nesting loop that decrements the value by 1
    # Until it is only 1 again
    while(i> 1):
     i = i - 1
    i = i + 1
print(i)