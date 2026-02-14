from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Create a mapping of friend to their position in the order
        position_map = {friend: index for index, friend in enumerate(order)}
        
        # Sort the friends based on their position in the order
        sorted_friends = sorted(friends, key=lambda friend: position_map[friend])
        
        return sorted_friends
        