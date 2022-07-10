def binary_search(array, value):
    low=0
    high=(len(array))-1  # High value is last index of array. [length of array -1 = Last index or high Value] 
                        # As we need the index of the value we are looking for.
    while low<=high :
        mid=(low+high)//2       #[Remember in python 3.x you need to use '//' instead of '/' to get the floor value]
        if array[mid]==value :
            return mid
        elif array[mid]<value:
            low=mid+1
        else :
            high=mid-1
    return "Your value does not exist in array"



test_list = [1,3,9,11,15,19,29,31]
test_val1 = 32
test_val2 = 15
test_val3 = 31
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))
print (binary_search(test_list, test_val3))
