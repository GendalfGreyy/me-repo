import time
def centavra():
    print('Выберите функцию команды и напишите её на следуйщей строке: << шифровка >> -- << дешифровка >>')
    jkl = input()
    if jkl == 'шифровка':
        print('Введите ваш текст в поле ввода для шифрования:')
        word = input()
        time.sleep(1)
        print('Введите диапазон шифрования:')
        hp = int(input())
        time.sleep(1)
        s = ''
        d = ''
        print('Теперь зашифруем ваш текст:')
        time.sleep(2)
        print('Шифруется')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        for i in range(len(word)):
            s += chr(ord(word[i])+hp)
        word = s
        print('Текст зашифрован:',s)
        time.sleep(1)
        print('Если хотите дешифровать ваш текст то введите кодовое слово << дешифровка >>,иначе введите слово << key >>')
        time.sleep(1)
        f = input()
        if f == 'дешифровка':
            for i in range(len(word)):
                d += chr(ord(word[i])-hp)
            print('Ваш первоначальный текст:',d)
            print('Если вы хотите еще какой-то текст зашифровать или дешифровать введите слово << key >>, если хотите завершить программу введи слово << non >>')
            g = input()
            if g == 'key':
                centavra()
            else:
                False
        elif f == 'key':
            centavra()
            print('Если вы хотите еще какой-то текст зашифровать или дешифровать введите слово << key >>')
            g = input()
            if g == 'key':
                centavra()
            else:
                False
    elif jkl == 'дешифровка':
        print('Введите ваш текст в поле ввода для дешифрования:')
        word = input()
        time.sleep(1)
        print('Введите диапазон дешифрования')
        hp = int(input())
        time.sleep(1)
        s = ''
        d = ''
        print('Теперь задешифруем ваш текст')
        time.sleep(2)
        print('Дешифруется')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        for i in range(len(word)):
            d += chr(ord(word[i])-hp)
        print('Ваш дешифрованный текст:',d)
        time.sleep(1)
        print('Если хотите зашифровать ваш текст то введите кодовое слово << шифровка >>,иначе введите слово << key >>')
        time.sleep(1)
        f = input()
        if f == 'шифровка':
            for i in range(len(word)):
                d += chr(ord(word[i]) - hp)
            print('Ваш первоначальный текст:',d)
            time.sleep(1)
            print('Если вы хотите еще какой-то текст зашифровать или дешифровать введите слово << key >>, если хотите завершить программу введите слово << non >>')
            g = input()
            if g == 'key':
                centavra()
            else:
                False
centavra()
