# Bitacora extraida de: 3_3_2026.docx

actualizacion de phpmyadmin

https://es.pinterest.com/pin/281543712493310/

https://github.com/grantshandy

https://photos.app.goo.gl/2zFzGAdA7cQico5a8

revisar compatibilidad de versiones

Soluciones para actualizar:

1 instalar otro administrador de base de datos

https://www.phpmyadmin.net/downloads/

por favor hacer copia de seguridad de las base de datos del proyecto

"Es fundamental tener en cuenta estas consideraciones sobre la actualización de phpMyAdmin y las versiones de base de datos. Entender estas dependencias nos ayudará a prevenir errores de compatibilidad, especialmente si trabajamos con Laravel 11 o superior, donde la versión de PHP puede entrar en conflicto tanto con el servidor como con las herramientas de frontend.

Por su parte, Django es más directo: su principal punto de fricción suele ser exclusivamente la versión de MariaDB/MySQL. Les recomiendo verificar siempre estas versiones, ya sea que desarrollen de forma local o en otros entornos, para asegurar una instalación limpia y evitar errores de migración o incompatibilidad desde el inicio del proyecto."

<?php

/**

 * Configuración básica de phpMyAdmin

 */

$i = 0;

$i++;

/* Tipo de autenticación */

$cfg['Servers'][$i]['auth_type'] = 'config'; // Usa 'config' para entrar directo o 'cookie' para pedir login

$cfg['Servers'][$i]['host'] = 'localhost';

$cfg['Servers'][$i]['compress'] = false;

$cfg['Servers'][$i]['AllowNoPassword'] = true; // <--- ESTA ES LA LÍNEA CLAVE

/* Configuración del usuario (ajusta si no usas root) */

$cfg['Servers'][$i]['user'] = 'root';

$cfg['Servers'][$i]['password'] = ''; // Deja vacío si el usuario no tiene contraseña

/* Directorios de almacenamiento temporal (opcional pero recomendado) */

$cfg['UploadDir'] = '';

$cfg['SaveDir'] = '';

/**

 * Frase de seguridad (blowfish_secret)

 * Debes poner una cadena larga y aleatoria de al menos 32 caracteres.

 */

$cfg['blowfish_secret'] = 'una_cadena_aleatoria_de_32_caracteres_o_mas'; 

?>

https://meet.google.com/imf-yuqr-erh

cuando tiene problema de puertos aca los puede configurar

https://mariadb.com/docs/platform/post-download/mariadb-server-12.2.2

que cosas las que se ven 

ojo sin clave

C:\Users\AdminSena>mariadb-upgrade -u root -p

si pone problema en  el buscador coloca  servicios

reinicie dando clic derecho

https://www.tutorialspoint.com/postgresql/index.htm

Chicos ya con estas herramientas que aprendimos el día de hoy ya sabemos que ustedes pueden actualizar María bebé pueden utilizar otras herramientas de gestión y con la última que les mostré podemos estar administrando Hey ya gemelito no lo diferencia uno es barbado y se baña el otro no el muchacho no fuera de charlas vamos a hablar sobre los entornos virtuales los entornos virtuales me parece fantástico Andy joango porque podemos ahí colocar las versiones de conectores de base de datos compatibles con el diyango y compatibles con el lenguaje de programación que estemos utilizando en ese momento al igual que las diferentes librerías que podemos utilizar por ejemplo las de generación de Excel de PDF si vamos a estar utilizando analítica de datos en nuestro proyecto entre otros Me parece muy chévere porque simula lo que es como un contenedor lo que hace un contenedor muchachos es estabilizar las versiones de los lenguajes de programación de nuestro proyecto un docker ojo que les voy a decir esto cuando empiecen aduquerizar un docker no es para almacenar información que eso es lo que pasa que ustedes instala el motor de base de datos en el docker y pretenden almacenar información no muchachos el toker es un contenedor que lo único que hace es establecer y establece estandarizar las versiones de lo que de las herramientas que usted está utilizando también es funcional para establecer en cada contenedor lo que pertenece al proyecto si lo estás haciendo con arquitectura Limpia por ejemplo si hace microservicios cada contenido representa un micro servicio si usted lo está haciendo con otra arquitectura diferente entonces uno lo está haciendo como él lo visto controlado entonces uno es para el modelo el otro son para los controladores y el otro contenedor es para vistas Entonces de esa manera se trabaja bien lo chévere con con este entorno virtual que les voy a mostrar un video para que pueda quedar más concreto la definición es que en caso de que ustedes les toca estar trabajando con su proyecto se sienta en un equipo donde no tiene instalado esa versión de Django Entonces no vas a generar conflictos porque usted ya tiene esa carpetita ya lista con todo ya preparado o sea que puede cambiar de computador pero si usted tiene que tiene otra versión de Dyango puede ser más viejo más reciente no generar conflictos porque lo que va a estar ejecutando es lo que está dentro de esa carpeta dentro de ese entorno virtual por estar comiendo si me entendieron Bueno entonces 

https://www.youtube.com/watch?v=qD8j5J6wFuw

https://meet.google.com/svo-wzrk-vkf

si no esta intalasa el componente se instala

pip install virtualenv

luego este comando 

diccionario: 

 cd para abrir carpeta ubicarse en ella

cd inventario_django

mkdir para crear carpeta

mkdir inventario_django 

dir es para listar carpeta

crear el entorno virtual 

python -m venv env

activacion: env\Scripts\activate

# Framework principal (Compatible con MariaDB 10.4 de XAMPP)

Django>=5.0,<5.1

# Conector de base de datos

mysqlclient>=2.2.4

# Generación de PDFs

reportlab>=4.0.0

weasyprint>=61.0

# Manejo de variables de entorno (Seguridad)

python-dotenv>=1.0.0

para instalar 

(env) C:\Users\AdminSena\Downloads\clasemartes\Django\inventario_django>pip install -r requirements.txt

pip list  o pip freeze cualquiera de los dos muestra las librerias instaladas

para ver si esta insalatod la librerias

pip show django

https://pip.pypa.io/en/latest/user_guide/

https://docs.djangoproject.com/en/1.8/howto/windows/

:: 1. Instalar Django 5.0 (Compatible con MariaDB 10.4+)

pip install django==5.0

:: 2. Instalar el conector para MySQL/MariaDB

pip install mysqlclient==2.2.4

:: 3. Instalar librerías para PDF

pip install reportlab==4.1.0

pip install weasyprint==61.2

:: 4. Instalar manejo de variables de entorno

pip install python-dotenv==1.0.1
