class Solution(object):
    def findMaxAverage(self, nums, k):
        # Initialize window sum with first k elements
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        
        # Slide the window through the rest of the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            current_avg = window_sum / k
            max_avg = max(max_avg, current_avg)
            
        return max_avg