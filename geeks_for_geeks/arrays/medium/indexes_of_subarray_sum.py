'''
Solve - https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&company%5B%5D=Facebook&category%5B%5D=Arrays&sortBy=

Indexes of Subarray Sum

Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray 
(a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based 
indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose 
sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input       : arr[] = [1, 2, 3, 7, 5], target = 12
Output      : [2, 4]
Explanation : The sum of elements from 2nd to 4th position is 12.

Input       : arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output      : [1, 5]
Explanation : The sum of elements from 1st to 5th position is 15.

Input       : arr[] = [5, 3, 4], target = 2
Output      : [-1]
Explanation : There is no subarray with sum 2.
'''
class Solution:
    '''
    Nested Loops

    Outter loop picks the starting element, and the inner loop calculates the cumulative sum of elements starting from this 
    element.

    For each starting element, the inner loop iterates through subsequent elements and adding each element to a cumulative sum.
    If at any point the sum equals the "target" sum, then return starting and ending indices; Otherwise return [-1]
    
    Time Complexity     - O(n^2)
    Space Complexity    - O(1)

    https://www.geeksforgeeks.org/dsa/find-subarray-with-given-sum/#naive-using-nested-loop-on2-time-and-o1-auxiliary-space
    '''
    def _subarraySum_nestedLoops(self, arr, target):
        arr_len = len(arr)
    
        # For each starting element
        for i in range(arr_len):
            cumulative_sum = 0
            
            # the inner loop iterates through subsequent elements and adding each element to a cumulative sum.
            for j in range(i, arr_len):
                cumulative_sum += arr[j]
                # If at any point the sum equals the "target" sum, then return starting and ending indices
                if cumulative_sum == target:
                    return [
                        (i+1), 
                        (j+1)
                    ]
    
        # If no subarray is found
        return [-1]
    

    '''
    Sliding Window

    Start with an empty window. We will add elements to the window while the current sum is less than the target. If the
    sum is greater than the target, then remove the elements from the start of the current window. If the current sum 
    matches the target then return the result.
    
    Time Complexity     - O(n)
    Space Complexity    - O(1)

    https://www.geeksforgeeks.org/dsa/find-subarray-with-given-sum/#expected-approach-using-sliding-window-ontime-and-o1-auxiliary-space
    '''
    def _subarrySum_slidingWindow(self, arr, target):
        left, right, cumulative_sum = 0, 0, 0
        
        for i in range(len(arr)):
            cumulative_sum += arr[i]

            if cumulative_sum >= target:
                right = i

                while cumulative_sum > target and left < right:
                    cumulative_sum -= arr[left]
                    left += 1

                if cumulative_sum == target:
                    return [
                        (left+1),
                        (right+1)
                    ]

        return [-1]
    

    '''
    Hashing and Prefix Sum

    The previous example with the sliding window has the caveat that the array will ONLY contain positive integers. To 
    handle ALL cases, we'll implement hashing and prefix sum.

    The idea is to store the sum of elements of every prefix of the array in the hashmap (every index stores the sum
    of elements to that index hashmap). So to check if there is a subarray with sum equal to target, check for every
    index "i", and sum to that current index as "cumulative_sum". If there is a prefix with a sum equal to 
    (cumulative_sum - target), then the subarry is found
    
    Time Complexity     - O(n)
    Space Complexity    - O(n)

    https://www.geeksforgeeks.org/dsa/find-subarray-with-given-sum/#-hashing-prefix-sum-ontime-and-on-space
    '''
    def _subarrySum_hashingAndPrefixSum(self, arr, target):
        sum_map = {}
        cumulative_sum = 0

        for i, num in enumerate(arr):
            cumulative_sum += num
            
            if cumulative_sum == target:
                return [
                    1, 
                    (i+1)
                ]
            if (cumulative_sum - target) in sum_map:
                start = sum_map[cumulative_sum - target] + 1
                return [
                    (start+1), 
                    (i+1)
                ]
            if cumulative_sum not in sum_map:
                sum_map[cumulative_sum] = i
                
        return [-1]
    

    def subarraySum(self, arr, target):
        # return self._subarraySum_nestedLoops(arr, target)
        # return self._subarrySum_slidingWindow(arr, target)
        return self._subarrySum_hashingAndPrefixSum(arr, target)


####################################################################################
# Execute command - python ./geeks_for_geeks/arrays/easy/move_all_zeros_to_end.py
####################################################################################
def verifyResults(solution : Solution, arr: list, target: int, expected_output: list):
    output = solution.subarraySum(arr, target)
    assert expected_output == output

if __name__ == "__main__":
    solution = Solution()

    # Example 1 Test case
    verifyResults(
        solution,
        [1, 2, 3, 7, 5],
        12,
        [2, 4])

    # Example 2 Test case
    verifyResults(
        solution,
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        15,
        [1, 5])

    # Example 3 Test case
    verifyResults(
        solution,
        [5, 3, 4],
        2,
        [-1])
