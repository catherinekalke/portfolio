import string

NUMBER_OF_ATTEMPTS = 2
ENTER_ANSWER = 'Hit %s for your answer\n'
TRY_AGAIN = 'Incorrect!!! Try again.'
NO_MORE_ATTEMPTS = 'Incorrect!!! You ran out of your attempts'

def question(message, options, correct, attempts=NUMBER_OF_ATTEMPTS):
    '''
    message - string 
    options - list
    correct - int (Index of list which holds the correct answer)
    attempts - int
    '''
    optionLetters = string.ascii_lowercase[:len(options)]
    print message
    print ' '.join('%s: %s' % (letter, answer) for letter, answer in zip(optionLetters, options))
    while attempts > 0:
        #response = input(ENTER_ANSWER % ', '.join(optionLetters)) # For python 3
        response = raw_input(ENTER_ANSWER % ', '.join(optionLetters)) # For python 2
        if response == optionLetters[correct]:
            return True
        else:
            attempts -= 1
            print TRY_AGAIN

    print NO_MORE_ATTEMPTS
    return False


print("Mathematics Quiz")

# question1 and question2 will be 'True' or 'False' 
question1 = question('Who is president of USA?', ['myself', 'His Dad', 'His Mom', 'Barack Obama'], 3)
question2 = question('Who invented Facebook?', ['Me', 'His Dad', 'Mark Zuckerberg', 'Aliens', 'Someone else'], 2)

animals_questions = 'Animals Questions'
capitals_questions = 'Capitals Questions'
math_questions = 'Math Questions'

questions = [animals_questions, capitals_questions, math_questions]

quiz = {animals_questions: [("All lionesses in a pride", True),
                        ("Another animals question", False),
                        ("Last animals question", False)],

        capitals_questions: [("Cairo is the capital city of Egypt", True),
                         ("Another capitals question", True),
                         ("Last capitals question", False)],

        math_questions: [("20 is log 100 for base 1o", False),
                     ("Another math question", True),
                     ("Last math question", False)]
}

result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(raw_input)
                'Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(animals_questions,
                                                                                          capitals_questions,
                                                                                          math_questions)))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print "Invalid value, please try again\n"
            else:
                return quiz_number


def get_answer(question, correct_answer):
    while True:
        try:
            print "Q: {}".format(question)
            answer = int(raw_input("1 for True\n0 for False\nYour answer: "))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if answer is not 0 and answer is not 1:
                print "Invalid value, please try again\n"
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print "\nYou chose the {}\n".format(quiz_name)
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print "Your answer is: {}\n".format(str(get_answer(q[0], q[1])))

import sys
import random

class Question(object):
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def ask(self):
        print self.question + "?"
        for n, option in enumerate(self.options):
            print "%d) %s" % (n + 1, option)

        response = int(sys.stdin.readline().strip())   # answers are integers
        if response == self.answer:
            print "CORRECT"
        else:
            print "wrong"

questions = [
    Question("How many legs on a horse", 4, ["one", "two", "three", "four", "five"]),
    Question("How many wheels on a bicycle", 2, ["one", "two", "three", "twenty-six"]),

    # more verbose formatting
    Question(question="What colour is a swan in Australia",
             answer=1,
             options=["black", "white", "pink"]),    # the last one can have a comma, too
    ]

random.shuffle(questions)    # randomizes the order of the questions

for question in questions:
    question.ask()

    # read the mutliple choice quiz data file
# reorganize into a list of tuples, each tuple has this order
# (question, answer1, answer2, answer3, answer4, answer_code)
 
# read the appended text file as a list of lines
fin = open("Quiz.dat", "r")
lineList = fin.readlines()
fin.close()
 
quiz_list = []
for k, line in enumerate(lineList):
    tuple_complete = False
    line1 = line.strip()
    # build a tuple for each question
    if k % 6 == 0:
        answer_code = line1
        if answer_code == 'end':
            break
    if k % 6 == 1:
        question = line1
    if k % 6 == 2:
        answer1 = line1
    if k % 6 == 3:
        answer2 = line1
    if k % 6 == 4:
        answer3 = line1
    if k % 6 == 5:
        answer4 = line1
        tuple_complete = True
    if tuple_complete:
        tuple1 = (question, answer1, answer2, answer3, answer4, answer_code)
        print tuple1  # test
        quiz_list.append(tuple1)
 
print "-"*70
#print quiz_list  # for testing
print "-"*70
 
# shuffle the list and display the first 10 question tuples
import random
random.shuffle(quiz_list)
for k, quest in enumerate(quiz_list):
    if k < 10:
        print quest
guessed = ""
while count >= 0:
    guess = input ("Please make a guess: ")   
    # ... check guess, continue if not a letter
    guessed += guess

    if guess in randWord:
        # ... print 'correct', else 'not correct', decrease count

    newBlanks = " ".join(c if c in guessed else "_" for c in randWord)
    print("Word: ",newBlanks) 

    def rev_mad_lib(string, number_of_questions, answers):
    i=0
    n=1
    print "The current paragraph reads as such: " + string
    while i < len(number_of_questions):  
        print "What is the answer for question #", n
        current_answer=raw_input("My answer is: ")
        answer=answers[i]
        y=1
        while current_answer!=answers[i]:
            if y < tries:
               current_answer=raw_input("Try again. Enter the correct answer: ") 
               y=y+1
            elif y == tries:
               print "The correct answer is" + answers[i]
#            y=y+1
            return answer  
        n=n+1
        i=i+1     

print rev_mad_lib(string, number_of_questions, answers)     
    


#      n = 1
#      current_question = user_input which is the input for the current blank
#      while user_input != answer_list and n < tries: WHILE LOOP #2
#              answer = user_input
#      n+=1
#      if tries == 3:
#             print the string with the blank filled in
#i+=1
#print "No more tries"
