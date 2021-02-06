# https://www.youtube.com/watch?v=CKHBA1m13y8


def isomorphicStrings(a, b):

    if len(a) != len(b):
        return False

    a_map = {}
    b_map = {}

    for i in range(len(a)):
        a_ch = a[i]
        b_ch = b[i]

        if a_ch not in a_map:
            a_map[a_ch] = b_ch
        if b_ch not in b_map:
            b_map[b_ch] = a_ch

        if a_map[a_ch] != b_ch or b_map[b_ch] != a_ch:
            return False

    return True





a = "egg"
b = "add"
# Output: true
print(isomorphicStrings(a, b