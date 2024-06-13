from setKeyLength import complete_key


def encrypt(curr_key, curr_phrase):
    curr_key = curr_key.upper()
    curr_phrase = curr_phrase.upper()
    completed_key = complete_key(curr_key, len(curr_phrase))
    size = len(completed_key)

    encrypted_phrase = ''

    index_phrase = 0
    index_key = 0

    while index_phrase < size:
        if curr_phrase[index_phrase] == ' ':
            encrypted_phrase += curr_phrase[index_phrase]
            index_phrase += 1
        elif curr_phrase[index_phrase].isalpha():
            p = ord(curr_phrase[index_phrase]) - ord('A')
            k = ord(completed_key[index_key]) - ord('A')
            encrypted_phrase += chr(((p + k) % 26) + ord('A'))

            index_phrase += 1
            index_key += 1
        else:
            encrypted_phrase += curr_phrase[index_phrase]
            index_phrase += 1
            index_key += 1

    return encrypted_phrase
