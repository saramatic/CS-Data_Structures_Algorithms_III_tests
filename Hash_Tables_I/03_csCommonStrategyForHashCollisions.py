"""

What is the most commomn strategy for dealing with hash collisions?

A. Recently, a few perfect hash functions were developed. Effectively, this means that most hash table implementations no longer have to deal with has collions

B. When the hash function returns the same index when given two different keys, the hash table only stores the value of whichever key was input last

C. Not storing the values directly at an index of the has table's array. Instead, they array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list.


Answer is:

Not storing the values directly at an index of the has table's array. Instead, they array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list.
"""