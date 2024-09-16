# Name: Nikhil Rajendra Gaikwad

# write simple python program to calculate equivalent registers connected in series and parallel. 
# Accept values of R1, R2 and R3 from the users.






# 'For registers in series'

# r_1 = int(input('\nEnter value for R1\n--------> '))
# r_2 = int(input('\nEnter value for R2\n--------> '))
# r_3 = int(input('\nEnter value for R3\n--------> '))

# r_eq = r_1 + r_2 + r_3

# print("The equivalent resistance in series would be", r_eq,'Ω')



'For registers in parallel'

def logic(v_1, v_2, v_3):
    r_eq = ((1/v_1)+(1/v_2)+(1/v_3))
    return 1/r_eq

r_1 = int(input('\nEnter value for R1\n--------> '))
r_2 = int(input('\nEnter value for R2\n--------> '))
r_3 = int(input('\nEnter value for R3\n--------> '))

output = logic(r_1, r_2, r_3)
output = str(output)
print("The equivalent resistance in parallel would be",output[:4] ,'Ω')
