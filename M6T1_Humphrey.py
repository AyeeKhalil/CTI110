#Khalil Humphrey
#M6T1 Kilometer Converter
#10/26/17



def main():
    kilometers = float(input("Enter in a distance traveled in kilometers: "))

    show_miles(kilometers)
    

def show_miles(km):
    miles = km * 0.6214

    print(km, 'kilometers is equal to', miles, 'miles.')


main()

    
