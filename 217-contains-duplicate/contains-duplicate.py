#understands sets
class Solution:
    def containsDuplicate(self, nums: list[int]):


        seen = set()

        for num in nums:

            if num in seen:

               return True
            seen.add(num)
        return False
        