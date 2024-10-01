def merge_files(file_list, output_file):
    # Содержание файлов и их количество строк
    file_data = []

    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_data.append((filename, line_count, lines))

    # Сортируем по количеству строк
    file_data.sort(key=lambda x: x[1])

    # Записываем в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename, line_count, lines in file_data:
            outfile.write(f"{filename}\n{line_count}\n")  # Имя файла и количество строк
            outfile.writelines(lines)  # Сами строки файла

# Задайте список файлов и имя выходного файла
files_to_merge = ['1.txt', '2.txt', '3.txt']  # Здесь разместите ваши файлы
output_filename = 'merge.txt'  # Имя выходного файла

# Вызов функции с указанием файлов и имени выходного файла
merge_files(files_to_merge, output_filename)
