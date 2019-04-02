#!/usr/env python
"""

Practice Python exercices:

All exercices come from: https://www.practicepython.org/exercises/

"""
import datetime
import os
import random

from bs4 import BeautifulSoup
import requests

###############################################################################
#                                 EXERCISE 01                                 #
#-----------------------------------------------------------------------------#
# Create a program that asks the user to enter their name and their age.      #
# Print out a message addressed to them that tells them the year that they    #
# will turn 100 years old.                                                    #
#                                                                             #
# Extra 1: Add on to the previous program by asking the user for another      #
# number and printing out that many copies of the previous message.           #
#                                                                             #
# Extra 2: Print out that many copies of the previous message on separate     #
# lines.                                                                      #
###############################################################################

def _get_name_year():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    year = (100 - age) + datetime.datetime.now().year
    return name, year

def _get_msg_01(name, year):
    return "{} will turn 100 years old in {}".format(name, year)

def ex_01():
    name, year = _get_name_year()
    print(_get_msg_01(name, year))

def ex_01_extra_01():
    name, year = _get_name_year()
    n = int(input("Choose a number: "))
    print(n * _get_msg_01(name, year))

def ex_01_extra_02():
    name, year = _get_name_year()
    n = int(input("Choose a number: "))
    for i in range(n): print(_get_msg_01(name, year))

###############################################################################
#                                 EXERCISE 02                                 #
#-----------------------------------------------------------------------------#
# Ask the user for a number. Depending on whether the number is even or odd,  #
# print out an appropriate message to the user.                               #
#                                                                             #
# Extra 1: If the number is a multiple of 4, print out a different message.   #
#                                                                             #
# Extra 2: Ask the user for two numbers: one number to check (call it num)    #
# and one number to divide by (check). If check divides evenly into num, tell #
# that to the user. If not, print a different appropriate message.            #
###############################################################################

def _get_number():
    return int(input("Choose a number: "))

def _is_odd(number):
    return (number % 2) == 1

def _is_multiple_of_4(number):
    return (number % 4) == 0

def _get_msg_02(number, number_type):
    return "{} is an {} number".format(number, number_type)

def ex_02():
    number = _get_number()
    if _is_odd(number):
        number_type = 'odd'
    else:
        number_type = 'even'
    print(_get_msg_02(number, number_type))

def ex_02_extra_01():
    number = _get_number()
    if _is_odd(number):
        number_type = 'odd'
    else:
        if _is_multiple_of_4(number):
            print("{} is a multiple of 4.".format(number))
            return
        else:
            number_type = 'even'
    print(_get_msg_02(number, number_type))

def ex_02_extra_02():
    check = _get_number()
    num = _get_number()
    if check % num == 0:
        print("{} divides evenly into {}.".format(check, num))
    else:
        print("{} does not divide evenly into {}.".format(check, num))

###############################################################################
#                                 EXERCISE 03                                 #
#-----------------------------------------------------------------------------#
# Take a list, say for example this one:                                      #
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]                                  #
# and write a program that prints out all the elements of the list that are   #
# less than 5.                                                                #
#                                                                             #
# Extra 1: Instead of printing the elements one by one, make a new list that  #
# has all the elements less than 5 from this list in it and print out this    #
# new list.                                                                   #
#                                                                             #
# Extra 2: Write this in one line of Python.                                  #
#                                                                             #
# Extra 3: Ask the user for a number and return a list that contains only     #
# elements from the original list a that are smaller than that number given   #
# by the user.                                                                #
###############################################################################

ex_03_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def ex_03():
    b = []
    for elt in ex_03_list:
        if elt < 5: print(elt)

def ex_03_extra_01():
    b = []
    for elt in ex_03_list:
        if elt < 5: b.append(elt)
    print(b)

def ex_03_extra_02():
    print([elt for elt in ex_03_list if elt < 5])

def ex_03_extra_03():
    number = int(input("Choose a number: "))
    print([elt for elt in ex_03_list if elt < number])    
 
