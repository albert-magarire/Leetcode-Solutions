'''
THE PROBLEM:
    Given a String s, write a function to find the maximum number of vowels in a substring of size k
'''

'''
THOUGHT PROCESS:
    A general solution would be to create a new array to store the substrings
    Create a set with vowels
    Iterate through the first k values in the string
    Everytime you encounter a vowel, then increment counter by 1
    Then iterate again, but after moving the k values to the right by 1(including the next value and dropping the first value) 
    Check if the total of vowels and compare with the current max
    If the total is greater than max, then update max, else move on to the next iteration
    Store the substring with the maximum number of vowels
    
'''

'''
CHOSEN SOLUTION:
    To solve the problem, I have decided to use a sliding window technique
    Initialize a window of size k
    Count number of vowels in the window
    Store that as max, and slide the window across the string(add new character and drop the old character)
    Track the number of vowels
    Update the count and max
    
'''
class Solution:
    def substring_with_most_vowels(s, k):
        #create a set with all vowels for O(1) checking
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        
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

