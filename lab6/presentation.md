---
## Front matter
lang: ru-RU
title: "Лабораторная работа № 6"
subtitle: "Мандатное разграничение прав в Linux"
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

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux. Проверить работу SELinx на практике совместно с веб-сервером Apache.

# Запуск веб-сервера

![](images/report/img2.png){ #fig:001 width=100% }

# Статистика SELinux

![](images/report/img5.png){ #fig:002 width=100% }

# Проверка доступа к файлу через браузер

![](images/report/img11.png){ #fig:003 width=100% }

# Изменение контекста безопасности файла

![](images/report/img13.png){ #fig:004 width=100% }

# Повторная проверка доступа к файлу через браузер

![](images/report/img14.png){ #fig:005 width=100% }

# Список доступных httpd портов

![](images/report/img19.png){ #fig:006 width=100% }

# Повторная проверка доступа к файлу браузером через 81-ый порт

![](images/report/img21.png){ #fig:007 width=100% }