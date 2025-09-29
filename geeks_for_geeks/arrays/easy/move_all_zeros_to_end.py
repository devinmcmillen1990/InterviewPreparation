'''
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end 
while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you 
should not use extra space for another array.

Examples:

Input       : arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output      : [1, 2, 4, 3, 5, 0, 0, 0]
Explanation : There are three 0s that are moved to the end.

Input       : arr[] = [10, 20, 30]
Output      : [10, 20, 30]
Explanation : No change in array as there are no 0s.

Input       : arr[] = [0, 0]
Output      : [0, 0]
Explanation : No change in array as there are all 0s.
'''
class Solution:
    def pushZerosToEnd(self, arr):
        #self.pushZerosToEnd_twoTraversals(arr)
        self.pushZerosToEnd_oneTraversal(arr)


    '''
    Two Traversals

    First Traversal
    1. Traverse the array & maintain the count of non-zero elements.
        a. This keeps track of where the next non-zero element should be placed in the array
    2. If the element is non-zero, place it at arr[count] and increment by 1

    *  After traversing all the elements, all non-zero elements will be shifted to the front while 
    maintaining their original order.

    Second Traversal
    1. After the First Traversal, all non-zero elements will be at the start of the array and count will store the index 
    where the first 0 should be stored.
    2. Iterate from count to the end and fill all indices with 0

    Time Complexity     - O(n)
    Space Complexity    - O(1)

    https://www.geeksforgeeks.org/dsa/move-zeroes-end-array/#better-approach-two-traversals-on-time-and-o1-space
    '''
    def pushZerosToEnd_twoTraversals(self, arr):
        arr_len = len(arr)
        count = 0

        # First Traversal
        for i in range(arr_len):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        # Second Traversal
        while count < arr_len:
            arr[count] = 0
            count += 1


    '''
    One Traversal

    This is similar to the Two Traversal approach where we have a count to track where the next non-zero element should be placed.
    However, on encountering a non-zero element, instead of directly placing the non-zero element at arr[count], we will swap
    the non-zero element with arr[count].
        * This will ensure that if there is any zero present at arr[count], it is pushed towards the end of array and not overwritten.

    Time Complexity     - O(n)
    Space Complexity    - O(1)
    
    https://www.geeksforgeeks.org/dsa/move-zeroes-end-array/#expected-approach-one-traversal-on-time-and-o1-space
    '''
    def pushZerosToEnd_oneTraversal(self, arr):
        count = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
