from decrypt import decrypt
from encrypt import encrypt


def option_encrypt():
    phrase = input('Digite a frase a ser encriptada: ')
    key = input('Digite a chave que será usada na encriptação da mensagem: ')

    print(encrypt(key, phrase).lower())


def option_decrypt():
    phrase = input('Digite a frase encriptada que deseja desencriptar: ')
    key = input('Digite a chave na encriptação da mensagem: ')

    print(decrypt(key, phrase).lower())


def menu():
    while True:
        print('\nMenu:')
        print('1. Encriptar uma mensagem.')
        print('2. Desencriptar uma mensagem.')
        print('3. Sair')

        choice = input("Escolha uma opção (1-3): ")

        if choice == '1':
            option_encrypt()
        elif choice == '2':
            option_decrypt()
        elif choice == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção entre 1 e 4.')

