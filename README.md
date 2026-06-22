# 🏋️‍♂️ Tone Trainer - Sistema de Gestión Premium

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

**Tone Trainer** es una plataforma web *SaaS* moderna y de alto rendimiento diseñada para la administración integral de gimnasios. Combina una arquitectura robusta en backend con una experiencia de usuario (UX) inmersiva estilo *Glassmorphism* y navegación de una sola página (SPA).

---

## 🚀 Características Principales

*   **⚡ Navegación Ultrarrápida (SPA):** Transiciones fluidas sin recargar la página gracias a interceptores de peticiones Fetch API.
*   **🎨 Diseño Premium Dark-Mode:** Interfaz moderna con *Glassmorphism*, tarjetas translúcidas, desenfoques de fondo e iconografía SVG vectorial.
*   **🛡️ 4 Capas de Seguridad:**
    1.  *Protección CSRF* en todos los formularios.
    2.  *Control de Acceso Basado en Roles (RBAC)*.
    3.  *Prevención XSS* mediante Auto-Escaping.
    4.  *Inmunidad a Inyecciones SQL* gracias al ORM de Django.
*   **👥 Sistema de Registro Público:** Los clientes pueden crear su propia cuenta desde el Login e integrarse de inmediato a la base de datos del gimnasio.

---

## 🔐 Roles del Sistema

El proyecto maneja un ecosistema de 3 roles estructurados:

1.  👑 **Administrador (`Admin`):** Tiene control total (CRUD) sobre los miembros registrados. Puede crear nuevos clientes, actualizar sus datos personales, gestionar membresías y eliminar registros.
2.  ⚕️ **Nutricionista (`Nutricionista`):** Cuenta con un módulo exclusivo para el *Área de Nutrición*. Puede visualizar la lista de miembros y asignarles Planes Nutricionales (dietas, peso, métricas).
3.  👤 **Usuario / Cliente (`Usuario`):** Acceso restringido y enfocado. Al iniciar sesión, ingresa directamente a su panel personal para visualizar la dieta que le ha sido asignada.

---

## 🏗️ Arquitectura y Patrones de Diseño

*   **MVC (Django MVT):** Separación limpia entre los Datos (Models), Interfaz (Templates) y Lógica de Negocio (Views).
*   **Singleton:** Configuración centralizada e instanciada una sola vez (`settings.py`).
*   **Active Record / Repository:** Manejo de base de datos a través de abstracción (Django ORM).
*   **Factory Method:** Construcción dinámica de inputs HTML a partir de Modelos mediante `forms.ModelForm`.

---

## ⚙️ Instalación y Uso Local

Sigue estos pasos para arrancar el proyecto en tu máquina local:

1.  **Clonar el repositorio**
    ```bash
    git clone https://github.com/Maximilianoarizmendy/lillyana.git
    cd lillyana/lillyana
    ```

2.  **Activar el entorno virtual**
    ```bash
    # En Windows
    venv\Scripts\activate
    ```

3.  **Instalar dependencias** *(Asegúrate de tener Django instalado)*
    ```bash
    pip install django pypandoc pypandoc-binary
    ```

4.  **Aplicar migraciones**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Poblar la base de datos (Opcional)**
    ```bash
    python seed.py
    ```

6.  **Correr el servidor**
    ```bash
    python manage.py runserver
    ```
    Visita `http://127.0.0.1:8000/` en tu navegador.

---

## 👨‍💻 Credenciales por Defecto (Script `seed.py`)

Si corriste el script de poblado, puedes usar los siguientes usuarios de prueba:

*   **Admin:** `admin` | Clave: `admin123`
*   **Nutricionista:** `nutricionista` | Clave: `nutri123`

---
*Desarrollado con pasión para llevar la gestión deportiva al siguiente nivel.* 🏋️‍♀️🔥
