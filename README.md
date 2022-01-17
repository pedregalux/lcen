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

<img src="https://miro.medium.com/fit/c/262/262/2*HiWjbN9GrdV-jsf4vm5_2A.png" width="150">(https://ciudadaniai.org/index)
<img src="https://gitlab.com/pedregalux/images2021/-/raw/master/lcen.jpg" width="150">(https://laconstitucionesnuestra.cl)


La Constitución es Nuestra es un proyecto de Ciudadanía Inteligente, The Global Initiative y Constitu+yo.

## Objetivos del proyecto
- Ser una plataforma para la creación de propuestas para la nueva constitución
- Entregar información sobre l*s integrantes de la Convención Constituyente
- Difundir información sobre el proceso constituyente

El objetivo de esta guía es documentar los pasos necesarios para la instalación y la modificación del código del proyecto para otras necesidades.

## Componentes del proyecto

LCeN es la suma de varios componentes principales:

- [Django] - El framework de aplicaciones web
- [Python] - Lenguaje de programación que utiliza Django
- [MySQL] - Base de datos -se puede utilizar otra!-
- [NGINX] - Servidor web utilizado -se puede reemplazar por otro!-
- [wsgi] - Software que permite la comunicación entre la aplicación y el servidor web

La instalación de Python, MySQL, nginx y wsgi en un servidor para hacer correr el proyecto **no** se cubre en esta guía, sin embargo acá hay una lista de tutoriales muy buenos que pueden servir:

- [Django-MySQL](https://www.delftstack.com/es/howto/django/django-mysqldb/)
- [Django-NGINX-uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
- [Django-Apache](https://tomdeneire.medium.com/how-to-deploy-a-django-applications-on-linode-ubuntu-20-04-lts-9235150bad3e)
- [NGINX](https://www.linode.com/docs/guides/how-to-configure-nginx/)
- [Django-uwsgi](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/uwsgi/)

Todo el código utilizado está [público](https://github.com/ciudadanointeligente/lcen) on GitHub.

Todo el código utilizado está [público](https://gitlab.com/ciudadaniai/lcen) on Gitlab.

## Instalación

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## Licencia



**Paz y Software Libre!**
