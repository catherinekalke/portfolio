parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN With Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced=[] 
    ml_string=ml_string.split()
    for word in ml_string:
        replacement=word_in_pos(word,parts_of_speech)
        if replacement!= None:
           word=word.replace(replacement,"Corgi")
           replaced.append(word)
        else:
           replaced.append(word)
    replaced=" ".join(replaced)  
    return replaced      
            
print play_game(test_string, parts_of_speech)

#Same as above but with user input for the word

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN With Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):    
    replaced=[] 
    ml_string=ml_string.split()
    for word in ml_string:
        replacement=word_in_pos(word,parts_of_speech)
        if replacement!= None:
           user_input=raw_input('-->')
# This will work if the raw input module is installed on Sublime Text2
           word=word.replace(replacement,user_input)
           replaced.append(word)
        else:
           replaced.append(word)
    replaced=" ".join(replaced)  
    return replaced      
            
print play_game(test_string, parts_of_speech)

