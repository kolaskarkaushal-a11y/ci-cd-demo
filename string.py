def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))
