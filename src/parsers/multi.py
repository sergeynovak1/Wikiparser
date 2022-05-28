from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from wiki_parser import wiki_parser


def multi(mode, url, base_path, max_workers=5, deep=3):
    "функция вызова парралельного парсинга от заданного mode"
    start_with = wiki_parser(url, base_path)
    for _ in range(deep - 2):
        ex = mode(max_workers=max_workers) #запускаем executor от заданного режима
        end_with = []
        futures = [ex.submit(wiki_parser, url, base_path) for url in start_with] #запускаем параллельно
        for i in futures:
            end_with.append(i.result())
        start_with = end_with
        ex.shutdown() #завершение путём закрытия


if __name__ == "__main__":
    multi(ThreadPoolExecutor, 'https://en.wikipedia.org/wiki/Vladimir_Putin', r'C:\Users\novak\OneDrive\Рабочий стол\Новая папка (2)\Новая папка\Thread', 4)
    multi(ProcessPoolExecutor, 'https://ru.wikipedia.org/wiki/USA', r'C:\Users\novak\OneDrive\Рабочий стол\Новая папка (2)\Новая папка\Process')