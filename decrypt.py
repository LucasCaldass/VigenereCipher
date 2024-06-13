from setKeyLength import complete_key


def decrypt(curr_key, curr_phrase):
    curr_key = curr_key.upper()
    curr_phrase = curr_phrase.upper()
    completed_key = complete_key(curr_key, len(curr_phrase))
    size = len(completed_key)

    decrypted_phrase = ''

    index_phrase = 0
    index_key = 0

    while index_phrase < size:
        if curr_phrase[index_phrase] == ' ':
            decrypted_phrase += curr_phrase[index_phrase]
            index_phrase += 1
        elif curr_phrase[index_phrase].isalpha():
            c = ord(curr_phrase[index_phrase]) - ord('A')
            k = ord(completed_key[index_key]) - ord('A')
            decrypted_phrase += chr(((c - k) % 26) + ord('A'))

            index_phrase += 1
            index_key += 1
        else:
            decrypted_phrase += curr_phrase[index_phrase]
            index_phrase += 1
            index_key += 1

    return decrypted_phrase
