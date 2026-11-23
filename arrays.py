# Static Arrays- Have a fixed size , don't exist independently in python.( are used under the hood )

# Dynamic arrays are used in code as lists(usually)
# when appending any element to a full list(dynamic array) . a static array is used under hood which will alot memory ( usually twice the size) for a new list/array.

# Arrays are fast as they get to element by address as the address will b ein a contiguous block.
# target address = Base address + ( index * element size)


# all deletions and insertions apart from the end will be o(n).

# all insertions at the end will be mostly o(1) but once i na while be o(n) when the 
# arrays is ull and a larger arrays needs to be allocated someplace else , then all elements will be shifted and it will be o(n)

Array1 = [1,2,3,4,5] 

Array1.append(34) # adds at the end of array in O(1) -> amortized meaning usually this but when array full the this action can be O(n)

Array1.insert(2,332)  # insert in the middle or at start by specifying index and then telling the value we want to insert  --> O(n)
ṇ
print(Array1[2]) # accessing the element at index 2 in array  -->  O(1)

if 3311 in Array1:
    print(True)  # checking for an element in array --> O(n) as it iterats over each element in the array matching values. prints bool True if found else False
else: print(False)







