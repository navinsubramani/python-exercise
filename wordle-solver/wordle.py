from ast import Pass
from tkinter import W
import WordList

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    print("Total Words: "+ str(len(valid_words)))
    return valid_words

def get_5letter_words():
    words_1 = []

    li_wordlist = WordList.a.split("\n")
    for w in li_wordlist:
        li_w = w.split(" ")
        words_1.extend(li_w)

    li_wordlist = WordList.b.split("\n")
    words_1.extend(li_wordlist)
    
    words_2 = []
    for w in words_1:
        if len(w) == 5:
            words_2.append(w)

    for w in load_words():
        if len(w) == 5:
            words_2.append(w)

    words = set(words_2)
    print("Total 5 Letter Words: "+str(len(words_2)))
    return words_2

def find_wordle(wordle_green,wordle_yellow,wordle_ignore):
    words = get_5letter_words()
    
    # filter the words that have the gray letters
    filtered_words = []    
    for w in words:
        i_present = False
        for i in wordle_ignore:
            if w.count(i) > 0:
                i_present = True
                break
        if i_present ==  False:
            filtered_words.append(w)
    
    filtered_words = set(filtered_words)
    filtered_words = list(filtered_words)
    print("Filtered with Gray: "+ str(len(filtered_words)))
    
    # select the words that have the green letters in the right place
    selected_words = []
    for w in filtered_words:
        if wordle_green['1'] != '':
            if w[0] != wordle_green['1']:
                continue
        if wordle_green['2'] != '':
            if w[1] != wordle_green['2']:
                continue
        if wordle_green['3'] != '':
            if w[2] != wordle_green['3']:
                continue
        if wordle_green['4'] != '':
            if w[3] != wordle_green['4']:
                continue
        if wordle_green['5'] != '':
            if w[4] != wordle_green['5']:
                continue        
        selected_words.append(w)
    print("Selected with Green: "+ str(len(selected_words)))

    # filter the words that have the yellow letters in wrong place
    selected_words_1 = []
    for w in selected_words:
        if wordle_yellow['1'] != []:
            if wordle_yellow['1'].count(w[0]) > 0:
                continue
        if wordle_yellow['2'] != []:
            if wordle_yellow['2'].count(w[1]) > 0:
                continue
        if wordle_yellow['3'] != []:
            if wordle_yellow['3'].count(w[2]) > 0:
                continue
        if wordle_yellow['4'] != []:
            if wordle_yellow['4'].count(w[3]) > 0:
                continue
        if wordle_yellow['5'] != []:
            if wordle_yellow['5'].count(w[4]) > 0:
                continue
        selected_words_1.append(w)
    print("Filtered with Yellow: "+str(len(selected_words_1)))

    # filter the words that have yellow letters in it
    selected_words_2 = []
    Yellow_letters = wordle_yellow['1'] + wordle_yellow['2'] + wordle_yellow['3'] + wordle_yellow['4'] + wordle_yellow['5']
    Yellow_letters = set(Yellow_letters)
    for w in selected_words_1:
        have_yellow = True
        for letter in Yellow_letters:
            if w.find(letter) < 0:
                have_yellow = False
                continue
        if have_yellow:
            selected_words_2.append(w)
    print("Selected with Yellow: "+str(len(selected_words_2)))

    return selected_words_2


wordle_green = {
    '1':'c',
    '2':'h',
    '3':'',
    '4':'e',
    '5':''
}
wordle_yellow = {
    '1':[],
    '2':[],
    '3':[],
    '4':[],
    '5':[]
}
wordle_ignore = ['r','u','l','o','d','x','a','g','s','y','b','r']

final_words = find_wordle(wordle_green, wordle_yellow, wordle_ignore)
print(final_words)
