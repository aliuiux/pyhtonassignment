s = "   Python is fun!   "

# Remove leading/trailing spaces
stripped_string = s.strip()

# Left justify with '*'
left_justified = stripped_string.ljust(20, '*')

# Right justify with '*'
right_justified = stripped_string.rjust(20, '*')

print("Stripped:", stripped_string)
print("Left Justified:", left_justified)
print("Right Justified:", right_justified)
