#Bradley Smith / 2/18/2017 / Assignment 3:Hamburger
#Professor Amal Abdef Raouf / CSC 212

#This programs creates a hamburger object from the Hamburger class and tests it to the fullest! Afterwards allowing the user to use the "bite" method to virtually consume the burger.
class Hamburger:
    #This constructor builds a hamburger
    #@param weight The weight of the burger.
    #@param doneness The doneness of the burger.
    #@param cheese Whether the burger has cheese or not.
    #@param toppings A list of toppings on the burger.
    def __init__(self,weight,doneness,cheese,toppings):
        self.weight   = weight
        self.doneness = doneness
        self.cheese   = cheese
        self.toppings = toppings

    #This function returns the weight of the burger.
        #@return weight The weight of the burger. 
    def getWeight(self):
        return self.weight

    #This function sets the weight of the burger.
    #@param weight The weight of the burger.
    def setWeight(self,weight):
        self.weight = weight

    #This function returns the doneness of the burger.
        #@return doneness the doneness of the buger.
    def getDoneness(self):
        return self.doneness

    #This function sets the doneness of the burger.
    #@param doneness The doneness of the burger.
    def setDoneness(self,doneness):
        self.doneness = doneness

    #This function returns whether or not there is cheese on the burger.
        #@return cheese The boolean of cheese.
    def getCheese(self):
        return self.cheese

    #This function sets the value of cheese to true or false.
    #@param cheese The boolean of cheese.
    def setCheese(self, cheese):
        self.cheese = cheese

    #This function returns the list of toppings in a string format for printing.
        #@return A string of the list of toppings.
    def getToppings(self):
        return ", ".join( str(i) for i in self.toppings[0:-1] )+ ', and ' + self.toppings[-1] + "."

    #This function sets the values of the topping list.
    #@param toppings The list of toppings.
    def setToppings(self, toppings):
        self.toppings = toppings

    #This function allows the user to 'bite' the burger, consuming it ounce by ounce
    def bite(self):
        if self.weight > 0:
            self.weight -=1
        else:
            print("There is no more left!")

    #This print function prints the values of each variable a burger consists of.
            #@return A string of values that make up the burger.
    def __str__(self):
        if self.getCheese == True:
            return "You ordered a " +str(self.getWeight())+ " ounce burger cooked " +self.getDoneness()+ " with cheese, topped off with " + self.getToppings()
            
        else:
            return "You ordered a " +str(self.getWeight())+ " ounce burger cooked " +self.getDoneness()+ " without cheese, topped off with " + self.getToppings()

#This main function creates a burger with hard-coded values, then changes those values individually, printing those values.
        #There is also a loop that handles the bite function before sending the user off.
def main():
    burger=Hamburger(4,'medium',True,['pickles', 'lettuce', 'tomato'])
    print(burger)
    
    burger.setWeight(8)
    burger.setDoneness('medium-rare')
    burger.setCheese(False)
    burger.setToppings(['onion', 'bacon', 'mayonnaise'])

    print(burger)
    
    while burger.weight > 0:
        bite = input("Would you like to take a bite? Y/N: ")
        if bite == 'Y' or bite == 'y' or bite == 'yes' or bite == 'Yes' or bite == 'YES':
            burger.bite()
            print("Mm, that was good.")
        else:
            break
    print("That's all! Thanks for stopping by!") 
        





if __name__ == "__main__":
    main()
