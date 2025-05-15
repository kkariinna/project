#!/bin/bash

apt update


#apt install tasksel
#tasksel install lamp-server

apt install git
apt install mysql-server mysql-client

apt install sqlite3
sqlite3 --version

apt install net-tools
apt install python3-pip
apt install python3-venv
pip3 install pymysql
pip3 install numpy
pip3 install matplotlib

apt install zip
apt install unzip
apt install vim

#apt-get update && sudo apt-get install yarn
apt install npm
apt install npx
apt install yarn
apt install node

curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
echo ""
echo "npm npx yarn node" 
npm -v
npx -v
yarn -v
node -v


echo ""
echo "Устанавливаем временной  пояс"
rm /etc/localtime
ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime

echo ""
echo "ssh"
#service ssh start
#systemctl status ssh
echo ""


echo ""
echo "ftp"
apt install vsftpd
cp   apache_users/vsftpd.conf /etc/
service vsftpd restart
echo ""

ls -lAF

echo ""
echo ""
echo "Создаем пользователей "
cd apache_users
chmod 755 ./UsersDb_add_del_g01.sh
./UsersDb_add_del_g01.sh
cd ~
echo ""
echo "passwd:g01"
echo ""
ls -lAF



echo ""
echo "Устанваливаем веб-сервер  и открываем порты"
apt install apache2
systemctl stop apache2
cp apache_users/apache2.conf /etc/apache2/
cp apache_users/charset.conf /etc/apache2/conf-enabled/
cp apache_users/ports.conf /etc/apache2/
cp apache_users/.htpasswd /etc/apache2/
ls -lAF /etc/apache2/
cat /etc/apache2/ports.conf

echo "Добавляем  пользователей"
cp  apache_users/g00.conf /etc/apache2/sites-enabled/
cp  apache_users/g01.conf /etc/apache2/sites-enabled/
cp  apache_users/g02.conf /etc/apache2/sites-enabled/
cp  apache_users/g03.conf /etc/apache2/sites-enabled/
cp  apache_users/g04.conf /etc/apache2/sites-enabled/
cp  apache_users/g05.conf /etc/apache2/sites-enabled/
cp  apache_users/g06.conf /etc/apache2/sites-enabled/
cp  apache_users/g07.conf /etc/apache2/sites-enabled/
cat  /etc/apache2/sites-enabled/g00.conf
cat  /etc/apache2/sites-enabled/g01.conf
cat  /etc/apache2/sites-enabled/g02.conf
cat  /etc/apache2/sites-enabled/g03.conf
cat  /etc/apache2/sites-enabled/g04.conf
cat  /etc/apache2/sites-enabled/g05.conf
cat  /etc/apache2/sites-enabled/g05.conf
cat  /etc/apache2/sites-enabled/g07.conf
a2ensite /etc/apache2/sites-enabled/g00.conf
a2ensite /etc/apache2/sites-enabled/g01.conf
a2ensite /etc/apache2/sites-enabled/g02.conf
a2ensite /etc/apache2/sites-enabled/g03.conf
a2ensite /etc/apache2/sites-enabled/g04.conf
a2ensite /etc/apache2/sites-enabled/g05.conf
a2ensite /etc/apache2/sites-enabled/g06.conf
a2ensite /etc/apache2/sites-enabled/g07.conf
a2dissite /etc/apache2/sites-enabled/000-default.conf
echo "Your choices are:"
echo "Which site(s) do you want to disable (wildcards ok)?"
echo "000-default"
a2dissite
echo ""
echo "Разрешаем CGI -скрипты"
a2enmod cgi
a2enmod headers

echo ""  
echo "!!!Azure"  
echo "Azure - Сетевые подключения - Открыть порты: 8001-8005 "  
echo "Проверить  браузером  c своими IP-адресами..."
echo "http://40.85.118.142"
echo "http://127.0.0.1:8001"
echo "http://40.85.118.142:8005"


apt install ufw
ufw disable
ufw allow 21
ufw allow 22
ufw allow 80
ufw allow 3000
ufw allow 8000
ufw allow 8001
ufw allow 8002
ufw allow 8003
ufw allow 8004
ufw allow 8005
ufw allow 8006
ufw allow 8007
ufw allow 8008
ufw allow 8009
ufw enable
ufw disable
ufw status verbose
echo ""
echo "Рестартуем http-сервер"
systemctl restart apache2

echo "Проверить  браузером c своими IP-адресами..."
echo "http://127.0.0.1:8001/cgi-bin/form_new.py"

echo "systemctl stop apache2 - при необходимости"
