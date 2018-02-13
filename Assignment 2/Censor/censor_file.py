#Bradley Smith 2/9/2017
#Amal Abdel Raouf
#Assignment 2 (Censor File)

#This program opens and rewrites a file into a new file, censoring
#all words that are a length of 4.

#This main function opens\creates the new files then calls the other method
#to change them. Then it prints out the files contents to compare.
def main():
    file = input("What file do you want to censor?: ")
    fin = open(file)
    nin = open("new_words.txt","w")
    censor(fin, nin)
    fin = open(file, "r")
    nin = open("new_words.txt","r")
    print("\nHere is the first file")
    print(fin.read())
    print("\nHere is the second file")
    print(nin.read())
    fin.close()
    nin.close()

#This function Takes the lines of the file, splits them into a list,
#then changes the 4 letter words to asterisks. Finally, it write those
#edited strings to a new file.
def censor(fin, nin):
    i = 0
    for line in fin:  #Splits the files lines into a list.
        splits = list(line.split())
        print("Here are the words in line " + str(i+1) + ".")
        for value in splits: #Checks the list for words of length 4 and changes them.
            print(value + ' ', end ='')
            if int(len(value)) == 4:
                   value = '****'
            nin.write(value + ' ')
        print('\n')
        nin.write('\n')
        i = i + 1
    
if __name__=="__main__":
    main()


            
