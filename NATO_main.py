import pandas
try:
    nato_file = pandas.read_csv(r"C:\Users\RAKESH KUMAR DABAS\PycharmProjects\PythonProject\day-26\.venv\NATO-alphabet-start"
                            r"\NATO-alphabet-start\NATO_nato_phonetic_alphabet.csv")

    nato_dict = {row.letter:row.code for (index,row) in nato_file.iterrows()}
    # print(nato_dict.items())
    def generate_phonetic():
        try:
            user_input = input("Enter your word: ").upper()
            output_list = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print(f"Only letters in the alphabet.")
            generate_phonetic()
        else:
            print(output_list)

except FileNotFoundError:
    print("File Not Found. Please Check")

else:
    generate_phonetic()










# nato_dict = {row.letter:row.code for (letter,code) in nato_file.iterrows()}     #Wrong way

# output_list = [value for key,value in nato_dict.items() if key in user_input]   #Wrong way
# user_input.t0_list()

# for i in user_input:
#     for key,value in nato_dict.items():
#         if i == key :
#             output_list.append(value)

