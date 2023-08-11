# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

with open("Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

for name in names_list:
    stripped_name = name.strip()
    replaced_name = letter_content.replace('[name]', name)

    with open(f"Output/ReadyToSend/letter_to {name}", mode='w') as output:
        output.write(replaced_name)
