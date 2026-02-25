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

symbols_and_numbers = "\n\r\t,:;.~|_@?!\"+=^#&$()[]{}<>*-0123456789"

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
    
    word_count = len(words)
 
    print()
    slow("(ᵕ—ᴗ—) Counting each word in the text...")
    time.sleep(1)
    print()
    time.sleep(1)

    slow("(づᴗ_ᴗ)づ 'Here, Total Words = " + str(word_count) + "'")
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()
