print('Quiz program!\n')
attempt = 1
max_attempts = 4

while attempt < max_attempts:
   attempt += 1

   answer = input('What is the capital of Wisconsin? ')
   if answer == 'Madison':
      print("Correct!")
      break
   else:
      print('You got it wrong, please try again.\n')

print("Thanks for playing. It took you %s attempt(s)." %(attempt-1))
