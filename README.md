<div align="justify">
  
# SEMANA_11_RESTAURANTE

# Universidad Estatal Amazonica (UEA)

# Sistema de Gestión de Restaurante - Relaciones, Ventas y Persistencia de Datos en JSON

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

---

## Descripción General del Sistema

Este proyecto es una aplicación desarrollada en Python que permite gestionar productos, usuarios y ventas de un restaurante mediante una interfaz de consola, incorporando el control de stock y las relaciones entre las diferentes entidades del sistema, ademas, la información se almacena de forma permanente mediante archivos JSON, permitiendo conservar los datos después de cerrar la aplicación y recuperarlos nuevamente cuando el sistema se inicia.

---

## Estructura del Proyecto

El sistema se encuentra organizado en módulos para separar las responsabilidades y facilitar la comprensión del código, de manera que la carpeta datos almacena la información persistente, modelos contiene las clases principales, servicios administra la lógica del sistema y el acceso a los archivos JSON, mientras que main.py funciona como punto de entrada y permite al usuario interactuar mediante un menú de consola.

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   ├── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.json
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

Cada componente cumple una función específica, por lo que Producto administra los datos y el stock de los productos, Usuario representa a las personas registradas, mientras que Venta relaciona al usuario con el producto adquirido y la cantidad comprada, por otra parte, Restaurante administra las colecciones y aplica las reglas de negocio, finalmente, Archivo_Servicio se encarga de guardar y cargar la información mediante archivos JSON.

---

## Flujo de Venta

El proceso comienza verificando que el usuario y el producto existan, posteriormente se comprueba que la cantidad solicitada sea mayor que cero y que exista suficiente stock, si todas las condiciones se cumplen, el sistema disminuye el inventario, registra la venta y actualiza los archivos productos. json y ventas. json, mientras que si alguna validacion falla, la operacion es rechazada sin modificar la información almacenada.

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
