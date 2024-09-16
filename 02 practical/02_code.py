# Name: Nikhil Rajendra Gaikwad



# print("light")

# write simple python program to calculate value voltage by applying Ohm's law. Accept value of current(I) and resistance (R) from the users

# formula  I = V * R

# wrapping logic of the code in a function
def logic(value_of_V,value_of_R):
    return value_of_V * value_of_R

# taking inputs from the user inorder to process it
current = int(input("Enter the value of current I:\n-------> "))
resistance = int(input("Enter the value of resistance R:\n-------> "))

# assign the value return from the logic to a new variable
output = logic(current, resistance)

# printing the output in the terminal
print(f"The votage V is {output} volts")


