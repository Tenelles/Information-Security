---
# Front matter
lang: ru-RU
title: "Лабораторная работа № 8"
subtitle: "Элементы криптографии. Шифрование (кодирование) различных исходных текстов одним ключом"
author: "Сухарев Кирилл"

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Цель работы

Освоить на практике применение режима однократного гаммирования на примере кодирования различных исходных текстов одним ключом.

# Генерация ключа

    import random
    import string
    
    def generate_key(length):
      return ''.join(random.choice(string.ascii_letters + string.digits)
          for _ in range(length))

# Шифрование

    def single_gamming(message, key):
      return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

# Проверка работоспособности

![](images/report/img1.png){ #fig:001 width=100% }

# Листинг программы

## Листинг программы, ч. 1

    import random
    import string

    def generate_key(length):
      return ''.join(random.choice(string.ascii_letters + string.digits) \
                    for _ in range(length))

    def single_gamming(message, key):
      return ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

## Листинг программы, ч. 2

    visible = "You are at home!"
    hidden = "What a nice day!"
    key = generate_key(25)
    encrypted1 = single_gamming(visible, key)
    encrypted2 = single_gamming(hidden, key)
    prediction = single_gamming(single_gamming(encrypted1, encrypted2), visible)
    print(hidden)
    print(prediction)