###############################################################################
#                                 EXERCISE 04                                 #
#-----------------------------------------------------------------------------#
# Create a program that asks the user for a number and then prints out a list #
# of all the divisors of that number.                                         #
###############################################################################

def ex_04():
    number = int(input("Choose a number: "))
    if number % 2 == 0:
        divisors = [1] + list(range(2, number+1, 2))
    else:
        divisors = [i for i in range(1, number+1) if (number % i == 0)]
    print(divisors)

###############################################################################
#                                 EXERCISE 05                                 #
#-----------------------------------------------------------------------------#
# Take two lists, say for example these two:                                  #
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]                                  #
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]                             #
# and write a program that returns a list that contains only the elements     #
# that are common between the lists (without duplicates). Make sure your      #
# program works on two lists of different sizes.                              #
#                                                                             #
# Extra 1: Randomly generate two lists to test this                           #
#                                                                             #
# Extra 2: Write this in one line of Python                                   #
###############################################################################

def ex_05():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(list(set(a + b)))

def ex_05_extra_01():
    a = list(random.randint(1,100) for i in range(10))
    b = list(random.randint(1,100) for i in range(8))
    print(a)
    print(b)
    print(list(set(a + b)))

def ex_05_extra_02():
    print(list(set(list(random.randint(1,100) for i in range(10)) + list(random.randint(1,100) for i in range(8)))))

###############################################################################
#                                 EXERCISE 06                                 #
#-----------------------------------------------------------------------------#
# Ask the user for a string and print out whether this string is a palindrome #
###############################################################################

def ex_06():
    word = input("Write a word: ")
    if word == ''.join(list(reversed(word))):
        print("{} is a palindrome".format(word))
    else:
        print("{} is not a palindrome".format(word))

###############################################################################
#                                 EXERCISE 07                                 #
#-----------------------------------------------------------------------------#
# Write one line of Python that takes this list a and makes a new list that   #
# has only the even elements of this list in it.                              #
###############################################################################

ex_07_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def ex_07():
    print([i for i in ex_07_list if i % 2 == 0])

###############################################################################
#                                 EXERCISE 08                                 #
#-----------------------------------------------------------------------------#
# Make a two-player Rock-Paper-Scissors game.                                 #
# Remember the rules:                                                         #
# - Rock beats scissors                                                       #
# - Scissors beats paper                                                      #
# - Paper beats rock                                                          #
###############################################################################

def ex_08():
    player = ''
    while player not in ['R', 'S', 'P']:
        player = input("Choose a token (rock R, scissors S, paper P): ").capitalize()
    ia = random.choice(['R', 'S', 'P'])
    if player == ia:
        print("It's a tie! Player1={}, IA={}".format(player, ia))
    else:
        if player == 'R':
            if ia == 'S':
                print("Player1 wins! Player1={}, IA={}".format(player, ia))
            else:
                print("IA wins! Player1={}, IA={}".format(player, ia))
        elif player == 'S':
            if ia == 'P':
                print("Player1 wins! Player1={}, IA={}".format(player, ia))
            else:
                print("IA wins! Player1={}, IA={}".format(player, ia))
        else:
            if ia == 'R':
                print("Player1 wins! Player1={}, IA={}".format(player, ia))
            else:
                print("IA wins! Player1={}, IA={}".format(player, ia))

###############################################################################
#                                 EXERCISE 09                                 #
#-----------------------------------------------------------------------------#
# Generate a random number between 1 and 9 (including 1 and 9).               #
# Ask the user to guess the number, then tell them whether they guessed too   #
# low, too high, or exactly right.                                            #
#                                                                             #
# Extra 01: keep the game going until the user types “exit”                   #
#                                                                             #
# Extra 02: keep track of how many guesses the user has taken, and when the   #
# game ends, print this out.                                                  #
###############################################################################

def ex_09():
    number = random.randint(1, 9)
    while True:
        print(number)
        guess = int(input("Choose a number between 1 and 9: "))
        i = number - guess
        if i == 0:
            print("You guessed right! Correct number is: {}.".format(guess))
            break
        elif i > 0:
            print("Too low! You guess was {}.".format(guess))
        elif i < 0:
            print("Too high! You guess was {}.".format(guess))

