# AuthUsers
Este microservicio es el encargado de realizar la busqueda del encryptedToken para un internalId dado.

# Autor
Andres Areiza

# Prerrequisitos
Contar con Python 3 instalado en la computadora donde se ejecutara la API.
Descargar las dependencias del proyecto utilizando el siguiente comando (estando ubicado en la carpeta del proyecto):

pip3 install -r requirements.txt

# ¿Como ejecutar la app local?
Ejecutar el siguiente comando:
uvicorn main:app --reload --port=< puerto >
Donde <puerto> debe ser reemplazado por un numero de puerto (Debe ser diferente para cada API para evitar colisiones).

# ¿Como probar la app localmente?
Tenemos dos posibilidades para realizar pruebas con nuestra app:

## Utilizando Swagger
Para esto, simplemente debemos acceder a la ruta /docs de nuestra API en ejecucion y se nos mostrara la pagina de swagger con todos los endpoints listos para probar.

## Accediendo a los endpoints directamente
Podemos acceder directamente al endpoint correspondiende de nuestra API y escribir valores en la URL para hacer nuestras pruebas.

## Con Postman
Para esto, debemos agregar la request con la ruta de nuestra API y enviarle el valor de path necesario:

# ¿Como abrir la app cuando está en ejecución?
Para abrir la app luego de su ejecución, accedemos a la siguiente ruta en el navegador de preferencia:
  
http://localhost:8000
  
Donde <puerto> debe ser reemplazado por el numero de puerto escogido durante el comando de ejecución o 8000 por defecto.
