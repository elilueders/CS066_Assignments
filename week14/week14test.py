def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

import time
import random

N = 10000
random_list = [random.randint(1,1000000) for i in range(N)]
random_list_copy1 = random_list[:]
random_list_copy2 = random_list[:]
random_list_copy3 = random_list[:]
random_list_copy4 = random_list[:]

# start = time.time()
# bubbleSort(random_list_copy1)
# end = time.time()
# print("Bubble sort:",(end-start),"seconds")


# start = time.time()
# insertionSort(random_list_copy2)
# end = time.time()
# print("Insertion sort:",(end-start),"seconds")

# start = time.time()
# mergeSort(random_list_copy3)
# end = time.time()
# print("Merge sort:",(end-start),"seconds")

start = time.time()
random_list_copy4.sort()
end = time.time()
print("Timsort sort:",(end-start),"seconds")

