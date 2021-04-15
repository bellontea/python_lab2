def task_9_1():
    m = int(input())
    n = int(input())
    lib_book = list()
    found = list()

    i = 0
    while (i != m):
        lib_book.append(input())
        i += 1
    
    lib_book.sort()
    i = 0
    while (i != n):
        book = input()
        for j in lib_book:
            if (j == book):
                found.append("YES")
                break
        if (len(found) == i):
            found.append("NO")
        i += 1
    print(*found, sep="\n")

def task_9_2():
    m = int(input())
    students = list()
    attend = list()

    for i in range(m):
        n = int(input())
        for j in range(n):
            student = input()
            if (i == 0):
                students.append(student)
                attend.append(1)
                continue
            for k in range(len(students)):
                if (student == students[k]):
                    attend[k] += 1
                    break

    print()
    for z in range(len(students)):
        if (attend[z] == m):
            print(students[z], sep="\n")

def task_9_3():
    n = int(input())
    workers = list()
    count = 0

    for i in range(n):
        workers.append(input())
    for j in workers:
        if (workers.count(j) > 1):
            count += 1
    
    print()
    print(count)

def task_9_4():
    m = int(input())
    products = list()
    for i in range(m):
        products.append(input())
    
    products.sort()

    n = int(input())
    ingredients = list()
    recepies = list()

    for i in range(n):
        count = 0
        name = input()
        quantity = int(input())
        for j in range(quantity):
            ingredients.append(input())
            for k in products:
                if (ingredients[j] == k):
                    count += 1
                    break
        if (count == quantity):
            recepies.append(name)
        ingredients.clear()
    
    print()
    print(*recepies, sep="\n")

def task_9_5():
    m = int(input())
    dishes = list()
    for i in range(m):
        dishes.append(input())
    
    dishes.sort()

    n = int(input())
    cooked = list()

    for i in range(n):
        quantity = int(input())
        for j in range(quantity):
            cooked.append(input())

    print()
    for i in dishes:
        if (cooked.count(i) == 0):
            print(i, sep="\n")


def task_10_1():
    str = input()
    n = int(input())
    n -= 1
    print()
    if ((n >= len(str)) or (n <= 0)):
        print("ОШИБКА")
    else:
        print(str[n])

def task_10_2():
    n = int(input())
    str = input()
    res = ""

    for i in range(len(str)):
        if (str[i].isalpha() == False):
            res += str[i]
            continue

        letter = str[i].lower()
        j = 0
        while (chr(ord(letter) + j) != "я" and (n - j) != 0):
            j += 1
        if ((n - j) != 0):
            if (str[i].isupper()):
                res += chr(ord("а") + n - j).upper()
            else:
                res += chr(ord("а") + n - j)
        else:
            if (str[i].isupper()):
                res += chr(ord(letter) + n).upper()
            else:
                res += chr(ord(letter) + n)

    print()
    print(res)

def task_10_3():
    str = input()
    if (str[0].lower() == "а"):
        print("\nДА")
    else:
        print("\nНЕТ")

def task_10_4():
    str = input()
    print("\n" + str[-1])

def task_10_5():
    while (input()[0].lower() == 'а'):
        pass

def task_10_6():
    path = input()
    print("\n" + path[0], end="")
    steps = 1
    size = len(path)

    for i in range(size):
        if (path[i] == '>'):
            print(path[0], end="")
            steps += 1

        if (path[i] == 'V'):
            print()
            j = i + 1
            if (i != size - 1 and path[j] == '<'):
                count_left = 0
                while (j != size - 1 and path[j] != 'V'):
                    steps -= 1
                    count_left += 1
                    j += 1
            for j in range(steps - 1):
                print(' ', end="")
            if (i + 1 < size and path[i + 1] == '<'):
                for k in range(count_left):
                    print(path[0], end="")
            print(path[0], end="")
    print()


def task_11_1():
    str = input()
    size = len(str)
    count = 0
    max = 0
    for i in range(size):
        if(i + 1 != size and str[i + 1] == 'о'):
            count += 1
        else:
            if (count > max):
                max = count
            count = 0
    print()
    print(max)

