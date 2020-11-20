# 1. Given a string, write a function that uses recursion to reverse it.

# strings are indexed sequences of characters

def recursive_string(string):
    # Base case
    # Take first character using slicing and when the length is less than or equal to one:
    if len(string) <= 1:
        return string
    # Recursive case
    else :
        return recursive_string(string[1:]) + string[0]
    # Slicing everything index '1' and on. Then concatenate the first index and so on, to the end of the sliced string. 
reversed = recursive_string("hello")
print (reversed)

 

# 2. Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index.

List=[1,2,3,4]
def product(self, nums: List[int]) -> List[int]:
    left = [1]*len(nums) # [1,1,1,1]
    # keeping it 1 when there is nothing to the left of index 0
    # product from left to right
    for i in range(1,len(nums)):
        left[i] = left[i-1]* nums[i-1]
        # 
        # ex) if we are at index 3, to the left is i-1 = index 3 * 
    # porduct from right to left
    right = [1]*len(nums) #[1,1,1,1]
    for i in range(len(nums)-2,-1,-1): # ex) len(nums-2) = index 2 
        right[i] = right[i+1]*nums[i+1]

    result = [1]*len(nums)
    for i in range(len(nums)):
        result[i] = left[i] * right[i]
        
    return result










# For example, an input of [1, 2, 3, 4] would return [24, 12, 8, 6] by performing [2x3x4, 1x3x4, 1x2x4, 1x2x3].

# You cannot use division in your answer! Meaning you can't simply multiply all the numbers and then divide by each element for each index!

