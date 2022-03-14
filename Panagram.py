import string

def isPanagram(str):
    alpha = string.ascii_lowercase

    for c in alpha:
        if c not in str:
            return False
    return True


x = isPanagram("The quick brown fox jumps over the lazy dog")
print(x)
