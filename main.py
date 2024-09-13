# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

      if letter not in alphabet:
          output_text += letter
      else:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
caesar(text,shift,direction)

# TODO-3: Can you figure out a way to restart the cipher program?
end_of_sess= False
# if encode_or_decode =  "encode" or "decode"
#     endofsess= False

while end_of_sess is False:
    decision2 = input("do you still want to encode or decode something? \n").lower()
    if decision2 == "no":
        end_of_sess = True
        print("Goodbye")
    elif decision2 == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift,direction)
