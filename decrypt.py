from setKeyLength import complete_key


def decrypt(curr_key, curr_phrase):
    curr_key = curr_key.upper()
    curr_phrase = curr_phrase.upper()
    completed_key = complete_key(curr_key, len(curr_phrase))

    decrypted_phrase = ''

    for char_phrase, char_key in zip(curr_phrase, completed_key):
        if char_phrase.isalpha():
            shift = ord(char_key) - ord('A')
            decrypted_char = chr(((ord(char_phrase) - ord('A') - shift) % 26) + ord('A'))
            decrypted_phrase += decrypted_char
        else:
            decrypted_phrase += char_phrase

    return decrypted_phrase
