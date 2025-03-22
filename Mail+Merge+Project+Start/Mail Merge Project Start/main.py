#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as dile:
    names = dile.read()
    print(names)
with open("./Input/Names/invited_names.txt") as file:
    letters = file.read()
    for letter in letters:
        name = letter.strip()
        new_letter = letters.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as mile:
            mile.write(new_letter)

