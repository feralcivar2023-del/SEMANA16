# 🍽️ Restaurante App — Semana 14,15,16
*Nombre:* María Fernanda Alcívar Carrillo
*Materia:* Programación Orientada a Objetos

Este es mi trabajo de la Semana 14. Es una aplicación hecha en Python con Tkinter, siguiendo la estructura que vimos en clase, adaptada al tema de un restaurante.

## ¿Qué hace?
-  Iniciar y cerrar sesión con usuario y contraseña
- *Gestión completa de productos*: Registrar, Ver, Modificar y Eliminar
- Ver la lista de usuarios registrados en el sistema
- Interfaz con menú lateral profesional
-  La pestaña de Ventas está pendiente para la siguiente entrega



## 📂 Cómo están organizados los archivos
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   └── usuarios.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   └── main.py
└── README.md
## Cada parte hace su tarea
- *modelos*: Guarda la información, no lee archivos
- *servicios*: Revisa contraseñas, guarda productos, lee y escribe los JSON
- *ui*: Son las ventanas — solo muestran lo que el servicio les da
- *main.py*: Controla cuándo se ve la pantalla de inicio y cuándo el menú principal

## 🎨 Diseño
- Menú lateral izquierdo con: Productos, Usuarios, Ventas
- Al entrar se muestra directo la lista de productos
- Formulario a la izquierda → tabla con todos los productos a la derecha
- Al hacer clic en un producto de la tabla, se llenan los campos automáticamente
- Botones: Registrar, Actualizar, Eliminar, Limpiar

## 🔑 Para entrar
| Usuario | Contraseña |
|---|---|
| admin | 123456 |
| camarero | restaurante |

## Cómo se usa
1. Abro la carpeta del proyecto
2. Escribo en la terminal: python main.py
3. Inicio sesión con mis datos
4. En *Productos* lleno los campos y doy clic en Registrar
5. Para modificar: elijo un producto de la tabla → cambio los datos → Actualizar
6. Para borrar: elijo el producto → Eliminar → confirmar
7. En *Usuarios* veo quiénes están registrados en el sistema
8. Cierro sesión cuando termino

## Lo que aprendí
- A separar cada parte para que cumpla una sola función
- Que la interfaz no debe tocar los archivos directamente
- A validar que el precio sea un número antes de guardar
- A diseñar con menú lateral sin abrir ventanas nuevas
- Que los datos se quedan guardados aunque cierre el programa

## Nota
La pestaña de Ventas se completará en la siguiente entrega. Todo funciona con archivos JSON locales, no necesita instalar nada extra.
## Propósito de la Semana 16
 
El objetivo principal fue completar la interfaz gráfica con identidad visual y funcionalidades interactivas, integrando todo lo desarrollado en semanas anteriores. Se dio evolución al proyecto agregando recursos gráficos, manejo de eventos, gestión de usuarios por roles y persistencia de datos consolidada, entregando una aplicación profesional, funcional y lista para usar.
 
📈 Evolución respecto al proyecto anterior
 
- Semana 13–14: Estructura base — modelos  Usuario ,  Producto ; servicio de archivos; vista de inicio de sesión y menú principal
​
- Semana 15: Extensión del dominio — modelo  Venta , persistencia en  ventas.json , métodos para registrar y listar ventas
​
- Semana 16: Mejora de interfaz — recursos visuales ( assets ), manejo de eventos con  bind  y  command , gestión de usuarios con distinción de accesos, validaciones y presentación final
## ¿Qué hace esta aplicación?
 
Sistema de gestión para restaurante desarrollado en Python con Tkinter. Permite:
 
- ✅ Iniciar y cerrar sesión con usuario y contraseña
​
- ✅ Visualizar la lista de productos del restaurante
​
- ✅ Registrar y consultar ventas
​
- ✅ Administrar usuarios registrados
​
- ✅ Interfaz gráfica con logotipo, ícono y diseño personalizado
 
## 📂 Estructura del proyecto
restaurante_app/
├── assets/                    # Recursos visuales
│   ├── logo.ico              # Ícono de la ventana
│   └── logotipo.png          # Logotipo de inicio
├── datos/                     
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/                   # Clases de datos
│   ├── _init_.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/                 # Lógica de negocio
│   ├── _init_.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/                        # Interfaz gráfica
│   ├── _init_.py
│   ├── login_view.py
│   └── main_view.py
└── main.py                    # Archivo principal
 
👤 Gestión de usuarios y roles
 
Se implementó el control de acceso según el tipo de usuario:
 
- Administrador: Acceso completo — productos, usuarios, ventas, registrar y eliminar
​
- Usuario estándar: Acceso restringido — puede consultar productos y registrar ventas, sin modificar listas
​
- La distinción se valida desde  RestauranteServicio  al iniciar sesión, y la interfaz muestra u oculta opciones según el perfil.
 
🎧 Eventos,  bind ,  command  y callbacks
 
-  command : Asigna una función directamente al presionar un botón. Ejemplo:
 
 
Ejecuta  _al_registrar()  al hacer clic.
​
-  bind : Asocia eventos del teclado, ratón o foco a funciones. Ejemplo:
 
 
Permite navegar con Enter y mejorar la experiencia de uso.
​
- Callbacks: Son las funciones que se ejecutan cuando ocurre un evento. Se usan para conectar la vista con el servicio sin acoplar el código:  _al_iniciar_sesion ,  _al_cerrar_sesion ,  _al_actualizar_lista  reciben el control desde la interfaz y delegan la lógica al servicio.
 
💾 Persistencia de datos
 
La información se guarda y lee permanentemente en archivos JSON:
 
-  usuarios.json  → credenciales y datos de acceso
​
-  productos.json  → catálogo con id, nombre, precio y descripción
​
-  ventas.json  → registros con id de producto, id de usuario, cantidad y fecha
 
La clase  ArchivoServicio  centraliza las operaciones de lectura y escritura, asegurando que los cambios se mantengan al cerrar y reabrir la aplicación.
 
🚀 Cómo ejecutarla
 
1. Abre la carpeta  restaurante_app  en tu editor
​
2. Ejecuta el archivo:
 python main.py
 3. Ingresa con  usuario y contraseña registrados
 
📝 Notas
 
- Todos los datos se guardan automáticamente en archivos  .json 
​
- Los recursos visuales están en formato  .png  y  .ico