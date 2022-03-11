import time

def sum_of_n_loop(n):
    total = 0
    
    for i in range(n+1):
        total += i
        
    return total

def sum_of_n_formula(n):
    return n*(n+1)/2

start = time.time()
print(sum_of_n_loop(100000000))
end = time.time()
print("That took",end-start,"seconds")


start = time.time()
print(sum_of_n_formula(100000000))
end = time.time()
print("That took",end-start,"seconds")
#print("That took",f"{end-start:.10f}","seconds") #you can do this to format your float values