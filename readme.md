Сейчас добавлена работа с Telegram, по аналогии можно добавлять другие мессенджеры и площадки.

0. Создать бота в телеграм через Bot Father

Для локального запуска
1. Загрузить и установить ngrok, поместить в корень проекта ngrok
2. Запустить локальный туннель ngrok
./ngrok http 80
3. Заполнить файл variables.override.env своими переменными, где token - токен полученный от Bot Father, FQDN - полученный https от ngrok
4. Локально запустить, проверить своего бота
sudo docker-compose -f docker-compose.override.yml up --build



Для развертывания на ВМ
1. Добавить ssh ключ для управления ВМ
2. Установить Docker на ВМ
3. На локальной машине установить Docker и Docker Machine
4. Добавить docker-machine для управения удаленным хостом Docker
sudo docker-machine create --driver generic --generic-ip-address={your_ip_address} --generic-ssh-key ~/.ssh/id_rsa vm_name
sudo -s
eval $(docker-machine env vm_name)
4. Заполнить файл variables нужными переменными
5. Развернуть бота:
sudo docker-compose -f docker-compose.yml up -d --build

При перезагрузке ВМ, сервис бота будет автоматически восстановлен.