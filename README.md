# HomeWork

## Русский язык
Скрипт, отправляющий домашнее задание в беседу ВКонтакте

### Установка
* Установите Python 3.8  
* pip install -r `путь/к/корневой/папке/requirements.txt`  
* Загрузите файл `homework (send to google drive).py` и `timetables (send to google drive).py` на ваш Google Диск (удалив скобочки и их содержимое из имени файла), предварительно вписав в него нужные значения.  
* Получите ID этого файла (Обязательно открыть доступ по ссылке).  
* Впишите нужные значения в файл `timetables.py` (Папка `timetables`).  
* Перейдите на сайт `https://vkhost.github.io/`, выберите Kate Mobile, разрешите доступ и скопируйте из адресной строки всё, после `access_token=` и до `&expires_in`.  
* Откройте vk.com и перейдите в нужную беседу, затем скопируйте число после sel=c  
* Открываем файл `main.py` и редактируем Options  

### Запуск (Windows)
* Запустите launch.bat

### Запуск (Linux)
* Запустите launch.sh

### Обновление информации
Файл с домашним заданием (`homework.py`) и расписанием (`timetables.py`) обновляется вами посредством Text Editor в Google Drive и синхронизируется автоматически.

### Баги  
* Проблемы с отображением дня в конце месяцев (30 - 31)

## English
A script that sends homework to a VKontakte conversation

### Installation
* Install Python 3.8  
* pip install -r `path/to/root/folder/requirements.txt`  
* Upload the `homework (send to google drive).py` and `timetables (send to google drive).py` files to your Google Drive (by removing the parentheses and their contents from the file name), after entering the desired values into it.  
* Get the ID of this file (Be sure to share the link).  
five). Enter the desired values in the `timetables.py` file (the `timetables` folder).  
* Go to `https://vkhost.github.io/`, select Kate Mobile, allow access and copy everything from the address bar, after `access_token=` and before `&expires_in`.  
* Open vk.com and go to the desired conversation, then copy the number after `sel=c`  
* Open `main.py` file and edit Options  

### Startup (Windows)
* Just run `launch.bat`

### Launch (Linux)
* Just run `launch.sh`

### Updating information
The file with homework (`homework.py`) and timetable (`timetables.py`) is updated by you through the Text Editor in Google Drive and automatically synchronized.

### Bugs
* Problems displaying the day at the end of months (30 - 31)
