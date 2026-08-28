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

## Persistencia y Pruebas

La informacion se mantiene mediante tres archivos JSON, donde productos.ison almacena el catálogo y stock, usuarios.ison conserva los usuarios registrados y ventas.json mantiene el historial de compras, para comprobar su funcionamiento se realizaron ventas exitosas, intentos de compra con stock insuficiente y consultas del historial, verificando que los cambios se conservaran correctamente después de reiniciar la aplicación.

---

## Reflexión Final

La implementación de relaciones, ventas y persistencia permite que el sistema sea más completo y cercano a una situación real, ya que los productos, usuarios y ventas pueden relacionarse y conservar su información de manera permanente, además, la separación de responsabilidades facilita el mantenimiento del código y fortalece la aplicación de los conceptos de Programacion Orientada a Objetos en Python.

<div>
