PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt",) as names_file:
    name=names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_let:
    letter=starting_let.read()
    for name in name:
        stripped_name=name.strip()
        new_letter=letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_of_{stripped_name}","w") as completed_letter:
            completed_letter.write(new_letter)
