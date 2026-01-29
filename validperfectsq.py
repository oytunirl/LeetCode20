class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        temp = num
        p = 2
        is_square = True

        while p * p <= temp:
            count = 0
            while temp % p == 0:
                temp //= p
                count += 1
            if count % 2 != 0:
                is_square = False
                break
            p += 1

        # leftover prime
        if temp > 1:
            is_square = False
        
        return is_square

            