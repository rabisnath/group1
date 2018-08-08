#filter for palindromes

new_array=[]
def palindrome(table):
    for key in table:
        for word in table[key]:
            if word[::-1] == word:
                new_array.append[word]
    return new_array






