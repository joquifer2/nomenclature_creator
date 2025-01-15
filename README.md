Generador de Nomenclaturas Publicitarias (Multi-Nomenclaturas)

Descripción General

Esta aplicación está diseñada para ayudar a profesionales del marketing a crear nomenclaturas publicitarias estructuradas y consistentes. Su principal propósito es simplificar la creación y gestión de nomenclaturas para campañas, grupos de anuncios, anuncios individuales y UTMs, asegurando la coherencia en la organización de datos publicitarios.

Objetivos

Unificar nombres en distintas plataformas publicitarias.

Simplificar el proceso de creación de nomenclaturas personalizadas.

Permitir exportaciones de nomenclaturas en formato Excel.

Facilitar el análisis de datos mediante una estructura coherente.

Funcionalidades Principales

1. Flujo paso a paso

Configuración por niveles:

Campañas

Grupos de Anuncios

Anuncios

UTMs

Guarda las configuraciones como listas de nomenclaturas.

2. Flexibilidad en campos personalizados

Añade campos personalizados en cada nivel.

Elige entre dos estructuras de nomenclaturas:

Clásica (separada por guiones bajos _).

Con corchetes [valor]-[valor].

3. Exportación a Excel

Descarga todas las nomenclaturas guardadas en un archivo Excel.

Cada nivel se almacena en una hoja diferente del archivo.

4. Persistencia de datos en sesión

Utiliza st.session_state para guardar los datos temporalmente.

5. Diseño modular

La app está organizada en niveles.

Incluye una sección "Acerca de" con información del autor.

Funciones del Código

1. reset_session_state(keys)

Propósito: Restablece los valores de los campos en la sesión.

Uso: Borra claves especificadas para restablecer valores iniciales.

2. main()

Propósito: Controla el flujo de navegación entre niveles.

Uso: Inicializa listas en st.session_state y muestra el menú lateral.

3. pantalla_inicio()

Propósito: Muestra introducción y guía de uso.

Uso: Explica el flujo de trabajo y proporciona un video tutorial.

4. nivel_campanas()

Propósito: Configura campañas publicitarias.

Uso: Selecciona plataforma, red publicitaria, geografía, etc. Guarda en st.session_state['campaign_data_list'].

5. nivel_grupos_anuncios()

Propósito: Configura grupos de anuncios.

Uso: Añade segmentación, formato y campos personalizados. Guarda en st.session_state['group_data_list'].

6. nivel_anuncios()

Propósito: Configura anuncios individuales.

Uso: Define tipo de creativo, variantes A/B y campos personalizados. Guarda en st.session_state['ad_data_list'].

7. nivel_utms()

Propósito: Crea URLs con parámetros UTM.

Uso: Genera URLs rastreables para seguimiento. Guarda en st.session_state['utm_data_list'].

8. reorder_dicts(list_of_dicts)

Propósito: Reordena claves de diccionarios para garantizar formato consistente.

Uso: Asegura que la columna "Nomenclatura generada" quede al final.

9. exportar_nomenclaturas()

Propósito: Exporta todas las nomenclaturas a Excel.

Uso: Divide niveles en hojas separadas y permite vista previa antes de la descarga.

10. acerca_de()

Propósito: Proporciona información sobre el autor.

Uso: Incluye enlaces al sitio web y LinkedIn.

Conclusión

La aplicación está optimizada para la gestión de nomenclaturas publicitarias, proporcionando un flujo de trabajo estructurado para crear nombres consistentes a nivel de campañas, grupos de anuncios, anuncios individuales y UTMs. Es altamente personalizable y facilita la exportación de datos en Excel para análisis adicionales.

Información del Autor

Nombre: Jordi Quiroga

Correo Electrónico: jordi@jordiquiroga.com

Sitio Web: jordiquiroga.com

LinkedIn: Jordi Quiroga Fernández
