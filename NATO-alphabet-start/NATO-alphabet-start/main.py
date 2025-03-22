import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data1 = data.to_dict()
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_alphabet)
data = input("Enter a Word: ").upper()
output = [phonetic_alphabet[letter] for letter in data]
print(output)
