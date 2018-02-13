'''
Simulation of printer queue in a computer lab with students 
submitting print tasks.  Objective: estimate task waiting time in queue
for different printer print rates. 

Assumptions: On average, there are 10 students in the lab.  A student
sends two print jobs on average, 1-20 pages long (equally likely). 
Printer can print in draft mode (10 ppm) or high quality (5 ppm).

Observations: With 10 students in the lab at any given time printing twice,
there are 20 print jobs per hour (or every 3600 seconds). So, we expect to 
see 1 job every 180 seconds (20 tasks / 3600 seconds).  

Simulation logic:
1. Create a queue of print tasks. Each task will be given a timestamp 
upon its arrival. The queue is empty to start.

2. For each second (current_second):
• Does a new print task get created? If so, add it to the queue with 
  the current_second as the timestamp.
• If the printer is not busy and if a task is waiting,
   – Remove the next task from the print queue and assign it to 
  the printer.
   – Subtract the timestamp from the current_second to compute the waiting 
  time for that task.
   – Append the waiting time for that task to a list for later processing.
   – Based on the number of pages in the print task, figure out how much 
     time will be required.
• The printer now does one second of printing if necessary. It also subtracts 
   one second from the time required for that task.
• If the task has been completed, in other words the time required has reached 
   zero, the printer is no longer busy.
   
3. After the simulation is complete, compute the average waiting time from 
   the list of waiting times generated.
'''

'''
This program has been edited by Bradley Smith on 3/26/2017 for CSC 212. Submited to Amal Abdel Raouf.

Simulation Changes:
1. The simulation is now able to be configured from a file supplied by the user.
   - Those values are limited to certain ranges depending on the category.
     a. Duration of simulation in secionds(Valid range is 3600-36000)
     b.	Number of simulation experiments (valid range is 1-100) 
     c.	Minimum task size (must be in range 1-100)
     d.	Maximum task size (must be in range 1-100 and >= minimum)
     e.	Number of printers (must be 1 or 2)
     f.	Page rate of printer 1 (must be in the range 1-50)
     g.	Page rate of printer 2 (if number of printers is 1, this value would not be specified)

2. The results of the simulations will be printed as well as written to a file. Those results are:
    - Average Wait time
    - Tasks remaining.
    - Tasks created.
    - Overall Average wait time.

3. A few changes in format to incorporate the addition of a second printer.

4. The addition of exception handling to consider input validation.
    - TypeError: When an input from the file is not integer.
    - IndexError: When an input doesn't meet the valid range of values.

Future Considerations:
1. Paper limits
2. Paper jams
3. Ink limits
4. IT Service
5. Student attendence

'''

from Queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task: #This task class is edited to consider max and min task size submitted from the file. 
    def __init__(self,time, min_size, max_size):
        self.timestamp = time
        self.pages = random.randrange(min_size, max_size)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

#The simulation class has been heavily edited to include the second printer.
#The parameters consider all of the configurations from the config file.
#This now returns a value for averaging all of the average waiting times.

def simulation(duration, min_size, max_size, num_printers, ppm1, ppm2,sim_num):

    printQueue = Queue()
    labprinter = Printer(ppm1)
    waitingtimes = []
    printjobs = 0                  #Added a counter for how many jobs the printer does.
    fout = open('sim_out.txt','a') #This opens a file for appending the waiting times.
    if(num_printers == 2):         #This if function only intiates if a second printer is configurated. 
        labprinter2 = Printer(ppm2)#It creates a separate list for wait times and counter for jobs.
        waitingtimes2 = []
        printjobs2 = 0
    
    
    for currentSecond in range(duration):
        if newPrintTask():
            task = Task(currentSecond, min_size, max_size) #Now needs to pass configurations from file.
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.is_empty()):
            printjobs += 1
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        #This if function only initiates if two printers are configured. 
        if (num_printers == 2 and (not labprinter2.busy())) and (not printQueue.is_empty()):
            printjobs2 += 1
            nexttask = printQueue.dequeue()
            waitingtimes2.append(nexttask.waitTime(currentSecond))
            labprinter2.startNext(nexttask)

        labprinter.tick()
        if(num_printers == 2): #This if function only initiates if two printers are configured.
            labprinter2.tick()
    #This block will print the results of average wait times and also write to the file.
    print("-----------------------------Simulation %3d-----------------------------"%(sim_num + 1))
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait for printer 1: %6.2f secs.%3d tasks remaining of %3d tasks." \
          %(averageWait,printQueue.size(),printjobs))
    fout.write("Average Wait for printer 1: %6.2f secs.%3d tasks remaining of %3d tasks.\n" \
          %(averageWait,printQueue.size(),printjobs))
    #This block does the same as the previous block, only when there are two printers configured.
    #In rare cases where the second printer is never used, this prevents a division by 0 error.
    if (num_printers == 2 and printjobs2 > 0):
        averageWait2 = sum(waitingtimes2)/len(waitingtimes2)
        print("Average Wait for printer 2: %6.2f secs.%3d tasks remaining of %3d tasks." \
              %(averageWait2,printQueue.size(),printjobs2))
        fout.write("Average Wait for printer 2: %6.2f secs.%3d tasks remaining of %3d tasks.\n" \
              %(averageWait2,printQueue.size(),printjobs2))
    #In case the second printer was never used, this prints and writes that to rhe file.    
    elif(num_printers ==2):
        print("The second printer was never used.")
        fout.write("The second printer was never used.\n")
    print("\n")
    #This block closes the file and returns the averageWait time. In cases where there are two
    #printers, the formula changes.
    fout.close()
    if(num_printers ==1):
        return averageWait
    if(num_printers ==2):
        averageWait = (averageWait + averageWait2) / 2
        return averageWait
    
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

