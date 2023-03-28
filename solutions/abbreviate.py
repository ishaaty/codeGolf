def abbreviate(s):
    return s[0] + str(len(s[1:-1])) + s[-1] if len(s[1:-1]) != 0 else s[0] + s[-1] if len(s) != 1 else s[0]

print(abbreviate("hiThere"))
print(abbreviate("BCA-ATCS-Olympics"))
print(abbreviate("br"))
print(abbreviate("a"))