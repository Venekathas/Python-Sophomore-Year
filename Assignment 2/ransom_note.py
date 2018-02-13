ransom = input("Put in your ransom note, you horrible person: ")
magazine = input("Enter the words on the magazine clipping you made: ")

i = 0
l = 0
for ch in ransom:
    if ransom[i] not in magazine:
        print("Sorry, your note won't fit.")
    else:
        print("It's there!")
        i = i + 1
