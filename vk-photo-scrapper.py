#!/usr/bin/env python
import requests
import os.path


def get_file(filename):
    return open(filename)


def get_links(f):
    links = []
    for line in f:
        if (found := line.find('https://')) != -1:
            links.append(line[found:])
    total = len(links)
    print(f'Скрипт нашёл {total} фотографий в файле.')
    return links


def open_links(links):
    for link_index in range(len(links)):
        try:
            if os.path.exists(f'{link_index}.jpg'):
                continue
            f = open(f'{link_index}.jpg', "wb")
            ufr = requests.get(links[link_index])
            f.write(ufr.content)
            f.close()
        except:
            print('Сайт/ссылка недоступна.')
    print('Все файлы выведены.')
    return True


def main():
    return open_links(get_links(get_file(input('Введите имя файла: '))))


if __name__ == '__main__':
    main()
