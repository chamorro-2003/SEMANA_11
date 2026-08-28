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

Cada componente del proyecto cumple una función determinada para evitar mezclar responsabilidades y facilitar el mantenimiento del sistema, por lo tanto, la clase **Producto** representa los artículos disponibles en el restaurante y administra información como su identificación, nombre, precio, categoría y cantidad disponible en stock, mientras que **Usuario** representa a las personas registradas y permite identificar a quienes realizan las compras, por otra parte, **Venta** relaciona un usuario con un producto y una cantidad adquirida, mientras que **Restaurante** administra las colecciones y aplica las reglas necesarias para realizar las diferentes operaciones del sistema.

---

## Flujo de Venta

El proceso comienza verificando que el usuario y el producto existan, posteriormente se comprueba que la cantidad solicitada sea mayor que cero y que exista suficiente stock, si todas las condiciones se cumplen, el sistema disminuye el inventario, registra la venta y actualiza los archivos productos. json y ventas. json, mientras que si alguna validacion falla, la operacion es rechazada sin modificar la información almacenada.

---

## Persistencia y Pruebas

La informacion se mantiene mediante tres archivos JSON, donde productos.ison almacena el catálogo y stock, usuarios.ison conserva los usuarios registrados y ventas.json mantiene el historial de compras, para comprobar su funcionamiento se realizaron ventas exitosas, intentos de compra con stock insuficiente y consultas del historial, verificando que los cambios se conservaran correctamente después de reiniciar la aplicación.

---

## Reflexión Final

La incorporación de relaciones entre entidades, control de inventario y persistencia en **JSON** permite que el sistema se aproxime cada vez más al funcionamiento de una aplicación real, ya que ahora no solamente se administran productos y usuarios, sino que también es posible relacionarlos mediante las ventas realizadas y conservar esta información después de cerrar el programa, además, la separación de responsabilidades facilita la comprensión del código y permite realizar cambios de manera más segura, fortaleciendo así el aprendizaje de **Programación Orientada a Objetos** y proporcionando una estructura preparada para incorporar nuevas funcionalidades en futuras versiones.

<div>
