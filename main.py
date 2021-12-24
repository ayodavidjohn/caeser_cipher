# Caesar Cipher Project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']

direction = input("TYPE 'encode' to encrypt, TYPE 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the Shift number: \n"))


# Don't change the code above
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index()
        if cipher_direction == "decode":
          shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)