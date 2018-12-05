import time
import threading

start_time = time.time()

n = 179
k = n

def slowsort(A, i, j):
    if i >= j:
        return
    m = (i+j)//2
    slowsort(A, i, m)
    slowsort(A, m+1, j)
    if A[m] > A[j]:
            A[m],A[j] = A[j],A[m]
    slowsort(A, i, j-1)

def print_result():
    print(numList)

# fill list with number from n down to 0
# you could use a for loop instead, but the following statement is more "pythonic" ;-)
numList = list(range(n, 0-1, -1))

print(numList)

#numList_woThread = numList #copy the list for testing it with slowsort without threading

#start_time_woThreads = time.time()

#slowsortin without threads:
#slowsort(numList_woThread, 0, n)

#end_time_woThreads = time.time()


#print("Without multithreading: -- %s seconds --" % (end_time_woThreads - start_time_woThreads))


#split list into two for faster processing
list1 = numList[0:n//2]
list2 = numList[n//2:n+1]

#start threads, each thread computes one portion of the original list
t1 = threading.Thread(target=slowsort, args=(list1, 0, len(list1)-1,))
t2 = threading.Thread(target=slowsort, args=(list2, 0, len(list2)-1,))


t1.start()
t1_start_time = time.time()

t2.start()
t2_start_time = time.time()

t1.join() #wait for thread1 to finish
t1_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t1.name, t1_end_time - t1_start_time))

t2.join() #wait for thread2 to finish
t2_end_time = time.time()
print("Thread: %s -- %s seconds --" % (t2.name, t2_end_time - t2_start_time))


list2.extend(list1) #reconnect the two list portions
print(list2)


print("--- %s seconds ---" % (time.time() - start_time))