#I created this function to get the information from the config file. It returns all of the
#configuration information in order to make the simulation run.
def get_info():

    #this block opens the file and creates a line object to read specific lines.
    file = "sim_config.txt"
    fin = open(file)
    line = fin.readlines()

    #This is a try except block that tries setting the values from the file to certain variables.
    #If any of them are out of range, an IndexError will be raised with a custom string per assignment. And the program will be terminated.
    #If any values are not integers, a ValueError is raised and terminates the program.
    while True:
        try:
            duration = int(line[0])
            if(duration > 36000 or duration < 3600):
                raise IndexError('Invalid number for duration. Exiting.')
            num_sims = int(line[1])
            if(num_sims > 100 or num_sims < 1):
                raise IndexError('Invalid number of simulations. Exiting.')
            min_size = int(line[2])
            if(min_size > 100 or min_size < 1):
                raise IndexError('Invalid number of min task size. Exiting.')
            max_size = int(line[3])
            if (max_size > 100 or max_size < min_size):
                raise IndexError('Invalid number of max task size. Exiting.')
            num_printers = int(line[4])
            if (num_printers != 1 and num_printers != 2):
                raise IndexError('Invalid number of printers. Exiting.')
            ppm1 = int(line[5])
            if(ppm1 > 50 or ppm1 < 1):
                raise IndexError('Invalid number of PPM. Exiting.')
            #This block will automatically assign the higher PPM to PPM1, so later, when both printers
            #are idle, the next available task will be assigned to the printer with higher PPM.
            if (num_printers > 1):
                ppm2 = int(line[6])
                if(ppm2 > 50 or ppm2 < 1):
                    raise IndexError('Invalid number of PPM. Exiting.')
                if(ppm2 > ppm1):
                    ppm1, ppm2 = ppm2, ppm1
            else:
                ppm2 = 0
            break
        except ValueError:
            print("One or more values was not an integer. Exiting.")
            exit()
        except IndexError as e:
            print(e)
            exit()
    #Closes the file.        
    fin.close()
    #Returns all of the configuration settings to the main function.
    return duration, num_sims, min_size, max_size, num_printers, ppm1, ppm2
#I edited the main function to first call get_info() in order to extract the configurations from the config file.
def main():
    #This calls get_info() and assigns all the config information to be passed to the simulatio.
    duration, num_sims, min_size, max_size, num_printers, ppm1, ppm2 = get_info()
    
    #This opens the sim_out file in write mode in order to clear the file when it is later appended.
    fout = open('sim_out.txt', 'w')
    
    #This list will be used to calculate total average wait time. 
    overall_waittime = []
    
    #This for loop calls the simulation num_sims amount of times.
    #Each time it is receiving an average waittime from that simulation and putting it into a list.
    #The call to simulation is sending all of the configurations plus the simulation number it is currently on.
    for i in range(num_sims):
        overall_waittime.append(simulation(duration, min_size, max_size, num_printers, ppm1, ppm2, i))

    #This block calculates the total average wait time then prints/writes the result to a file.
    averageWait = (sum(overall_waittime)/len(overall_waittime))
    fout = open('sim_out.txt', 'a')
    print("Overall average wait time is %6.2f seconds." %(averageWait))
    fout.write("Overall average wait time is %6.2f seconds.\n" %(averageWait))
    fout.close()
    
if __name__ == "__main__":
    main()
