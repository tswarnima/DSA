class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Double hashing parameters to prevent collisions
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761
        
        # Shift elements to ensure all values are positive
        min_val = min(nums)
        arr = [x - min_val + 1 for x in nums]
        
        def has_unique(length: int) -> bool:
            p1 = pow(BASE1, length - 1, MOD1)
            p2 = pow(BASE2, length - 1, MOD2)
            
            h1 = h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
            seen_once = {(h1, h2)}
            seen_multiple = set()
            
            for i in range(length, n):
                # Remove leading element and add trailing element
                h1 = ((h1 - arr[i - length] * p1) * BASE1 + arr[i]) % MOD1
                h2 = ((h2 - arr[i - length] * p2) * BASE2 + arr[i]) % MOD2
                state = (h1, h2)
                
                if state in seen_multiple:
                    continue
                if state in seen_once:
                    seen_once.remove(state)
                    seen_multiple.add(state)
                else:
                    seen_once.add(state)
                    
            return len(seen_once) > 0

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
