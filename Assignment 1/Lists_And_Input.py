string = input("Give me some words separated by spaces. Feel free to repeat!: ")
i = 0
words = set(string.split())
for i in words:
    print(i)
