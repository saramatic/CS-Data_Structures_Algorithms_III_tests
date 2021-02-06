"""
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true
Example 2:

Input:
a = "foo"
b = "bar"

Output:
false
Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true
Example 4:

Input:
a = "abc"
b = ""

Output:
false
[execution time limit] 4 seconds (py3)

[input] string a

[input] string b

[output] boolean


"""
def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False
    
    a_list = [0 for _ in range(128)]
    b_list = [0 for _ in range(128)]
    
    for i in range(0, len(a)):
        # this is a hashmap easy
        a_idx = ord(a[i]);
        b_idx = ord(b[i]);
        
        if a_list[a_idx] != b_list[b_idx]:
            return False
            
        a_list[a_idx] = i+1
        b_list[b_idx] = i+1
        print(a_list)
        print(b_list)
    return True

a = "egg"
b = "add"
# Output: true
print(csIsomorphicStrings(a, b))
    
