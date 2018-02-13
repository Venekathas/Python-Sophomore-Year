#Bradley Smith / 2/19/2017  /  Assignment 3:SocialEvents
#Professor Amal Abdef Raouf / CSC 212

#This program allows the user to create any number of events, with titles, dates, and attendees.
#Then it displays them in multiple,user specified options.

import operator

class SocialEvent:
    #This constructor builds a social event.
    #@param title The title of the event.
    #@param date The date of the event.
    #@param attend The number of attendees for the event.
    def __init__(self, title, date, attend):
        self.title=title
        self.date=date
        self.attend=attend

    #This function returns the title of the event.
        #@return title The title of the event.
    def getTitle(self):
        return self.title

    #This function sets the title of the event.
    #@param title The title of the event.
    def setTitle(self, title):
        self.title=title

    #This function returns the date of the event.
        #@return date The date of the event.
    def getDate(self):
        return self.date

    #This function sets the date of the event.
    #@param date The date of the event.
    def setDate(self, date):
        self.date=date

    #This function returns the number of attendees for the event.
        #@return attend The number of attendees for the event.
    def getAttend(self):
        return self.attend
    
    #This function sets the number of attendees for the event.
    #@parm attend The number of attendees for the event.
    def setAttend(self, attend):
        self.attend=attend

    #This function displays the event details in an order specified the user.
        #@param eventList The list of event objects.
        #@param choice The choice the user made.
    def displayEvent(self,eventList, choice):
        if choice == 'title':
            for event in sorted(eventList, key=operator.attrgetter('title')):
                print("%-30s %-12s %0d" \
              % (event.title, event.date, event.attend))

        if choice == 'date':
            for event in sorted(eventList, key=operator.attrgetter('date')):
                print("%-30s %-12s %0d" \
              % (event.title, event.date, event.attend))

        if choice == 'attendees':
            for event in sorted(eventList, key=operator.attrgetter('attend')):
                print("%-30s %-12s %0d" \
              % (event.title, event.date, event.attend))

    #This function prints the values of the event object.
        #@return A string of details.
    def __str__(self):
        return "Title: " + self.getTitle() + "\nDate: " + self.getDate() + "\nAttendees: " + str(self.getAttend())

#This main function creates a number of events with user input.
    #From there, it gets a choice from the user to see how they would like their event list to be displayed.
def main():
    events =int(input("How many events are you planning?: "))

    eventList = []
    for x in range (events):
        print("Event " + str(x+1) + ":")
        title, date, attend = input("What is the name of the event?: "),input("When is the event?(YYYY/MM/DD): "),int(input("How many are attending the event?: "))
        event = SocialEvent(title, date, attend)
        eventList.append(event)
        
    while 1 == 1:
        choice = input("How would you like to display the events? By title, date, or attendees? If you're done, type done.\nEnter Title, Date, Attendees, or Done:")
        
        if choice.lower() == 'done':
            break
        else:
            print("Event Name                   | Event Date | Attendees")
            event.displayEvent(eventList, choice.lower())
        





if __name__ == "__main__":
    main()
