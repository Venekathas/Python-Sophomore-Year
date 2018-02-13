text = input("Please enter a random assortment of letters!: ")
word = input("Now give me a word you want to find in that jumbled mess you gave me.: ")

index = (text.find(word))
if index < 0:
    print("Not found")
else:
    print(text.find(word))
    i = index + 1
    while 0 < text.find(word, i) :
        print(text.find(word, index + i))
        i = i + text.find(word, index + i)
