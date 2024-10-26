TIME COMPLEXITY:
    ### 1. Initialization of the Vowel Set:
    - Creating a set of vowels is done in constant time, \( O(1) \), because it involves a fixed number of elements.
    
    ### 2. Calculating the Vowel Count for the First Window:
    - iteration through the first \( k \) characters of the string to count vowels takes \( O(k) \) time.
    
    ### 3. Sliding the Window Across the String:
    - iteration from \( k \) to \( \text{len}(s) - 1 \), which means it runs \( \text{len}(s) - k \) times. In the worst case, this is approximately \( O(n) \), where \( n \) is the length of the string.
      
    - Inside the Loop:
      - Checking if the character entering the window (`s[i]`) is a vowel: \( O(1) \) (set lookup time is constant).
      - Checking if the character leaving the window (`s[i - k]`) is a vowel: \( O(1) \).
      - Updating the maximum count and start index (if needed): \( O(1) \).
    
    Thus, the operations inside the loop are all \( O(1) \), and since the loop runs \( O(n) \) times, the time complexity for this part is \( O(n) \).
    
    ### 4. Returning the Result:
    - Extracting the substring with the most vowels takes \( O(k) \), but this is negligible compared to the \( O(n) \) time complexity of the main loop.
    
    ### Overall Time Complexity
    The total time complexity is:
    
    \[
    O(k) + O(n) = O(n)
    \]
    
    where \( n \) is the length of the input string. Hence, the solution has a linear time complexity, \( O(n) \), making it efficient for large input sizes.

SPACE COMPLEXITY:
    ### 1. Vowel Set:
    - The set of vowels contains a fixed number of elements (`{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}`), which does not depend on the size of the input string. Hence, the space complexity for the set is \( O(1) \).
    
    ### 2. Variables:
    - The solution uses a few variables (`current_vowel_count`, `max_vowel_count`, `start_index`, and loop indices), all of which require constant space, \( O(1) \).
    
    ### 3. Substring Extraction:
    - When returning the substring with the most vowels, a new string of length \( k \) is created. The space complexity for storing this substring is \( O(k) \).
    
    ### Overall Space Complexity:
    The total space complexity is:
    
    \[
    O(1) + O(k) = O(k)
    \]
    
    Thus, the solution has a space complexity of \( O(k) \), where \( k \) is the length of the substring being analyzed.
