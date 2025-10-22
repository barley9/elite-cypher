class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        left, right = 0, 1
        current_sum = sum(nums[left:right])
        while right <= len(nums):
            print(
                (left, right),
                nums[left:right],
                sum(nums[left:right]),
                sum(nums[left:right]) * (right - left),
                sum(nums[left:right]) * (right - left) < k,
                f"=> +{right - left}" if (sum(nums[left:right]) * (right - left) < k) else '',
                total,
            )
            if current_sum * (right - left) < k:
                total += (right - left)
                right += 1
                if right > len(nums): continue
                current_sum += nums[right - 1]
            elif right - left > 1:
                current_sum -= nums[left]
                left += 1
            else:
                current_sum -= nums[left]
                left += 1
                right += 1
                current_sum += nums[right]
            
        return total