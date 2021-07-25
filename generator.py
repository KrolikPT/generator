#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# ------------------------------------------------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------------------------------------------------
import random
import sys
import os

# ------------------------------------------------------------------------------------------------------------------
# LETTERS
# ------------------------------------------------------------------------------------------------------------------
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = "abcdefghijklmnopqrstuvwxyz"
all_letters = big_letters + small_letters

# ------------------------------------------------------------------------------------------------------------------
# NUMBERS
# ------------------------------------------------------------------------------------------------------------------
numbers = "0123456789"

# ------------------------------------------------------------------------------------------------------------------
# NUMBERS AND LETTERS
# ------------------------------------------------------------------------------------------------------------------
numbers_big_letters = numbers + big_letters
numbers_small_letters = numbers + small_letters
numbers_all_letters = numbers + all_letters

# ------------------------------------------------------------------------------------------------------------------
# SYMBOLS
# ------------------------------------------------------------------------------------------------------------------
symbols = "|!#$%&/()=?»*`ª^;:_@£§€{[]},.-º~+´'«"
symbols_big_letters = symbols + big_letters
symbols_small_letters = symbols + small_letters
symbols_all_letters = symbols + all_letters
symbols_numbers = symbols + numbers

# ------------------------------------------------------------------------------------------------------------------
# ALL
# ------------------------------------------------------------------------------------------------------------------
all = big_letters + small_letters + numbers + symbols

# ------------------------------------------------------------------------------------------------------------------
# OPTIONS
# ------------------------------------------------------------------------------------------------------------------
options = {
    "1" : big_letters,
    "2" : small_letters,
    "3" : all_letters,
    "4" : numbers,
    "5" : numbers_big_letters,
    "6" : numbers_small_letters,
    "7" : numbers_all_letters,
    "8" : symbols,
    "9" : symbols_big_letters,
    "10" : symbols_small_letters,
    "11" : symbols_all_letters,
    "12" : symbols_numbers,
    "13" : all
}

# ------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------
def menu():

    print("####################################################################################")
    print("#################################### GENERATOR #####################################")
    print("####################################################################################")
    print("# 1 - Big Letters")			    
    print("# 2 - Small Letters")			    
    print("# 3 - All Letters")			    
    print("# 4 - Numbers")				    
    print("# 5 - Numbers & Big Letters")		    
    print("# 6 - Numbers & Small Letters")	            
    print("# 7 - Numbers & All Letters")
    print("# 8 - Symbols")
    print("# 9 - Symbols & Big Letters")
    print("# 10 - Symbols & Small Letters")
    print("# 11 - Symbols & All Letters")
    print("# 12 - Symbols & Numbers")
    print("# 13 - ALL")
    print("####################################################################################")
    print("# USO: python generator.py [Option] [Length] [Results] [File.txt]                  #")
    print("####################################################################################")


def generator(list, length, results, filename):

    word = ""
    c = 0
    wordlist = []

    while c < int(results):
        while len(word) < int(length):
            n_rand = random.randint(0, len(list) - 1)
            word += list[n_rand]  

        wordlist.append(word)
        word = ""
        c += 1

    with open(filename, "a+") as f:
        for item in wordlist:
            f.writelines("%s\n" % (item))

    print("A list with %s results was generated!" % len(wordlist))

# ------------------------------------------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------------------------------------------
if len(sys.argv) == 5:
    # Check Option
    if sys.argv[1] in options.keys():
        try:
            generator(options[sys.argv[1]], sys.argv[2], sys.argv[3], sys.argv[4])
        except:
            print("There was an error creating the list!")
            print("HELP: python generator.py")
            sys.exit(0)
    else:
        menu()   
else:
    menu()





