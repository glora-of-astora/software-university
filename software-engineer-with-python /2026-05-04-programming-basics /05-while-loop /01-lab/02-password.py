username = input()
password = input()
new_password = ''

while True:
    new_password = input()
    if new_password == password:
        print(f'Welcome {username}!')
        break
    else:
        continue

# ALTERNATIVE SOLUTION

# username = input()
# password = input()
# password_try = input()

# while password_try != password:
#     password_try =  input()
# THE WHILE LOOPS WORKS AS A FILTER HERE

# print(f'Welcome {username}!')
# THAT IS WHY WE BRING THE PRINT FUNCTION OUTSIDE OF IT
# WE WILL NEVER GO OUT OF THE WHILE LOOP
# UNLESS WE INPUT THE CORRECT PASSWORD FIRST
# AND IF WE DO, THE PASSWORD_TRY INPUT IS SKIPPED