"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?   Expected Output is a Sorted list while the Actual Output is a list index out of range error.
# - What error message (if any) is there?   IndexError: list index out of range
# - What line number is causing the error?   File "exercise-3.py", line 26, in insertion_sort
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] # 2
        print("key", key)

        # sorted partition
        j = i-1 # 0
            # 2     # 5
        while key < arr[j] and j >= 0: 
            # 2         # 5
            arr[j+1] = arr[j]
            print("check", arr[j+1])
            j -= 1
            print("j", j)
        arr[j+1] = key
        print("change", arr[j+1])
        print(arr)
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    # print(answer)

