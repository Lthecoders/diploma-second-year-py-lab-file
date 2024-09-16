# Name: Nikhil Rajendra Gaikwad


# print("Nikhil")



# write a program to display resistor color code using switch statement.



# creating logic of code
def logic(resister_color):
    match resister_color:
        case 'black':
            return 0
        case 'brown':
            return 1
        case 'red':
            return 2
        case 'orange':
            return 3
        case 'yellow':
            return 4
        case 'green':
            return 5
        case 'blue':
            return 6
        case 'violet':
            return 7
        case 'gray':
            return 8
        case 'white':
            return 9
        
user_input=input("Enter the color \n-------> ").strip().lower()

output = logic(user_input)

print(f"The color {user_input} has {output} as it's color code")
        



