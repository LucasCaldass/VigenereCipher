from setKeyLength import complete_key


def encrypt(curr_key, curr_phrase):
    curr_key = curr_key.upper()
    curr_phrase = curr_phrase.upper()
    completed_key = complete_key(curr_key, len(curr_phrase))  # Modificando o tamanho da chave para ser o mesmo da frase

    encrypted_phrase = ''

    for char_phrase, char_key in zip(curr_phrase, completed_key):
        if char_phrase.isalpha():
            shift = ord(char_key) - ord('A')
            encrypted_char = chr(((ord(char_phrase) - ord('A') + shift) % 26) + ord('A'))
            encrypted_phrase += encrypted_char
        else:
            encrypted_phrase += char_phrase

    return encrypted_phrase
