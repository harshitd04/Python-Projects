def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        
        return True
    else:
        return False

year = int(input("Enter the Year: "))

if is_leap_year(year) == True:
    print("Leap Year")
else:
    print("Not a Leap Year")
        
    