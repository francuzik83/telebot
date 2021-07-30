import re
import random


string = str(input())
word_list = string.split()
word_list_change = []
for i, q in enumerate(word_list):
    flag = re.search(r'\W',q)
    word = list(q)
    word_size = len(word)
    if flag == None:
        slice_word = word[1: word_size -1]
        random.shuffle(slice_word)
        word[1: word_size -1] = slice_word
        new_word = ''.join(word)
        word_list_change.insert(i,new_word)
        #print(word_list_change)
    else:
        slice_word = word[1: word_size - 2]
        random.shuffle(slice_word)
        word[1: word_size - 2] = slice_word
        new_word = ''.join(word)
        word_list_change.insert(i, new_word)
        #print(word_list_change)
new_string = ' '.join(word_list_change)
print(new_string)






