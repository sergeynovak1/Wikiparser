import os


def merge(path1, path2, path):
    "сливаем 2 файла построчно"
    with open(path, "w", encoding="utf-8") as file:
        with open(path1, "r", encoding="utf-8") as file1:
            with open(path2, "r", encoding="utf-8") as file2:
                line1 = file1.readline()
                line2 = file2.readline()
                while True:
                    if line1 == "" and line2 == "":
                        break
                    if line1 == "":
                        while line2 != "":
                            file.write(line2)
                            line2 = file2.readline()
                        break
                    if line2 == "":
                        while line1 != "":
                            file.write(line1)
                            line1 = file1.readline()
                        break
                    if line1.split("\t")[0] < line2.split("\t")[0]:
                        file.write(line1)
                        line1 = file1.readline()
                    elif line1.split("\t")[0] > line2.split("\t")[0]:
                        file.write(line2)
                        line2 = file2.readline()
                    else:
                        eq1 = line1.split("\t")
                        eq2 = line2.split("\t")
                        file.write(eq1[0] + "\t" + str(int(eq1[1]) + int(eq2[1])) + "\n")
                        line1 = file1.readline()
                        line2 = file2.readline()


def non_merge(path1, path):
    "перемещаем файл"
    with open(path, "w", encoding="utf-8") as file:
        with open(path1, "r", encoding="utf-8") as file1:
            line1 = file1.readline()
            while True:
                while line1 != "":
                    file.write(line1)
                    line1 = file1.readline()
                break


def merge_multi(paths, path):
    "сливаем список файлов"
    temp_path = path[:-9]
    del_paths = []
    elem1 = paths[0]
    i = 0
    for elem2 in paths[1:]:
        i += 1
        temp = temp_path + 'file0' + str(i) + '.txt'
        merge(elem1, elem2, temp)
        elem1 = temp
        del_paths.append(temp)
    non_merge(elem1, path)
    for i in del_paths:
        os.remove(i)


merge_multi([r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file1.txt', r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file2.txt', r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file.txt'], r'C:\Users\novak\OneDrive\Рабочий стол\Project\src\merge\file.txt')