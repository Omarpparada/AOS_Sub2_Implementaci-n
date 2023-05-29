# **_AOS_Sub2_Implementación [GRUPO 7]_**

_EQUIPO 7:_

- Álvaro Alonso Devesa - a.adevesa@alumnos.upm.es
- Omar Piñeiro Parada - omar.pparada@alumnos.upm.es
- Alberto Guardiola Churiaque - alberto.guardiola.churiaque@alumnos.upm.es
- Javier Rodriguez de Trujillo - j.rodriguezdetrujillo@alumnos.upm.es
- Alberto Rey Cristino - alberto.rey.cristino@alumnos.upm.es

### Creación de la imagen para el servicio

Para la creación del servicio se ha optado por el lenguaje de programación Python y la librería FastAPI subido al siguiente enlace [https://hub.docker.com/r/omarpp/aos_vehiculos] 
la cual se conecta a una base de datos MariaDB.

Para la utilización de la imágenes, es necesario encontrarse en la carpeta del proyecto y ejecutar el siguiente comando:<br>
`docker-compose up`<br> o el comando: `docker-compose up -d` si se desea ejecutar en segundo plano*.

### **_Docker compose_**
Tras el análisis del resto de servicios se concluyen las siguientes decisiones de diseño de cara al despliegue con `docker-compose`. Debido a que prácticamente ningún grupo ha especificado el lugar donde se ha subido la imagen en docker hub, hemos creado un mock del swagger de los grupos y los incluímos en el docker-compose usando puertos distintos. El puerto de cada subservicio, excluyendo el 2, sigue el patrón `<:800[Número de subservicio]`

Para el servicio que se quiere implementar, como hemos mencionado anteriormente, se ha usado una base de datos basada en MariaDB, conectándose al puerto 3306 con 4 vehículos de ejemplo. Para mantener la persistencia, la base de datos se monta sobre la carpeta `./docker`. Además, en caso de que sea la primera vez que se ejecuta el `docker-compose up`, la base de datos ejecutará el script sql con ruta: `./scripts/dump.sql`.

Para el servicio de vehículos, se opta por el uso del lenguaje de programación Python y la librería FastAPI, usando como puerto interno el 8001 pero conectando al puerto `8000` de `127.0.0.1`** usando uvicorn, la api y los recursos utilizados por este contenedor, que se encuentran en la carpeta `./python`, así como un archivo `requirements.txt` para la instalación de las dependencias y un `Dockerfile` para construir la imagen del entorno en alpine.

<br><br>**_*NOTA:_** En el caso de que sea la primera vez que se levanta el contenedor, el tiempo de espera será mayor debido a la creación de la base de datos. Este tiempo no es apreciado en el caso de que el contenedor se levante en segundo plano. Por lo tanto, para que funcione correctamente será necesario esperar unos segundos adicionales.<br>

<br>**_**NOTA:_** Para ejecutar el enlace correspondiente para usar el servicio hay que usar la ip **`127.0.0.1:8000/docs`**, en caso contrario puede producirse un _error de CORS_.<br>

### Kubernetes
Para el despliegue de los servicios mediante Kubernetes se ha decidido utilizar las imágenes de las implementaciones de cada subservicio. Se ha intentado seguir dentro de lo posible el siguiente esquema para el despliegue: ![Image text](https://github.com/Omarpparada/AOS_Sub2_Implementaci-n/blob/main/Kubernetes/esquema.png)

Como se puede observar, el servicio Vehiculos que hemos implementado está asociado al `puerto 8002` y los puertos coinciden con el número de cada subservicio. Los puertos de los contenedores se tienen que adaptar a los que utilizan las imágenes empleadas. En nuestro caso, la imagen utiliza el puerto :8001.

Como se puede observar en el esquema, solo hay un subservicio, excluyendo el nuestro, del que se conoce la imagen. Por tanto, el subservicio Notificaciones y Vehiculos son los que se despliegan con el archivo `k8s.yaml`. Si se observa el archivo, se puede apreciar que el resto de servicios han sido comentados debido a la falta de imágenes para desplegarlos (comprobado a fecha de domingo 28 por la tarde). En caso de que las hubieran subido, se hubiera incluido la imagen de cada equipo en el esquema de Deployment y se hubieran ajustado los puertos del servicio y deployment dependiendo de la documentacion de la implementación de cada subservicio. Se asume que cada servicio cuenta con un sistema de persistencia al que se le realizan las peticiones.
Para realizar la práctica hemos usado `Minikube`para simular el entorno con Kubernetes. Lo iniciamos con `minikube start`, y una vez instalado utiliza una imagen de Docker.

Para realizar el despliegue de los servicios en el clúster Kubernetes hay que tener el servicio activo. Una vez arrancado, se utiliza dentro del directorio principal el comando:
```
kubectl apply -f k8s.yaml
```
Una vez ejecutado se despliega en el clúster. Se pueden ver los servicios diponibles con `kubectl get services`. En nuestro caso, para comprobar el despliegue, hemos utilizado el comando:
```
minikube service vehiculos-s 
``` 
Como resultado de este comando, se abre una nueva ventana en el navegador con la dirección IP y puerto en el que se encuentra este servicio, para ver la interfaz solo hay que añadir a la dirección `/docs`, por ejemplo `http://127.0.0.1:62146/docs`. Como resultado aparece una interfaz generada por la imagen omarpp/aos_vehiculos que es la que se genera con el docker-compose en el puerto 8000.

