#!/bin/bash
apt-get update
apt-get install -y python3 python-dev-is-python3 git gcc make
cd /usr/local
git clone https://github.com/chrisemunt/mg_python.git &&
cd /usr/local/mg_python/src
python3 setup.py install
export YOTTAADR=yottadb
cp -f /home/htmlentry/apache2.conf /etc/apache2
chmod +x /var/www/html
apachectl -DFOREGROUND
