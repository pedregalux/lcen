Aplicaciones necesarias para correr el proyecto
-----------------------------------------------

- pip install django

- pip install mysqlclient

- pip install pillow

- pip install python-decouple

- pip install django-formtools

- pip install crispy-bootstrap5

- pip install django-allauth

- pip install django-extensions

- pip install django-filter

- pip install django-import-export



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


## Repositorios FCI

Todo el código utilizado está [público](https://github.com/ciudadanointeligente/lcen) on GitHub.

Todo el código utilizado está [público](https://gitlab.com/ciudadaniai/lcen) on Gitlab.

## Plugins


| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development



#### Building for source



## Docker





```sh
127.0.0.1:8000
```

## Licencia



**Paz y Software Libre!**
