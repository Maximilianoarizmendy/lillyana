# Bitacora extraida de: 17-03-2026.docx

activamos el entorno

C:\Users\AdminSena\Downloads\clasemartes\Django\inventario_django>env\Scripts\activate

entramos a la carpeta indicada para iniciar el servidor 

(env) C:\Users\AdminSena\Downloads\clasemartes\Django\inventario_django\dcrm>python manage.py runserver

https://meet.google.com/bwa-aoba-tsy

primer paso 

vamos a la carpeta website y creamos el archivo urls.py

intervenimos los archivo  urls.py y views.py

comando para refrescar

resultado

creamos la carpeta templates y  el home.html

home.html

https://getbootstrap.com/docs/5.0/getting-started/introduction/

<!doctype html>

<html lang="en">

  <head>

    <!-- Required meta tags -->

    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>

  </head>

  <body>

    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

    <!--

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    -->

  </body>

</html>

configuramos  views.py la pagina que vamos a ejecutar

error de importaciones colocamos asi el codigo 

1. SPA (Single Page Application)

Es una aplicación de una sola página. Carga un único archivo HTML inicial y, a medida que el usuario navega, solo actualiza las partes necesarias de la interfaz mediante JavaScript, sin recargar el navegador por completo. 

YouTube +2

Experiencia: Muy fluida, similar a una aplicación de escritorio o móvil.

Velocidad: La carga inicial puede ser lenta, pero la navegación posterior es casi instantánea.

Ejemplos: Gmail, Google Maps, Facebook, Netflix.

Tecnologías comunes: React, Angular, Vue.js. 

YouTube +7

2. MPA (Multi-Page Application)

Es el modelo tradicional de múltiples páginas. Cada vez que el usuario hace clic en un enlace o interactúa con el servidor, el navegador descarga y recarga una página HTML completa desde cero. 

YouTube +1

Experiencia: Interrupciones visuales debido a las recargas constantes del navegador.

SEO: Es superior para el posicionamiento en buscadores, ya que cada página tiene su propio contenido indexable.

Escalabilidad: Ideal para sitios con catálogos inmensos y mucho contenido estático.

Ejemplos: Amazon, Wikipedia, portales de noticias. 

YouTube +2

🔎 Explicación del diagrama

1️⃣ Cliente

Puede ser:

navegador web


aplicación móvil


otro sistema


Envía solicitudes al sistema.

2️⃣ API Gateway

Es el punto de entrada al sistema.

Funciones:

Recibir solicitudes


Redirigirlas al microservicio correcto


Controlar seguridad y autenticación


3️⃣ Microservicios

Cada servicio maneja una función específica.

Ejemplos:

Servicio Usuarios → gestión de cuentas


Servicio Productos → catálogo


Servicio Pedidos → compras


Cada uno funciona de forma independiente.

4️⃣ Base de datos independiente

Cada servicio tiene su propia base de datos.

Ejemplo:

DB Usuarios


DB Productos


DB Pedidos


Esto evita dependencias entre servicios.

🔄 Flujo de funcionamiento

1 Usuario hace una solicitud

2 API Gateway recibe la solicitud

3 Se envía al microservicio correspondiente

4 El microservicio consulta su base de datos

5 Se envía la respuesta al usuario

📦 Ejemplo real (tienda online)

Microservicios:

Usuarios


Productos


Carrito


Pagos


Envíos


Cada uno funciona como un sistema independiente.

📊 Tipos de códigos de estado HTTP

Los códigos HTTP se dividen en 5 categorías principales.

🟢 1xx – Respuestas informativas

Indican que la solicitud fue recibida y el proceso continúa.

Ejemplo:

100 Continue → El servidor recibió la solicitud inicial y el cliente puede continuar.


🟢 2xx – Respuestas exitosas

Significa que la solicitud se procesó correctamente.

Ejemplos:

200 OK → La solicitud fue exitosa.


201 Created → Se creó un nuevo recurso.


204 No Content → La solicitud fue exitosa pero no hay contenido para devolver.


Ejemplo práctico:

HTTP/1.1 200 OK

🟡 3xx – Redirección

Indican que el cliente debe realizar otra acción para completar la solicitud.

Ejemplos:

301 Moved Permanently → La página se movió permanentemente.


302 Found → Redirección temporal.


304 Not Modified → El recurso no ha cambiado.


Ejemplo:

HTTP/1.1 301 Moved Permanently

🔴 4xx – Error del cliente

Significa que el problema está en la solicitud enviada por el cliente.

Ejemplos:

400 Bad Request → Solicitud incorrecta.


401 Unauthorized → No autorizado.


403 Forbidden → Acceso prohibido.


404 Not Found → Recurso no encontrado.


Ejemplo:

HTTP/1.1 404 Not Found

🔴 5xx – Error del servidor

Significa que el servidor falló al procesar la solicitud.

Ejemplos:

500 Internal Server Error → Error interno del servidor.


502 Bad Gateway → Problema entre servidores.


503 Service Unavailable → Servicio no disponible.


504 Gateway Timeout → Tiempo de espera agotado.

base.html

<!doctype html>

<html lang="en">

  <head>

    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Django CRM</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

  </head>

  <body>

    {% include 'navbar.html' %}

    <div class="container">

        <br/>

            {% block content %}

            {% endblock %}

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>

  </body>

</html>

supervisar errores en el navegador

para refrescar el navegador y cargar cambios seria ctrl+shiff+ r

  o si quiere F5

formatos:

https://github.com/topics/markdown-template

https://github.com/LillianaU/expresiones_regulares/blob/main/pasopasogit.md

creación de repositorio

https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%C3%A1sicos-para-Ramificar-y-Fusionar

Navarra.html

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">

  <div class="container-fluid">

    <a class="navbar-brand" href="{% url 'home' %}">Django CMR</a>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">

      <span class="navbar-toggler-icon"></span>

    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">

      <ul class="navbar-nav me-auto mb-2 mb-lg-0">

        <li class="nav-item">

          <a class="nav-link" href="#">Link</a>

        </li>

      </ul>

    </div>

  </div>

</nav>

quedamos en esta parte por que repasamos subir archivos en git 

el uso kilo

https://github.com/LillianaU/clase_dj_Ficha-3147211.git
