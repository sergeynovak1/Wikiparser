def read_to_list(path):
    "считываем данные из файла в массив"
    with open(path, "r", encoding="utf-8") as file:
        list1 = [line.split() for line in file.readlines()]
    return list1


def merge_list(list1, list2):
    "сливаем два массива"
    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if int(list1[i][1]) > int(list2[j][1]):
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:]
    res += list2[j:]
    return res


def write_to_file(list1, path):
    "записываем массив в файл"
    with open(path, "w", encoding="utf-8") as file:
        for elem in list1:
            string = elem[0] + '\t' + elem[1] + '\n'
            file.write(string)


def merge(path1, path2, path):
    "сливаем 2 файла"
    list1 = read_to_list(path1)
    list2 = read_to_list(path2)
    list3 = merge_list(list1, list2)
    write_to_file(list3, path)


def merge_multi(paths, path):
    "сливаем список файлов"
    elem1 = paths[0]
    list1 = read_to_list(elem1)
    for elem2 in paths[1:]:
        list2 = read_to_list(elem2)
        list1 = merge_list(list1, list2)
    write_to_file(list1, path)


merge_multi([r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file1.txt', r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file2.txt', r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file.txt'], r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file.txt')