def encode(password):
  encoded_pass = ""
  for digit in password:
    digit = int(digit) + 3
    encoded_pass = encoded_pass + str(digit)

