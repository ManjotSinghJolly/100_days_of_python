import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

# Looping through the rows of the dataframe
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a text: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()