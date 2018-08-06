#import other scripts

#opening the word bank
word_list = open("eng_dict.txt", "r")

#make hash table
#the keys will be alphabetized strings, the values will be lists of english words that match the key in content
anagram_table = {}

#fill in hash table
#def fill_table(dict_name):
	#for word in word_list:
		#alphabetize
		#make new key if not present
		#add to existing value if already in table

#filter the table for short anagrams
#def filter_table_forlength(min_len):
	#for entry in table, remove if key lenght < min_len

#sort the hash table

#filter for surprising result

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


def test():
	#for line in word_list:
	#	print(line)
	#print(alphabetize("alphabetize"))
	

test()