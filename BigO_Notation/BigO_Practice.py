# O(1) - constant time
def contsantO ():
    # O(1) - constant time
    # work does not grow with input size
    # accessing array element is the same regardless of size
    ar = [1,2,3,4,5]
    print(ar[1])


# O(n) linear time
# O(n) - linear time
# work grows directly with input size linearly

def find_number(arr,target):
    # if the list doubles in size, number of checks double also
    for num in arr:
        if num == target:
            return True
    return False

#print(find_number([1,2,3,4,5],5))


###############
### O(log n) - logarithmic time
###############

# usually happens when yhou repeatedly divide or multiply the problem in half

def binary_search(arr,target):
    low = 0 #low index
    high = len(arr)-1 #high index

    while low <= high:
        mid = (low + high)//2

        if arr[mid]==target:
            print(f'index value is: {mid}')
            return mid
        elif arr[mid]< target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#binary_search([1,2,3,4,5],3)



######################
## O(N^2) -- Quadratic Time
#######################
# usually caused by nested loops

def quadtime(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#quadtime(5)

##########################
## O(2^2) -- exponential
############################

# increases exponentially
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)









