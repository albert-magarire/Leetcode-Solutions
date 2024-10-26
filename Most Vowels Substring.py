class Solution:
    def substring_with_most_vowels(s, k):
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        
        '''
        loop through k values in the string s
        generate a value 1 every time we encounter a vowel while looping through the array
        find the sum of all the ones that have been generated
        '''
        current_vowel_count = sum(1 for i in range(k) if (s[i]) in vowel)
        max_vowel_count = current_vowel_count
        start_index = 0
    
        # Step 2: Slide the window
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
        
    s = "hellobeautifulworld"
    k = 5
    result = substring_with_most_vowels(s, k)
    print(result)  # Output could be "eauti" because it contains 4 vowels
