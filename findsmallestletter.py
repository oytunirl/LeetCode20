from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # get the first element for convenience
        first_element = letters[0]
        
        # sort the list
        letters.sort()

        # check the list 
        for letter in letters:
            if letter > target:
                return letter
            else:
                continue
        
        # if it doesnt return just return the first element
        return first_element