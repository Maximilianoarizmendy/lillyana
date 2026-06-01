# Bitacora extraida de: Bitácora 24-03-2026.docx

Bitácora 24-03-2026

Configuración de bootstrap nativo servidor local 

En 

Importamos 

import os # type: ignore

Estructura de carpetas

Configuramos lo que esta en amarillo

Ahora configurar las urls

Atajos 

https://docs-emmet-io.translate.goog/cheat-sheet/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

https://coderslink.com/talento/blog/ahorra-tiempo-al-escribir-codigo-html-en-visual-studio-code-utilizando-emmet/

atajos

body.bg-info.bg-opcity-25>div.container.py-5>div.row.justify-content-center>div.col-md-8>div.card.shadow>div.card-body>h3.text-center.md-4{Contrato}+form>div.row>div.col-md-6.mb-3>label.form-label{Ingrese sus datos}+input.form-control+div.col-md-6.mb-3>label.form-label{login}+input.form-control+div.col-md-6.mb-3>label.form-label{clave}+textarea.form-control+button.btn.btn-primary.w-100{Guardar}

formulario que voy a utilizar

{% extends 'base.html' %} {%block content%}

<div class="container py-5">

  <div class="row justify-content-center">

    <div class="col-md-8">

      <div class="card shadow">

        <div class="card-body">

          <h3 class="text-center md-4">Contrato</h3>

          <form>

            <div class="mb-3">

              <label for="exampleInputEmail1" class="form-label"

                >Usuario</label

              >

              <input

                type="email"

                class="form-control"

                id="exampleInputEmail1"

                aria-describedby="emailHelp"

              />

              <div id="emailHelp" class="form-text">

                We'll never share your email with anyone else.

              </div>

            </div>

            <div class="mb-3">

              <label for="exampleInputPassword1" class="form-label"

                >Password</label

              >

              <input

                type="password"

                class="form-control"

                id="exampleInputPassword1"

              />

            </div>

            <button type="submit" class="btn btn-primary">Submit</button>

          </form>

        </div>

      </div>

    </div>

  </div>

</div>

{% endblock %}

quedaria asi :

{% extends 'base.html' %} {%block content%}

<div class="container py-5">

    {%if user.is_authenticated%}<!-- primero condicionamos-->

  <div class="row justify-content-center">

    <div class="col-md-8">

      <div class="card shadow">

        <div class="card-body">

          <h3 class="text-center md-4">Bienvenidos a este CRM 👩🏻‍🤝‍🧑🏻</h3>

          {%else%}<!-- colocmanos un sino-->

          <h1 class="text-center md-4">Ingrese al Sistema  👩🏻‍🤝</h1><!-- colocmanos h1-->

          <form method="POST" action="{% url 'home'%}"><!-- configuracion de form-->

            {% csrf_token %}<!-- token para login se a correcto validar-->

            <div class="mb-3">

              <label for="exampleInputEmail1" class="form-label"

                >Usuario</label

              >

              <input

                type="email"

                class="form-control"

                id="exampleInputEmail1"

                aria-describedby="emailHelp"

              />

              <div id="emailHelp" class="form-text">

                We'll never share your email with anyone else.

              </div>

            </div>

            <div class="mb-3">

              <label for="exampleInputPassword1" class="form-label"

                >Password</label

              >

              <input

                type="password"

                class="form-control"

                id="exampleInputPassword1"

              />

            </div>

            <button type="submit" class="btn btn-primary">Submit</button>

          </form>

        </div>

      </div>

    </div>

  </div>

</div>

{%endif%}<!---->

{% endblock %}

seria el resultado 

home.html

congiguracion de los campos las variables que usara views

{% extends 'base.html' %} {%block content%}

