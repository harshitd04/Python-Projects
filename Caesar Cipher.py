
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(shift, text):
    encrypted_text = ""
    for i in text:
        index = alphabet.index(i)
        add = index + shift
        if add > 25:
            add -= 26
        encrypted_text += alphabet[add]
    print(f"The encrypted text is : {encrypted_text}")

def decrypt(shift , text):
    decrypted_text = ""
    for i in text:
        index = alphabet.index(i)
        dec = index - shift
        if dec < 0 :
            dec -= 2
        decrypted_text += alphabet[dec]

    print(f"The decrypted text is : {decrypted_text}")

if direction == "encode":
    encrypt(shift, text)
elif direction == "decode":
    decrypt(shift,text)
else:
    print("Wrong input.")
