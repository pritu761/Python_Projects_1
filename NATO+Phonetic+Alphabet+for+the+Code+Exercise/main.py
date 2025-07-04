# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output_list = []
word = input("Enter a word: ").upper()
for letter in word:
    try:
        output_list=phonetic_dict[letter]
    except KeyError:
        print("Please enter letters no numbers nor symbols")
        continue 
print(output_list)