def task_11_2():
    n = int(input())
    str_list = list()

    for i in range(n):
        str_list.append(input())

    print()

    for str in str_list:
        if (str.find("####") == 0):
            continue
        if (str.find("%%") == 0):
            newstr = str.replace("%%", "", 1)
            print(newstr)
        else:
            print(str)

def task_11_3():
    str = input()
    n = int(input())
    letter = input()
    print()

    if (n > len(str) or n < 1 or len(letter) != 1 or letter.isalpha() == False):
        print("ОШИБКА")
    else: 
        if (str[n - 1] == letter):
            print("ДА")
        else:
            print("НЕТ")

def task_11_4():
    n = int(input())
    mark = False
    slash = False
 
    char = 0
    result = list()
 
    for i in range(n):
        str = input()
        result.append("")

        while str[char] == ' ':
            result[i] += ' '
            char += 1

        for j in range(char, len(str)):
            if not slash:
                if (str[j] == "'"):
                    result[i] += str[j]
                    mark = not mark
                elif (str[j] == "\\"):
                    result[i] += str[j]
                    slash = True
                elif (str[j] == "#"):
                    if mark:
                         result[i] += str[j]
                    else:
                        break
                elif (str[j] == " "):
                    if mark:
                        result[i] += str[j]
                    else:
                        if (j + 1 != len(str)):
                            if (str[j + 1] == " "):
                                result[i] += ""
                            else:
                                result[i] += str[j]
                else:
                    result[i] += str[j]
            else:
                slash = False
                result[i] += str[j]

        mark = False
        slash = False    
        char = 0
    
    print()
    print(*result, sep="\n")

def task_11_5():
    str = input()
    size = len(str)
    n = int(size / 2)

    for i in range(n):
        print()
        start = i + 1
        end = size - i - 1
        for j in range(start, end):
            print(str[j], sep='', end='')


def task_12_1():
    n = int(input())
    white_list = list()
    req_list = list()

    for i in range(n):
        white_list.append(input())

    m = int(input())

    for j in range(m):
        req = input()
        if (white_list.count(req) != 0):
            req_list.append(req)

    print()
    print(*req_list, sep="\n")

def task_12_2():
    n = input()
    mistakes = []
    right_result = []
    m = int(n[:4])
    result = int(n[4:])

    for i in range(m):
        line = input()
        price, num, sum = int(line[0:7]), int(line[8:12]), int(line[13:18])
        if (price * num != sum):
            mistakes.append(i + 1)
        right_sum = num * price
        right_result.append(right_sum)

    for j in right_result:
        result -= j

    print()
    print(abs(result))

    for k in mistakes:
        print(k, end=' ')

def task_12_3():
    n = int(input())
    shopping_list = list()
    count_list = list()

    for i in range(n):
        shopping_list.append(input())
        count_list.append(input())
    
    shopping_list.reverse()
    count_list.reverse()
    print()
    for i in range(n):
        print(shopping_list[i] + " " + count_list[i])

def task_12_4():
    str = input()
    size = len(str)
    num = str[0]
    count = 1
    print()

    for i in range(size):
        if (i + 1 != size and str[i + 1] == num):
            count += 1
        else:
            print(count, num)
            if (i + 1 != size):
               num = str[i + 1]
               count = 1

def task_12_5():
    n = int(input())
    print()
    num = 1 / n
    str_num = str(num)
    size = len(str_num)

    i = str_num.find('.') + 1
    while (i < size and str_num.count(str_num[i], i) == 1):
        i += 1
    
    if (i == size):
        start = 0
    else:
        start = str_num[i]
    res = start
    while (i + 1 < size and str_num[i + 1] != start):
        res += str_num[i + 1]
        i += 1

    print(res)

def task_12_6():
    dictionary = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
                  'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
                  'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}
    
    str = input()
    print()

    for i in range(5):
        for j in str:
            print(dictionary.get(j)[i], end='')
        print()

def task_12_7():
    n = int(input())
    m = int(input())
    str_list = []
    
    for i in range(n):
        str_list.append(input())

    print()

    for i in range(0, n, 2):
        for j in range(0, m, 2):
            print(str_list[i][j], sep='', end='')
        print()


