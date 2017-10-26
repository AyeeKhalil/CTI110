#Write a program that uses a value-returning function to convert feet to inches
#10/26/17
#CTI-110 M6T2_FeettoInches
#Khalil Humphrey

Inches_per_foot = 12
def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    


def feet_to_inches(feet):
    return feet * Inches_per_foot

main()

