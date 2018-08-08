

#program to check if first and last letters are switched

def first_last_switched(table):
    first_last_switched_table = {}
    for key in table:
        for i in range(len(table[key])-1):
            wordOneletterOne == table[key][i][0]
            wordTwoletterLast == table[key][i+1][len(table[key][i+1])-1]
            if wordOneletterOne == wordTwoletterLast:
                first_last_switched_table[key] = {wordOneletterOne, wordTwoletterLast}
    return first_last_switched_table



#Checks to see if first letter occurs often

def number_of_positions_switched(table):
    first_letter_recurring_table = {}
    for key in table:
        for i in range(len(table[key])+1):
            wordOneletterOne == table[key][i][0]
            wordTwoletterOne == table[key][i+1][0]
            if wordOneletterOne == wordTwoletterOne:
                first_letter_recurring_table[key] = {wordOneletterOne, wordTwoletterOne}
        if len(first_letter_recurring_table[key]) < 3:
            del first_letter_recurring_table[key]
    return first_letter_recurring_table
                
                
                
                






