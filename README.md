# BlackGamesorderbot
Проект нового бота на базе aiogram3

##  Описание проекта
Бот для заказа услуг, отправки и оплаты через счёт-фактуру.

### Функциональность:
1) Выбор всего спектра услуг поэтапно
2) Отображение стоимости во время выбора
3) Генерация счёта на оплату
4) Отправка счёта с qr-кодом на оплату по реквизитам

### Расширенный список функций
1) Список услуг
2) Список заказов
3) Выставление счета
4) Отслеживание заказа
5) Хранение заказов и их статусов
6) Отправка новых заказов администратору.
7) Кодификатор номера заказов
8) Изменение статуса заказа через администратора
9) Отмена заказа со стороны пользователя
10) Отправка сообщения о смене статуса заказа/его отмене.
11) Генератор счета на услуги
12) Система промокодов

### Кодификатор номера заказов
1) Регион - 44
2) Город(Н.П.) - 0
3) Дата - YYYY:MM:DD
4) Тип клиента - YL
5) Тип заказа - ST
6) Подтип заказа - WPS
7) Номер заказа - 1

Регион - Стандартный номера регионов

Город - Номера городов из таблицы. {ссылка}

Дата - текущая дата в формате YYYY:MM:DD

Тип клиента:
    1) YL - Юридическое лицо
    2) FL - Физическое лицо
    3) YLP - Юридическое лицо постоянный клиент
    4) FLP - Физическое лицо постоянный клиент

Тип заказа:
    1) ST - сайт
        a) WPS - Wordpress
        b) BS - Bitrix Site
        c) OC - OpenCart
        d) DW - Drupal
        e) PR - Prestashop
        f) MS - Moodle
    2) PSI - Проектировка сетевой инфраструктуры
    3) BTG - Бот телеграмм
    4) BDS - Бот дискорд
    5) NI - Настройка инфраструктуры
    6) CK - Написание курсов

Номер заказ в системе за этот квартал

### Используемые библиотеки
vitualenv
