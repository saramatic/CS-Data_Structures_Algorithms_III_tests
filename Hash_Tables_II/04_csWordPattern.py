"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in s.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
a contains only lower-case English letters and spaces ' '.
a does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
[execution time limit] 4 seconds (py3)

[input] string pattern

[input] string a

[output] boolean


"""

def csWordPattern(pattern, a):
    # word key - letter value
    d1 = {}
    d2 = {}
    
    # split the string of words into a List
    words = a.split()
    
    # case where pattern and str are not equal returns False
    if len(words) != len(pattern):
        return False


    # iterate thru pattern and words
    for i in range(len(words)):
        # if word not seen in d1 and pattern not seen in d2
        if words[i] not in d1 and pattern[i] not in d2:
            # map word to letter in pattern
            d1[words[i]] = pattern[i]
            # not sure that this does anything
            # let's comment it out
            d2[pattern[i]] = pattern[i]
        
        # otherwise it is in both maps
        # check if word matches pattern    
        # NOTE is d2[pattern[i]==None] it will give you an error below
        elif d1.get(words[i]) != pattern[i]:
            # this is just to look-see
            # print(d1.get(words[i]), pattern[i])
            return False

    return True




pattern = "abba"
a = "lambda school school lambda"
print(csWordPattern(pattern, a))


pattern = "abba" 
a = "dog cat cat fish"
print(csWordPattern(pattern, a))

pattern = "aaaa"
a = "dog cat cat dog"
print(csWordPattern(pattern, a))
    
