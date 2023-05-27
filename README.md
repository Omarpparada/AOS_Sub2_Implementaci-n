# **_AOS_Sub2_Implementación [GRUPO 7]_**

_EQUIPO 7:_

- Álvaro Alonso Devesa - a.adevesa@alumnos.upm.es
- Omar Piñeiro Parada - omar.pparada@alumnos.upm.es
- Alberto Guardiola Churiaque - alberto.guardiola.churiaque@alumnos.upm.es
- Javier Rodriguez de Trujillo - j.rodriguezdetrujillo@alumnos.upm.es

### Creación de la imágen para el servicio

Para la creación del servicio se ha obtado por el lenguaje de programación Python y la libreria FastAPI subido a el siguiente enlace [https://hub.docker.com/r/omarpp/aos_vehiculos] 
a la siguiente el cuál se conecta a una base de datos de MariaDB.

Para la utilización de la imágens, solamente es necesario encontrarse en la carpeta del proyecto y ejecutar el siguiente comando:<br>
`docker-compose up`<br> o el comando: `docker-compose up -d` si se desea ejecutar en segundo plano*.

### **_Docker compose_**
Tras el análisis del resto de servicios se concluyen las siguientes decisiones de diseño de cara al despliegue con `docker-compose`. Debido a que practicamente ningun grupo ha especificado el lugar donde se ha subido la imagen en docker hub, hemos creado un mock del swagger de los grupos e incluirlos en el docker-compose usando puertos distintos.

Para el serivio que se quiere implementar, como hemos mencionado anteriormente, se ha usado una base de datos basada en MariaDB, conectandose al puerto 3306 con 4 vehículos de ejemplo, para mantener la persistencia, la base de datos se monta sobre la carpeta `./docker`. Además, en caso de que sea la primera que se ejecuta el `docker-compose up`, la base de datos realizará los comandos situados en `./pytyhon/scripts/dump.sql`.

Para el servicio de vehículos, se opta por el uso del lengiuaje de programación Python y la libreria FastAPI, usando como puerto interno el 8001 pero connectando al puerto `8000` de `127.0.0.1`** usando uvicorn, la api y los recursos utilizados por este contenedor se encuentran en la carpeta `./pyton` así como  un archivo `requierements.txt` para la instalación de las dependencias.

<br><br>**_*NOTA:_** En el caso de que sea la primera vez que se levanta el contenedor, el timpo de espera será mayor debido a la cración de la base de datos. Este tiempo no es apreciado en el caso de que el contenedor se levante en segundo plano. Por lo tanto, para que funcione correctamente será necesario esperar unos segundos adicionales.<br>

<br>**_**NOTA:_** Para ejecutar el enlace correspondiente para usar el servicio, el enlace hay que usar la ip `127.0.0.1`, en caso contrario puede producirse un _error de CORS_.<br>
