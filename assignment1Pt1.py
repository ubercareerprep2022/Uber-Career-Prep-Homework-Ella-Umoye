from pydoc import ispackage

# Method 1
def isPermutation(string1, string2):
    """return a boolean value: true if string1 and string2 are anagrams/permutations
    of each other. Otherwise, return false"""

    # The set method in python checks is useful for this as it simply returns non-repeating
    # elements of the string. If they're anagrams, then their set version will be the same
    return set(string1) == set(string2)
print(isPermutation("damn", "dann"))

# Method 2
def isPermutation(string1, string2):
    """Return true if two strings are anagrams of each other using the dictionary method"""
    # Check if the lengths are the same, if they are not return false as they aren't
    # anagrams.
    # The logic is, if they are anagrams of each other, the dictionary should contain
    # all the lements of the strings, if not then I return False.
    dictionary = {}
    if len(string1) != len(string2):
        return False
    else:
        for string in string1:
            if string in dictionary:
                dictionary[string] += 1
            else:
                dictionary[string] = 0
        for string in string2:
            if string not in dictionary:
                return False
        return True

print(isPermutation("dame", "damn"))
    