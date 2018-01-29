# Author: Ajibola Vincent
# Course: COSC 5330
# Title: Operating Systems
# Professor: DR Arun Kulkarni
# Description: Program to demonstrate Banker's algorithm

# import numpy as package to handle array computation
import numpy as np

#list of processes
processes = ['P1', 'P2', 'P3', 'P4', 'P5']
# order is a list which contains the order of operations
order = []


# function  to read input from file
def get_input():
    allread = []
    # open the file for reading
    with open('C:\\Users\\Ajibola Vincent\\PycharmProjects\\Bankz\\input.txt','r') as f:
            test = f.readlines()
            for line in test:
                allread.append(line.split())
                allread = list(map(lambda x: [int(x[i]) for i in range(len(x))], allread))
            n = int(allread[0][0])
            print("Number of processes is ", n)
            r = int(allread[1][0])
            print("Number of resources is ", r)
            existing = allread[2]
            print("Total number of existing resources ", existing)
            # split the list into arrays of allocation and needed
            allocation = allread[3:8]
            needed = allread[8:]
            #return a tuple of 3 lists
            return allocation,needed,existing


# function for Bankers algorithm
def bankers(my_tuple):
    a, ne,e = my_tuple
    n = len(processes)
    done = False
    # Initialise false as list on processes
    finish = [False] * n
    # convert the list to numpy arrays
    a = np.array(a)
    e = np.array(e)
    ne = np.array(ne)
    alloc = a.sum(axis=0)
    #calculate the available vector
    avail = e - alloc
    print("The initial available vector is ", avail)
    while not done:
        done = True
        for i in range(n):
            if (not finish[i]) and (ne[i] <= avail).all():
                finish[i] = True
                # append the completed process to the order list
                order.append(processes[i])
                print("Executing process ", processes[i])
                #Release the allocated resources upon completion and add to available
                avail += a[i]
                done = False
                print("The available vector is now ", avail)


# function to check for safe state
def safe_state(my_tuple):
    allocated, need, existing = my_tuple
    # Determine the number of processes n
    n = len(allocated)
    # Initialise Finish and Work vectors
    finish = np.array([False] * n)
    temp1 = np.array(allocated)
    temp2 = temp1.sum(axis=0)
    work = existing - temp2
    done = False
    print("*************************************************")
    print("Checking if state is safe")
    print("Initial Work vector: ", work)
    print("Initial Finish vector: ", finish)
    print("*************************************************")
    while not done:
        done = True
        for i in range(n):
            # check if the need vector is less than or equal to the available vector
            if (not finish[i]) and (need[i] <= work).all():
                work = work + allocated[i]
                finish[i] = True
                done = False
                print("Could finish process: ")
                print("Work vector: ", work)
                print("Finish vector: ", finish)

    return all(finish);


# main method
def main():
    print("Checking safe state")
    #run safe state function
    safe_state(get_input())
    print("****************************************************************")
    print("Bankers Algorithm Now Running")
    #run banker's algorithm
    bankers(get_input())
    for i in range(len(processes)):
        #print order of execution
        print("The order of execution is",order[i])
    print("Ended")


if __name__ == "__main__":
    main()
