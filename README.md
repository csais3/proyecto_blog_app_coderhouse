# proyecto_blog_app_coderhouse
Proyecto final de Python Framework Django de la plataforma CoderHouse 

## Aplicacion de blog web.
Este proyecto fue diseñado para que los usuarios puedan hacer un blog en linea con articulos de temas de su preferencia.
Puedes hacer lo siguiente:

## Si no estas registrado:
Leer Posts.

## Si estas registrado:
Crear, leer, actualizar y eliminar posts.
Subir imagen para su post para un mejor diseño.

## Para instalar este software necesitas:

En la consola del desarrollador posicionarte en la carpeta del software y correr los siguientes comandos para instalar todas las librerias necesarias y la version de Python que fue utilizada al igual que la version de Django.

 Comando: "pip install -r requirements.txt" si cuentas con la version de Python 2
 O
 Comando: "pip3 install -r requirements.txt" si cuentas con la version de Python 3

Es necesario tener instalado Python para poder correr estos comandos.

Esto descargara e instalará una lista de archivos en tu computadora.

# Configurando la aplicacion de Django.

Una vez que hayas terminado de instalar todas las dependencias para este proyecto es necesario correr los siguientes comandos en la misma terminal.

Para migrar la base de datos necesaria:
Comando: "python mananage.py makemigrations blog_app"

Migramos la base de datos:
Comando: "python mananage.py migrate"
> python mananage.py migrate

En windows usamos el comando:

c:\> py mananage.py migrate

Para correr el servidor de prueba utilizamos el siguiente comando en la consola:
Comando: "python mananage.py runserver"
windows:

Verificar si funciona el servidor de prueba ve a:
localhost:8000/ o 127.0.0.1:8000/

Si todo a sido configurado correctamente deberas ver la aplicacion corriendo correctamente en 
127.0.0.1:8000/ o localhost:8000/