def task_13_1():
    n = int(input())
    items = []
    items_updated = []

    for i in range(n):
        items.append(input())
    
    shifts = int(input())

    for i in range(shifts):
        left = int(input())
        for j in range(left):
            items_updated.append(items[int(input()) - 1])
        items.clear()
        items = items_updated.copy()
        items_updated.clear()

    print()
    print(*items, sep='\n')

def task_13_2():
    n = int(input())
    nums = []

    for i in range(n):
        nums.append(int(input()))

    nums.sort(reverse = True)

    print()
    print(*nums, sep='\n')

def task_13_3():
    n = int(input())
    sequence = []
    sequence_reverse = []
    sequence.append(0)

    for i in range(n - 1):
        end = len(sequence) - 1
        count = 0
        for start in range(end + 1):
            if (sequence[start] == sequence[end]):
                count += 1
            end -= 1
        sequence.append(count)

    print()
    print(*sequence, sep='\n')

def task_13_4():
    s = int(input())
    stats1 = []
    stats2 = []

    for i in range(s):
        stats1.append(int(input()))

    stats2 = stats1.copy()

    train = int(input())

    for i in range(train):
        brother = int(input())
        stat = int(input())
        upgrade = int(input())

        if (brother == 1):
            stats1[stat] += upgrade
        else:
            stats2[stat] += upgrade
    
    coincidence = 0
    for i in range(s):
        if (stats1[i] == stats2[i]):
            coincidence += 1

    print()
    print(*stats1, sep=' ')
    print(*stats2, sep=' ')
    print(coincidence)

def task_13_5():
    n = int(input())
    teams = []

    for i in range(n):
        teams.append([input(), int(input())])

    teams.sort(key=lambda score: score[1], reverse=True)

    passed = []
    not_passed = []
    m = n // 2 + n % 2

    for i in range(m):
        passed.append(teams[i][0])

    for i in range(m, n):
        not_passed.append(teams[i][0])

    passed.sort()
    not_passed.sort()

    print()
    print(*passed, *not_passed, sep='\n')

def task_13_6():
    dictionary = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
                  'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
                  'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
                  'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
                  'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
                  'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
                  'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
                  'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
                  'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
                  'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
                  'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
                  'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
                  'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
    
    str = input()
    print()

    for i in range(5):
        for j in str:
            print(dictionary.get(j)[i], end='')
        print()

def task_13_7():
    n = int(input())
    prisoners = []
    dead = []

    for i in range(n):
        prisoners.append(input())

    k = int(input())

    i = 0
    k -= 1
    while (len(prisoners) != 0):
        if (i < len(prisoners)):
            dead.append(prisoners.pop(i))
            i += k
        else:
            i = 0

    print()
    print(*dead, sep='\n')


def task_14_1():
    n = int(input())
    recipe = []

    for i in range(n):
        str = input()
        if (str.find("лук") == -1):
            recipe.append(str)

    print()
    print(*recipe, sep=", ")

def task_14_2():
    login_pass = []
    inf = list(input().split(':'))

    while inf != ['']:
        login_pass.append(inf)
        inf = list(input().split(':'))
    easy_pass = list(input().split(';'))

    print()
    for i in range(len(login_pass)):
        if (easy_pass.count(login_pass[i][1]) != 0):
            print('To:', login_pass[i][0])
            name = login_pass[i][4].split(',')
            print(name[0] + ',' + ' ваш пароль слишком простой, смените его.')

def task_14_3():
    print()
    print("\n".join(input().split()))

def task_14_4():
    column = [int(number) for number in input().split()]

    max_column = max(column) + 1

    print()
    for i in range(max_column + 1):
    	print("*", end="")

    	for j in column:

    		if(i == 0):
    			print("*", end="")
    			continue;

    		if(i > max_column - j):
    			print("*", end="")
    		else:
    			print(" ", end="")

    	print("*")

def task_14_5():
    symb = ["?","&","=","#"]
    url = input()
    key = input()
    
    print()
    i = url.find("?" + key + "=") + len(key) + 2
    for j in range(i, len(url)):
    	if(url[j] in symb):
    		break;
    	print(url[j], end="")
    print()

