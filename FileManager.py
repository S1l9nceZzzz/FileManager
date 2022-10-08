import os
import json
import shutil


class FileManager:
    def __init__(self):

        with open("settings.json", "r") as read_file:
            self.settings = json.load(read_file)

    def help(self):
        print('Command list:\n1) show_dir\n2) open_file\n3) write_file\n4) move_file'+
              '\n5) copy_file\n6) mk_folder\n7) dlt_folder\n8) rnm\n9) rmv_file\n'+
              '10) ch_dir\n11) mk_file\n12) go_back')

    def show_dir(self):
        print('\n'+'\n'.join(os.listdir()))

    def open_file(self):
        try:
            filename = input('>>> Введите имя файла: ')
            assert filename
            with open(filename, 'r') as file:
                text = '\n'.join([row for row in file.readlines()])
                print(text, end='\n')
        except:
            print('>>> Возникла ошибка')

    def write_file(self):
        try:
            filename = input('>>> Введите имя файла в который идет запись: ')
            text = input('>>> Вводимый в файл текст: \n')
            assert filename, text
            with open(filename, 'a') as file:
                file.write(text)
        except:
            print('>>> Возникла ошибка')

    def move_file(self):
        try:
            filename = input('>>> Введите имя передвигаемого файла: ')
            movepath = input('>>> Введите новый путь(абсолютный): ')
            assert filename, movepath
            os.rename(f'{self.settings["root_directory"]}{self.entry_main.get().split("|")[0]}',
                      f'{self.settings["root_directory"]}{self.entry_main.get().split("|")[1]}')
        except:
            print('>>> Возникла ошибка')
        
    def copy_file(self):
        try:
            filename = input('>>> Введите имя копируемого файла: ')
            copypath = input('>>> Введите путь(абсолютный) копирования: ')
            assert filename, movepath
            shutil.copyfile(f'{self.settings["root_directory"]}{filename}', f'{copypath}')
        except:
            print('>>> Возникла ошибка')
            
    def mk_folder(self):
        try:
            foldername = input('>>> Введите имя создаваемой папки: ')
            assert foldername
            os.mkdir(foldername)
            print('>>> Папка создана успешно')
        except:
            print('>>> Возникла ошибка')

    def dlt_folder(self):
        try:
            foldername = input('>>> Введите имя удаляемой папки: ')
            assert foldername
            os.rmdir(foldername)
            print('>>> Папка успешно удалена')
        except:
            print('>>> Возникла ошибка')

    def rnm(self):
        try:
            oldname = input('>>> Введите имя объекта: ')
            newname = input('>>> Введите новое имя: ')
            os.rename(oldname, newname)
            print('>>> Переименование прошло успешно')
        except:
            print('>>> Возникла ошибка')

    def rmv_file(self):
        try:
            filename = input('>>> Введите имя удаляемого файла: ')
            assert filename
            os.remove(filename)
            print('>>> Файл успешно удален')
        except:
            print('>>> Возникла ошибка')

    def ch_dir(self):
        try:
            newpath = input('>>> Введите новый путь: ')
            assert filename
            os.chdir(filename)
            print('>>> Путь изменен')
        except:
            print('>>> Возникла ошибка')

    def go_back(self):
        try:
            assert len(os.getcwd()) > len(settings['root'])
            os.chdir('..')
            print('>>> Сделан шаг назад')
        except:
            print('>>> Возникла ошибка')

    def mk_file(self):
        try:
            filename = input('>>> Введите имя нового файла(без .txt): ')
            assert filename
            with open(f'{filename}.txt', 'w') as file:
                print('>>> Файл создан успешно')
        except:
            print('>>> Возникла ошибка')


if __name__ == "__main__":
    file_manager = FileManager()
    os.chdir(file_manager.settings['root_directory'])
    running = True
    while running:
        inp = input('>>> ')
        if inp.strip() in ['mk_file', 'show_dir', 'open_file', 'write_file', 'move_file',
                           'copy_file', 'mk_folder', 'dlt_folder', 'rnm', 'rmv_file', 'ch_dir', 'go_back']:
            eval(f'file_manager.{inp}()')
