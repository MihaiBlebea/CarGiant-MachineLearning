
def write_txt(file_name, content):
    file = open(file_name + '.txt', 'w')
    file.write(str(content) + '\n')
