# Sistema de Control de Inventario

## Descripción

Este proyecto fue desarrollado como parte del Parcial 2 de la materia **Programación I** de la **Tecnicatura Universitaria en Programación a Distancia**.

El sistema permite gestionar el inventario de una ferretería mediante una interfaz de consola, controlando herramientas disponibles y sus cantidades en stock.

La aplicación fue desarrollada utilizando únicamente listas, diccionarios, funciones, estructuras condicionales y repetitivas, respetando las restricciones establecidas en la consigna del parcial.

---

# Funcionalidades

## 1. Carga Inicial de Herramientas

Permite registrar múltiples herramientas junto con su stock inicial.

Validaciones:

* No permite nombres vacíos.
* No permite herramientas duplicadas.
* No permite cantidades negativas.
* Solo puede ejecutarse si el inventario está vacío.

---

## 2. Mostrar Inventario

Muestra todas las herramientas registradas junto con la cantidad disponible de cada una.

Ejemplo:

```text
1. Martillo | Cantidad: 10
2. Taladro | Cantidad: 5
3. Destornillador | Cantidad: 0
```

---

## 3. Consultar Stock

Permite buscar una herramienta por nombre e informar la cantidad disponible.

La búsqueda ignora:

* Mayúsculas y minúsculas.
* Espacios al inicio y al final.

Ejemplos válidos:

```text
Martillo
martillo
 MARTILLO
```

---

## 4. Reporte de Herramientas Agotadas

Muestra únicamente las herramientas cuyo stock es igual a cero.

---

## 5. Alta de Nuevo Producto

Permite agregar una nueva herramienta al inventario.

Validaciones:

* Nombre obligatorio.
* No permite duplicados.
* No permite cantidades negativas.

---

## 6. Actualización de Stock

Permite modificar el stock de una herramienta existente mediante dos operaciones:

### Venta

Disminuye la cantidad disponible.

Validaciones:

* No permite vender más unidades de las disponibles.
* No permite cantidades negativas o iguales a cero.

### Ingreso

Aumenta la cantidad disponible por reposición de mercadería.

Validaciones:

* Solo acepta cantidades enteras mayores a cero.

---

## 7. Salir

Finaliza la ejecución del programa.

---

# Estructura de Datos

El sistema utiliza una única lista denominada:

```python
inventario = []
```

Cada herramienta se almacena como un diccionario con la siguiente estructura:

```python
{
    "herramienta": "Martillo",
    "cantidad": 10
}
```

---

# Estructura del Proyecto

```
parcial2.py
README.md
```

---

# Funciones Principales

| Función               | Descripción                      |
| --------------------- | -------------------------------- |
| mostrar_menu()        | Muestra las opciones disponibles |
| cargar_herramientas() | Realiza la carga inicial         |
| mostrar_inventario()  | Muestra el inventario completo   |
| buscar_herramienta()  | Busca una herramienta por nombre |
| consultar_stock()     | Consulta el stock disponible     |
| reporte_agotados()    | Lista herramientas agotadas      |
| alta_producto()       | Agrega una nueva herramienta     |
| actualizar_stock()    | Gestiona ventas e ingresos       |
| main()                | Controla el flujo principal      |

---

# Manejo de Errores

El sistema utiliza:

```python
try:
except:
```

para controlar errores de entrada y validaciones de negocio.

Entre las validaciones implementadas se encuentran:

* Nombres vacíos.
* Herramientas duplicadas.
* Cantidades negativas.
* Opciones inválidas.
* Stock insuficiente para ventas.
* Búsquedas de herramientas inexistentes.

---

# Tecnologías Utilizadas

* Python 3
* Visual Studio Code

---

# Autor

Isabella Yanes

Tecnicatura Universitaria en Programación a Distancia

Programación I – Parcial 2

Año 2026