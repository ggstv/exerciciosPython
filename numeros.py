string = input('Digite algo: ')
for char in range(0, len(string)):
    if string[char].isnumeric():
        print(f'{string[char]}')