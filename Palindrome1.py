#filter for palindromes


def palindrome(table):
    new_array=[]
    for key in table:
        for i in table[key]:
            if i[::-1] == table[key][i+1]:
                new_array.append[i]
    return new_array






