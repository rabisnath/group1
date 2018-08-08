
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
    

        


#Kevin's stuff (close)

   #testing to see if first three letters of an anagram match last three letters of another
	first_last_switched_table = first_last_switched(anagram_table)
	print_hash(first_last_switched_table)
	print(len(first_last_switched_table))

        #testing to see which anagrams start with the same letter
	first_letter_recurring_table = recurring_first_letter(anagram_table)
	print_hash(first_letter_recurring_table)
	print(len(first_letter_recurring_table))

                
                
                






