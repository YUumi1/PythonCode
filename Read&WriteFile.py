import string
import time

def fuctionWrite():
    
    file = open('Race1.txt','w')
    
    print('Enter a string and u will see the sorcery😒😒')
    userString = input('Input >> ')
    
    print('Output>> ',end='')
    
    for x in range(len(userString)):
        
        if userString[x] in string.punctuation:
            
            continue  
        
        if userString[x] in string.whitespace:
            
            continue
        
        print(userString[x].lower(),end='')
            
        file.write(userString[x].lower())
        
def functionRead():
    
    file = open('Race1.txt','r')
    
    if file:
        
        print('Output>> ',end='')
        print(file.read())
        
    else:
        
        print('There is any of file named "Race1.txt"')

while 1:
    
    print("Do you want to write or read a file named 'Race1.txt'")
    choose = input()
    
    if choose.lower().startswith('w'):
        
        fuctionWrite()
        
        print('\nSaving to the file....Please wait...',end='')
        time.sleep(1)
        print('...',end='')
        time.sleep(1)
        print('...')
    
    else:
        
        print('Reading Please wait...',end='')
        time.sleep(1)
        print('...',end='')
        time.sleep(1)
        print('...')
        
        functionRead()
        
    print('Do you want to continue?')
    tend = input()
    
    if tend.lower().startswith('n'):
        
        print("The progaram exited...",end='')
        time.sleep(1)
        print('...',end='')
        time.sleep(1)
        print('...')
        
        break
