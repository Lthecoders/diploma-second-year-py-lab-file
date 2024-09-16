
# Name: Nikhil Rajendra Gaikwad

"""
*b. Create a simple program, to demonstrate use of: for
loop in Python (e.g.: various pattern building, printing
multiplication table, checking palindrome number etc.)

"""

# for loop in python

# various pattern building

# for i in range(6):
#     print('*'*i)


# printing multiplication table

# for i in range(11):
#     print(f'2 x {i} = {2*i}')



# checking for palindrome number

number = input('Enter a number\n-------> ').strip()

for i in number:
    if number == number[::-1]:
        print(f'{number} is a PALINDROME number')
        break
    elif number != number[::-1]:
        print(f'{number} is NOT a PALINDROME number')
        break
    else:
        print("error bro")

    
