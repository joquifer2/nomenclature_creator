o# Generador de Nomenclaturas para Campañas de Marketing

> **Una herramienta diseñada para ayudar a agencias y profesionales del marketing a crear nomenclaturas estructuradas, consistentes y exportables para campañas, anuncios y UTMs.**

---

## 📌 Descripción General

Esta aplicación está diseñada para ayudar a los profesionales y agencias de marketing a **estandarizar las nomenclaturas** de sus campañas.  
Proporciona un enfoque sistemático para nombrar campañas, grupos de anuncios, anuncios y UTMs, facilitando la creación de una estructura clara y consistente en diferentes plataformas publicitarias.

La aplicación está desarrollada con **Streamlit** y es completamente interactiva.

---

## 🎯 Características Clave

- ✅ **Generador de Nomenclatura de Campañas:** Define estructuras de nombres para campañas, grupos de anuncios, anuncios y UTMs.
- ✅ **Flujo de Trabajo Paso a Paso:** Guía interactiva para construir la nomenclatura desde la campaña hasta los UTMs.
- ✅ **Campos Personalizados:** Flexibilidad para añadir tus propios campos en cada nivel.
- ✅ **Exportación a Excel:** Permite exportar las nomenclaturas generadas en formato Excel.
- ✅ **Interfaz Intuitiva:** Uso sencillo y visual mediante una barra lateral en Streamlit.
- ✅ **Funcionalidad de Copiado:** Copia de nomenclaturas o UTMs con un solo clic.

---

## 🚀 Cómo Usar

1. **Inicio:** Introducción general y navegación por los pasos.
2. **Nivel 1: Campañas:** Configura plataforma, red, geografía, objetivo, tipo de campaña, producto y promoción.
3. **Nivel 2: Grupos de Anuncios:** Define segmentación, formato y campos personalizados.
4. **Nivel 3: Anuncios:** Configura el tipo de creativo, variante A/B, ángulo y campos adicionales.
5. **Nivel 4: UTMs:** Genera URLs con parámetros UTM heredando información de niveles anteriores.
6. **Exportar:** Descarga todas las nomenclaturas generadas en un archivo Excel estructurado.
7. **Acerca de:** Información sobre el creador y el propósito de la aplicación.

---

## 🧰 Tecnologías Usadas

| Herramienta     | Uso principal                                   |
|------------------|------------------------------------------------|
| **Python**       | Lenguaje base de la aplicación                 |
| **Streamlit**    | Framework para la interfaz web                 |
| **Pandas**       | Manipulación de datos y exportación            |
| **xlsxwriter**   | Exportación de archivos Excel                  |
| **HTML/JS**      | Funcionalidad de copiado al portapapeles       |

---

## 📁 Estructura del Proyecto

```
nomenclaturas_streamlit/
│
├── app.py                  # Archivo principal de la aplicación
├── images/                 # Imágenes de la aplicación (por ejemplo, retrato del autor)
├── requirements.txt        # Lista de dependencias del proyecto
├── README.md               # Documentación del proyecto
└── ...
```

## 🧪 Estado del Proyecto

Esta aplicación es una **prueba de concepto funcional** en desarrollo continuo.  
El objetivo es facilitar la adopción de buenas prácticas en el nombrado de campañas publicitarias, mejorando la organización y trazabilidad de datos en proyectos de marketing multicanal.

---

## 🙋‍♂️ Acerca del Autor

**Jordi Quiroga**  
Data Analyst & Data Infrastructure Specialist para Marketing Digital  
Más de 15 años ayudando a equipos de marketing a integrar, automatizar y analizar sus datos.

- 📩 **Contacto:** jordi@jordiquiroga.com  
- 🌐 **Sitio web:** [jordiquiroga.com](https://www.jordiquiroga.com)  
- 🔗 **LinkedIn:** [Jordi Quiroga Fernández](https://www.linkedin.com/in/jordiquirogafernandez/)

---

## 🐞 Problemas o Feedback

Si encuentras algún error o tienes sugerencias de mejora, por favor crea un `issue` en este repositorio.  
Tu feedback es esencial para seguir mejorando esta herramienta.

---

## 📄 Licencia

Este proyecto se encuentra bajo desarrollo personal y no tiene una licencia específica asignada aún.  
Para usos personalizados o colaboraciones, contacta directamente con el autor.

Puedes verlo aquí: https://nomenclaturecreatorv3.streamlit.app/
