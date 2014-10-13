string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""

# iterate through the string
# set each element in the string to a dictionary key, with the value "1"
# unless it is already in the dictionary, in which case we need to add 1 to the value

def count_unique(string1):
	x = 0
	new_dict = {}
	for i in range(len(string1)):
		key = string1[i]
		if key not in new_dict:
			new_dict[key] = 1
		else:
			new_dict[key] += 1
	print '\n', "Frequency of letters in string: ", new_dict, '\n'
	print "*********************" , '\n'

count_unique(string1)

# open and read the file into a string
# and then proceed as above
# in commented out lines below, I'm also practicing making that twain.text file into a list of words.


def count_uniquetwain(filename):
	f = open("twain.txt")
	string1 = f.read().strip()
	# list1 = string1.split()
	x = 0
	new_dict = {}
	for i in range(len(string1)):
		key = string1[i]
		if key not in new_dict:
			new_dict[key] = 1
		else:
			new_dict[key] += 1
	print "Frequency of Twain string items: ", new_dict, '\n'
	print "*********************", '\n'
	# print list1

count_uniquetwain("twain.txt")

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""

# Go through list 1, and compare the first item in list 1 to each item in list 2.
# If we come across a member of list 1 that is in list 2, add it to the list to return.
# Repeat the above, only with the second item in list 1, and so forth.
# When done, print the resultant list.


def common_items(list1, list2):
	new_list = []
	for i in range(len(list1)):
	    for x in range(len(list2)):
	        if list1[i] == list2[x] and list1[i] not in new_list:
	        	# Have I violated the rules?
				new_list.append(list1[i])
	print "List style: ", new_list, '\n'
	print "*********************", '\n'

common_items(list1, list2)

def common_items_sets(list1, list2):
	pass
# Can I use sets?


"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""


def common_items2(list1, list2):
	new_dict = {}
	for i in range(len(list1)):
	    for x in range(len(list2)):
	        if list1[i] == list2[x] and list1[i] not in new_dict:
	        	# Have I violated the rules?
				new_dict[list1[i]] = list2[x]
	dict_list = new_dict.keys()
	print "Dictionary style: ", dict_list, '\n'
	print "*********************", '\n'

common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""

def sum_zero(list1):
	new_list = []
	for i in range(len(list1)):
	    for x in range(len(list1)):
	        if list1[i] + list1[x] == 0 and (list1[i], list1[x]) not in new_list:
	        	# Have I violated the rules?
				new_list.append((list1[i], list1[x]))
	print "Sum zero: ", new_list, '\n'
	print "*********************", '\n'

sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	new_list = []
	for word in words:
		if word not in new_list:
			new_list.append(word)
	print "Deduplicated list: ", new_list, '\n'
	print "*********************", '\n'

find_duplicates(words)

"""
Done! Given a list of words, print the words in ascending order of length
Done! Bonus: do it on a file instead of the list provided
Not done...yet:  Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	new_list = []
	for word in words:
		if (word, len(word)) not in new_list:
			new_list.append((word, len(word)))
	# sort by alphabet, then frequency
	sorted_list = sorted(sorted(new_list), key=lambda x: x[1])
	print "Word lengths: ", sorted_list, '\n'
	print "*********************", '\n'

word_length(words)

def word_length_with_file(filename):
	f = open(filename)
	string1 = f.read().strip()
	list1 = string1.split()
	new_list = []
	for word in list1:
		if (word, len(word)) not in new_list:
			new_list.append((word, len(word)))
	# sort by frequency
	sorted_list = sorted(new_list, key=lambda x: x[1])
	print "Word lengths: ", sorted_list, '\n'
	print "*********************", '\n'

word_length_with_file("Twain.txt")


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def pirate_translator():
	print "WTF!"

	pirate_dictionary = {'sir': 'matey', 'hotel': 'fleabag inn', 'student':
	'swabbie', 'boy': 'matey', 'madam': 'proud beauty', 'professor': 'foul blaggart', 'restaurant': 'galley',
	'your': 'yer', 'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'lawyer': 'foul blaggart', 'the': "th'",
	'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be', 'man': 'matey'}
	
	user_sentence = raw_input("Enter a sentence for translation into piratude!  ")
	word_list = user_sentence.split()
	for i in range(len(word_list)):
		if word_list[i] in pirate_dictionary:
			word_list[i] = pirate_dictionary[word_list[i]]
	print " ".join(word_list)

pirate_translator()

