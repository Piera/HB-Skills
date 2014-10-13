# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    print "WTF?"
    new_list = []
    for i in number_list:
        if i % 2 != 0:
            new_list.append(i)
    print new_list
    return new_list

all_odd(number_list)


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    print "WTF?"
    new_list = []
    for i in number_list:
        if i % 2 == 0:
            new_list.append(i)
    print new_list
    return new_list

all_even(number_list)


# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    print "WTF?"
    new_list = []
    for i in word_list:
        if len(i) >= 4:
            new_list.append(i)
    print new_list
    return new_list

long_words(word_list)


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    print "WTF?"
    new_min = 0
    x = 0
    for i in number_list:
        if number_list[x] < number_list[x+1]:
            new_min = number_list[x]
    print new_min
    return new_min

smallest(number_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    print "WTF?"
    new_max = 0
    x = 0
    for i in number_list:
        if number_list[x] > number_list[x+1]:
            new_max = number_list[x]
    print new_max
    return new_max

largest(number_list)


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    print "WTF?"
    new_list =[]
    x = 0
    for i in number_list:
        x = float(i) / 2
        new_list.append(x)
    print new_list
    return new_list

halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    print "WTF?"
    new_list = []
    for i in word_list:
        new_list.append(len(i))
    print new_list
    return new_list

word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
def sum_numbers(number_list):
    print "WTF?"
    running_total = 0
    while len(number_list) > 0:
        x = number_list.pop()
        running_total= running_total + x
    print running_total
    return running_total

sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
def mult_numbers(number_list):
    print "WTF?"
    total_mult = 1
    while len(number_list) > 0:
        x = number_list.pop()
        total_mult = total_mult * x
    print total_mult
    return total_mult

mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    print "WTF?"
    total_string = "" 
    while len(word_list) > 0:
        x = word_list.pop()
        total_string = total_string + x
    print total_string
    return total_string

join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
def average(number_list):
    print "WTF?"
    d = len(number_list)
    running_total = 0
    while len(number_list) > 0:
        x = number_list.pop()
        running_total= running_total + x
    avg_of_list = running_total / d
    print avg_of_list
    return avg_of_list

average(number_list)