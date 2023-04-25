"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730308175"

word: str = input('Enter a 5-character word:') #5 character input string
if (len(word) != 5): """ ensure that the input is 5 characters """
    print('Error: Word must contain 5 characters')
    exit() #exit program if not true

letter: str = input('Enter a single character:') # 1 character input string
if (len(letter) != 1): #ensure that the input is 1 character
    print('Error: Character must be a single character.')
    exit() # exit program if not true

print(f'Searching for {letter} in {word}') # print searching to show that the following code will be assessing where the letter is in word

letter_count = str = 0 # start letter count in word at zero
if (letter == word[0]): #check if letter at index 0
    letter_count += 1 # start append for letter
    print(f'{letter} found at index 0')
if (letter == word[1]): #check if letter at index 1
    letter_count += 1 # continue append
    print(f'{letter} found at index 1')
if (letter == word[2]): #check if letter at index 2
    letter_count += 1 #continue append
    print(f'{letter} found at index 2')
if (letter == word[3]): #check if letter at index 3
    letter_count += 1 #continue append
    print(f'{letter} found at index 3')
if (letter == word[4]): #check if letter at index 4
    letter_count += 1 #continue append
    print(f'{letter} found at index 4')  
if letter_count > 1: #count multiple matching indices over 1 and print the following line
    print(f'{letter_count} instances of {letter} found in {word}')
if letter_count == 1: #if only 1 single matching index, print the following line
    print(f'1 instance of {letter} found in {word}')
if letter_count <= 0: #if no indices of letter in word, print the following line
    print(f'No instances of {letter} found in {word}')