def ex_09_extra_01():
    number = random.randint(1, 9)
    while True:
        guess = input("Choose a number between 1 and 9 (extra 01): ")
        if guess.lower() == 'exit':
            break
        guess = int(guess)
        i = number - guess
        if i == 0:
            print("You guessed right! Correct number is: {}.".format(guess))
            break
        elif i > 0:
            print("Too low! You guess was {}.".format(guess))
        elif i < 0:
            print("Too high! You guess was {}.".format(guess))

def ex_09_extra_02():
    number = random.randint(1, 9)
    turns = 0
    while True:
        turns += 1
        guess = input("Choose a number between 1 and 9 (extra 02): ")
        if guess.lower() == 'exit':
            return
        guess = int(guess)
        i = number - guess
        if i == 0:
            print("You guessed right! Correct number is: {}.".format(guess))
            break
        elif i > 0:
            print("Too low! You guess was {}.".format(guess))
        elif i < 0:
            print("Too high! You guess was {}.".format(guess))
    print("It took you {} turns to complete the game.".format(turns))

###############################################################################
#                                 EXERCISE 10                                 #
#-----------------------------------------------------------------------------#
# Take two lists, say for example these two:                                  #
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]                                  #
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]                             #
# and write a program that returns a list that contains only the elements     #
# that are common between the lists (without duplicates). Make sure your      #
# program works on two lists of different sizes.                              #
#                                                                             #
# Extra 01: Write this in one line of Python                                  #
###############################################################################

ex_10_list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ex_10_list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def ex_10():
    new_list = []
    for i in ex_10_list_b:
        if i in ex_10_list_a:
            new_list.append(i)
    print(new_list)

def ex_10_extra_01():
    print([i for i in ex_10_list_b if i in ex_10_list_a])

###############################################################################
#                                 EXERCISE 11                                 #
#-----------------------------------------------------------------------------#
# Ask the user for a number and determine whether the number is prime or not. #
###############################################################################

def ex_11():
    number = int(input("Choose a number: "))
    if number % 2 == 0:
        print("{} is not a prime number".format(number))
    else:
        divisors = [i for i in range(1, number+1) if (number % i == 0)]
        if len(divisors) == 2 and number in divisors and 1 in divisors:
            print("{} is a prime number".format(number))
        else:
            print("{} is not a prime number".format(number))

###############################################################################
#                                 EXERCISE 12                                 #
#-----------------------------------------------------------------------------#
# Write a program that takes a list of numbers and makes a new list of only   #
# the first and last elements of the given list.                              #
###############################################################################

def ex_12():
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print([b[0], b[-1]])

###############################################################################
#                                 EXERCISE 13                                 #
#-----------------------------------------------------------------------------#
# Write a program that asks the user how many Fibonacci numbers to generate   #
# and then generates them.                                                    #
###############################################################################

def _fib(n):
    x, y = 0, 1
    for i in range(n + 1):
        yield y
        x, y = y, x+y

def ex_13():
    n = int(input("Choose a of Fibonacci sequence length: "))
    print(list(_fib(n)))


###############################################################################
#                                 EXERCISE 14                                 #
#-----------------------------------------------------------------------------#
# Write a program that takes a list and returns a new list that contains all  #
# the elements of the first list minus all the duplicates.                    #
###############################################################################

def ex_14():
    b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(list(set(b)))

###############################################################################
#                                 EXERCISE 15                                 #
#-----------------------------------------------------------------------------#
# Write a program that asks the user for a long string containing multiple    #
# words. Print back to the user the same string, except with the words in     #
# backwards order. For example, say I type the string:                        #
#       My name is Michele                                                    #
# Then I would see the returned string would be:                              #
#       Michele is name My                                                    #
###############################################################################

def ex_15():
    phrase = input("Write a phrase: ")
    print(' '.join(reversed(phrase.split())))

