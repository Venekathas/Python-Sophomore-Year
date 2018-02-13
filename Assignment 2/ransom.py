#Bradley Smith 2/7/2017
#Amal Abdel Raouf
#Assignment 2 (Ransom Note)

#This program gets two strings from the user, a ransom note and a
#magazine clipping. Then it checks to see if the ransom note can
#be made with the magazine clipping provided.


ransom = input("Put in your ransom note, you horrible person: ")
magazine = input("Enter the words on the magazine clipping you made: ")

i = 0
for ch in ransom:

    #If the letter isn't present, it denies the user and breaks the loop.
    if ransom[i] not in magazine:
       print("Sorry, your note won't fit.")
       break
    #If the letter is there, the program moves onto the next part.
    else:
       print("The character '" + ransom[i] +"' is there there!")
       chInMag = magazine.count(ransom[i])
       chInRan = ransom.count(ransom[i])

    #This checks to see if there are enough letters in the clipping to
    #use in the note. If there are not, it breaks the loop.
    if chInMag >= chInRan:
        print("And you have enough characters for it too.")
        i = i + 1
    else:
        print("But there aren't enough of that character.")
        break

    
