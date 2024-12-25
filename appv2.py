import streamlit as st
import pandas as pd
from io import BytesIO


def main():
    # ======================================================
    # INICIALIZACIÓN DE LISTAS PARA ALMACENAR MÚLTIPLES ITEMS
    # ======================================================
    if 'campaign_data_list' not in st.session_state:
        st.session_state['campaign_data_list'] = []
    if 'group_data_list' not in st.session_state:
        st.session_state['group_data_list'] = []
    if 'ad_data_list' not in st.session_state:
        st.session_state['ad_data_list'] = []
    if 'utm_data_list' not in st.session_state:
        st.session_state['utm_data_list'] = []

    # SIDEBAR: Selección de niveles
    st.sidebar.title("Pasos del Proceso de Nomenclatura")
    paso = st.sidebar.radio("Selecciona un paso para configurarlo:", [
        "Inicio",
        "Nivel 1: Campañas",
        "Nivel 2: Grupos de Anuncios",
        "Nivel 3: Anuncios",
        "Nivel 4: UTMs",
        "Exportar Nomenclaturas",
        "Acerca de"
    ])

    if paso == "Inicio":
        pantalla_inicio()
    elif paso == "Nivel 1: Campañas":
        nivel_campanas()
    elif paso == "Nivel 2: Grupos de Anuncios":
        nivel_grupos_anuncios()
    elif paso == "Nivel 3: Anuncios":
        nivel_anuncios()
    elif paso == "Nivel 4: UTMs":
        nivel_utms()
    elif paso == "Exportar Nomenclaturas":
        exportar_nomenclaturas()
    elif paso == "Acerca de":
        acerca_de()


# =========================
# PANTALLA DE INICIO
# =========================
def pantalla_inicio():
    st.title("Generador de Nomenclaturas Publicitarias (Multi-Nomenclaturas)")
    st.write("""
    Esta aplicación está diseñada para ayudar a los profesionales del marketing a crear un sistema robusto de nomenclaturas publicitarias
    y **permite generar múltiples nomenclaturas** por cada nivel (Campañas, Grupos de Anuncios, Anuncios y UTMs).
    
    **¿Qué hace la aplicación?**
    - Genera nomenclaturas consistentes para **Campañas**, **Grupos de Anuncios**, **Anuncios** y **UTMs**, 
      de acuerdo a las mejores prácticas del sector.
    - Facilita la unificación de datos entre diferentes plataformas publicitarias.
    - Permite exportar estas nomenclaturas en un archivo Excel para su uso posterior.

    **Flujo de uso para crear múltiples nomenclaturas**:
    1. Ve a cada nivel (1,2,3,4).
    2. Rellena los campos y haz clic en "**Guardar**" para añadir esa nomenclatura a la lista.
       Puedes volver a rellenar los campos y pulsar "**Guardar**" cuantas veces quieras.
    3. Al finalizar, en "**Exportar Nomenclaturas**", podrás descargar un Excel con todas las nomenclaturas 
       creadas (una hoja por cada nivel).
    """)
    st.video("https://youtu.be/B6icv3ke_dw")