###############################################################################
#                                 EXERCISE 16                                 #
#-----------------------------------------------------------------------------#
# Write a password generator in Python. Strong passwords have a mix of        #
# lowercase letters, uppercase letters, numbers, and symbols. The passwords   #
# should be random, generating a new password every time the user asks for a  #
# new password.                                                               #
#                                                                             #
# Extra 01: Ask the user how strong they want their password to be. For weak  #
# passwords, pick a word or two from a lists.                                 #
###############################################################################

def ex_16():
    symbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@&/\?-_!$')
    random.shuffle(symbols)
    password = []
    for i in range(random.randint(6,15)):
        password.append(random.choice(symbols))
    print(''.join(password))

def ex_16_extra_01():
    strong_symbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@&/\?-_!$')
    random.shuffle(strong_symbols)
    weak_symbols = 'Alpha Beta Gamma Delta'.split()
    mode = input("Do you want a weak or strong password (W, S)? ").capitalize()
    if mode == 'W':
        print(random.choice(weak_symbols))
    else:
        password = []
        for i in range(random.randint(6,15)):
            password.append(random.choice(strong_symbols))
        print(''.join(password))

###############################################################################
#                                 EXERCISE 17                                 #
#-----------------------------------------------------------------------------#
# Use the BeautifulSoup and requests Python packages to print out a list of   #
# all the article titles on the New York Times homepage.                      #
###############################################################################

def ex_17():
    pass

###############################################################################
#                                 EXERCISE 18                                 #
#-----------------------------------------------------------------------------#
# Create a program that will play the “cows and bulls” game with the user.    #
# The game works like this:                                                   #
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. #
# For every digit that the user guessed correctly in the correct place, they  #
# have a “cow”.                                                               #
# For every digit the user guessed correctly in the wrong place is a “bull”.  #
# Every time the user makes a guess, tell them how many “cows” and “bulls”    #
# they have.                                                                  #
# Once the user guesses the correct number, the game is over.                 #
# Keep track of the number of guesses the user makes throughout the game and  #
# tell the user at the end.                                                   #
###############################################################################

def _compare_digits(guess, number):
    correct, misplaced = 0, 0
    for i in range(len(guess)):
        count = number.count(guess[i])
        if count == 0:
            pass
        else:
            if guess[i] == number[i]:
                correct += 1
            else:
                for j in range(len(guess)):
                    if i != j:
                        if guess[j] == number[j]:
                            pass
                        elif guess[i] == number[j]:
                            misplaced += 1
    return correct, misplaced

def ex_18():
    num = str(random.randint(1000, 9999))
    num = '3233'
    score = {'cow': 0, 'bull': 0}
    turns = 0
    print(num)
    while score['cow'] != len(str(num)):
        turns += 1
        print("cow={}, bull={}".format(score['cow'], score['bull']))
        player = input("Guess the 4-digit number: ")
        score['cow'], score['bull'] = _compare_digits(player, num)
    print("You found the correct number {} in {} turns".format(num, turns))

###############################################################################
#                                 EXERCISE 19                                 #
#-----------------------------------------------------------------------------#
# Using the requests and BeautifulSoup Python libraries, print to the screen  #
# the full text of the article on this website:                               #
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# The article is long, so it is split up between 4 pages. Your task is to     #
# print out the text to the screen so that you can read the full article      #
# without having to click any buttons.                                        #
###############################################################################

def ex_19():
    r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
    obj = BeautifulSoup(r.text, "html.parser")
    all_p = [p for p in obj.find_all('p') if p.attrs['data-reactid'] is not None]
    for p in all_p:
        print(p.text)

###############################################################################
#                                 EXERCISE 20                                 #
#-----------------------------------------------------------------------------#
# Write a function that takes an ordered list of numbers and another number.  #
# The function decides whether or not the given number is inside the list and #
# returns (then prints) an appropriate boolean.                               #
#                                                                             #
# Extra 01: Use binary search.                                                #
###############################################################################

def ex_20():
    if 100 in [1, 2, 5, 6, 10, 22, 39, 40]:
        print("Number is in list")
    else:
        print("Number is not in list")

