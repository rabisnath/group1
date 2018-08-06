#import other scripts

#opening the word bank
word_list = open("eng_dict.txt", "r")

def alphabetize(string):
	arr = []
	for char in string:
		arr.append(char)
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

anagram_table = make_table(word_list)

def print_hash(table):
	for key in table:
		print(str(key) + " : " + str(table[key]))

#sort the hash table

#filter for surprising result




def test():
	#for line in word_list:
	#	print(line)
	#print(alphabetize("alphabetize"))
	print_hash(anagram_table)
	
	

test()