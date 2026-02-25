# _______________ "Activity 2" _______________
# Word count of shakespeare.txt

import time
import sys

def slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

symbols_and_numbers = "\n\r\t,:;.~|_@?!\"'+=^#&$()[]{}<>*-0123456789"

with open("shakespeare.txt") as file:
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()
    slow("'You want the word count for shakespeare.txt?'")
    time.sleep(1)
    
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
    slow("(ᵕ—ᴗ—) Counting each word in the text...")
    time.sleep(1)
    
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
