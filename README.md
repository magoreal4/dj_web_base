# dj_web_base

Estructura básica de un proyecto Django para desplegar mediante sockets

## 1. Clonando el repositorio

```$
git clone https://github.com/magoreal4/dj_web_base.git
mv dj_web_base <your project>
```
## 2. Entorno virtual y paquetes

```$
python3.8 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt
```
## 3. Realizar cambios en los archivos

```txt
web_base.com
web_base.socket
web_base.service
```
## 3. Base de datos y archivos estaticos

```$
python ./app/manage.py migrate
python ./app/manage.py collectstatic
```

## 4. Service, socket 

```$
sudo cp web_base.socket /etc/systemd/system/web_base.socket
sudo cp web_base.service /etc/systemd/system/web_base.service
sudo systemctl enable web_base
sudo systemctl start web_base
```

## 5. Nginx

```$
sudo cp web_base.com /etc/nginx/sites-available/web_base.com
sudo ln -s /etc/nginx/sites-available/web_base.com /etc/nginx/sites-enabled/web_base.com
sudo nginx -t
sudo systemctl restart nginx
```

## Oros comandos

```$
python ./app/manage.py runserver 8005
python ./app/manage.py createsuperuser
pip freeze> requirements.txt
python ./app/manage.py collectstatic --no-input --clear
sudo chmod 777 static_volume/
systemctl status nginx
systemctl status web_base

systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
rm /etc/systemd/system/[servicename] # and symlinks that might be related
rm /usr/lib/systemd/system/[servicename] 
rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed
```
