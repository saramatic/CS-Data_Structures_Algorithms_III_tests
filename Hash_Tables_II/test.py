# https://www.youtube.com/watch?v=n3V-wvCXDCs

def csGroupAnagrams(strs):

    dict = {}
    
    for word in strs:
        sortedword = "".join(sorted(word))
        print(sortedword)
    
        if sortedword not in dict:
            dict[sortedword] = [word]
            
        else:
            dict[sortedword].append(word)

 
    result = []
    
    for item in dict.values():
        result.append(item)
    
    return result


strs = ["apt","pat","ear","tap","are","arm"]

# Output:
# [["apt","pat","tap"],["ear","are"],["arm"]]

print(csGroupAnagrams(strs))