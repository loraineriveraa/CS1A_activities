# _______________ "Activity 5" _______________
# Write output to wordcount.txt (Alphabetically sorted)

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
    slow("'(>-<)/ Moving the alphabetical word count to wordcount.txt...'")
    time.sleep(1)
    
    text_content = file.read().lower()
    
    for char in symbols_and_numbers:
        text_content = text_content.replace(char, ' ')
        
    words = text_content.split()
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    sorted_keys = sorted(word_freq.keys())

    with open("wordcount.txt", "w") as out_file:
        out_file.write("Output in Alphabetical Order\n")
        out_file.write("____________________________\n")
        for key in sorted_keys:
            out_file.write(f"{key} : {word_freq[key]}\n")

    print()
    slow("(˶˃ ᵕ ˂˶) Done! Check 'wordcount.txt' for the results.")
    time.sleep(1)
    print()

    slow("(づᴗ_ᴗ)づ COMPLETE!!!")
    print()
    print("₊˚ ✧ ----------━━━━⊱⋆⊰━━━━---------- ✧ ₊˚")
    print()
