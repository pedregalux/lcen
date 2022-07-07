
# La Constitución es Nuestra

## Guía de instalación y desarrollo

<a href="https://ciudadaniai.org/index"><img src="https://gitlab.com/pedregalux/images2021/-/raw/master/logofci.png" width="150"></a>
<a href="https://laconstitucionesnuestra.cl/"><img src="https://gitlab.com/pedregalux/images2021/-/raw/master/lcen.jpg" width="150"></a>

La Constitución es Nuestra es un proyecto de Ciudadanía Inteligente, The Global Initiative y Constitu+yo.

## Objetivos del proyecto
- Ser una plataforma para la creación de propuestas para la nueva constitución
- Entregar información sobre l*s integrantes de la Convención Constituyente
- Difundir información sobre el proceso constituyente

El objetivo de esta guía es documentar los pasos necesarios para la instalación y la modificación del código del proyecto para otras necesidades.

## Componentes del proyecto

LCeN es la suma de varios componentes principales:

- [Django](https://www.djangoproject.com) - El framework de aplicaciones web
- [Python](https://www.python.org) - Lenguaje de programación que utiliza Django
- [MySQL-MariaDB](https://mariadb.org) - Base de datos -se puede utilizar otra!-
- [NGINX](https://nginx.org/en/) - Servidor web utilizado -se puede reemplazar por otro!-
- [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) - Software que permite la comunicación entre la aplicación y el servidor web

La instalación de Python, MySQL, nginx y wsgi en un servidor para hacer correr el proyecto **no** se cubre en esta guía, sin embargo acá hay una lista de tutoriales muy buenos que pueden servir:

- [Django-MySQL](https://www.delftstack.com/es/howto/django/django-mysqldb/)
- [Django-NGINX-uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
- [Django-Apache](https://tomdeneire.medium.com/how-to-deploy-a-django-applications-on-linode-ubuntu-20-04-lts-9235150bad3e)
- [NGINX](https://www.linode.com/docs/guides/how-to-configure-nginx/)
- [Django-uwsgi](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/uwsgi/)



## Instalación

Clone el proyecto desde la última versión de desarrollo en Github. Esta está en [este repositorio](https://github.com/pedregalux/lcen). Existen dos ramas principales, dev y master, para desarrollo y producción respectivamente.

```sh
git clone https://github.com/pedregalux/lcen
```

Le recomendamos usar virtualenv, un paquete de python para crear un [entorno virtual de desarrollo](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) local para este proyecto, así no afectará otras instalaciones de python y django que pueda tener en su servidor o máquina local. Si ya tiene instalados python3 y viartualenv, el comando para crear el ambiente de trabajo debería ser:
```sh
python3 -m venv /ruta/entorno/virtual
```
Luego se activa con:
```sh
source bin/activate
```

Aplicaciones de django requeridas:

1. Obviamente Django:
```sh
pip install django
```

2. mysqlclient para conectar la aplicación con la base de datos creada en MySQL o MariaDB:
```sh
pip install mysqlclient
```

3. pillow da a python soporte para trabajar con imágenes:
```sh
pip install pillow
```

4. python-decouple para separar en un archivo .env las contraseñas e información sensible:
```sh
pip install python-decouple
```

5. django-formtools para usar formularios separados en pasos:
```sh
pip install django-formtools
```

6. crispy-bootstrap5 integra los estilos de bootstrap 5 a los formularios:
```sh
pip install crispy-bootstrap5
```

7. django-allauth es la aplicación para que usuarios de google y facebook -u otras- puedan usar sus credenciales en la plataforma:
```sh
pip install django-allauth
```

8. django-extensions instala utilidades varias que sirven para el desarrollo:
```sh
pip install django-extensions
```

9. django-filter para usar algunos buscadores:
```sh
pip install django-filter
```

10. django-import-export para exportar usuarios, propuestas, etc.:
```sh
pip install django-import-export
```

## Creación de base de datos

Cree una base de datos MySQL, MariaDB o Postgresql, la que prefiera. Guarde su nombre, usuario y contraseña.

## Configuración de partida

Para mantener ordenado el proyecto, las contraseñas se guardan en un archivo .env local que es independiente del código, para eso debe crear un archivo .env en la raíz del proyecto, la carpeta lcen.

En ese archivo debe incluir la siguiente información:

<code>SECRET_KEY=xxxxxxx  (cualquier contraseña que quiera, bien larga)</code>

<code>DEBUG=True  (en producción se debe cambiar a False)</code>

<code>ALLOWED_HOSTS=  ()</code>

<code>DB_NAME=lcen2021  ()</code>

<code>DB_USER=root  ()</code>

<code>DB_PASSWORD=chanaral  ()</code>

<code>DB_HOST=localhost  ()</code>

<code>STATIC_URL='/static/'  ()</code>

<code>STATIC_ROOT=/home/felipe/lcen/static/  ()</code>

<code>STATICFILES_DIRS=/home/felipe/lcen/lcen/static  ()</code>

<code>MEDIA_ROOT=/home/felipe/lcen/lcen/media/  ()</code>

<code>MEDIA_URL='/media/'  ()</code>

## Repositorios FCI

Todo el código utilizado está [público](https://github.com/ciudadanointeligente/lcen) on GitHub.

Todo el código utilizado está [público](https://gitlab.com/ciudadaniai/lcen) on Gitlab.




## Licencia

[Licencia](https://www.gnu.org/licenses/gpl-3.0.txt)

**Paz y Software Libre!**
