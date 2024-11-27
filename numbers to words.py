# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

# 3 -> 'three' -> 5
# 20 -> 'twenty' -> 6

numbers_to_strings = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    200: 'twohundred',
    300: 'threehundred',
    400: 'fourhundred',
    500: 'fivehundred',
    600: 'sixhundred',
    700: 'sevenhundred',
    800: 'eighthundred',
    900: 'ninehundred',
    1000: 'onethousand'
}

# 72 -> 70 2 -> 'seventy', 'two' -> 10

def find_total_letters(n):
    list_of_numbers = range(1, n + 1)
    sum_of_letters = 0
    for number in list_of_numbers:
        # 1. convert number to the word representation
        if number in numbers_to_strings:
            word = numbers_to_strings[number]
        else:
            num_digits = len(str(number))
            if num_digits == 2:
                # Number is between 21 and 99
                tens_digit = int(str(number)[0]) * 10
                ones_digit = int(str(number)[1])
                word = numbers_to_strings[tens_digit] + numbers_to_strings[ones_digit]
            elif num_digits == 3:
                # Number is between 101 and 999
                hundreds_digit = int(str(number)[0]) * 100
                potential_tens_word = int(str(number)[1:])
                if potential_tens_word in numbers_to_strings:
                    # The last 2 digits exist as a word (ex. 11, eleven)
                    word = numbers_to_strings[hundreds_digit] + 'and' + numbers_to_strings[potential_tens_word]
                else:
                    tens_digit = int(str(number)[1]) * 10
                    ones_digit = int(str(number)[2])
                    word = numbers_to_strings[hundreds_digit] + 'and' + numbers_to_strings[tens_digit] + numbers_to_strings[ones_digit]

        # 2. count up the total number of letters
        word_length = len(word)

        # 3. add value from 2 to sum_of_letters
        sum_of_letters = sum_of_letters + word_length
    return sum_of_letters


print find_total_letters(1000)

def some_function(one_parameter, another_parameter, a_third_parameter):
    print "The parameter 'one_parameter' is equal to:", one_parameter
    print "The parameter 'another_parameter' is equal to:", another_parameter
    print "The parameter 'a_third_parameter' is equal to:", a_third_parameter

print some_function(1,2,3)

#sentence = "A NOUN went on a walk. They can VERB really well."
#sentence1 = sentence.replace("NOUN","duck")
#sentence2 = sentence1.replace("VERB", "waddle")

#print sentence2
from random import randint

def random_verb():
    random_num = randint(0,1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

#test_string_3 = "This is a good NOUN to use when you VERB your food"
#sentence4 = test_string_3.replace("NOUN",random_noun())
#sentence5 = sentence4.replace("VERB",random_verb())
    
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
#print sentence5

def process_madlib(mad_lib):
        #test_string_1 = "This is a good NOUN to use when you VERB your food"
    #test_string_1 = "This is a good NOUN to use when you VERB your food"
    #test_string_1 = "This is a good NOUN to use when you VERB your food"
    #sentence1 = test_string_1.replace("NOUN",random_noun())
    sentence1 = mad_lib.replace("NOUN",random_noun())
    sentence2 = sentence1.replace("VERB",random_verb())
    return sentence2
    
#test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib("This is a good NOUN to use when you VERB your food")
print process_madlib("I'm going to VERB to the store and pick up a NOUN or two.")

#print process_madlib(test_string_2)

 
