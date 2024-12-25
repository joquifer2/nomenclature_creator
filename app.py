import streamlit as st
import pandas as pd
from io import BytesIO
from collections import OrderedDict


# ======================================
# FUNCIÓN PARA RESETEAR CAMPOS
# ======================================
def reset_session_state(keys):
    """
    Restaura los valores por defecto en session_state para los campos especificados,
    de modo que vuelvan al estado inicial (o vacío).
    """
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]


# ======================================
# FUNCIÓN PRINCIPAL (MAIN)
# ======================================
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


# ======================================
# PANTALLA DE INICIO
# ======================================
def pantalla_inicio():
    st.title("Generador de Nomenclaturas Publicitarias (Multi-Nomenclaturas)")
    st.write("""
    Esta aplicación está diseñada para ayudar a los profesionales del marketing a crear un sistema robusto de nomenclaturas publicitarias,
    **permitiendo generar múltiples nomenclaturas** por cada nivel (Campañas, Grupos de Anuncios, Anuncios y UTMs).
    
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
       creadas (una hoja por cada nivel), con la columna "Nomenclatura generada" siempre al final.
    """)
    st.video("https://youtu.be/B6icv3ke_dw")


# ======================================
# NIVEL 1: CAMPAÑAS
# ======================================
def nivel_campanas():
    st.header("Nivel 1: Campañas")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

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
    platform_options = ["Selecciona el canal o la plataforma publicitaria", "FB", "GG", "LI", "TT", "Personalizado"]
    platform = st.selectbox(
        "Canal o plataforma, FB (Facebook), IG (Instagram), GG (Google), entre otros",
        platform_options,
        key="platform",
        help="Si no quieres que aparezca en la nomenclatura, selecciona 'Personalizado' y déjalo en blanco."
    )
    if platform == "Personalizado":
        platform = st.text_input(
            "Introduce manualmente el nombre de la plataforma",
            key="platform_custom",
            help="Escribe manualmente el nombre de la plataforma si seleccionaste 'Personalizado'."
        )

    ad_network_options = ["Selecciona la red publicitaria", "Display", "Social", "Search", "Native", "Personalizado"]
    network = st.selectbox(
        "Red publicitaria, si procede (Social, Search, Display, Native...)",
        ad_network_options,
        key="network",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if network == "Personalizado":
        network = st.text_input(
            "Introduce manualmente la red publicitaria",
            key="network_custom",
            help="Escribe manualmente la red publicitaria si seleccionaste 'Personalizado'."
        )

    geography_options = ["Selecciona el área geográfica", "ES", "LATAM", "EU", "Global", "Personalizado"]
    geography = st.selectbox(
        "Área geográfica, si procede (España, LATAM, EU...)",
        geography_options,
        key="geography",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if geography == "Personalizado":
        geography = st.text_input(
            "Introduce manualmente un área geográfica",
            key="geography_custom",
            help="Escribe el acrónimo del área geográfica si seleccionaste 'Personalizado'."
        )

    objective_options = ["Selecciona el objetivo publicitario", "Awareness", "Conversiones", "Leads", "Engagement", "Tráfico", "Ventas", "Registro", "Personalizado"]
    objective = st.selectbox(
        "Objetivo publicitario (Tráfico, Leads, Ventas...)",
        objective_options,
        key="objective",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if objective == "Personalizado":
        objective = st.text_input(
            "Introduce manualmente el objetivo publicitario",
            key="objective_custom",
            help="Escribe manualmente el objetivo si seleccionaste 'Personalizado'."
        )

    campaign_options = ["Selecciona el tipo de campaña", "Prospecting", "Retargeting", "Personalizado"]
    campaign_type = st.selectbox(
        "Tipo de campaña (Prospecting, Retargeting...)",
        campaign_options,
        key="campaign_type",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if campaign_type == "Personalizado":
        campaign_type = st.text_input(
            "Introduce manualmente el tipo de campaña",
            key="campaign_type_custom",
            help="Escribe manualmente el tipo de campaña si seleccionaste 'Personalizado'."
        )

    product = st.text_input(
        "Producto (introduce el valor manualmente)",
        key="product",
        help="Este campo es manual, puedes modificar el valor según el producto que desees."
    )
    promotion = st.text_input(
        "Promoción (introduce el valor manualmente)",
        key="promotion",
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
        key="num_campos",
        help="Usa este número para indicar cuántos pares [nombre, valor] quieres añadir."
    )

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Campaña {i + 1}", key=f"nombre_campo_{i}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}", key=f"valor_campo_{i}")
        if valor_campo:  
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura de la nomenclatura (clásica o con corchetes)
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_campaign",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # ---------------------------
    # BOTÓN PARA GUARDAR CAMPAÑA
    # ---------------------------
    if st.button("Guardar Campaña"):
        # Filtrar placeholders vacíos
        parts = [
            p for p in [
                platform, network, geography, objective, campaign_type, product, promotion
            ]
            if p and not p.startswith("Selecciona") and not p.startswith("Introduce")
        ]
        for _, valor_campo in campos_personalizados:
            parts.append(valor_campo)

        # Generar nomenclatura
        if len(parts) == 0:
            campaign_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                campaign_nomenclature = "_".join(parts)
            else:
                campaign_nomenclature = "-".join([f"[{p}]" for p in parts])

        # Diccionario (usamos OrderedDict para un orden fijo)
        camp_dict = OrderedDict()
        # Predefinidos
        if platform and not platform.startswith("Selecciona") and not platform.startswith("Introduce"):
            camp_dict["Plataforma"] = platform
        if network and not network.startswith("Selecciona") and not network.startswith("Introduce"):
            camp_dict["Red"] = network
        if geography and not geography.startswith("Selecciona") and not geography.startswith("Introduce"):
            camp_dict["Geografía"] = geography
        if objective and not objective.startswith("Selecciona") and not objective.startswith("Introduce"):
            camp_dict["Objetivo"] = objective
        if campaign_type and not campaign_type.startswith("Selecciona") and not campaign_type.startswith("Introduce"):
            camp_dict["Tipo de campaña"] = campaign_type
        if product:
            camp_dict["Producto"] = product
        if promotion:
            camp_dict["Promoción"] = promotion

        # Personalizados
        for (n_cp, v_cp) in campos_personalizados:
            camp_dict[n_cp] = v_cp

        # Colocamos "Nomenclatura generada" al final
        camp_dict["Nomenclatura generada"] = campaign_nomenclature

        # Lo añadimos a la lista
        st.session_state["campaign_data_list"].append(dict(camp_dict))

        # Mensaje
        st.success(f"Campaña guardada. Nomenclatura generada: {campaign_nomenclature}")

        # Reset y refresh
        reset_session_state([
            "platform", "platform_custom", "network", "network_custom",
            "geography", "geography_custom", "objective", "objective_custom",
            "campaign_type", "campaign_type_custom", "product", "promotion",
            "num_campos", "structure_type_campaign"
        ])
        for i in range(num_campos):
            reset_session_state([f"nombre_campo_{i}", f"valor_campo_{i}"])
        st.experimental_rerun()

    # MOSTRAR LISTA DE CAMPAÑAS
    st.subheader("Campañas guardadas hasta ahora:")
    if len(st.session_state["campaign_data_list"]) == 0:
        st.info("No has guardado ninguna campaña todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["campaign_data_list"])
        st.dataframe(df_preview)


# ======================================
# NIVEL 2: GRUPOS DE ANUNCIOS
# ======================================
def nivel_grupos_anuncios():
    st.header("Nivel 2: Grupos de Anuncios")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    with st.sidebar:
        st.subheader("Nivel 2: Grupos de Anuncios")
        st.write("""
        Configura las características del grupo de anuncios, incluyendo la segmentación y el formato.
        Además, puedes añadir campos personalizados para definir mejor las características del grupo de anuncios.
        """)

    segmentation_options = ["Introduce el público objetivo o segmento", "Lkl", "Int", "Kw", "Bbdd", "Personalizado"]
    segmentation = st.selectbox(
        "Público objetivo o segmento (lookalike, intereses, keywords, bbdd...)",
        segmentation_options,
        key="segmentation",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if segmentation == "Personalizado":
        segmentation = st.text_input(
            "Introduce manualmente el público objetivo o segmento",
            key="segmentation_custom",
            help="Escribe manualmente el público objetivo o segmento si seleccionaste 'Personalizado'."
        )

    group_format_options = ["Introduce el tipo de formato", "Imagen", "Video", "Carrusel", "Audio", "Personalizado"]
    group_format = st.selectbox(
        "Formato, (opcional, si todos los anuncios dentro del grupo comparten el formato)",
        group_format_options,
        key="group_format",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if group_format == "Personalizado":
        group_format = st.text_input(
            "Introduce manualmente el formato",
            key="group_format_custom",
            help="Escribe manualmente el formato si seleccionaste 'Personalizado'."
        )

    st.subheader("Añadir Campos Personalizados (Grupo de Anuncios)")
    num_campos_grupos = st.number_input(
        "Número de campos personalizados a añadir para Grupos de Anuncios",
        min_value=0,
        max_value=10,
        step=1,
        key="num_campos_grupos"
    )

    campos_personalizados = []
    for i in range(num_campos_grupos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Grupo de Anuncio {i + 1}", key=f"nombre_campo_grupo_{i}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}", key=f"valor_campo_grupo_{i}")
        if valor_campo:
            campos_personalizados.append((nombre_campo, valor_campo))

    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_group",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    if st.button("Guardar Grupo de Anuncios"):
        parts = []
        if segmentation and not segmentation.startswith("Introduce"):
            parts.append(segmentation)
        if group_format and not group_format.startswith("Introduce"):
            parts.append(group_format)
        for _, valor_campo in campos_personalizados:
            parts.append(valor_campo)

        if len(parts) == 0:
            group_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                group_nomenclature = "_".join(parts)
            else:
                group_nomenclature = "-".join([f"[{p}]" for p in parts])

        group_dict = OrderedDict()
        if segmentation and not segmentation.startswith("Introduce"):
            group_dict["Segmentación"] = segmentation
        if group_format and not group_format.startswith("Introduce"):
            group_dict["Formato"] = group_format

        for (n_cp, v_cp) in campos_personalizados:
            group_dict[n_cp] = v_cp

        group_dict["Nomenclatura generada"] = group_nomenclature

        st.session_state["group_data_list"].append(dict(group_dict))
        st.success(f"Grupo de Anuncios guardado. Nomenclatura: {group_nomenclature}")

        reset_session_state([
            "segmentation", "segmentation_custom", "group_format", "group_format_custom",
            "num_campos_grupos", "structure_type_group"
        ])
        for i in range(num_campos_grupos):
            reset_session_state([f"nombre_campo_grupo_{i}", f"valor_campo_grupo_{i}"])
        st.experimental_rerun()

    st.subheader("Grupos de Anuncios guardados hasta ahora:")
    if len(st.session_state["group_data_list"]) == 0:
        st.info("No has guardado ningún grupo de anuncios todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["group_data_list"])
        st.dataframe(df_preview)


# ======================================
# NIVEL 3: ANUNCIOS
# ======================================
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

    type_creative_options = ["Introduce el tipo de creativo", "Personalizado", "Video", "Imagen", "Carousel", "Banner", "Audio", "Native", "Pop-up"]
    type_creative = st.selectbox(
        "Tipo de Creativo",
        type_creative_options,
        key="type_creative",
        help="Selecciona el tipo de creativo o introduce uno manual. Si no quieres que aparezca, 'Personalizado' y déjalo en blanco."
    )
    if type_creative == "Personalizado":
        type_creative = st.text_input(
            "Introduce el tipo de creativo",
            key="type_creative_custom",
            help="Escribe el tipo de creativo si seleccionaste 'Personalizado'."
        )

    variant = st.text_input(
        "Variación creativa (introduce el valor manualmente para pruebas A/B)",
        key="variant",
        help="Especifica la variante para las pruebas A/B (e.g., A, B, etc.)."
    )

    creative_angle = st.text_input(
        "Ángulo creativo (introduce el valor manualmente)",
        key="creative_angle",
        help="Especifica el ángulo creativo del anuncio (e.g., Oferta, Solución, etc.)."
    )

    ad_id = st.text_input(
        "ID del Anuncio (opcional, introduce el valor manualmente)",
        key="ad_id",
        help="Introduce un identificador único para el anuncio."
    )

    st.subheader("Añadir Campos Personalizados (Anuncios)")
    num_campos_anuncios = st.number_input(
        "Número de campos personalizados a añadir para Anuncios",
        min_value=0,
        max_value=10,
        step=1,
        key="num_campos_anuncios"
    )

    campos_personalizados = []
    for i in range(num_campos_anuncios):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Anuncio {i + 1}", key=f"nombre_campo_anuncio_{i}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}", key=f"valor_campo_anuncio_{i}")
        if valor_campo:
            campos_personalizados.append((nombre_campo, valor_campo))

    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_ad",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    if st.button("Guardar Anuncio"):
        parts = []
        if type_creative and not type_creative.startswith("Introduce"):
            parts.append(type_creative)
        if variant:
            parts.append(variant)
        if creative_angle:
            parts.append(creative_angle)
        if ad_id:
            parts.append(ad_id)

        for (_, valor_cp) in campos_personalizados:
            parts.append(valor_cp)

        if len(parts) == 0:
            ad_nomenclature = ""
        else:
            if structure_type == "Estructura clásica (_)":
                ad_nomenclature = "_".join(parts)
            else:
                ad_nomenclature = "-".join([f"[{p}]" for p in parts])

        ad_dict = OrderedDict()
        if type_creative and not type_creative.startswith("Introduce"):
            ad_dict["Tipo de creativo"] = type_creative
        if variant:
            ad_dict["Variación creativa"] = variant
        if creative_angle:
            ad_dict["Ángulo creativo"] = creative_angle
        if ad_id:
            ad_dict["ID del Anuncio"] = ad_id

        for (n_cp, v_cp) in campos_personalizados:
            ad_dict[n_cp] = v_cp

        ad_dict["Nomenclatura generada"] = ad_nomenclature

        st.session_state["ad_data_list"].append(dict(ad_dict))
        st.success(f"Anuncio guardado. Nomenclatura: {ad_nomenclature}")

        reset_session_state([
            "type_creative", "type_creative_custom", "variant", "creative_angle",
            "ad_id", "num_campos_anuncios", "structure_type_ad"
        ])
        for i in range(num_campos_anuncios):
            reset_session_state([f"nombre_campo_anuncio_{i}", f"valor_campo_anuncio_{i}"])
        st.experimental_rerun()

    st.subheader("Anuncios guardados hasta ahora:")
    if len(st.session_state["ad_data_list"]) == 0:
        st.info("No has guardado ningún anuncio todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["ad_data_list"])
        st.dataframe(df_preview)


# ======================================
# NIVEL 4: UTMs
# ======================================
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

    base_url = st.text_input(
        "URL base para la campaña",
        value="https://midominio.com",
        key="base_url",
        help="Introduce manualmente la URL base para la campaña."
    )

    source_options = ["Introduce la Fuente", "Google", "Facebook", "LinkedIn", "Newsletter", "Personalizado"]
    source = st.selectbox(
        "Fuente (utm_source)",
        source_options,
        key="utm_source",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if source == "Personalizado":
        source = st.text_input(
            "Introduce manualmente la fuente",
            key="utm_source_custom",
            help="Escribe manualmente la fuente si seleccionaste 'Personalizado'."
        )

    medium_options = ["Introduce el Medio", "CPC", "Display", "Email", "Social", "Personalizado"]
    medium = st.selectbox(
        "Medio (utm_medium)",
        medium_options,
        key="utm_medium",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if medium == "Personalizado":
        medium = st.text_input(
            "Introduce manualmente el medio",
            key="utm_medium_custom",
            help="Escribe manualmente el medio si seleccionaste 'Personalizado'."
        )

    campaign_utm = st.text_input(
        "Campaña (utm_campaign)",
        key="utm_campaign",
        help="Introduce la nomenclatura de campaña o déjalo vacío si no aplica."
    )

    term_utm = st.text_input(
        "Término (utm_term)",
        key="utm_term",
        help="Introduce la nomenclatura de Grupo de Anuncios o keywords."
    )

    content_utm = st.text_input(
        "Contenido (utm_content)",
        key="utm_content",
        help="Introduce la nomenclatura de Anuncio si deseas."
    )

    if st.button("Guardar UTMs"):
        final_source = source if source and not source.startswith("Introduce") else ""
        final_medium = medium if medium and not medium.startswith("Introduce") else ""

        utm_url = (
            f"{base_url}"
            f"?utm_source={final_source}"
            f"&utm_medium={final_medium}"
            f"&utm_campaign={campaign_utm}"
            f"&utm_term={term_utm}"
            f"&utm_content={content_utm}"
        )

        utm_dict = OrderedDict()
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

        utm_dict["Nomenclatura generada"] = utm_url

        st.session_state["utm_data_list"].append(dict(utm_dict))
        st.success(f"UTM guardada. URL generada: {utm_url}")

        reset_session_state([
            "base_url", "utm_source", "utm_source_custom", "utm_medium", "utm_medium_custom",
            "utm_campaign", "utm_term", "utm_content"
        ])
        st.experimental_rerun()

    st.subheader("UTMs guardadas hasta ahora:")
    if len(st.session_state["utm_data_list"]) == 0:
        st.info("No has guardado ninguna UTM todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["utm_data_list"])
        st.dataframe(df_preview)


# ======================================
# REORDENAR DICCIONARIOS
# ======================================
def reorder_dicts(list_of_dicts):
    """
    Toma una lista de diccionarios, recopila todas las claves (excepto 'Nomenclatura generada')
    en orden de aparición y, finalmente, añade 'Nomenclatura generada' al final.
    Devuelve una nueva lista de diccionarios con las mismas claves, pero en ese orden unificado.
    """
    if not list_of_dicts:
        return []

    all_keys = []
    for d in list_of_dicts:
        for k in d.keys():
            # recolección de claves
            if k not in all_keys and k != "Nomenclatura generada":
                all_keys.append(k)

    # Al final, metemos 'Nomenclatura generada'
    all_keys.append("Nomenclatura generada")

    new_list = []
    for d in list_of_dicts:
        reordered = OrderedDict()
        for k in all_keys:
            reordered[k] = d.get(k, None)  # si no existe, lo dejamos en None
        new_list.append(dict(reordered))

    return new_list


# ======================================
# EXPORTAR NOMENCLATURAS
# ======================================
def exportar_nomenclaturas():
    st.header("Exportar Nomenclaturas")
    st.write("""
    Aquí puedes descargar un Excel con todas las nomenclaturas que se han ido guardando: 
    - Campañas (Nivel 1)  
    - Grupos de Anuncios (Nivel 2)  
    - Anuncios (Nivel 3)  
    - UTMs (Nivel 4)  

    Se reordenan todas las columnas para que "Nomenclatura generada" quede siempre al final,
    incluso si añadiste columnas nuevas en nomenclaturas posteriores.
    """)

    def list_of_dicts_to_df(list_of_dicts):
        if not list_of_dicts:
            return pd.DataFrame()
        # Reordenamos con reorder_dicts
        reordered_list = reorder_dicts(list_of_dicts)
        return pd.DataFrame(reordered_list)

    # Convertir cada lista de nomenclaturas en DataFrame con orden de columnas unificado
    df_campaigns = list_of_dicts_to_df(st.session_state["campaign_data_list"])
    df_groups    = list_of_dicts_to_df(st.session_state["group_data_list"])
    df_ads       = list_of_dicts_to_df(st.session_state["ad_data_list"])
    df_utms      = list_of_dicts_to_df(st.session_state["utm_data_list"])

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
            df_groups.to_excel(writer,    index=False, sheet_name='Grupos')
            df_ads.to_excel(writer,       index=False, sheet_name='Anuncios')
            df_utms.to_excel(writer,      index=False, sheet_name='UTMs')
            writer.book.close()

        st.download_button(
            label="Descargar nomenclaturas como Excel",
            data=output.getvalue(),
            file_name=f"{file_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# ======================================
# ACERCA DE
# ======================================
def acerca_de():
    st.title("Acerca de")
    st.write("""
    **¡Hola, encantado de saludarte!**

    Soy Jordi Quiroga, 
    analista de datos, especialista en integración de fuentes y científico de datos en proyecto. 

    Llevo más de 15 años ayudando a agencias y profesionales del marketing a transformar sus datos en insights accionables.
    
    Esta aplicación permite crear múltiples nomenclaturas por cada nivel (1-4),
    y asegura que "Nomenclatura generada" quede siempre al final, aun si se añaden nuevos campos en nomenclaturas posteriores.
    
    Para más información: **jordi@jordiquiroga.com**

    **Sitio web:** https://www.jordiquiroga.com  
    **Perfil de LinkedIn:** [Jordi Quiroga Fernández](https://www.linkedin.com/in/jordiquirogafernandez/) 
    """)


# ======================================
# EJECUCIÓN DEL MAIN
# ======================================
if __name__ == "__main__":
    main()




  







