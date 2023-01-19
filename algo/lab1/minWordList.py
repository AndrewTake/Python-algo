# Run the tests
# python3 -m unittest -v tests.py

def our_shared_values(left, right):
    dict1 = {}
    dict2 = {}
    output = []
    # get(key,0)
    # this sets key to 0 if the key does not exist
    # the 0 is incremented and acts as a counter
    for word in left:
        dict1[word] = dict1.get(word, 0) + 1

    for word in right:
        dict2[word] = dict2.get(word, 0) + 1

    for word in dict1.keys():
        # for holds the dictionary
        if word in dict2.keys():
            # if targets a value in the dictionary
            # minimum is a function that we can use to compare and find the smallest amount of overlapping values
            minimum_amount = min(dict1.get(word), dict2.get(word))
            for i in range(minimum_amount):
                # this takes the amount of minimum amounts. If range of minimum amounts is 1. the word is added once to the list.
                output.append(word)

    return output
