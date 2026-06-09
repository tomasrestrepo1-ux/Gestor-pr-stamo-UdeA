![imagen](https://raw.githubusercontent.com/tomasrestrepo1-ux/Gestor-pr-stamo-UdeA/refs/heads/main/Img/bob%20rico.jpg)

# **Gestor de prestamos🤑🤑**
En este repositorio crearemos un gestor de pretamos para el cliente Michael Gamboa, donde administre a quien le presta y lo que presto. 
# *Integrantes*
## **Tomas Restrepo**
### *Descripcion*
> Soy estudiante de ingenieria industrial de la universidad de Antioquia. Me destaco por mi capacidad de trabajar bajo presion, resolver problemas y por mi buen compañerismo.
## **Juan Paternina**
### *Descripcion*
> Soy estudiante de ingenieria industrial de la universidad de Antioquia. Destaco por mi diciplina, actitud y capacidad de memorizacion.
# *Vision*
> esperamos tener alto aprendizaje con este proyecto, desarrollar una herramienta funcional que cumpla las espectativas de todos.
# *especificaciones*
## *funcionales*
> 1. Registrar usuarios con: su nombre, apellido, documento de identificacion, correo electronico, y tiempo de prestamo definido.
> 2. Registrar productos con: nombre de producto, una categoria, precio de compra, un ID para el producto, y estado en el que se encuentra.
> 3. Registrar prestamos.
> 4. Generar ventas.
> 5. Consultar estado general del prestamo.
> 6. Administrar: total de pretamos realizados, items devueltos, items vendidos, pago realizado, lista de usuarios, usuario con mayor y menor cantidad de prestamos.
## *no funcionales*
> Al administrar, los detalles que pueda ver el cliente sean iguales a los que conoce en la realidad, el nivel de satisfacción de los usuarios sea lo suficientemente elevado para saber si vale la pena el sofware.
# *Plan de Proyecto*
## Actividades del proyecto.
> 1. Requisitos del cliente -> 6 horas
> 2. Diseño del sistema -> 8 horas 
> 3. Desarrollo del sistema -> 20 horas
> 4. Pruebas del sistema -> 6 horas
> 5. Documentación -> 6 horas
> 6. Entrega final -> 4 horas
> *Para un total de 50 horas de trabajo*
## Cronograma
![imagen](https://raw.githubusercontent.com/tomasrestrepo1-ux/Gestor-pr-stamo-UdeA/refs/heads/main/Img/6f3f84cc-bcb5-4eec-ab77-01f86371c5fc.jfif)
## Presupuesto del proyecto 
> el valor de hora se calculara dividiendo un salario minimo (1.750.000) por las 50 horas que dura el trabajo. 1.750.000 / 50 = 35.000
> *Haciendo asi que el valor de cada actividad sea de:*
> 1. Requisitos	->	210.000
> 2. Diseño	->	280.000
> 3. Desarrollo	->	700.000
> 4. Pruebas	 -> 210.000
> 5. Documentación	 -> 210.000
> 6. Entrega final	->	140.000
> 7. Total	->	1.750.000
>## Plan de versiones de "Gestor de prestamos"
# 8. Plan de Versionado

Este plan describe la evolución de las versiones del software y su avance incremental, tomando como base un ciclo de desarrollo de 6 semanas (estimado en 42 días continuos o 30 días hábiles de trabajo). Los días se contabilizan desde el inicio del proyecto (Día 1) hasta la entrega final (Día 42).

---

##  Resumen del Ciclo de Lanzamientos

| Versión | Denominación | Alcance / Hito Clave | Línea del Tiempo (Días) | Avance Estimado |
| :--- | :--- | :--- | :--- | :--- |
| **v0.1.0** | *Alpha Inicial (Base)* | Finalización de Requisitos y Diseño del Sistema | Día 1 al Día 14 | 15% |
| **v0.2.0** | *Alpha Funcional* | Módulo de Gestión de Usuarios e Ítems listo | Día 8 al Día 28 | 45% |
| **v0.5.0** | *Beta Inicial* | Integración de Préstamos y Ventas (Core del negocio) | Día 15 al Día 35 | 80% |
| **v0.9.0** | *Beta Candidate* | Pruebas integrales, corrección de bugs y estabilización | Día 29 al Día 35 | 95% |
| **v1.0.0** | *Release Version* | Documentación finalizada y entrega formal del producto | Día 36 al Día 42 | 100% |

---

##  Detalle por Versiones y Avance Incremental

###  Versión 0.1.0 — Alpha Inicial (Fase de Definición y Arquitectura)
* **Línea del tiempo:** Días 1 a 14 (Semanas 1 y 2)
* **Avance acumulado:** 15%
* **Descripción del incremento:**
  * Consolidación y validación del documento de **Requisitos** (Semana 1).
  * Finalización del **Diseño del sistema** (Semana 2), incluyendo diagramas de arquitectura, modelo de entidad-relación de la base de datos y maquetado inicial (wireframes) de las interfaces de usuario.
* **Entregables técnicos:** Documentación técnica inicial y repositorio de código inicializado con la estructura del proyecto.

###  Versión 0.2.0 — Alpha Funcional (Gestión de Entidades Base)
* **Línea del tiempo:** Días 8 a 28 (Semanas 2 a 4)
* **Avance acumulado:** 45%
* **Descripción del incremento:**
  * Implementación completa del módulo de **Desarrollo (usuario e ítems)**.
  * CRUD (Crear, Leer, Actualizar, Borrar) de usuarios, perfiles, roles y permisos.
  * Registro, catalogación y control de inventario de los ítems/artículos disponibles para el flujo del sistema.
* **Entregables técnicos:** Base de datos desplegada con datos de prueba iniciales e interfaces de administración funcionales.

###  Versión 0.5.0 — Beta Inicial (Núcleo Operativo del Sistema)
* **Línea del tiempo:** Días 15 a 35 (Semanas 3 a 5)
* **Avance acumulado:** 80%
* **Descripción del incremento:**
  * Culminación del bloque crítico de **Desarrollo (préstamos y ventas)**.
  * Lógica de negocio para la asignación, control de fechas de devolución, estados de préstamos y procesamiento de transacciones de ventas.
  * Integración modular entre los usuarios/ítems (v0.2.0) y las nuevas operaciones financieras y de préstamo.
* **Entregables técnicos:** Despliegue en entorno de *Staging* o pruebas internas con los flujos principales punta a punta operativos.

###  Versión 0.9.0 — Beta Candidate (Fase de Estabilización y Calidad)
* **Línea del tiempo:** Días 29 a 35 (Semana 5)
* **Avance acumulado:** 95%
* **Descripción del incremento:**
  * Ejecución intensiva de la fase de **Pruebas** (unitarias, de integración, de carga y de usabilidad).
  * Reporte, priorización y solución inmediata de errores (bugs), fallos de interfaz y optimización de consultas en la base de datos.
* **Entregables técnicos:** Versión candidata a liberación (*Release Candidate*), congelamiento de código (*Code Freeze*).

###  Versión 1.0.0 — Versión de Producción (Entrega Final)
* **Línea del tiempo:** Días 36 a 42 (Semana 6)
* **Avance acumulado:** 100%
* **Descripción del incremento:**
  * Finalización de la **Documentación** (Manual de usuario, manual técnico de despliegue y actas de conformidad).
  * Proceso de **Entrega** formal al cliente o puesta en producción en el entorno definitivo.
  * Cierre oficial del proyecto.
* **Entregables técnicos:** Código fuente definitivo etiquetado (`tag: v1.0.0`), manuales oficiales en PDF y entorno de producción operativo.
# *Licencia*

<a href="https://github.com/tomasrestrepo1-ux/Gestor-pr-stamo-UdeA">Plata</a> © 2026 by <a href="https://github.com/tomasrestrepo1-ux">Tomas Restrepo</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
