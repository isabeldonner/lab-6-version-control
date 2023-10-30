def encode(password):
  encoded_pass = ""
  for digit in password:
    digit = int(digit) + 3
    encoded_pass = encoded_pass + str(digit)
def display_menu():
  global password
  print('Menu')
  print('-------------')
  print('1. Encode')
  print('2. Decode')
  print('3. Quit')
  selection = int(input('Please enter an option: ')
  while selection != 3:
    if selection == 1:
      password = input('Please enter your password to encode: ')
      encoded_pass = encode(password)
      print('Your password has been encoded and stored!')
      display_menu()
    elif selection == 2:
      decoded_pass = decode(password)
      print('The encoded password is' , encoded_pass, ', and the original password is' , decoded_pass)
if __name__ == "__main__":
  display_menu()

  
