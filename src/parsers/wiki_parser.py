"""Module for parsing wiki"""

import os
import re
import requests
import uuid
from bs4 import BeautifulSoup

from src.maps.hash_map import HashMap


def wiki_parser(url: str, base_path: str) -> list[str]:
    """parsing wiki"""
    def found_url():
        for elem in os.listdir(base_path):  # прохожусь по директориям
            with open(os.path.join(base_path, elem, "url.txt"), "r", encoding="utf-8") as file_url:
                if file_url.read() == url:
                    with open(os.path.join(base_path, elem, "content.bin"), "rb") as file:
                        byte = file.read()
                        return get_valid_url(byte)
        return url_is_not_found()

    def url_is_not_found():
        "создание папки и запись туда url"
        dirname = uuid.uuid4().hex
        path = os.path.join(base_path, dirname)
        os.mkdir(path)
        with open(os.path.join(path, 'url.txt'), 'w', encoding="utf-8") as file:
            file.write(url)  # записываю в папку url
        return write_content(path)

    def write_content(path):
        "запись байт кода"
        if os.path.exists(path):
            byte = requests.request("GET", url).content
            with open(os.path.join(path, "content.bin"), "wb") as file:
                file.write(byte)
            get_valid_url(byte)
            get_text(path)

    def get_text(path):
        "получение текста из байт кода"
        if not os.path.exists(os.path.join(path, "content.bin")):
            while True:
                if os.path.exists(os.path.join(path, "content.bin")):
                    break
        with open(os.path.join(path, "content.bin"), "rb") as file:
            soup = BeautifulSoup(file, "lxml")
            hash_map = HashMap()
            for string in soup.stripped_strings:
                for word in re.findall(r'\w+', string):
                    if word is None:
                        continue
                    try:
                        hash_map[word] += 1
                    except KeyError:
                        hash_map[word] = 1
        write_to_file(os.path.join(path, "words.txt"), sorted(hash_map, key=lambda x: x[0]))

    def write_to_file(path, mapa):
        "запись MAp в файл"
        with open(path, "w", encoding="utf-8") as file:
            for i in mapa:
                file.write(f"{i[0]}\t{i[1]}\n")

    def get_valid_url(byte):
        "получение валидных ссылок"
        txt = byte.decode("UTF-8")
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', txt)  # ищем все ссылки
        filtered_urls = filter(lambda url: url.startswith('/wiki/'),
                               urls)  # отсортировываем те, которые начинаются с wiki
        corrected_urls = map(lambda url: "https://ru.wikipedia.org" + url, filtered_urls)  # формируем ссылку
        return list(corrected_urls)

    return found_url()


#wiki_parser('https://ru.wikipedia.org/wiki/Random', r'C:\Users\novak\OneDrive\Рабочий стол\Новая папка (2)\Новая папка\Thread')
#wiki_parser('https://ru.wikipedia.org/wiki/Moscow', r'C:\Users\novak\OneDrive\Рабочий стол\Новая папка (2)\Новая папка')
#wiki_parser('https://ru.wikipedia.org/wiki/Russia', r'C:\Users\novak\OneDrive\Рабочий стол\Новая папка (2)\Новая папка')


