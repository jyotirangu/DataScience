# Frozen set is just an immutable version of a Python set object

# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

fs1 | fs2

# what works and what does not
# works -> all read functions
# does't work -> write operations

# When to use
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
fs