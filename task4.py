s = "the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index_fox = s.find("fox")

# Count occurrences of "the"
count_the = s.count("the")

# If "fox" is not found, the index should be -1 (find method returns -1 by default if not found)
index_fox = index_fox if index_fox != -1 else -1

print(f"index of 'fox' is {index_fox}")
print(f"'the' appears {count_the} times")
