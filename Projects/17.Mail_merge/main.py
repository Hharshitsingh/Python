PLACEHOLDER = "[name]"
with open(r"./Input\Names\invited_names.txt") as name_file:
    names = name_file.readlines()
    # print(names)

with open(r"./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        # print(new_letter)
        with open(f"./Output/letter_for_{strip_name}.docx", "w") as completed:
            completed.write(new_letter)