

def binary_search(arr,ele):
    # first and last index values
    first = 0
    last = len(arr) -1
    found = False
    while first <= last and not found:
        mid = int((first+last)/2)
        # match found
        if arr[mid] == ele:
            found = True
        # set new midpoints up or down on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up
            else:
                first = mid + 1
    return found

# ----- Recursive version of binary search ---------
def rec_bin_search(arr, ele):
    #Base cAse
    if len(arr) == 0:
        return False
    # recursive case
    else:
        
        mid = len(arr)/2
        # if match found
        if arr[mid]==ele:
            return True
        else:
        # calll again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
        # or call on the first half
            else: 
                return rec_bin_search(arr[mid+1],ele)


# ENTER IN TERMINAL

# my_array = [i for i in range(1, 101)]
# from samples import binary_search, rec_bin_search
# my_array
#(should return array of numbers..)
# then enter:
# binary_search(my_array, 50)
