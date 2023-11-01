def encode(password):
  encoded_pass = ""
  for digit in password:
    if int(digit) >= 7:
      digit = str((int(digit) + 3) % 10)
      encoded_pass += digit
    else:
      digit = str(int(digit) + 3)
      encoded_pass = encoded_pass + digit
  return encoded_pass

def decode(password):
  decoded_pass = ""
  for digit in password:
    if int(digit) < 3:
      decoded_pass += str((int(digit) + 7))
    else:
      decoded_pass += str(int(digit) - 3)
  return decoded_pass

def display_menu():
  selection = 0
  while selection != 3:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')
    selection = int(input('Please enter an option: '))
    if selection == 1:
      password = input('Please enter your password to encode: ')
      encoded_pass = encode(password)
      print('Your password has been encoded and stored!\n')
    elif selection == 2:
      decoded_pass = decode(encoded_pass)
      print('The encoded password is', encoded_pass, ', and the original password is', decoded_pass, '\n')


if __name__ == "__main__":
  display_menu()