"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?   Expected Output is 4 while the Actual Output is a list index out of range error.
# - What error message (if any) is there?   IndexError: list index out of range.
# - What line number is causing the error?   File "exercise-1.py", line 23, in find_largest_diff.
# - What can you deduce about the cause of the error?   the list index cannot be accessed properly.





# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
"""Line 23 attempts to access the next index in the list but reaches outside of the list.
I resolved the bug by lowering the number of loops that occur in the for loop so that the loop would end before
receiving IndexError: list index out of range."""

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums) - 1): # <-- fix by adding range(len(list_of_nums) - 1)
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)