
# Given an integer array nums, return true if any value appears at least twice in the
# array, and return false if every element is distinct.

class Solution1:
  def containsDuplicate(self, nums) -> bool:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
          return True
    return False # if no duplicates are found, return false

class Solution2:
  def containsDuplicate(self, nums):
    unique_set = set()  # Use set to store unique elements
    for x in nums:
      if x in unique_set:
        return True
      unique_set.add(x)
    return False  # Return False if no duplicates found

# Best Solution

class Solution3:
  def containsDuplicate(self, nums) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
      if nums[i] == nums[i + 1]:
        return True
    return False # if no duplicates are found, return false

if __name__ == '__main__':

  sol1 = Solution1()
  sol2 = Solution2()
  sol3 = Solution3()

  nums1 = [1, 2, 3, 4]
  print(sol1.containsDuplicate(nums1)) # Expected output: False
  print(sol2.containsDuplicate(nums1))
  print(sol3.containsDuplicate(nums1))

  nums2 = [1, 2, 3, 1]
  print(sol1.containsDuplicate(nums2))# Expected output: True
  print(sol2.containsDuplicate(nums2))
  print(sol3.containsDuplicate(nums2))

  nums3 = []
  print(sol1.containsDuplicate(nums3)) # Expected output: False
  print(sol2.containsDuplicate(nums3))
  print(sol3.containsDuplicate(nums3))

  nums4 = [1, 1, 1, 1]
  print(sol1.containsDuplicate(nums4)) # Expected output: True
  print(sol2.containsDuplicate(nums4))
  print(sol3.containsDuplicate(nums4))
