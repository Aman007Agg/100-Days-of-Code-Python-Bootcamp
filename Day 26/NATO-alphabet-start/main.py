import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(df)
# print(df.to_dict())

# for (index, row) in df.iterrows():
#     # print(row.letter)
#     # print(row.code)

alphabet_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(alphabet_dict)

word = input("Enter a word:").upper()
output_list = [alphabet_dict[letter] for letter in word]
print(output_list)