def _binary_search(number, alist):
    alist.sort()
    first, last = 0, len(alist)-1
    found = False
    while not found and first <= last:
        middle = (first + last) // 2
        if number == alist[middle]:
            found = True
        elif number > alist[middle]:
            first = middle + 1
        elif number < alist[middle]:
            last = middle - 1
    return middle

def ex_20_extra_01():
    alist = [1, 2, 5, 6, 10, 22, 39, 40]
    number = 22
    if _binary_search(number, alist):
        print(True)
    else:
        print(False)

###############################################################################
#                                 EXERCISE 21                                 #
#-----------------------------------------------------------------------------#
# Take the code from exercise 17 and instead of printing the results to a     #
# screen, write the results to a txt file.                                    #
#                                                                             #
# Extra 01: Ask the user to specify the name of the output file that will be  #
# saved.                                                                      #
###############################################################################

def ex_21():
    pass

###############################################################################
#                                 EXERCISE 22                                 #
#-----------------------------------------------------------------------------#
# Given a .txt file that has a list of a bunch of names, count how many of    #
# each name there are in the file, and print out the results to the screen.   #
# Use this file: http://www.practicepython.org/assets/nameslist.txt           #
#                                                                             #
# Extra 01: Instead of using the .txt file from above, use this one:          #
#   http://www.practicepython.org/assets/Training_01.txt                      #
# and count how many of each “category” of each image there are.              #
###############################################################################

def _get_file_content_list(filename):
    content_list = []
    with open(filename, 'r') as f:
        for line in f:
            content_list.append(line.strip()) # line.strip() to strip EOL chars
    return content_list

def ex_22():
    name_list = _get_file_content_list('nameslist.txt')
    name_count_dict = {}
    for name in name_list:
        if name not in name_count_dict.keys():
            name_count_dict[name] = 1
        else:
            name_count_dict[name] += 1
    print(name_count_dict)

def ex_22_extra_01():
    category_list = {}
    with open(filename, 'r') as f:
        for line in f:
            cat = line.split('/')[2]
            if cat not in category_list.keys():
                category_list[cat] = 1
            else:
                category_list[cat] += 1
    print(category_list)

###############################################################################
#                                 EXERCISE 23                                 #
#-----------------------------------------------------------------------------#
# Given two .txt files that have lists of numbers in them, find the numbers   #
# that are overlapping.                                                       #
# List of all prime numbers under 1000:                                       #
#   http://www.practicepython.org/assets/primenumbers.txt                     #
# List of happy numbers up to 1000:                                           #
#   http://www.practicepython.org/assets/happynumbers.txt                     #
###############################################################################

def ex_23():
    def _get_file_content_list(filename):
        content_list = []
        with open(filename, 'r') as f:
            for line in f:
                content_list.append(int(line))
        return content_list

    happy_numbers = _get_file_content_list('happynumbers.txt')
    prime_numbers = _get_file_content_list('primenumbers.txt')
    overlap = set(happy_numbers).intersection(set(prime_numbers))
    print(overlap)

###############################################################################
#                                 EXERCISE 24                                 #
#-----------------------------------------------------------------------------#
# Tic Tac Toe exercise series: part 1                                         #
#                                                                             #
# Ask the user what size game board and print it to the screen.               #
# The board size below is 3x3.                                                #
#    --- --- ---                                                              #
#   |   |   |   |                                                             #
#    --- --- ---                                                              #
#   |   |   |   |                                                             #
#    --- --- ---                                                              #
#   |   |   |   |                                                             #
#    --- --- ---                                                              #
# Board sizes vary depending on the game played (8x8 for chess, 19x19 for Go) #
###############################################################################

def ex_24():
    def _draw_row_seperation(size):
        return size * ' ---' + ' '
    def _draw_col_seperation(size):
        return size * '|   ' + '|'

    size = int(input("Choose a size: "))
    for i in range(size):
        print(_draw_row_seperation(size))
        print(_draw_col_seperation(size))
    print(_draw_row_seperation(size))

