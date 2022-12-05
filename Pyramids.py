def triangle(n):

    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):
        check = True
        if (i % 2) != 0:
            check = False
        # inner loop to handle number spaces
        # values changing acc. to requirement
        if check:
            for j in range(0, k-1):
                print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            if ((i + 1) % 2) != 0:
                print("* ", end="")

        # ending line after each row
        if (i % 2) != 0:
            print("\r")


# Driver Code
userInput = int(input('Enter number of rows:\n'))
# userInput = 13
n = userInput * 2
triangle(n)
