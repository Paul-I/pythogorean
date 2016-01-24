'#Float raw input is what allows the user to enter the number'
a = float(raw_input("the length of the first side of your triangle? : "))
b = float(raw_input("the length of the second side of your triangle? : "))
'#This is the main equation, this is how the program solve the problem'
C_squared = a**2 + b**2
c = C_squared**0.5
'#This is what tells the user the answer.'
print "The length of your triangle is %r" % c
