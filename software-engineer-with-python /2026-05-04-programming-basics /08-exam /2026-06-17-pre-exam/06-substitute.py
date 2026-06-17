K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_iterations = 0
is_found = False

for digit1 in range(K, 8 + 1):
    for digit2 in range(9, L - 1, -1):
        for digit3 in range(M, 8 + 1):
            for digit4 in range(9, N - 1, -1):

                if ((digit1 % 2 == 0) and (digit3 % 2 == 0) and (digit2 % 2 != 0) and (digit4 % 2 != 0)):

                    if ((digit1 == digit3) and (digit2 == digit4)):
                        print('Cannot change the same player.')

                    elif digit1 != digit3 or digit2 != digit4:
                        print(f'{digit1}{digit2} - {digit3}{digit4}')
                        valid_iterations += 1

                        if valid_iterations == 6:
                            is_found = True
                            break

            if is_found:
                break

        if is_found:
            break

    if is_found:
        break
