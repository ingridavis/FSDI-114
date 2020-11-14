# Create a function that checks whether two words are anagrams of each other.

# Two words are anagrams of each other if they are of the same length (number of letters) and use all of the same letters.

# For example: star and rats are anagrams of each other because they are of the same length and use all the same letters, the same number of times.

# Another example is cars and scar. Note again that they not only use the same letters but they use these letters the same amount of times.

# Your function must take two strings and return "True" if they are anagrams of each other; False otherwise.

print(" --- Directions: Enter two words that are anagrams of each other. --- ")

question1 = input("Enter first word: ")
question2 = input("Enter second word: ")
question1_lower = question1.lower()
question2_lower = question2.lower()
print("You entered the following words: {} and {}".format(question1_lower, question2_lower))
print(" --- Checking to see if your words meet the anagram critera... --")
def user_input(question1_lower, question2_lower):
    if len(question1_lower) == len(question2_lower):
        print(" Good: words are the same length.")
    else:
        print(" Please enter words that are the same length.")

user_input(question1, question2)

# sort each word alphabetically, then compare
question1_sorted = sorted(question1_lower)
print(question1_sorted)
question2_sorted = sorted(question2_lower)
print(question2_sorted)

def compare_inputs():
    result = question1_sorted == question2_sorted
    print("Your anagram is :", result)

compare_inputs()