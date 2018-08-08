def findPalindrome():
    list3 = []
    for line in open("eng_dict.txt","r"):
        list1 = line.strip()
        list2 = line.split()
        for word in list2:
            if word[::-1] == word:
                list3.append(word)
    print(list3)
findPalindrome()