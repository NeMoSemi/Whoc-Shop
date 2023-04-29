token = #your token


def change_var(name_of_var, new_value):
    with open('configefile.txt', mode='r') as f:
        file = f.readlines()
        new_file = file
        for string in file:
            strok = string.replace('\n', '').split()
            if strok[0] == name_of_var:
                new_file[file.index(string)] = f'{name_of_var} = {new_value}\n'
                break
        with open('configefile.txt', mode='w') as save:
            for i in new_file:
                save.write(i)


#функция для возврата значения переменной из конфиг файла
def know_var(name_of_var):
    with open('configefile.txt', mode='r') as f:
        file = f.readlines()
        for string in file:
            #храним строки из конфиг файла в виде ['имя переменной', '=', 'значение переменной']
            strok = string.replace('\n', '').split()
            if strok[0] == name_of_var:
                if strok[-1] == 'True':
                    return True
                if strok[-1] == 'False':
                    return False
                else:
                    return strok[-1]
