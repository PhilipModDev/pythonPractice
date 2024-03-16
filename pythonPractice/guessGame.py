
gussNumber = 10
maxGuesses = 4
counter = 0
guess = 0

print('Game starting.')

while guess != gussNumber :
    if counter > maxGuesses : break
    guess = int(input('Guess'))
    print('Number of Guess left',maxGuesses - counter)
    
    if guess < gussNumber :
        print('To low.')
    
    if guess > gussNumber :
        print('To high')   
        
    counter = counter + 1  
  
if counter > maxGuesses :
    print('You lost.')  
print('great Job your tries were',counter)   
