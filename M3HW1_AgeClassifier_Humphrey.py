#CTI-110
#M3HW1- Age Classifier
#Khalil Humphrey
#9/12/17

def main():
    #Age Ranges
    Infant_age = 1
    Child_age = 13
    Teenager_age = 20

    #Define your age
    
    age = int(input('Enter in a age : '))

    if age <= Infant_age:
        print('Age is a: Infant')

    elif age < Child_age:
        print ('Age is a: Child')

    elif age < Teenager_age:
        print ('Age is a: Teenager')

    else:

        print ('Age is a: Adult')
        
        
        
#Close the main and run it
        
main()

    
