alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

continue_looping = True
while continue_looping:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
                shift_amount*= -1
        for char in start_text:
            if char in alphabet_list:
                position = alphabet_list.index(char)
                new_position = position + shift_amount
                end_text += alphabet_list[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        continue_looping = False
        print("Goodbye") 