<div class="container py-5">

    {%if user.is_authenticated%}<!-- primero condicionamos-->

  <div class="row justify-content-center">

    <div class="col-md-8">

      <div class="card shadow">

        <div class="card-body">

          <h3 class="text-center md-4">Bienvenidos a este CRM 👩🏻‍🤝‍🧑🏻</h3>

          {%else%}<!-- colocmanos un sino-->

          <h1 class="text-center md-4">Ingrese al Sistema  👩🏻‍🤝</h1><!-- colocmanos h1-->

          <form method="POST" action="{% url 'home'%}"><!-- configuracion de form-->

            {% csrf_token %}<!-- token para login se a correcto validar-->

            <div class="mb-3">

              <label for="form-control" class="form-label"

                >Usuario</label

              >

              <input

                type="text"

                class="form-control"

                name="username" placerholder="Username" required/>

                </div>

            <div class="mb-3">

              <label for="exampleInputPassword1" class="form-label" >Password</label >

              <input type="password" class="form-control" name="password" placerholder="Password" required/>

            </div>

            <button type="submit" class="btn btn-primary">Login</button>

          </form>

        </div>

      </div>

    </div>

  </div>

</div>

{%endif%}<!---->

{% endblock %}

Views 

# Importa la función render, que permite combinar una plantilla HTML con datos y devolver una respuesta HTTP.

from django.shortcuts import render, redirect

# Importa el modelo User de Django, que representa a los usuarios en la base de datos.

# Importa funciones para autenticación de usuarios:

# - authenticate: verifica credenciales.

# - login: inicia sesión.

# - logout: cierra sesión.

from django.contrib.auth import authenticate, login, logout

# Importa el sistema de mensajes de Django para mostrar notificaciones al usuario.

from django.contrib import messages

# Aquí se deben crear las vistas de la aplicación.

# Esta función define la vista principal (home) del sitio.

def home(request):

    # Renderiza la plantilla 'home.html' y la retorna como respuesta HTTP.

    # No se pasan datos adicionales al contexto (diccionario vacío).

    if request.method == 'POST':

        # Si el método de la solicitud es POST, significa que se está enviando un formulario.

        # Aquí puedes manejar la lógica del formulario, como la autenticación de usuarios.

        username = request.POST['username'] # Obtiene el nombre de usuario del formulario.

        # Obtiene la contraseña del formulario.

        password = request.POST['password']

        # Authenticate

        user = authenticate(request, username=username, password=password)# Verifica las credenciales del usuario.

        # Si el usuario es autenticado correctamente, se inicia sesión.

        if user is not None: # Si el usuario es autenticado correctamente.

            login(request, user)# Inicia sesión.

            # Muestra un mensaje de éxito al usuario.

            messages.success(request, "You Have Been Logged In!")# # Muestra un mensaje de éxito al usuario.

            return redirect('home')

        else:

            # Si las credenciales son incorrectas, se muestra un mensaje de error.

            messages.error(request, "Invalid Credentials!")

            # Muestra un mensaje de error al usuario.

            return redirect('home')

    else:

        # Si el método de la solicitud no es POST, simplemente renderiza la plantilla 'home.html'.

        return render(request, 'home.html', {})

# Esta función define la vista de inicio de sesión (login) del sitio.

def login_user(request):

    pass

def logout_user(request):

    pass

Home 

{% extends 'base.html' %} {% block content %}

<div class="col-md-6 offset-md-3">

   {% if user.is_authenticated %} 

    <h1 class="text-center">👋Welcome 👋</h1>

   {% else %} 

  <h1 class="text-center">🔐Ingresar al sistemas 👤</h1>

  <form method="POST" action="{% url 'home' %}">

   {% csrf_token %}

<br/>

    <div class="mb-3">

      <input type="text" class="form-control" name="username" placeholder="Username" required>

    </div>

   <br/>

    <div class="mb-3">

       <input type="password" class="form-control" name="password" placeholder="Password" required />

    </div>

    <button type="submit" class="btn btn-secondary">login</button>

  </form>

</div>

{% endif %}

{% endblock %}
