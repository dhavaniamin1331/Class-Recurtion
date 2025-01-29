def headrec(n, num):
    # Base case: if n exceeds num, terminate the recursion 
    if n > num: 
        return 
    # Recursive call with the next value 
    headrec(n + 1, num)
    # Print the current value of n after returning from the recursive call 
    print(n)

# Promt the user to enter the value of n 
n = int(input("Enter n to print 1 to n: "))

# Intial call to headrec function starting fro 1 headrec(1, n)
