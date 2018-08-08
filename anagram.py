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
                        wordOneletterOne = table[key][i][0:3]
                        wordTwoletterLast = table[key][i+1][len(table[key][i+1])-3:]
                        if wordOneletterOne == wordTwoletterLast:
                                first_last_switched_table[key] = [table[key][i], table[key][i+1]]
        return first_last_switched_table



#Checks to see if first letter occurs often

def recurring_first_letter(table):
    first_letter_recurring_table = {}
    amt = 1
    for key in table:
        for i in range(len(table[key])-1):
            wordOneletterOne = table[key][i][0]
            wordTwoletterOne = table[key][i+1][0]
            if wordOneletterOne == wordTwoletterOne:
                first_letter_recurring_table[key] = [table[key][i], table[key][i+1]]
                amt += 1
    return first_letter_recurring_table
    

def main():

	anagram_table = make_table(word_list)

	#uncomment this line to see the whole anagram table
	#print_hash(anagram_table)

	filtered_table = filter_table_by_difference(anagram_table, 1000)
	#uncomment this line to see the anagrams found via the variance method
	#print_hash(filtered_table)

	#uncomment this line to see the number of anagrams found
	#print(len(anagram_table), len(filtered_table))

	#testing for patterns
 	#uncomment either of the methods in this section to see the anagrams kevin found
    #testing to see if first three letters of an anagram match last three letters of another
	first_last_switched_table = first_last_switched(anagram_table)
	#print_hash(first_last_switched_table)
	#print(len(first_last_switched_table))

  	#testing to see which anagrams start with the same letter
	first_letter_recurring_table = recurring_first_letter(anagram_table)
	#print_hash(first_letter_recurring_table)
	#print(len(first_letter_recurring_table))

	#uncomment the methods in this section to see the anagrams andrea found
	
if __name__ == "__main__":
	main()
