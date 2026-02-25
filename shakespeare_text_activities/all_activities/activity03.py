# _______________ "Activity 3" _______________
# Lowercase each word then count

import time
import sys

def slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

symbols_and_numbers = "\n\r\t,:;.~|_@?!\"+=^#&$()[]{}<>*-0123456789"

with open("shakespeare.txt") as file:
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()
    slow("'You want me to lowercase each word and count the shakespeare.txt?'")
    time.sleep(2)
    
    text_content = file.read()
    
    for char in symbols_and_numbers:
        text_content = text_content.replace(char, ' ')
        
    words = text_content.split()
    
    new_dictionary = {}
    for mem in words:
        word_lower = mem.lower()
        new_dictionary[word_lower] = new_dictionary.get(word_lower, 0) + 1

    word_count = len(words)
    alphabetically_sorted_list = sorted(new_dictionary)

    print()
    slow("(ᵕ—ᴗ—) Counting and lowering the letter of each word in the text...")
    time.sleep(3)
    
    print()
    print("━━━━⊱ Words in Alphabetical Order ⊰━━━━")
    for mem in alphabetically_sorted_list: 
        print(f'{mem} : {new_dictionary[mem]}')
    
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    time.sleep(1)

    slow("(づᴗ_ᴗ)づ 'Here, Total Words = " + str(word_count) + "'")
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()