# =========================
# NIVEL 1: CAMPAÑAS
# =========================
def nivel_campanas():
    st.header("Nivel 1: Campañas")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 1: Campañas")
        st.write("""
        En esta pantalla puedes configurar los parámetros principales de la campaña, 
        como la plataforma, el formato del anuncio, la audiencia y la geografía.
        También puedes añadir campos personalizados para describir más detalladamente la campaña.
        """)

    # ---------------------------
    # CAMPOS PRINCIPALES
    # ---------------------------

    # Campo de selección para Plataforma
    platform_options = ["Selecciona el canal o la plataforma publicitaria", "FB", "GG", "LI", "TT", "Personalizado"]
    platform = st.selectbox(
        "Canal o plataforma, FB (Facebook), IG (Instagram), GG (Google), entre otros",
        platform_options,
        help="Si no quieres que aparezca en la nomenclatura, selecciona 'Personalizado' y déjalo en blanco."
    )
    if platform == "Personalizado":
        platform = st.text_input(
            "Introduce manualmente el nombre de la plataforma",
            help="Escribe manualmente el nombre de la plataforma si seleccionaste 'Personalizado'."
        )

    # Campo de selección Red publicitaria
    ad_network_options = ["Selecciona la red publicitaria", "Display", "Social", "Search", "Native", "Personalizado"]
    network = st.selectbox(
        "Red publicitaria, si procede (Social, Search, Display, Native...)",
        ad_network_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if network == "Personalizado":
        network = st.text_input(
            "Introduce manualmente la red publicitaria",
            help="Escribe manualmente la red publicitaria si seleccionaste 'Personalizado'."
        )

    # Campo de selección para Geografía
    geography_options = ["Selecciona el área geográfica", "ES", "LATAM", "EU", "Global", "Personalizado"]
    geography = st.selectbox(
        "Área geográfica, si procede (España, LATAM, EU...)",
        geography_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if geography == "Personalizado":
        geography = st.text_input(
            "Introduce manualmente un área geográfica",
            help="Escribe el acrónimo del área geográfica si seleccionaste 'Personalizado'."
        )

    # Campo de selección para Objetivo
    objective_options = ["Selecciona el objetivo publicitario", "Awareness", "Conversiones", "Leads", "Engagement", "Tráfico", "Ventas", "Registro", "Personalizado"]
    objective = st.selectbox(
        "Objetivo publicitario (Tráfico, Leads, Ventas...)",
        objective_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if objective == "Personalizado":
        objective = st.text_input(
            "Introduce manualmente el objetivo publicitario",
            help="Escribe manualmente el objetivo si seleccionaste 'Personalizado'."
        )

    # Campo de selección para el tipo de campaña
    campaign_options = ["Selecciona el tipo de campaña", "Prospecting", "Retargeting", "Personalizado"]
    campaign_type = st.selectbox(
        "Tipo de campaña (Prospecting, Retargeting...)",
        campaign_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if campaign_type == "Personalizado":
        campaign_type = st.text_input(
            "Introduce manualmente el tipo de campaña",
            help="Escribe manualmente el tipo de campaña si seleccionaste 'Personalizado'."
        )

    # Campos manuales
    product = st.text_input(
        "Producto (introduce el valor manualmente)",
        help="Este campo es manual, puedes modificar el valor según el producto que desees."
    )
    promotion = st.text_input(
        "Promoción (introduce el valor manualmente)",
        help="Este campo es manual, personalizable para cada promoción."
    )

    # ---------------------------
    # CAMPOS PERSONALIZADOS
    # ---------------------------
    st.subheader("Añadir Campos Personalizados (Campaña)")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir",
        min_value=0,
        max_value=10,
        step=1,
        help="Usa este número para indicar cuántos pares [nombre, valor] quieres añadir."
    )

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Campaña {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo:  
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura de la nomenclatura (clásica o con corchetes)
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # ---------------------------
    # BOTÓN PARA GUARDAR CAMPAÑA
    # ---------------------------
    if st.button("Guardar Campaña"):
        # Filtrar placeholders vacíos (que empiezan con "Selecciona" o "Introduce")
        parts = [
            p for p in [
                platform, network, geography, objective, campaign_type, product, promotion
            ]
            if p and not p.startswith("Selecciona") and not p.startswith("Introduce")
        ]

        # Añadimos los campos personalizados
        for (nombre_cp, valor_cp) in campos_personalizados:
            parts.append(valor_cp)

        # Generar nomenclatura
        if len(parts) == 0:
            campaign_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                campaign_nomenclature = "_".join(parts)
            else:
                campaign_nomenclature = "-".join([f"[{part}]" for part in parts])

        # Crear diccionario con los campos “activos”
        campaign_dict = {}
        # Solo agregamos campo si no es placeholder ni vacío
        if platform and not platform.startswith("Selecciona") and not platform.startswith("Introduce"):
            campaign_dict["Plataforma"] = platform
        if network and not network.startswith("Selecciona") and not network.startswith("Introduce"):
            campaign_dict["Red"] = network
        if geography and not geography.startswith("Selecciona") and not geography.startswith("Introduce"):
            campaign_dict["Geografía"] = geography
        if objective and not objective.startswith("Selecciona") and not objective.startswith("Introduce"):
            campaign_dict["Objetivo"] = objective
        if campaign_type and not campaign_type.startswith("Selecciona") and not campaign_type.startswith("Introduce"):
            campaign_dict["Tipo de campaña"] = campaign_type
        if product:
            campaign_dict["Producto"] = product
        if promotion:
            campaign_dict["Promoción"] = promotion

        # Campos personalizados
        for (nombre_cp, valor_cp) in campos_personalizados:
            campaign_dict[nombre_cp] = valor_cp

        # Guardamos la nomenclatura completa en un campo adicional (opcional)
        campaign_dict["Nomenclatura generada"] = campaign_nomenclature

        # Añadir a la lista global
        st.session_state["campaign_data_list"].append(campaign_dict)

        # Mensaje
        st.success(f"Campaña guardada. Nomenclatura generada: {campaign_nomenclature}")

    # MOSTRAR LISTA DE CAMPAÑAS
    st.subheader("Campañas guardadas hasta ahora:")
    if len(st.session_state["campaign_data_list"]) == 0:
        st.info("No has guardado ninguna campaña todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["campaign_data_list"])
        st.dataframe(df_preview)


# =========================
# NIVEL 2: GRUPOS DE ANUNCIOS
# =========================
def nivel_grupos_anuncios():
    st.header("Nivel 2: Grupos de Anuncios")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 2: Grupos de Anuncios")
        st.write("""
        Configura las características del grupo de anuncios, incluyendo la segmentación y el formato.
        Además, puedes añadir campos personalizados para definir mejor las características del grupo de anuncios.
        """)

    # Segmentación
    segmentation_options = ["Introduce el público objetivo o segmento", "Lkl", "Int", "Kw", "Bbdd", "Personalizado"]
    segmentation = st.selectbox(
        "Público objetivo o segmento (lookalike, intereses, keywords, bbdd...)",
        segmentation_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if segmentation == "Personalizado":
        segmentation = st.text_input(
            "Introduce manualmente el público objetivo o segmento",
            help="Escribe manualmente el público objetivo o segmento si seleccionaste 'Personalizado'."
        )

    # Formato
    group_format_options = ["Introduce el tipo de formato", "Imagen", "Video", "Carrusel", "Audio", "Personalizado"]
    group_format = st.selectbox(
        "Formato, (opcional, si todos los anuncios dentro del grupo comparten el formato)",
        group_format_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if group_format == "Personalizado":
        group_format = st.text_input(
            "Introduce manualmente el formato",
            help="Escribe manualmente el formato si seleccionaste 'Personalizado'."
        )

    # Campos personalizados
    st.subheader("Añadir Campos Personalizados (Grupo de Anuncios)")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir para Grupos de Anuncios",
        min_value=0,
        max_value=10,
        step=1
    )

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Grupo de Anuncio {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo:
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # Botón "Guardar Grupo"
    if st.button("Guardar Grupo de Anuncios"):
        # Filtrar placeholders / vacíos
        parts = []
        if segmentation and not segmentation.startswith("Introduce"):
            parts.append(segmentation)
        if group_format and not group_format.startswith("Introduce"):
            parts.append(group_format)

        for (nombre_cp, valor_cp) in campos_personalizados:
            parts.append(valor_cp)

        # Construir nomenclatura
        if len(parts) == 0:
            group_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                group_nomenclature = "_".join(parts)
            else:
                group_nomenclature = "-".join([f"[{p}]" for p in parts])

        group_dict = {}
        if segmentation and not segmentation.startswith("Introduce"):
            group_dict["Segmentación"] = segmentation
        if group_format and not group_format.startswith("Introduce"):
            group_dict["Formato"] = group_format
        for (nombre_cp, valor_cp) in campos_personalizados:
            group_dict[nombre_cp] = valor_cp

        group_dict["Nomenclatura generada"] = group_nomenclature

        st.session_state["group_data_list"].append(group_dict)
        st.success(f"Grupo de Anuncios guardado. Nomenclatura: {group_nomenclature}")

    st.subheader("Grupos de Anuncios guardados hasta ahora:")
    if len(st.session_state["group_data_list"]) == 0:
        st.info("No has guardado ningún grupo de anuncios todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["group_data_list"])
        st.dataframe(df_preview)


# =========================
# NIVEL 3: ANUNCIOS
# =========================
def nivel_anuncios():
    st.header("Nivel 3: Anuncios")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    with st.sidebar:
        st.subheader("Nivel 3: Anuncios")
        st.write("""
        Define los detalles específicos del anuncio, como el tipo de creativo, la variante para pruebas A/B 
        y un identificador único del anuncio.
        Además, puedes añadir campos personalizados para especificar más detalles si es necesario.
        """)

    # Tipo de Creativo
    type_creative_options = ["Introduce el tipo de creativo", "Personalizado", "Video", "Imagen", "Carousel", "Banner", "Audio", "Native", "Pop-up"]
    type_creative = st.selectbox(
        "Tipo de Creativo",
        type_creative_options,
        help="Selecciona el tipo de creativo o introduce uno manual. Si no quieres que aparezca, 'Personalizado' y déjalo en blanco."
    )
    if type_creative == "Personalizado":
        type_creative = st.text_input(
            "Introduce el tipo de creativo",
            help="Escribe el tipo de creativo si seleccionaste 'Personalizado'."
        )

    # Variación creativa
    variant = st.text_input(
        "Variación creativa (introduce el valor manualmente para pruebas A/B)",
        help="Especifica la variante para las pruebas A/B (e.g., A, B, etc.)."
    )

    # Ángulo creativo
    creative_angle = st.text_input(
        "Ángulo creativo (introduce el valor manualmente)",
        help="Especifica el ángulo creativo del anuncio (e.g., Oferta, Solución, Innovación, etc.)."
    )

    # ID del Anuncio
    ad_id = st.text_input(
        "ID del Anuncio (opcional, introduce el valor manualmente)",
        help="Introduce un identificador único para el anuncio."
    )

    # Campos Personalizados
    st.subheader("Añadir Campos Personalizados (Anuncios)")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir para Anuncios",
        min_value=0,
        max_value=10,
        step=1
    )

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Anuncio {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo:
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # Botón "Guardar Anuncio"
    if st.button("Guardar Anuncio"):
        # Filtrar placeholders
        parts = []
        if type_creative and not type_creative.startswith("Introduce"):
            parts.append(type_creative)
        if variant:
            parts.append(variant)
        if creative_angle:
            parts.append(creative_angle)
        if ad_id:
            parts.append(ad_id)

        for (nombre_cp, valor_cp) in campos_personalizados:
            parts.append(valor_cp)

        if len(parts) == 0:
            ad_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                ad_nomenclature = "_".join(parts)
            else:
                ad_nomenclature = "-".join([f"[{p}]" for p in parts])

        ad_dict = {}
        if type_creative and not type_creative.startswith("Introduce"):
            ad_dict["Tipo de creativo"] = type_creative
        if variant:
            ad_dict["Variación creativa"] = variant
        if creative_angle:
            ad_dict["Ángulo creativo"] = creative_angle
        if ad_id:
            ad_dict["ID del Anuncio"] = ad_id
        for (nombre_cp, valor_cp) in campos_personalizados:
            ad_dict[nombre_cp] = valor_cp

        ad_dict["Nomenclatura generada"] = ad_nomenclature

        st.session_state["ad_data_list"].append(ad_dict)
        st.success(f"Anuncio guardado. Nomenclatura: {ad_nomenclature}")

        # Botón de copiar (HTML + JS) → puedes dejarlo si lo deseas en cada guardado
        # (O simplemente usar un 'st.write(ad_nomenclature)'.


    st.subheader("Anuncios guardados hasta ahora:")
    if len(st.session_state["ad_data_list"]) == 0:
        st.info("No has guardado ningún anuncio todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["ad_data_list"])
        st.dataframe(df_preview)


# =========================
# NIVEL 4: UTMs
# =========================
def nivel_utms():
    st.header("Nivel 4: UTMs")
    st.write("""
    Genera la URL con parámetros UTM para el seguimiento de la campaña publicitaria.
    Configura la fuente, el medio, la campaña y otros parámetros para crear un enlace rastreable.
    """)

    with st.sidebar:
        st.subheader("Nivel 4: UTMs")
        st.write("""
        Genera la URL con parámetros UTM para el seguimiento de la campaña publicitaria.
        Configura la fuente, el medio, la campaña y otros parámetros para crear un enlace rastreable.
        """)

    # URL base
    base_url = st.text_input(
        "URL base para la campaña",
        value="https://midominio.com",
        help="Introduce manualmente la URL base para la campaña."
    )

    # Fuente
    source_options = ["Introduce la Fuente", "Google", "Facebook", "LinkedIn", "Newsletter", "Personalizado"]
    source = st.selectbox(
        "Fuente (utm_source)",
        source_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if source == "Personalizado":
        source = st.text_input(
            "Introduce manualmente la fuente",
            help="Escribe manualmente la fuente si seleccionaste 'Personalizado'."
        )

    # Medio
    medium_options = ["Introduce el Medio", "CPC", "Display", "Email", "Social", "Personalizado"]
    medium = st.selectbox(
        "Medio (utm_medium)",
        medium_options,
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if medium == "Personalizado":
        medium = st.text_input(
            "Introduce manualmente el medio",
            help="Escribe manualmente el medio si seleccionaste 'Personalizado'."
        )

    # Campaña
    campaign_utm = st.text_input(
        "Campaña (utm_campaign)",
        help="Introduce la nomenclatura de campaña o déjalo vacío si no aplica."
    )

    # Término
    term_utm = st.text_input(
        "Término (utm_term)",
        help="Introduce la nomenclatura de Grupo de Anuncios o keywords."
    )

    # Contenido
    content_utm = st.text_input(
        "Contenido (utm_content)",
        help="Introduce la nomenclatura de Anuncio si deseas."
    )

    if st.button("Guardar UTMs"):
        # Filtrar placeholders
        final_source = source if source and not source.startswith("Introduce") else ""
        final_medium = medium if medium and not medium.startswith("Introduce") else ""

        utm_url = f"{base_url}?utm_source={final_source}&utm_medium={final_medium}&utm_campaign={campaign_utm}&utm_term={term_utm}&utm_content={content_utm}"

        # Crear dict
        utm_dict = {}
        if base_url:
            utm_dict["URL Base"] = base_url
        if final_source:
            utm_dict["Fuente"] = final_source
        if final_medium:
            utm_dict["Medio"] = final_medium
        if campaign_utm:
            utm_dict["Campaña"] = campaign_utm
        if term_utm:
            utm_dict["Término"] = term_utm
        if content_utm:
            utm_dict["Contenido"] = content_utm

        utm_dict["UTM generada"] = utm_url

        st.session_state["utm_data_list"].append(utm_dict)
        st.success(f"UTM guardada. URL generada: {utm_url}")

    st.subheader("UTMs guardadas hasta ahora:")
    if len(st.session_state["utm_data_list"]) == 0:
        st.info("No has guardado ninguna UTM todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["utm_data_list"])
        st.dataframe(df_preview)


# =========================
# EXPORTAR NOMENCLATURAS
# =========================
def exportar_nomenclaturas():
    st.header("Exportar Nomenclaturas")

    st.write("""
    Aquí puedes descargar un Excel con todas las nomenclaturas que se han ido guardando: 
    - Campañas (Nivel 1)  
    - Grupos de Anuncios (Nivel 2)  
    - Anuncios (Nivel 3)  
    - UTMs (Nivel 4)  
    Cada hoja del Excel mostrará las nomenclaturas y campos que has creado en cada nivel.
    """)

    def list_of_dicts_to_df(list_of_dicts):
        if not list_of_dicts:
            return pd.DataFrame()
        return pd.DataFrame(list_of_dicts)

    # Convertir cada lista de nomenclaturas en DataFrame
    df_campaigns = list_of_dicts_to_df(st.session_state["campaign_data_list"])
    df_groups = list_of_dicts_to_df(st.session_state["group_data_list"])
    df_ads = list_of_dicts_to_df(st.session_state["ad_data_list"])
    df_utms = list_of_dicts_to_df(st.session_state["utm_data_list"])

    st.subheader("Vista Previa: Campañas (Nivel 1)")
    st.dataframe(df_campaigns)

    st.subheader("Vista Previa: Grupos de Anuncios (Nivel 2)")
    st.dataframe(df_groups)

    st.subheader("Vista Previa: Anuncios (Nivel 3)")
    st.dataframe(df_ads)

    st.subheader("Vista Previa: UTMs (Nivel 4)")
    st.dataframe(df_utms)

    # Nombre de archivo personalizable
    file_name = st.text_input("Nombre del archivo Excel (sin extensión)", "nomenclaturas")

    if st.button("Descargar Excel"):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_campaigns.to_excel(writer, index=False, sheet_name='Campañas')
            df_groups.to_excel(writer, index=False, sheet_name='Grupos')
            df_ads.to_excel(writer, index=False, sheet_name='Anuncios')
            df_utms.to_excel(writer, index=False, sheet_name='UTMs')
            writer.book.close()

        st.download_button(
            label="Descargar nomenclaturas como Excel",
            data=output.getvalue(),
            file_name=f"{file_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# =========================
# ACERCA DE
# =========================
def acerca_de():
    st.title("Acerca de")
    st.write("""
    **¡Hola, encantado de saludarte!**

    Soy Jordi Quiroga, 
    analista de datos, especialista en integración de fuentes y científico de datos en proyecto. 

    Llevo más de 15 años ayudando a agencias y profesionales del marketing a transformar sus datos en insights accionables.
    
    He creado esta herramienta para solucionar uno de los problemas más frustrantes que encuentro en el día a día con mis clientes: 
    la falta de consistencia en las nomenclaturas.
   
    Esta aplicación pretende ayudar a los profesionales del marketing y a sus equipos 
    a dar el primer paso hacia la automatización de procesos, 
    mediante la adquisición de buenas prácticas tecnológicas que brillan por su eficiencia 
    y notable ahorro de tiempo y recursos.
    
    Estás ante una prueba de concepto. La herramienta la sigo mejorando día a día con tus comentarios. 
    Si quieres dejarme feedback o que personalice esta aplicación para ti, 
    puedes hacerlo a través de esta dirección: **jordi@jordiquiroga.com**

    Puedes descubrir más sobre mí en mi sitio web y en mi perfil de LinkedIn:
    """)
    st.write("**Sitio web:** https://www.jordiquiroga.com")
    st.write("**Perfil de LinkedIn:** [Jordi Quiroga Fernández](https://www.linkedin.com/in/jordiquirogafernandez/)")
    st.image("images/Jordi-portrait.jpg", caption="Jordi Quiroga", width=200)
    # Si tienes una imagen local, podrías usar: st.image("images/Jordi-portrait.jpg", caption="Jordi Quiroga", width=200)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    main()































