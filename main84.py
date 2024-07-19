def read_file(teste):
    try:
        with open(teste, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f'Error; file "{teste}" not found'
    
def write_file(teste , content):
    try:
        with open(teste, 'w') as file:
            file.write(content)
            return 'File written sucessfully'
    except Exception as e:
        return f'Error {e}'

file_content = read_file('teste.txt')
print(file_content)

write_status = write_file('teste.txt', 'Welcome Bruno Melo')
print(write_file)