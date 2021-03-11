from random import randint
import sys, getopt


'''
   Input: String 
   Returns: None
   
   Takes a sentence and builds a new one where the words match the first letter and length, prints the new sentence  
'''
def scrabbler(sentence):
    word_array = sentence.split(" ")
    new_sentence = []
    for word in word_array:
        scrabble_word = word_finder(word.lower())
        new_sentence.append(scrabble_word)

    print(*new_sentence)


'''
    Input: String
    Output: String
    
    Takes a string input searches the included dictionary for a word that matches on the first letter and length
'''
def word_finder(word):
    return_word = word
    word_file = open("corncob_lowercase.txt", "r")
    possible_words = []

    for dic_word in word_file:
        if word[0] < dic_word[0]:
            break
        if word[0] == dic_word[0] and len(dic_word.rstrip('\n')) == len(word):
            possible_words.append(
                dic_word.rstrip('\n')
            )

    if len(possible_words) != 0:
        return_word = possible_words[randint(0, len(possible_words)-1)]

    word_file.close()
    return return_word


'''
    Flags are -s and -sentence
'''
if __name__ == '__main__':
    command = sys.argv[1:]

    try:
        opts, args = getopt.getopt(command, "s:", ["sentence="])
    except getopt.GetoptError:
        print('scrabble_words.py -s "Insert Sentence Here"')
        sys.exit(2)

    for opt, args in opts:
        if opt in ('-s', '-sentence'):
            scrabbler(args)