###############################################################################
#                                 EXERCISE 25                                 #
#-----------------------------------------------------------------------------#
# Opposite of exercise 09: the user will have in their head a number between  #
# 0 and 100. The program will guess a number, and the user will say whether   #
# it is too high, too low, or your number.                                    #
# At the end of this exchange, your program should print out how many guesses #
# it took to get your number.                                                 #
###############################################################################

def ex_25():
    def _binary_search(first, last, turns=0):
        while first <= last:
            middle = (first + last) // 2
            print('IA proposes: %d.' % middle)
            player = input('Is it smaller (-) or greater (+)? ')
            if player == '-':
                turns += 1
                return _binary_search(first, middle - 1, turns)
            elif player == '+':
                turns += 1
                return _binary_search(middle + 1, last, turns)
            elif player == '=':
                return turns
            else:
                break
    print("Choose a number between 0 and 100.")
    print("The IA is going to guess it.")
    print("Type - if the IA's guess is smaller than the guess.")
    print("Type + if the IA's guess is greater than the guess.")
    print("Type = if the IA's guess is your number.")
    counter = _binary_search(0, 100, turns=1)
    if counter:
        print("The computer guessed your number in %d turns." % counter)

###############################################################################
#                                 EXERCISE 26                                 #
#-----------------------------------------------------------------------------#
# Tic Tac Toe exercise series: part 2                                         #
#                                                                             #
###############################################################################

def ex_26():
    pass

###############################################################################
#                                 EXERCISE 27                                 #
#-----------------------------------------------------------------------------#
# Tic Tac Toe exercise series: part 3                                         #
#                                                                             #
# Check whether someone has WON a game of Tic Tac Toe.                        #
# A game of Tic Tac Toe is represented as a list of lists, like so:           #
# game = [[1, 2, 0],                                                          #
#         [2, 1, 0],                                                          #
#         [2, 1, 1]]                                                          #
# where a 0 means an empty square, a 1 means that player 1 put their token in #
# that space, and a 2 means that player 2 put their token in that space.      #
###############################################################################

def ex_27():
    pass

###############################################################################
#                                 EXERCISE 28                                 #
#-----------------------------------------------------------------------------#
# Implement a function that takes as input three variables, and returns the   #
# largest of the three.                                                       #
# Do this without using the Python max() function!                            #
###############################################################################

def ex_28():
    def get_max(x, y, z):
        max_val = x
        if y > y: max_val = y
        if z > y: max_val = z
        return z
    print(get_max(16,88,4))

###############################################################################
#                                 EXERCISE 29                                 #
#-----------------------------------------------------------------------------#
# Tic Tac Toe exercise series: part 4 (final)                                 #
#                                                                             #
# Implement the Tic Tac Toe game.                                             #
# You should keep track of who won - if there is a winner, show a             #
# congratulatory message on the screen.                                       #
# If there are no more moves left, don’t ask for the next player’s move!      #
# Ask the players if they want to play again and keep a running tally of who  #
# won more.                                                                   #
###############################################################################

def ex_29():
    pass

###############################################################################
#                                 EXERCISE 30                                 #
#-----------------------------------------------------------------------------#
# Hangman exercise series: part 1                                             #
# Write a function that picks a random word from a list of words from the     #
# SOWPODS dictionary.                                                         #
#   http://norvig.com/ngrams/sowpods.txt                                      #
###############################################################################

def ex_30():
    pass

###############################################################################
#                                 EXERCISE 31                                 #
#-----------------------------------------------------------------------------#
# Hangman exercise series: part 2                                             #
#                                                                             #
# Ask a player to guess a letter and displays letters in the clue word that   #
# were guessed correctly. Stop the game when all the letters have been        #
# guessed correctly.                                                          #
#                                                                             #
# Extra 01: keep track of the letters the player guessed and display a        #
# different message if the player tries to guess that letter again.           #
###############################################################################

def ex_31():
    pass

