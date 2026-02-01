from typing import List  

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()

        for word in words:
            morse_word = ''.join(morse_code[ord(char) - ord('a')] for char in word)
            transformations.add(morse_word)
        return len(transformations)
    
    
