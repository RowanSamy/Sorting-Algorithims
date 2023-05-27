# imported libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import time
# *******************************************

# Merge algorithm
# function to merge 2 arrays
def merge(first, mid, last, a):
    nl = mid - first + 1
    nr = last - mid
    left = [0] * nl
    right = [0] * nr
    for i in range(0, nl):
        left[i] = a[first + i]
    for j in range(0, nr):
        right[j] = a[mid + 1 + j]
    i = 0
    j = 0
    k = first
    while i < nl and j < nr:
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = right[j]
            j = j + 1
            k = k + 1
    while i < nl:
        a[k] = left[i]
        i = i + 1
        k = k + 1
    while j < nr:
        a[k] = right[j]
        j = j + 1
        k = k + 1

# function to split array into smaller arrays
def mergesort(first, last, a,x):
    if abs(first- last )< x:
        selection(a,len(a))
    else:

        if first < last:
            mid = int((first + last) / 2)
            mergesort(first, mid, a,x)
            mergesort(mid + 1, last, a,x)
            merge(first, mid, last, a)

# ******************************************************

# Selection algorithm
def selection(a, n):
    for i in range(0, n - 1):
        imin = i
        for j in range(i + 1, n):
            if a[j] < a[imin]:
                imin = j
        if i != imin:
            a[i], a[imin] = a[imin], a[i]

# ******************************************************

# insertion algorithm
def insertion(a, n):

    for i in range(1, n):
        key = a[i]
        j = i
        while j > 0 and a[j - 1] > key:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = key

# ****************************************************

# Quick sort algorithm
# function to get the pivot in the right place elements before it must be smaller and after it must be bigger
def Partition(arr, start, end):
    x = arr[end]
    i = start - 1
    a = end
    for j in range(start, a):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# function to choose a random pivot
def Randomized_Partitions(arr, start, end):
    i = random.randint(start, end)
    arr[i], arr[end] = arr[end], arr[i]
    return Partition(arr, start, end)

# recursive function to split the array into partitions
def Randomize_QuickSort(arr, start, end):
    if start < end:
        q = Randomized_Partitions(arr, start, end)
        Randomize_QuickSort(arr, start, q - 1)
        Randomize_QuickSort(arr, q + 1, end)

# **********************************************************

# Get the smallest kth element
def GetK_Smallest(arr, k, start, end):
    # first get the index of the pivot
    pivot = Partition(arr, start, end)
    while (len(arr) > 0):
        # if pivot is equal to k means that the element at index pivot is the smallest k element
        if (k == pivot):
            return arr[pivot]
        # if k smaller than pivot return the array before the pivot
        elif k < pivot:
            pivot = Partition(arr, 0, pivot - 1)
        else:
        # if k greater than pivot return the array after the pivot
            pivot = Partition(arr, pivot + 1, len(arr) - 1)
    return arr[pivot]
# ****************************************************************
# hybrid function call the merge function by passing the threshold
def hybrid(arr, T):
    return mergesort(0,len(arr)-1,arr,T)
# ****************************************************************

