import time #Importing time to keep track of how long the methods run.
import random #Importing random for shuffling and list creation.
import BinaryTree #Importing binary tree to create trees.

'''
This program tests the sorting efficiencies of four different sorting algorithms.
First, it creates a list of 10,000 integers. Then it calls each method, recording
how long it takes for each function to sort the list. After that, it increases
the list size by 10,000 and starts all over again. Once an alogrithm takes
more than 60 seconds to sort the list, it is out of the running. The program will
run until all sorting algorithms are exhausted.

The main purpose of this program is to see which sorting algorithm is best at
different sizes of lists.
'''

'''
This method sorts a list using the bubble_sorting strategy.
@param a_list The list to be sorted.
@return The time it takes the function to finish.
'''
def bubble_sort(a_list):
    start = time.time()
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    end = time.time()
    return end-start

'''
This method sorts a list using the selection_sorting strategy.
@param a_list The list to be sorted
@return The time it takes the function to finish.
'''
def selection_sort(a_list):
    start = time.time()
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
    end = time.time()
    return end-start

'''
This method sorts a list using the merge_sorting strategy.
@param a_list The list to be sorted
@return The time it takes the function to finish.
'''
def merge_sort(a_list):
    start = time.time()
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
        
        
    end = time.time()
    return end-start
'''
This method sorts a list using the tree_sorting strategy.
@param a_list The list to be sorted
@return The time it takes the function to finish.
'''
def tree_sort(a_list):
    start = time.time()
    r = BinaryTree.BinaryTree(a_list[0])
    for x in range(len(a_list)):
        if x > 0:
            r.insert(a_list[x])
    end = time.time()
    return end-start

'''
This main method creates a list and a number of timers to test the four
sorting algorithms. It creates the variables, then in a while loop, adds
values to the list and calls the 4 methods, recording their times. It also
evaluates when one algorithm exhausts its 60 second time limit.
'''
def main():
    #Creates a list to be added to and sorted and timers to keep track of times.
    a_list = []
    b_timer, s_timer, m_timer, t_timer = 0, 0, 0, 0
    round_count = 1 #Adds a counter, just for fun.

    #This while loop makes sure the functions will be tested until all of them
    #fail their 60 second time limit.
    while b_timer or s_timer or m_timer < 60.00:
        #This just creates different printed outputs depending on if it is
        #round one or not.
        if round_count == 1:
            print("Creating a random list of 10,000 numbers.")
        else:
            print("Extending the list by 10,000.")
        #This for loop adds 10000 random numbers to the list.
        for x in range((10000)):
            a_list.append(random.randrange(1, 10000))
        print("\nRound: " + str(round_count) +" START!\n")
        round_count += 1
        
        #If bubble_sort hasn't hit its time limit, it will test the function's
        #ability to sort the list. Shuffling to assure the list is not pre-sorted.
        if b_timer < 60.00:
            print("Shuffling the list.")
            random.shuffle(a_list) #Shuffles the list to make it unsorted again.
            print("Starting the bubble sort.")
            b_timer = bubble_sort(a_list)
            print(b_timer)
            if b_timer > 60.00:
                print("Bubble Sort is out! ")

        #If selection_sort hasn't hit its time limit, it will test the function's
        #ability to sort the list. Shuffling to assure the list is not pre-sorted.                
        if s_timer < 60.00:
            print("Shuffling the list.")
            random.shuffle(a_list) #Shuffles the list to make it unsorted again.
            print("Starting the selection sort.")
            s_timer = selection_sort(a_list)
            print(s_timer)
            if s_timer > 60.00:
                print("Selection Sort is out.")

        #If merge_sort hasn't hit its time limit, it will test the function's
        #ability to sort the list. Shuffling to assure the list is not pre-sorted.         
        if m_timer < 60.00:
            print("Shuffling the list.")
            random.shuffle(a_list) #Shuffles the list to make it unsorted again.
            print("Starting the merge sort.")
            m_timer = merge_sort(a_list)
            print(m_timer)
            if m_timer > 60.00:
                print("Merge Sort is... finally out. What a waste of space!")

        #If tree_sort hasn't hit its time limit, it will test the function's
        #ability to sort the list. Shuffling to assure the list is not pre-sorted.             print("Merge Sort is...finally out.")
        if t_timer < 60.00:
            print("Shuffling the list.")
            random.shuffle(a_list) #Shuffles the list to make it unsorted again.
            print("Starting the tree sort.")
            t_timer = tree_sort(a_list)
            print(t_timer)
            if t_timer > 60.00:
                print("Tree Sort is...finally out.")

        random.shuffle(a_list)

if __name__ == "__main__":
    main()



