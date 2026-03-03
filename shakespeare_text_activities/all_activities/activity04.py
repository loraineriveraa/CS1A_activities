# _______________ "Activity 4" _______________
# Count of unique words

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
    slow("'Counting unique words in shakespeare.txt...'")
    time.sleep(1)
    
    text_content = file.read().lower()
    
    for char in symbols_and_numbers:
        text_content = text_content.replace(char, ' ')
        
    words = text_content.split()
    unique_words = set(words)
    unique_count = len(unique_words)
 
    print()
    slow("(づᴗ_ᴗ)づ 'Here, Total Unique Words = " + str(unique_count) + "'")
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()
