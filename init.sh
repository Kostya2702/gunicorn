sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
