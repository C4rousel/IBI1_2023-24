print("the first five numbers are")
a, b=0.5, 4 #determine the first number of the recursive sequences
for _ in range (5):# determine range
    a, b= b, 2*b+3 #define the sequences
    print ( a, end=" ")



    