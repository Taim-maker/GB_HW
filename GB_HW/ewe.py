TRUE_PASSWORD = 'qwerty'
COUNT = 3
user_count = 0
user_password = ''

while TRUE_PASSWORD != user_password and user_count != COUNT:
 user_password = input('enter password: ')
 if user_password == TRUE_PASSWORD:
    print('Password is ok')
 else:
    user_count=user_count + 1
    print('Password is not ok', ' left tries', COUNT-user_count)
print('End of programm')



# i = 0
# while i < 10:
#       print('Hello')
#       i= i + 1
#
# Print('Enc')