def task_15_1():
    letter = input().lower()
    words = input().split()

    print()
    for word in words:
        if (word.count(letter) != 0 or word.count(letter.upper())):
            print(word)

def task_15_2():
    str = input()

    spaces_tabs = 0
    spaces_tabs += str.count(' ')
    spaces_tabs += str.count('\t')

    print()
    print(len(str) - spaces_tabs)

def task_15_3():
    str = input()

    max = 0
    new_str = str.lower()
    for i in new_str:
        count = new_str.count(i)
        if (count > max):
            max = count
    
    print()
    print(max)

def task_15_4():
    med = []
    mod = []
    all = []

    for j in range(int(input())):
        s = list(map(int, input().split()))
        s.sort()
        z = s[len(s) // 2]
        max = 0

        for i in s:
            if s.count(i) > max:
                max = s.count(i)
                moda = i
        med.append(z)
        mod.append(moda)
        for i in s:
            all.append(i)

    print()
    all.sort()
    print(*med)
    print(*mod)
    med.sort()
    mod.sort()
    print(med[len(med) // 2])
    max = 0

    for i in mod:
            if mod.count(i) > max:
                max = mod.count(i)
                moda = i

    print(moda)
    print(all[len(all) // 2])
    max = 0

    for i in all:
        if all.count(i) > max:
            max = all.count(i)
            moda = i

    print(moda)

def task_15_5():
    n = int(input())
    queue = []
    for i in range(n):
        str = input()
        if (str.count("встал") == 1):
            queue.append(str[0:str.index(" встал")])
        elif (str.count("Привет") == 1):
            queue.insert((len(queue) // 2 + 1), str[str.index("! ") + 2:str.index(" будет")])
        elif (str.count("хватит") == 1):
            queue.remove(str[0:str.index(',')])
    print()
    print(*queue, sep='\n')

def task_16_1():
    s = [0 for i in range(30001)]
    pos = 0
    a = input()
    print()
    i = 0

    while(i < len(a)):
        if (a[i] == ">"):
            pos = pos + 1
        elif (a[i] == "<"):
            pos = pos - 1
        elif (a[i] == "."):
            print(s[pos])
        elif (a[i] == "+"):
            s[pos] = s[pos] + 1
            if (s[pos] > 255):
                s[pos] = 0
        elif (a[i] == "-"):
            s[pos] = s[pos] - 1
            if (s[pos] < 0):
                s[pos] = 255
        elif (a[i] == '['):
            if s[pos] == 0:
                c = 1
                while(c != 0):
                    i += 1
                    if (a[i] == '['):
                        c += 1
                    if (a[i] == ']'):
                        c -= 1
        elif (a[i] == ']'):
            c = -1
            i = i - 1
            while(c != 0):
                if (a[i] == ']'):
                    c -= 1
                if (a[i] == '['):
                    c += 1
                i -= 1
        i += 1 

def task_16_2():
    n = int(input())
    coord = []
    table = []
    result = []

    for i in range(n):
        table.append(input().split(','))

    m = int(input())

    for _ in range(m):
        coord = input().split(',')

        x = int(coord[0])
        y = int(coord[1])
        j = table[x][y]

        if ',' in table[x][y]:
            j = table[x][y]
            a = j[:j.find(',')]
            b = j[j.find(',') + 2:]
            result.append(','.join([a, b]))
        elif '\n' in table[x][y]:
            i = table[x][y]
            a = i[:i.find('\n')]
            b = i[i.find('\n') + 2:]
            result.append('\n'.join([a, b]))
        else:
            result.append(table[x][y])
    
    print()
    print(*result, sep='\n')

def task_16_3():
    n = int(input())
    b = [[int(input()) for _ in range(n)] for _ in range(n)]
    
    for _ in range(int(input())):
    	y = int(input())
    	x = int(input())
    	for i in range(-1, 2):
    		for j in range(-1, 2):
    			if(x + i >= 0 and y + j >= 0 and x + i < n and y + j < n):
    				b[x + i][y + j] -= 8 if i == 0 and j == 0 else 4

    print()
    for x in b:
    	for y in x:
    		print(y if y >= 0 else 0, end = " ")
    	print()

def task_16_4():
    n = int(input())
    routes = [[]]
     
    for i in range(n - 1):
        routes.append([int(j) for j in input().split()])
     
    station = input().split()
    A, B = int(station[0]), int(station[1])
     
    profit = routes[max(A, B)][min(A, B)]
    change = -1
     
    for i in range(n):
        if (i != A and i != B):
            if (profit > routes[max(A, i)][min(A, i)] + routes[max(i, B)][min(i, B)]):
                profit = routes[max(i, B)][min(i, B)] + routes[max(i, B)][min(i, B)]
                change = i
    
    print()            
    if (change != -1):
        print(change)
    else:
        print(A)


def task_17_1():
    dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
       'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
       'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
       'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 
       'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh',
       'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
       'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
     
    str = input()
    result = ""
     
    len_str = len(str)
    for i in range(0,len_str):
        result += (dic[str[i]] if (str[i] in dic) else str[i])
     
    print(result)

def task_17_2():
    book = {}
    for _ in range(int(input())):
        val, key = input().split()
        if key in book:
            book [key].append(val)
        else:
            book [key] = [val]

    key_list = []
    for _ in range(int(input())):
        key_list.append(input())

    print()
    for key in key_list:
        if key in book:
            print(*book [key])
        else:
            print('Нет в телефонной книге')

def task_17_3():
    book = {}
    for _ in range(int(input())):
        name, val, key = input().split()
        if key in book:
            book [key].append(name + ' ' + val)
        else:
            book [key] = [name + ' ' + val]
    
    key_list = []
    for _ in range(int(input())):
        key_list.append(input())

    print()
    for key in key_list:
        if key in book:
            print(*book [key], end = "\n\n")

def task_17_4():
    n = int(input())
    str = input()
    time = 0

    public,like = str.split(' опубликовал пост, количество просмотров: ')
    d = {public:[int(like),'root',time]}

    for i in range(1,n):
        str = input()
        time += 1
        if ' отрепостил пост у ' in str:
            repost,str = str.split(' отрепостил пост у ')
     
            if ', количество просмотров: ' in str:
                autor,like = str.split(', количество просмотров: ')
                like = int(like)
                d[repost] = [like,autor,time]
                while autor != 'root':
                    d[autor][0] += like
                    autor = d[autor][1]
        elif 'количество просмотров: ' in str:
            str,like = str.split('количество просмотров: ')
            d[public][0] += int(like)
    
    print()
    for j in sorted(d,key = lambda y: d[y][2]):
        print(d[j][0])

def task_17_5():
    allowed = []
    requests = []
    result = []
     
    for i in range(int(input())):
        allowed.append(input())

    for i in range(int(input())):
        requests.append(input())

    allowed_dir = [x.split('/')[1:] for x in allowed]
    req_dir = [x.split('/')[1:] for x in requests]
     
    for i in req_dir:
        for j in allowed_dir:
            if len(i) < len(j):
                continue
            elif (j == i[:len(j)]):
                result.append("YES")
                break
            else:
                result.append("NO")
                break

    print()
    print(*result, sep="\n")     
     

def main():
#    task_9_1()
#    task_9_2()
#    task_9_3()
#    task_9_4()
#    task_9_5()

#    task_10_1()
#    task_10_2()
#    task_10_3()
#    task_10_4()
#    task_10_5()
#    task_10_6()

#    task_11_1()
#    task_11_2()
#    task_11_3()
#    task_11_4()
#    task_11_5()

#    task_12_1()
#    task_12_2()
#    task_12_3()
#    task_12_4()
#    task_12_5()
#    task_12_6()
#    task_12_7()

#    task_13_1()
#    task_13_2()
#    task_13_3()
#    task_13_4()
#    task_13_5()
#    task_13_6()
#    task_13_7()

#    task_14_1()
#    task_14_2()
#    task_14_3()
#    task_14_4()
#    task_14_5()

#    task_15_1()
#    task_15_2()
#    task_15_3()
#    task_15_4()
#    task_15_5()

#    task_16_1()
#    task_16_2()
#    task_16_3()
#    task_16_4()

#    task_17_1()
#    task_17_2()
#    task_17_3()
#    task_17_4()
#    task_17_5()

main()

