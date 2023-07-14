![ejemplo](https://github.com/chifu504/E-comerse-django/blob/master/ejemplo2.png)
# Proyecto de E-commerce con Django

Este proyecto es un E-commerce desarrollado utilizando el framework Django. Proporciona una plataforma completa para la creación de una tienda en línea, donde los usuarios pueden explorar, buscar y comprar productos. El proyecto está diseñado para ser flexible y personalizable, permitiendo a los propietarios de tiendas adaptarla a sus necesidades específicas

## Tecnologías
- Django
- HTML/CSS
- JavaScript
- Celery
- RabbitMQ
- PostgreSQL
- Redis
- Docker
- WSGI
- NGINX
## Características principales

- Catálogo de productos: Permite a los usuarios ver una amplia variedad de productos con detalles como imágenes, descripciones, precios, etc.
- Búsqueda y filtrado: Facilita a los usuarios encontrar productos específicos mediante la búsqueda y el uso de filtros por categorías, precios, etc.
- Carrito de compras: Permite a los usuarios agregar productos al carrito de compras, ajustar las cantidades y finalizar la compra.
- Proceso de pago: Integración de una pasarela de pagos (Stripe) para realizar transacciones seguras y un sistema de cupones para aplicar descuentos en las compras.
- Generación de facturas PDF: Genera facturas de las compras realizadas dinámicamente en formato PDF para su descarga e impresión.
- Registro de usuarios: Implementación de funciones de registro de usuarios con autenticación normal y autenticación social.
- Administración del sitio: Panel de administración que facilita la gestión de productos, pedidos, clientes, acciones personalizadas y exportación de pedidos a archivos CSV.
- Tareas asincrónicas: Uso de Celery y RabbitMQ para tareas asincrónicas, como el envío de correos de confirmación de pedidos y envío de facturas en PDF.
- Base de datos PostgreSQL: Configuración y gestión de una base de datos PostgreSQL para almacenar los datos del proyecto.
- Sistema de recomendación: Implementación de un sistema de recomendación personalizado utilizando Redis.
- Funcionalidades adicionales: Desarrollo de características adicionales, lista de favoritos,likes,comentarios etc.
- Entorno Docker: Uso de Docker para entornos de desarrollo y despliegue eficientes.
- Optimización del rendimiento: Configuración y optimización del rendimiento de Django con WSGI y NGINX.
- Medidas de seguridad: Implementación de medidas de seguridad, incluyendo autenticación de usuarios, protección contra ataques CSRF, protección de URL, configuración de certificado SSL, etc.


## Instalación y configuración del proyecto E-commerce
### Requisitos

- Docker  instalado en tu sistema puedes descargarlo en https://www.docker.com/products/docker-desktop/.

Sigue estos pasos para configurar el proyecto E-commerce en tu entorno local:

1. Clona el repositorio del proyecto:

2. Accede a la carpeta del proyecto:

3. Ejecuta el siguiente comando para iniciar los contenedores de Docker:

   ```shell
   docker-compose up -d
   ```

   Esto creará y ejecutará los contenedores de Docker necesarios para el proyecto.

4. Una vez que los contenedores estén en ejecución, ejecuta las migraciones de la base de datos:

   ```shell
   docker-compose exec web python manage.py migrate
   ```

   Esto aplicará las migraciones y creará las tablas necesarias en la base de datos.

5. Crea una cuenta de administrador utilizando el siguiente comando:

   ```shell
   docker-compose exec web python manage.py createsuperuser
   ```

   Sigue las instrucciones en la consola para ingresar un nombre de usuario, dirección de correo electrónico y contraseña para el administrador.


### agregar funcionalidades de tu proyecto:

### Prueba de funcionalidades con Stripe
Para poder probar todas las funcionalidades relacionadas con pagos y webhooks de Stripe, es necesario seguir los siguientes pasos:

1. Crea una cuenta en Stripe en [stripe.com](https://stripe.com) si aún no tienes una.
2. Obtén las claves pública y privada de tu cuenta de Stripe.
3. Abre el archivo `settings.py` y busca las variables `STRIPE_PUBLISHABLE_KEY` y `STRIPE_SECRET_KEY`. Reemplaza los valores de estas variables con tus claves correspondientes.

Para probar los webhooks de Stripe de manera local, sigue estos pasos adicionales:

1. Descarga el ejecutable de Stripe CLI desde [aquí](https://github.com/stripe/stripe-cli/releases/tag/v1.14.7).
2. Ejecuta el archivo descargado desde tu terminal o línea de comandos en la ruta deseada.
3. Ejecuta el siguiente comando en la ruta de Stripe CLI para configurar y redireccionar los webhooks a tu entorno local:
   ```
   stripe listen --forward-to https://localhost/payment/webhook/ --skip-verify
   ```

### Uso de la API de correos de Google
Si deseas utilizar la API de correos de Google en tu proyecto, sigue estos pasos:

1. Genera una contraseña de aplicación para tu cuenta de Google. Asegúrate de tener la verificación en dos pasos activada en tu cuenta.
2. Abre el archivo `settings.py` y busca las variables `EMAIL_HOST_USER` y `EMAIL_HOST_PASSWORD`. Reemplaza los valores de estas variables con tu correo y contraseña de aplicación respectivamente.

### Uso de autenticación con Google
Si deseas utilizar la autenticación con Google en tu proyecto, sigue estos pasos:

1. Obtén un Google Client ID y Google Client Secret desde la API de Google.
2. Abre el archivo `settings.py` y busca las variables `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY` y `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET`. Reemplaza los valores de estas variables con tu Google Client ID y Google Client Secret respectivamente.

Recuerda seguir estos pasos para poder probar todas las funcionalidades correctamente y asegurarte de tener todas las configuraciones necesarias en tu proyecto.



¡Listo! Ahora has configurado el proyecto Biblioteca en tu entorno local. Puedes acceder a él en tu navegador y comenzar a utilizarlo.
Abre tu navegador web e ingresa la siguiente URL: https://localhost/



