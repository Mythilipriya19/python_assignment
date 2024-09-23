#Iterables and Iterators
def subset():
 a = list(map(int, input("Enter set value : ").split()))

 A = set(map(int, input("Enter set value : ").split()))

 B = set(map(int, input("Enter set value : ").split()))

 total = 0

 for i in a:
    if i in A:
        total += 1
    elif i in B:
        total -= 1

 return total