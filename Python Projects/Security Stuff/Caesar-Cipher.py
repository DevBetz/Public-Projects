


#note:encrypt and decrypt functions
#encrypt:
def encrypt(message, key):
  result = ""
  for letter in message:
    if letter.isalpha():
        if letter.islower():
            result += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        elif letter.isupper():
            result += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
    else:
        result += letter
  return (result)
  


#decrypt function:
def decrypt(message, key):
  result = ""
  for letter in message:
    if letter.isalpha():
        if letter.islower():
            result += chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
        elif letter.isupper():
            result += chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
    else:
        result += letter
  return result

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#main function
def main():
  user_choice = input("Welcome to the Caesar Cipher! Do you want to encrypt (e) or decrypt (d) text? ").lower()
  if user_choice not in ['e', 'd']:
      print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
      return
    
  message = input("What is your message? ")
  key = int(input("What is your key? "))
  
  
  
  if user_choice == 'e':
    encrypted_message = encrypt(message, key)
    print(f"Your encrypted message is: {encrypted_message}")

  elif user_choice == 'd':
    decrypted_message = decrypt(message, key)
    print(f"Your decrypted message is: {decrypted_message}")


main()


