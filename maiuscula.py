def to_camel_case(text):
    text = ''.join(word.title() for word in text.split('_'))
    print(text)
    return

text = input(f'Digite algo: ')
to_camel_case(text)
