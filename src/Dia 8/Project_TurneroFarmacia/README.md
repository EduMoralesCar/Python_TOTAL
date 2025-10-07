# 🏥 Turnero de Farmacia - Proyecto Día 8

Este proyecto simula el funcionamiento de un sistema de turnos para una farmacia con tres áreas de atención: **Farmacia**, **Perfumería** y **Cosmética**. El objetivo es aplicar conceptos clave de programación en Python para construir un software eficiente, modular y fácil de mantener.

---

## 🎯 Objetivo

Desarrollar un sistema interactivo que:
- Pregunte al cliente a qué área desea dirigirse.
- Genere un número de turno único por área.
- Muestre el turno con un mensaje estandarizado.
- Permita repetir el proceso para múltiples clientes.

---

## 🧠 Tecnologías y conceptos aplicados

| Concepto         | Aplicación en el proyecto                                      |
|------------------|---------------------------------------------------------------|
| Generadores      | Controlan la secuencia de turnos por área sin variables globales. |
| Decoradores      | Añaden un mensaje estándar antes y después del número de turno. |
| Modularización   | Separación del código en dos módulos: `numeros.py` y `principal.py`. |
| Manejo de errores| Validación de opciones ingresadas por el usuario.              |
| Interacción CLI  | Simulación de flujo real con múltiples clientes.               |

---

## 🧩 Estructura del proyecto
```
turnero_farmacia/ 
│
├── numeros.py # Generadores y decorador
├── principal.py # Lógica principal del programa
└── README.md # Documentación del proyecto
```

---

## 📦 Módulo `numeros.py`

Contiene:
- Generadores para cada área (`F`, `P`, `C`).
- Decorador `mensaje_turno` para estandarizar la salida.

Ejemplo de salida:

Su turno es: C-5
Aguarde y será atendido.

---

## 🧠 Módulo `principal.py`

Contiene la lógica de interacción:
- Muestra las áreas disponibles.
- Solicita la elección del cliente.
- Llama a la función correspondiente.
- Pregunta si desea sacar otro turno.

Ejemplo de flujo:

Seleccione el área (1/2/3): 2 
<br>
Su turno es: P-3
<br>
Aguarde y será atendido.
<br>
¿Desea sacar otro turno? (s/n): s

---

## ✅ Justificación técnica

- **Generadores**: permiten mantener el estado interno de cada área sin necesidad de variables externas.
- **Decoradores**: evitan duplicación de código y mejoran la legibilidad.
- **Modularización**: facilita el mantenimiento, testing y escalabilidad del sistema.
- **Interacción dinámica**: simula el comportamiento real de un sistema de turnos.

---

## 🚀 Ejecución

Para iniciar el programa, ejecutar:

```bash
python principal.py
```
