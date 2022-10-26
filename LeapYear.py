def leapYear(year):
    
    leap = False
    
    if  year % 100:
        
        if not year % 4: leap = True
        
        else: leap = False
    
    else:
        
        if not year % 400: leap = True
        
        else: leap = False
    
    return leap
        
print("Enter a year to check wheather a leap year or not")
year = int(input())

print(leapYear(year))