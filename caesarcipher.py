def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
# Output: "Counteer is found in unlikely places."
print(encrypt(decrypted_text, 13))
# Output: "Pbhentr vf sbhaq va hayvxryl cynprf."

encrypted_text2 = "Wklv lv d whvw phvvdjh."
decrypted_text2 = decrypt(encrypted_text2, 3)
print(decrypted_text2)
# Output: "This is a test message."
print(encrypt(decrypted_text2, 3))
# Output: "Wklv lv d whvw phvvdjh."

encrypted_text3 = "Dro aesmu lbygx pyh tewzc yfob dro vkji nyq."
decrypted_text3 = decrypt(encrypted_text3, 10)
print(decrypted_text3)
# Output: "The quick brown fox jumps over the lazy dog."
print(encrypt(decrypted_text3, 10))
# Output: "Dro aesmu lbygx pyh tewzc yfob dro vkji nyq."
