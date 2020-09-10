# [OpenSchool](https://nvkot.ru/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/master/LICENSE)

OpenSchool is a school framework for building user interfaces.

### License

OpenSchool is [MIT licensed](./LICENSE).

<h2>Author: Kot Nikolay Valerievich</h2><br>
<h3>Email: nik14201@yandex.ru, nvkot.ru@yandex.ru</h3><br>
<h3>telegram:@nik14201<h3><br>
<h4>site: https://nvkot.ru, https://school.ru</h4><br>

#Описание проекта
OpenSchool - проект онлайн школы для дистанционного обучения
В условиях пандемии все ощутили плюсы и минусы дистанционного образования.  
Безусловно очное образование необходимо и никуда не денется, но все мы видим,  
что в условиях эпидемии, даже простого гриппа зимой, многие школы уходят на каникулы на 2-3 недели,  
когда они могли бы продолжать образование дистанционно со своими учителями.
Опыт удаленной работы с централизованными сервисами показал, что данное решение не может быть гибким, не может подстроиться под конкретную школу коллектив учителей и детей, кому-то интерфейс может быть не понятен, он может раздражать, тормозить и при высоких нагрузках сервис может падать.
Для преодоления этих проблем мною была начата разработка и предложено децентрализованное решение с открытым исходным кодом, которое может быть легко адаптировано под конкретную школу под конкретных учителей и учеников.  
https://vk.com/openschool26  
Распространяется по MIT лицензии https://github.com/wildleek-ru/OpenSchool  
telegram:@nik14201  
skype: nik14201  
MIT license https://github.com/wildleek-ru/OpenSchool
OpenSchool is an open source online school project. This can be done on the server.
The project is different:  
1. For communication between schools, a decentralized or peer-to-peer network based on the equal rights of participants will be used. There are no dedicated servers in this network, and each individual school server will be a client in order to perform server functions.  
2. Used the advanced technologies django-rest-framework on the backend and Vue - Nuxt on the frontend.  
3. Well thought-out architecture of the project and code. Simplified parts to one or two models on each application.  
4. The project is divided into separate parts for the student, teacher and parent.  
5. Thought out the architecture of the entire system.  
OpenSchool проект онлайн школы чтобы любая школа могла его скачать и развернуть у себя на сервере.  
Проект отличается:  
1. Для связи между школами будет использована децентрализованная, или иначе пиринговая сеть основанная на равноправии участников. В этой сети отсутствуют выделенные серверы, а каждый отдельный школьный сервер будет является как клиентом, так и выполнять функции сервера.  
2. Использованием передовых технологий django-rest-framework на backend и Vue - Nuxt на frontend.  
3. Продуманной архитектурой проекта и кода. Упрощены отдельные части до одной-две модели на каждое приложение.  
4. Проект разделен на отдельные части для ученика, учителя и родителя.  
5. Продумана архитектура всей системы.  

В схеме можно выделить следующие логические связи:  
1. Школа -> город -> область, район или край  
2. Школа <- директор или завуч  
3. Ученик  
3.1 Ученик <- дневник  
3.2 Ученик -> класс  
4. Учитель  
4.1 Учитель <- дневник  
4.2 Учитель <- предмет  
5. Дневник  
5.1 Дневник -> домашнее задание -> урок  
5.2 Дневник -> Учитель  
5.3 Дневник -> Ученик  
6. Урок  
6.1 Урок -> предмет  
6.2 Урок -> класс  
6.3 Урок -> тема урока  

#Установка и настройка 
##Копирование на сервер с помощью zip архива
###Находясь в корневом каталоге проекта мы видим:
..  
.git/  
opt/  
README.md  
LICENSE Лицензия  
.gitignore для git игнорирования файлов  
deploy.sh  выполняется при автодеплое на сервере   
cleargit.sh  пример если нужно удалить случайно попавший большой файл  
bitbucket-pipelines.yml файл для автодеплоя в bitbucket.org  

####Находясь в корне проекта для архивирования выполним   
```zip -r school_from_server.zip ./ ```  
####Скопировать на сервер  
```scp school_from_server.zip username@xxx.xxx.xxx.xxx:/home/username/www/```  
предварительно создав в /home/username/ директрию  www  командой  
```mkdir www```

#Войти на сервер по ssh   
```ssh username@xxx.xxx.xxx.xxx```  
перейти в каталог  
```/home/username/www```   
и распаковать zip архив командой:  
```unzip school_from_server.zip```

#Подготовка сервера
Установить docker  
```sudo apt install docker.io  docker-compose``` 
####Добавить пользователя сервера username в группу docker
```sudo usermod -a -G docker username```  


##Для docker-compose.yml версия
```version: '3.3'```  
##Если нужно будет поднять версию до    
```version: '3.7'```  
##Тогда
Не всегда docker-compose в системе нужной версии, поэтому, чтобы  не мучиться с установкой  
нужной версии в системе можно docker-compose поставить в виртуальное окружение и потом запускать через него
Установить virtualenv  
```sudo apt install virtualenv```  
Создать виртуальное окружение командой  
```cd /home/username/```   
```virtualenv -p python3 .virt```  
Активировать виртуальное окружение  
```source .virt/bin/activate```  
Установить docker-compose последней версии  
```pip install docker-compose``` 

#Иначе 
Находясь в корневом каталоге приложения 
```/home/username/www/```  
перейти в каталог  
```opt/```
##Структура каталога opt/
..  
database/  Тут база данных postgres   
media/     Медиафайлы django  
statics/   Статика  
www/       Остальные файлы приложения  

##Перейти в каталог www/ 
```cd www```
## Структура каталога www/
backend/    Бекенд приложения  
frontend/   Приложения фронтенда  
config/     Конфиги nginx  
robot/      Для поисковика robot.txt
#####docker/   Файлы docker отсюда производится запуск

##Перейти в каталог docker  
```cd docker```
##Запустить скрипт сборки контейнеров
```sudo chmod a+x build.sh```
```./build.sh```

#####Если база уже есть и была скопирована с zip архивом, то приложение должно запуститься
#####Если базы небыло то она создалась с нуля и нужно выполнять миграции и создавать суперпользователя

```./makemigrations.sh```  
```./migrate.sh```  
```./createsuperuser```
###И дальше по обстоятельствам  

#Настройка nginx  
Установка nginx если он не установлен  
```sudo apt install nginx```  

Файлы nginx находятся в каталогах
./opt/www/config/local  Тут конфиги nginx для локальной разработки
./opt/www/config/server Тут конфиги nginx для сервера

Настроить ./opt/www/config/server/admin.local
```
server {
server_name dme.ubikiri.com;
set $django_host http://172.35.0.8:8080;
include /home/username/www/opt/www/config/server/settings.conf;
}
```

Создать символическую ссылку в nginx  
```sudo ln -s /home/username/www/opt/www/config/server/nginx.conf /etc/nginx/sites-enabled/school.local```   
Проверить настройки nginx
```nginx -t```
Перезапустить nginx
```sudo service nginx restart```
