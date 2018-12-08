# function to print the first m multiple 
# of a number n without using loop. 
def multiple(m, n): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(n, (m * n)+1, n) 
      
    print(*a) 
  
# driver code  
m = 2
n = 5
multiple(m, n) 
