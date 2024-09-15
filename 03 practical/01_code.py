
# print("Light")


"""
write a program to check whether entered
frequence is radio frequency or audio frequency
"""


# Input: Frequency from the user
frequency = float(input("Enter the frequency in Hz: "))

# Check if the frequency is within Audio Frequency range
if 20 <= frequency <= 20000:
    print("This is an Audio Frequency (AF).")
# Check if the frequency is within Radio Frequency range
elif 3000 <= frequency <= 3e11:  # 3e11 means 300 GHz in Hz
    print("This is a Radio Frequency (RF).")
# If neither, it’s outside of both ranges
else:
    print("This is outside of Audio and Radio frequency ranges.")

