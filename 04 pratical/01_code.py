# Name: Nikhil Rajendra Gaikwad


# Write program to display various radio frequency bands using if..else ladder


# output
# Frequency: 98 MHz
# Band: Very High Frequency (VHF)
# Range: 30 - 300 MHz


# starting of code



# creating logic of code
# Function to determine the frequency band based on input
def find_frequency_band(frequency):
    if frequency >= 3 and frequency < 30:
        return "Very Low Frequency (VLF)", "3 - 30 kHz"
    elif frequency >= 30 and frequency < 300:
        return "Low Frequency (LF)", "30 - 300 kHz"
    elif frequency >= 300 and frequency < 3000:
        return "Medium Frequency (MF)", "300 kHz - 3 MHz"
    elif frequency >= 3000 and frequency < 30000:
        return "High Frequency (HF)", "3 - 30 MHz"
    elif frequency >= 30000 and frequency < 300000:
        return "Very High Frequency (VHF)", "30 - 300 MHz"
    elif frequency >= 300000 and frequency < 3000000:
        return "Ultra High Frequency (UHF)", "300 MHz - 3 GHz"
    elif frequency >= 3000000 and frequency < 30000000:
        return "Super High Frequency (SHF)", "3 - 30 GHz"
    elif frequency >= 30000000 and frequency < 300000000:
        return "Extremely High Frequency (EHF)", "30 - 300 GHz"
    else:
        return "Unknown Frequency Band", "Out of range"

# Main program
frequency_input = float(input("Enter the frequency in kHz: "))

# Call function to find the frequency band
band_name, band_range = find_frequency_band(frequency_input)

# Display the result
print(f"\nFrequency: {frequency_input} kHz")
print(f"Band: {band_name}")
print(f"Range: {band_range}")





