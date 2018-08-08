#import other scripts
import math
#opening the word bank
word_list = open("eng_dict.txt", "r")

def string_to_array(string):
	arr = []
	for char in string:
		arr.append(char)
	return arr

def alphabetize(string):
	arr = string_to_array(string)
	n = len(arr)
	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	output_str = ""
	for char in arr:
		output_str += char
	return output_str

#function to delete an entry from a dict
def remove(table, key):
	new_table = table
	del new_table[key]
	return new_table

#make hash table
#the keys will be alphabetized strings, the values will be lists of english words that match the key in content
def make_table(source):
	hash_table = {}
	for word in source:
		word = word[:-1]
		#eliminating short words
		if len(word) < 8:
			continue
		#alphabetizing the word
		alpha = alphabetize(word)
		#make new key if not present
		#add to existing value if already in table
		if alpha in hash_table:
			hash_table[alpha].append(word)
		else:
			hash_table[alpha] = [word]
	#removing entries that just have one word (non-anagrams)
	filtered_table = {}
	for key in hash_table:
		if len(hash_table[key]) > 1:
			filtered_table[key] = hash_table[key]
	return filtered_table

def print_hash(table):
	for key in sorted(table):
		print(str(key) + " : " + str(table[key]))



#using a "difference metric" to find anagram pairs more generally
def to_ords(array): #takes a list of characters and returns a list of ordinal numbers
	output = []
	for i in range(len(array)):
		output.append(ord(array[i]))
	return output

def string_difference(stringA, stringB): #takes in two strings and returns the sum of the squares of the differences of the 1st 2nd etc char in each string
	if len(stringA) != len(stringB):
		raise ValueError("Strings must be same length")
	arrayA, arrayB = string_to_array(stringA), string_to_array(stringB)
	arrayA, arrayB = to_ords(arrayA), to_ords(arrayB)
	#print(arrayA, arrayB)
	square_diffs = []
	for i in range(len(stringA)):
		square_diffs.append( (arrayA[i] - arrayB[i]) ** 2)
	return sum(square_diffs)

def filter_table_by_difference(table, min_diff_score):
	output_table = {}
	for key in table:
		#if len(table[key]) > 2: #keeping all anagram tuples with three or more words
		#	output_table[key] = table[key]
		if string_difference(table[key][0], table[key][1]) >= min_diff_score:
                        output_table[key] = table[key]
	return output_table
		




#Kevin's stuff

def first_last_switched(table):
        first_last_switched_table = {}
        for key in table:
                for i in range(len(table[key])-1):
                        wordOneletterOne = table[key][i][0]
                        wordTwoletterLast = table[key][i+1][len(table[key][i+1])-1]
                        if wordOneletterOne == wordTwoletterLast:
                                first_last_switched_table[key] = {table[key][i], table[key][i+1]}
        print(first_last_switched_table)



#Checks to see if first letter occurs often

def number_of_positions_switched(table):
    first_letter_recurring_table = {}
    for key in table:
        for i in range(len(table[key])-1):
            wordOneletterOne = table[key][i][0]
            wordTwoletterOne = table[key][i+1][0]
            if wordOneletterOne == wordTwoletterOne:
                first_letter_recurring_table[key] = {table[key][i], table[key][i+1]}
        if len(first_letter_recurring_table[key]) < 3:
            del first_letter_recurring_table[key]
    return first_letter_recurring_table
        


#Kevin's stuff (close)



def test():

	anagram_table = make_table(word_list)

	#for line in word_list:
	#	print(line)
	#print(alphabetize("alphabetize"))

	#print_hash(anagram_table)

	filtered_table = filter_table_by_difference(anagram_table, 1000)
	print_hash(filtered_table)

	print(len(anagram_table), len(filtered_table))

	#testing for patterns

	first_last_switched(anagram_table)


	#number_of_positions_switched(anagram_table)



	#test_pairs = [
	#["aaaaa", "aaaaa"],
	#["listen", "silent"],
	#["aaaaaa", "ZZZZZZ"],
	#]
	#for pair in test_pairs:
	#	print(string_difference(pair[0], pair[1]))
	
	

test()