# ****************************main program*************************
print("**********Welcome**********")
# infinite loop until the user enter exit
while 1:
    # print menu of actions
    print("1.Quick sort")
    print("2.Merge sort")
    print("3.Selection sort")
    print("4.Insertion sort")
    print("5.Generate Graph")
    print("6.Hybrid sort")
    print("7.kth smallest")
    print("8.Exit")
    # take the user choice
    choice = int(input("what do you want to do ?! "))
    # check for the choice validity
    while choice < 1 or choice > 8:
        choice = int(input("Wrong choice Enter an action"))
    # Quick sort algorithm
    if choice == 1:
        s = int(input("Enter Size of random array: "))
        # making random array with size s taken from user
        ArrayOrg = np.random.randint(0, 20000000 + 1, s)
        print("Array before sorting ")
        print(ArrayOrg)
        Randomize_QuickSort(ArrayOrg, 0, len(ArrayOrg) - 1)
        print("Array After sorting ")
        print(ArrayOrg)
    # merge sort algorithm
    elif choice == 2:
        s = int(input("Enter Size of random array: "))
        ArrayOrg = np.random.randint(0, 20000000 + 1, s)
        print("Array before sorting ")
        print(ArrayOrg)
        mergesort( 0, len(ArrayOrg) - 1,ArrayOrg,0)
        print("Array After sorting ")
        print(ArrayOrg)
    # Selection sort algorithm
    elif choice == 3:
        s = int(input("Enter Size of random array: "))
        ArrayOrg = np.random.randint(0, 20000000 + 1, s)
        print("Array before sorting ")
        print(ArrayOrg)
        selection(ArrayOrg, len(ArrayOrg) )
        print("Array After sorting ")
        print(ArrayOrg)
    # Insertion sort algorithm
    elif choice == 4:
        s = int(input("Enter Size of random array: "))
        ArrayOrg = np.random.randint(0, 200000003+ 1, s)
        print("Array before sorting ")
        print(ArrayOrg)
        insertion(ArrayOrg, len(ArrayOrg) )
        print("Array After sorting ")
        print(ArrayOrg)
    # Generating Graph actions
    elif (choice == 5):
        print("1.Graph of:Quick,Merge,Insertion and selection")
        print("2.Graph of:Quick and Merge")
        print("3.Graph of:Insertion and selection")
        c= int(input("what do you want to do ?! "))
        while c< 1 or c> 3:
            choice = int(input("Wrong choice Enter an action"))
        # choosing the array size
        if c==1 or c==3:
         Num_Of_E = [10, 1000, 15000, 25000, 50000, 75000, 100000,150000, 200000]
        else:
         Num_Of_E = [10, 1000, 15000, 25000, 50000, 75000, 100000, 125000, 175000, 200000,500000,1000000,2500000,25000000,50000000]
        # making arrays to store execution time for all algorithms
        Quick = [0] * len(Num_Of_E)
        Merge = [0] * len(Num_Of_E)
        Insertion = [0] * len(Num_Of_E)
        Selection = [0] * len(Num_Of_E)
        # running all algorithms in different array sizes
        for i in range(len(Num_Of_E)):
            n = Num_Of_E[i]  # your array size
            Array = np.random.randint(0, 20000000 + 1, n)
            print("At n= " + str(n))

            if c==1 or c==2:
             Array3 = Array.copy()
             start_time3 = time.time()
             Randomize_QuickSort(Array3, 0, len(Array3) - 1)
             QuickTime = time.time() - start_time3
             print("Run time of Quick sort:" + str(QuickTime*1000) +" milliseconds" )
             Quick[i] = QuickTime * 1000

            if c == 1 or c == 2:
             Array4 = Array.copy()
             start_time4 = time.time()
             mergesort(0, len(Array4) - 1, Array4,0)
             MergeTime = time.time() - start_time4
             print("Run time of Merge sort:" + str(MergeTime*1000) +" milliseconds")
             Merge[i] = MergeTime * 1000

            if c == 1 or c == 3:
             Array1 = Array.copy()
             start_time1 = time.time()
             insertion(Array1,len(Array1))
             InsertionTime= time.time() - start_time1
             print("Run time of insertion sort:" + str(InsertionTime*1000)+" milliseconds")
             Insertion[i] = InsertionTime * 1000

            if c == 1 or c == 3:
             Array2 = Array.copy()
             start_time2 = time.time()
             selection(Array2, len(Array2))
             SelectionTime=time.time() - start_time2
             print("Run time of selection sort:" + str(SelectionTime*1000) +" milliseconds")
             Selection[i] = SelectionTime * 1000
            print("-----------------------------")
        # printing the time arrays
        if c == 1 or c == 2:
            print ("Quick sort execution time array")
            print(Quick)
        if c == 1 or c == 2:
            print(" Merge execution time array")
            print(Merge)
        if c == 1 or c == 3:
            print(" selection execution time array")
            print(Selection)
        if c == 1 or c == 3:
            print("Insertion execution time array")
            print(Insertion)

        # generating the graph
        if c == 1 or c == 2:
         plt.plot(Num_Of_E, Merge, color='r', label='merge', linestyle='dashed')
         plt.plot(Num_Of_E, Quick, color='blue', label='Quick', linestyle='-.')
        if c == 1 or c == 3:
         plt.plot(Num_Of_E, Selection, color='orange', label='Selection')
         plt.plot(Num_Of_E, Insertion, color='g', label='Insertion')
        # graph properties
        plt.xlabel('Length of array')
        plt.ylabel('Execution time (millisecond)')
        plt.title("Time performance of different sorting algorithms")
        plt.grid()
        plt.legend()
        plt.show()
    # hybrid sort algorithm
    elif choice ==6:
        # taking array size
        s = int(input("Enter the array size :"))
        # generating random array of length s
        arr = np.random.randint(0, 2000 + 1, s)
        #  taking the threshold
        T = int(input("Enter the threshold of the smallest element: "))
        # check for correct threshold
        while T > len(arr):
             T = int(input("Invalid K bigger that array length Enter a valid k: "))
        #  call hybrid function
        print("Array before sorting")
        print(arr)
        hybrid(arr,T)
        print("Array After sorting")
        print(arr)
    # testing K smallest element
    elif choice == 7:
        s = int(input("Enter the array size :"))
        # generating random array of length s
        arr = np.random.randint(0, 2000 + 1, s)
        k = int(input("Enter the K of the smallest element: "))
        while k > len(arr):
            k=int(input("Invalid K bigger that array length Enter a valid k: "))
        print("Random array is Array")
        print(arr)
        x = GetK_Smallest(arr, k - 1, 0, len(arr) - 1)
        print("The  " + str(k) + " smallest element is ", str(x))
    else:
        print("Thank you,Good bye :) ")
        exit()
    print("******************************************")
