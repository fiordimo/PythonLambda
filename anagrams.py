# Import DOM


def build_dict(path):
    # Load in word file and sort each line.
    alpha = {}
    f = open(path, "r")
    for line in f.readlines():
        line = line.strip()
        key = sorted_line(line)

        # Add each line to a dictionary based on its sorted key.
        if key in alpha:
            v = alpha.get(key) + "," + line
            alpha[key] = v
        else:
            alpha[key] = line
    return alpha


def sorted_line(line):
    # Sort the chars in this line and return a string.
    chars = [c for c in line]
    chars.sort()
    return "".join(chars)


def anagram(alpha, line):
    # Return a list of anagrams from the dictionary.
    # ... Use a sorted string as the key.
    key = sorted_line(line)
    values = alpha.get(key, "NONE")
    return values.split(",")


# Load our dictionary and use it.
#alpha = build_dict(r"Dictionary/Dictionary.txt")
#userinput = "tania"
#results = anagram(alpha, userinput.upper())

#print("Anagrams for " + userinput)
#print(results)
