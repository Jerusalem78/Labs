# Домашнее задание по лабораторной №3 по предмету "Информационные технологии"
# БВТ2404 - Фомин Денис Владиславович

# 1 и 3

def opening(method='all', path='example.txt'):
    try:
        with open(path,'r', encoding='UTF-8') as file:
            if method == 'all':
                print(file.read())
            else:
                for line in file.read().splitlines():
                    print(str(line))
    except FileNotFoundError:
        print('FileNotFoundError')

# 2

def writing(text, method='w'):
    if method not in 'wa':
        return 'неправильный метод'
    with open('user_input.txt', method, encoding='UTF-8') as file:
        file.write(text)


