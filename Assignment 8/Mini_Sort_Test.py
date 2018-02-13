import time
import random

    def bubble_sort(a_list):
        sort_list = []
        for x in range(len(a_list)):
            sort_list.append(a_list[x])
        print(a_list)
        print(sort_list)
        start = time.time()
        for pass_num in range(len(a_list) - 1, 0, -1):
            for i in range(pass_num):
                if a_list[i] > a_list[i + 1]:
                    temp = a_list[i]
                    a_list[i] = a_list[i + 1]
                    a_list[i + 1] = temp
        end = time.time()
        print(a_list)
        print(sort_list)
        return end-start

    def selection_sort(a_list):
        sort_list = []
        for x in range(len(a_list)):
            sort_list.append(a_list[x])
        print(a_list)
        print(sort_list)
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
        print(a_list)
        print(sort_list)
        return end-start
        
    def merge_sort(a_list):
        sort_list = []
        for x in range(len(a_list)):
            sort_list.append(a_list[x])
        print(a_list)
        print(sort_list)
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
            
        print(a_list)
        print(sort_list)
        end = time.time()
        return end-start

def main():
    unsorted_list = []
    print("Creating a random list of 10 numbers.")
    for x in range(10):
        unsorted_list.append(randrange(1, 10))
    round_count = 1
    print("Round: " + str(round_count))
    b_timer = bubble_sort(unsorted_list)
    print("The timer for bubble sort is: " + str(b_timer))

    s_timer = selection_sort(unsorted_list)
    print("The timer for selection sort is: " + str(s_timer))

    m_timer = merge_sort(unsorted_list)
    print("The timer for merge sort is: " + str(m_timer))

    while b_timer or s_timer or m_timer < 60.00:
        print("Extending the list by 2.")
        a_list = []
        round_count += 1
        print("Round: " + str(round_count) +" START!\n")
        
        for x in range((2*round_count)):
            a_list.append(randrange(1, 10))
        unsorted_list = a_list
            
        if b_timer < 60.00:
            print("Starting the bubble sort.")
            b_timer = bubble_sort(a_list)
            a_list = unsorted_list
            print(b_timer)
            if b_timer > 60.00:
                print("Bubble Sort is out! ")
                
        if s_timer < 60.00:
            print("Starting the selection sort.")
            s_timer = selection_sort(a_list)
            a_list = unsorted_list
            print(s_timer)
            if s_timer > 60.00:
                print("s_timer is out.")
                
        if m_timer < 60.00:
            print("Starting the merge sort.")
            m_timer = merge_sort(a_list)
            a_list = unsorted_list
            print(m_timer)
            if m_timer > 60.00:
                print("m_timer is out.")

if __name__ == "__main__":
    main()
