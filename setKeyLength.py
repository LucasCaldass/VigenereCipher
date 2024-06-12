def complete_key(curr_key, length):
    completed_key = (curr_key * (length // len(curr_key))) + curr_key[:length % len(curr_key)]
    return completed_key
