L = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# Note: ('d') is not a tuple. It should be ('d',)
filtered = [t for t in L if t]
print("Filtered list:", filtered)
