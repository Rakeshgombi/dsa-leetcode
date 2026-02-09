class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        hash_set = set()
        for i in range(n):    
            print(f'hash_set - {i}: {hash_set}')
            if nums[i] in hash_set:
                return True
            hash_set.add(nums[i])
            if (len(hash_set) > k):
                hash_set.remove(nums[i - k])

        return False


nums = [1, 2, 3, 4, 2, 3]
k = 2
soln = Solution()
soln.containsNearbyDuplicate(nums, k)