###############################################################################
#                                 EXERCISE 32                                 #
#-----------------------------------------------------------------------------#
# Hangman exercise series: part 3 (final)                                     #
#                                                                             #
# Implement the Hangman game.                                                 #
# The player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms)    #
# before they lose the game.                                                  #
# Only let the user guess 6 times, and tell the user how many guesses they    #
# have left.                                                                  #
# Keep track of the letters the user guessed. If the user guesses a letter    #
# they already guessed, don’t penalize them - let them guess again.           #
#                                                                             #
# Extra 01: When the player wins or loses, let them start a new game.         #
#                                                                             #
# Extra 02: Rather than telling the user "You have 4 incorrect guesses left", #
# display some picture art for the Hangman.                                   #
###############################################################################

def ex_32():
    pass

###############################################################################
#                                 EXERCISE 33                                 #
#-----------------------------------------------------------------------------#
# Create a dictionary (in a file) of names and birthdays.                     #
# Our program should ask the user to enter a name, and return the birthday    #
# of that person back to them.                                                #
# At the beginning of the program, the names of all the people whose birthday #
# is known should be printed.                                                 #
###############################################################################

def ex_33():
    pass

###############################################################################
#                                 EXERCISE 34                                 #
#-----------------------------------------------------------------------------#
# Same as exercise 33 but load the content of the dictionary from a JSON file #
#                                                                             #
# Extra 01: Ask the user for another scientist’s name and birthday to add to  #
# the dictionary, and update the JSON file.                                   #
###############################################################################

def ex_34():
    pass

###############################################################################
#                                 EXERCISE 35                                 #
#-----------------------------------------------------------------------------#
# Load the JSON file from exercise 34 and extract the months of all the       #
# birthdays, and count how many scientists have a birthday in each month.     #
# Your program should output something like:                                  #
# {                                                                           #
#     "May": 3,                                                               #
#     "November": 2,                                                          #
#     "December": 1                                                           #
# }                                                                           #
###############################################################################

def ex_35():
    pass

###############################################################################
#                                 EXERCISE 36                                 #
#-----------------------------------------------------------------------------#
# Use the bokeh Python library to plot a histogram of which months the        #
# scientists have birthdays in                                                #
#   https://www.practicepython.org/assets/scientist_birthdays.json            #
###############################################################################

def ex_36():
    pass

###############################################################################

if __name__ == '__main__':
    
    def jump(s):
        print(2 * os.linesep)
        print("----- EXERCISE {} ------".format(s))

    # jump("1")
    # ex_01()

    # jump("1-1")
    # ex_01_extra_01()

    # jump("1-2")
    # ex_01_extra_02()
    
    # jump("2")
    # ex_02()

    # jump("2-1")
    # ex_02_extra_01()

    # jump("2-2")
    # ex_02_extra_02()

    # jump("3") 
    # ex_03()

    # jump("3-1")
    # ex_03_extra_01()

    # jump("3-2")
    # ex_03_extra_02()

    # jump("3-3")
    # ex_03_extra_03()

    # jump("4")
    # ex_04()

    # jump("1") 
    # ex_05()

    # jump("5-1")
    # ex_05_extra_01()

    # jump("5-2")
    # ex_05_extra_02()
    
    # jump("6")
    # ex_06()
    
    # jump("7")
    # ex_07()
    
    # jump("8") 
    # ex_08()
    
    # jump("9") 
    # ex_09()

    # jump("9-1")
    # ex_09_extra_01()

    # jump("9-2")
    # ex_09_extra_02()

    # jump("10")
    # ex_10()

    # jump("10-1")
    # ex_10_extra_01()

    # jump("11")
    # ex_11()

    # jump("12")
    # ex_12()

    # jump("13")
    # ex_13()

    # jump("14")
    # ex_14()

    # jump("15")
    # ex_15()

    # jump("16")
    # ex_16()

    # jump("16-1")
    # ex_16_extra_01()    

    # jump("17")
    # ex_17()

    # jump("18")
    # ex_18()

    # jump("19")
    # ex_19()

    # jump("20")
    # ex_20()

    # jump("21")
    # ex_21()

    # jump("22")
    # ex_22()

    # jump("23")
    # ex_23()

    # jump("24")
    # ex_24()

    # jump("25")
    # ex_25()

    jump("26")
    ex_26()

