'''
THE PROBLEM:
    Given a String s, write a function to find the maximum number of vowels in a substring of size k
'''

'''
THOUGHT PROCESS:
    A general solution would be to create a new array to store the substrings
    Create a set with vowels
    Iterate through the first k values in the strinng
    Everytime you encounter a vowel, then increment countesr by 1
    Then iterate again, but after moving the k values to the right by 1(including the next value and dropping the first value) 
    Check if the total of vowels and compare with the current max
    If the total is greater than max, then update max, else move on to the next iteration
    Store the substring with the maximum number of vowels
    
'''

'''
CHOSEN SOLUTION:
    To solve the problem, I have decided to use a sliding window technique - This solution worked actually ✅
    Initialize a window of size k
    Count number of vowels in the window
    Store that as max, and slide the window across the string(add new character and drop the old character)
    Track the number of vowels
    Update the count and max
    
'''
class Solution:
    def substring_with_most_vowels(s, k):
        #create a set with all vowels for O(1) checkings
        vowel = {'a','e','i','o','u','A','E','I','O','U'}

        #we can do this in a better way by creating a function that checks if a character is a vowel
        # def is_vowel(char):
        #    return char in "AEIOUaeiou" --> this will return true or false
        
        '''
        loop through the first k values in the string s
        generate a value 1 every time we encounter a vowel while looping through the array
        find the sum of all the ones that have been generated
        '''
        current_vowel_count = sum(1 for i in range(k) if (s[i]) in vowel)
        max_vowel_count = current_vowel_count
        start_index = 0
    
        #Slide the window
        for i in range(k, len(s)):
            # Add the new character to the window
            if (s[i]) in vowel:
                current_vowel_count += 1
            # Remove the character that's sliding out of the window
            if (s[i - k]) in vowel:
                current_vowel_count -= 1
    
            # Update the maximum vowel count and starting index of the substring
            if current_vowel_count > max_vowel_count:
                max_vowel_count = current_vowel_count
                start_index = i - k + 1
    
        # Step 3: Return the substring with the most vowels
        return s[start_index:start_index + k]
'''
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
'''
