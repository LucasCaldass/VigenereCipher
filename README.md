# Vigenère Cipher

This project implements the Vigenère cipher.

The input can be a sentence with letters, characters and numbers, but the cipher it's designated to just encrypt the letters, so, the other characters will remain unchanged in the same position as in the original sentece.

## Project Structure

- `encrypt.py`: Function for encryption.
- `decrypt.py`: Function for decryption.
- `complete_key.py`: Function to adjust the key length.

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/LucasCaldass/VigenereCipher.git
    ```

2. Navigate to the project directory:
    ```sh
    cd VigenereCipher
    ```

3. Run the program:
    ```sh
    python main.py
    ```

## Usage Example

1. Select the option "Encrypt a message" or "Decrypt a message".
2. Provide the message to be encrypted or decrypted, along with the key to be used for the process.
3. The output will be the resulting message.
