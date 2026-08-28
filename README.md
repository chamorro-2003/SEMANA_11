<div align="justify">
  
# SEMANA_11_RESTAURANTE

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Relaciones, Ventas y Persistencia de Datos en JSON

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto es una aplicación desarrollada en Python que permite gestionar
productos, usuarios y ventas de un restaurante mediante una interfaz de consola,
incorporando el control de stock y las relaciones entre las diferentes entidades del
sistema, ademas, la información se almacena de forma permanente mediante
archivos JSON, permitiendo conservar los datos después de cerrar la aplicación y
recuperarlos nuevamente cuando el sistema se inicia

---

## Estructura del Proyecto

Para mantener una organización adecuada, el sistema se encuentra dividido en módulos que cumplen diferentes responsabilidades, de manera que la carpeta datos almacena la información de forma , la carpeta modelos contiene las clases que representan las entidades del sistema y la carpeta servicios administra tanto el acceso al archivo **JSON** como las operaciones relacionadas con los productos, mientras que el archivo **main.py** funciona como punto de entrada y coordina la interacción entre el usuario y los diferentes componentes de la aplicación.

```text
restaurante_app/
├── datos/
│   ├── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

---
## Componentes Técnicos Aplicados
---

## Responsabilidad de las Clases y Módulos

Cada componente del proyecto cumple una función específica para mantener el código organizado y facilitar su mantenimiento, por lo tanto, la clase **Producto** representa la información y las validaciones de cada producto, además de permitir convertir sus datos a un formato compatible con **JSON**, mientras que Usuario representa a los usuarios administradores durante la ejecución del programa, por otra parte, **Archivo_Servicio** se encarga de leer y guardar la información en el archivo **JSON**, Restaurante administra los productos en memoria y realiza las operaciones **CRUD**, finalmente, **main.py** controla el menú y la interacción con el usuario.

---

## Persistencia de Datos mediante JSON

La principal incorporación de esta versión es la posibilidad de conservar los productos después de cerrar el programa, para ello, la información se almacena en el archivo **datos/productos.json**, utilizando las funciones **json. load()** para leer los datos y **json.dump()** para guardarlos, de esta manera, cuando la aplicación inicia, los registros almacenados son recuperados y convertidos nuevamente en objetos de la clase **Producto**, mientras que después de registrar, actualizar o eliminar información, los cambios realizados se guardan nuevamente en el archivo para mantener los datos actualizados.

---

## Flujo de Carga y Guardado

El proceso comienza cuando el usuario ejecuta **main.py**, luego el sistema solicita a **ArchivoServicio** que cargue la información almacenada en **productos.json** posteriormente, los datos obtenidos mediante **json.load()** son revisados y utilizados para reconstruir los objetos **Producto**, los cuales son enviados al servicio **Restaurante** para trabajar con ellos en memoria. Después, cuando el usuario realiza una operación de registro, actualización o eliminación y esta se completa correctamente, el sistema convierte nuevamente los objetos a diccionarios mediante **a_diccionario()** y finalmente guarda la información actualizada utilizando **json.dump()**.

---

## Manejo de Excepciones

Para evitar que errores inesperados interrumpan el funcionamiento del sistema, se implementan diferentes excepciones según el problema que pueda presentarse, de modo que **FileNotFoundError** permite iniciar el programa con una lista vacía cuando el archivo todavía no existe, mientras que **JSONDecodeError** controla archivos **JSON** dañados o con una estructura incorrecta, asimismo, **PermissionError** permite controlar problemas relacionados con los permisos de lectura o escritura, **KeyError** identifica información faltante al reconstruir un producto y **ValueError** permite controlar datos que no cumplen las reglas establecidas, como precios o identificadores inválidos.

---

## Verificación de la Persistencia

Para comprobar que el sistema conserva correctamente la información, se realizó una prueba en la que primero se ejecuto **main.py** y posteriormente se registraron
dos productos mediante el menú, después se verificó que el archivo **datos/productos.json** almacenara los registros y se cerró completamente la aplicación. Luego, se volvió a ejecutar el sistema y se comprobó mediante la opción de listado que los productos continuaban disponibles, finalmente, se eliminó uno de ellos, se reinicio nuevamente la aplicación y se verifico que el cambio también permaneciera guardado en el archivo, demostrando así que la persistencia funciona correctamente.

---

## Reflexión Final

La incorporación de la persistencia de datos permite comprender la importancia de almacenar la información de manera permanente dentro de una aplicación, ya que anteriormente los datos podían mantenerse únicamente durante la ejecución del programa, mientras que mediante **JSON** es posible conservarlos y recuperarlos posteriormente. Además, separar la gestión de archivos en **Archivo_Servicio** permite mantener una estructura organizada y evita mezclar la lógica de almacenamiento con las reglas del restaurante, logrando así un sistema más claro, mantenible y preparado para incorporar nuevas funcionalidades en futuras versiones.

<div>
