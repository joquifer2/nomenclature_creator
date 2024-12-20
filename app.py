import streamlit as st
import pandas as pd
from io import BytesIO


def main():
    # Sidebar con los pasos del proceso
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

    # Lógica para cada paso según la selección
    if paso == "Inicio":
        pantalla_inicio()
    elif paso == "Nivel 1: Campañas":
        campaign_nomenclature = nivel_campanas()
        st.session_state["campaign_nomenclature"] = campaign_nomenclature
    elif paso == "Nivel 2: Grupos de Anuncios":
        group_nomenclature = nivel_grupos_anuncios()
        st.session_state["group_nomenclature"] = group_nomenclature
    elif paso == "Nivel 3: Anuncios":
        ad_nomenclature = nivel_anuncios()
        st.session_state["ad_nomenclature"] = ad_nomenclature
    elif paso == "Nivel 4: UTMs":
        st.header("Nivel 4: UTMs")
        st.write("""
        Genera la URL con parámetros UTM para el seguimiento de la campaña publicitaria.
        Configura la fuente, el medio, la campaña y otros parámetros para crear un enlace rastreable.
        """)

        # Obtener valores heredados de los niveles anteriores
        campaign_nomenclature = st.session_state.get("campaign_nomenclature", "")
        group_nomenclature = st.session_state.get("group_nomenclature", "")
        ad_nomenclature = st.session_state.get("ad_nomenclature", "")

        # Pasar los valores heredados (incluso si están vacíos) a nivel_utms
        utm_nomenclature = nivel_utms(campaign_nomenclature, group_nomenclature, ad_nomenclature)
        st.session_state["utm_nomenclature"] = utm_nomenclature
    elif paso == "Exportar Nomenclaturas":
        exportar_nomenclaturas(
            st.session_state.get("campaign_nomenclature", ""),
            st.session_state.get("group_nomenclature", ""),
            st.session_state.get("ad_nomenclature", ""),
            st.session_state.get("utm_nomenclature", "")
        )
    elif paso == "Acerca de":
        acerca_de()




def pantalla_inicio():
    st.title("Generador de Nomenclaturas Publicitarias")
    st.write("""
    Esta aplicación está diseñada para ayudar a los profesionales del marketing a crear un sistema robusto de nomenclaturas publicitarias.
    
    **¿Qué hace la aplicación?**
    - Genera nomenclaturas consistentes para **Campañas**, **Grupos de Anuncios**, **Anuncios** y **UTMs**, de acuerdo a las mejores prácticas del sector.
    - Facilita la unificación de datos entre diferentes plataformas publicitarias.
    - Permite exportar estas nomenclaturas en un archivo CSV para su uso posterior.

    **Pasos del Proceso**
    1. **Nivel 1: Campañas** - Configura las características principales de la campaña.
    2. **Nivel 2: Grupos de Anuncios** - Detalla la segmentación y el objetivo del grupo de anuncios.
    3. **Nivel 3: Anuncios** - Define los detalles del anuncio específico.
    4. **Nivel 4: UTMs** - Genera UTMs consistentes para el seguimiento de tus campañas.
    5. **Exportar Nomenclaturas** - Exporta todas las nomenclaturas generadas en un archivo excel.
    """)


def nivel_campanas():
    st.header("Nivel 1: Campañas")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 1: Campañas")
        st.write("""
        En esta pantalla puedes configurar los parámetros principales de la campaña, como la plataforma, el formato del anuncio, la audiencia y la geografía.
        También puedes añadir campos personalizados para describir más detalladamente la campaña.
        """)

    # Campo de selección para Plataforma
    platform_options = ["Selecciona el canal o la plataforma publicitaria", "FB", "GG", "LI", "TT", "Personalizado"]
    platform = st.session_state.get("platform", "Selecciona la plataforma publicitaria")
    if platform not in platform_options:
        platform = "Selecciona el canal o la plataforma publicitaria"
    platform_index = platform_options.index(platform)

    platform = st.selectbox(
        "Canal o plataforma, FB (Facebook), IG (Instagram), GG (Google), entre otros",
        platform_options,
        index=platform_index
    )
    if platform == "Personalizado":
        platform = st.text_input(
            "Introduce manualmente el nombre de la plataforma",
            st.session_state.get("platform_custom", ""),
            help="Escribe manualmente el nombre de la plataforma si seleccionaste 'Personalizado'."
        )
        st.session_state["platform_custom"] = platform
    st.session_state["platform"] = platform

    # Campo de selección Red publicitaria
    ad_network_options = ["Selecciona la red publicitaria", "Display", "Social", "Search", "Native", "Personalizado"]
    network = st.session_state.get("network", "Selecciona la red publicitaria")
    if network not in ad_network_options:
        network = "Selecciona la red publicitaria"
    network_index = ad_network_options.index(network)

    network = st.selectbox(
        "Red publicitaria, si procede (Social, Search, Display, Native...)",
        ad_network_options,
        index=network_index
    )
    if network == "Personalizado":
        network = st.text_input(
            "Introduce manualmente la red publicitaria",
            st.session_state.get("network_custom", ""),
            help="Escribe manualmente la red publicitaria si seleccionaste 'Personalizado'."
        )
        st.session_state["network_custom"] = network
    st.session_state["network"] = network

    # Campo de selección para Geografía
    geography_options = ["Selecciona el área geográfica", "ES", "LATAM", "EU", "Global", "Personalizado"]
    geography = st.session_state.get("geography", "Selecciona el área geográfica")
    if geography not in geography_options:
        geography = "Selecciona el área geográfica"
    geography_index = geography_options.index(geography)

    geography = st.selectbox(
        "Área geográfica, si procede (España, LATAM, EU...)",
        geography_options,
        index=geography_index
    )
    if geography == "Personalizado":
        geography = st.text_input(
            "Introduce manualmente un área geográfica",
            st.session_state.get("geography_custom", ""),
            help="Escribe el acrónimo del área geográfica si seleccionaste 'Personalizado'."
        )
        st.session_state["geography_custom"] = geography
    st.session_state["geography"] = geography

    # Campo de selección para Objetivo
    objective_options = ["Selecciona el objetivo publicitario", "Awareness", "Conversiones", "Leads", "Engagement", "Tráfico", "Ventas", "Registro", "Personalizado"]
    objective = st.session_state.get("objective", "Selecciona el objetivo publicitario")
    if objective not in objective_options:
        objective = "Selecciona el objetivo publicitario"
    objective_index = objective_options.index(objective)

    objective = st.selectbox(
        "Objetivo publicitario (Tráfico, Leads, Ventas...)",
        objective_options,
        index=objective_index
    )
    if objective == "Personalizado":
        objective = st.text_input(
            "Introduce manualmente el objetivo publicitario",
            st.session_state.get("objective_custom", ""),
            help="Escribe manualmente el objetivo si seleccionaste 'Personalizado'."
        )
        st.session_state["objective_custom"] = objective
    st.session_state["objective"] = objective

    # Campo de selección para el tipo de campaña
    campaign_options = ["Selecciona el tipo de campaña", "Prospecting", "Retargeting", "Personalizado"]
    campaign_type = st.session_state.get("campaign_type", "Selecciona el tipo de campaña")
    if campaign_type not in campaign_options:
        campaign_type = "Selecciona el tipo de campaña"
    campaign_type_index = campaign_options.index(campaign_type)

    campaign_type = st.selectbox(
        "Tipo de campaña (Prospecting, Retargeting...)",
        campaign_options,
        index=campaign_type_index
    )
    if campaign_type == "Personalizado":
        campaign_type = st.text_input(
            "Introduce manualmente el tipo de campaña",
            st.session_state.get("campaign_type_custom", ""),
            help="Escribe manualmente el nombre del tipo de campaña si seleccionaste 'Personalizado'."
        )
        st.session_state["campaign_type_custom"] = campaign_type
    st.session_state["campaign_type"] = campaign_type

    # Campos manuales
    product = st.text_input(
        "Producto (introduce el valor manualmente)",
        st.session_state.get("product", ""),
        help="Este campo es manual, puedes modificar el valor según el producto que desees."
    )
    st.session_state["product"] = product

    promotion = st.text_input(
        "Promoción (introduce el valor manualmente)",
        st.session_state.get("promotion", ""),
        help="Este campo es manual, personalizable para cada promoción."
    )
    st.session_state["promotion"] = promotion

    # Añadir Campos Personalizados para Campañas
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir",
        min_value=0,
        max_value=10,
        value=st.session_state.get("num_campos", 0),
        step=1
    )
    st.session_state["num_campos"] = num_campos

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(
            f"Nombre del Campo personalizado Campaña {i + 1}",
            st.session_state.get(f"nombre_campo_{i}", "")
        )
        valor_campo = st.text_input(
            f"Valor para {nombre_campo}",
            st.session_state.get(f"valor_campo_{i}", "")
        )
        st.session_state[f"nombre_campo_{i}"] = nombre_campo
        st.session_state[f"valor_campo_{i}"] = valor_campo
        if valor_campo:
            campos_personalizados.append(valor_campo)

    # Añadir un selectbox para elegir la estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        index=0
    )
    st.session_state["structure_type"] = structure_type

    # Generar nomenclatura para Campaña según la estructura seleccionada
    nomenclature_parts = [platform, network, geography, objective, campaign_type, product, promotion] + campos_personalizados

    if any(part.startswith("Selecciona") for part in nomenclature_parts) or not any(nomenclature_parts):
        campaign_nomenclature = ""  # Mostrar cuadro vacío hasta que los campos estén completos
    else:
        if structure_type == "Estructura clásica (_)":
            campaign_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Estructura clásica
        elif structure_type == "Estructura con corchetes ([valor]-[valor])":
            campaign_nomenclature = '-'.join([f"[{part}]" for part in filter(None, nomenclature_parts)])  # Estructura con corchetes

    st.session_state["campaign_nomenclature"] = campaign_nomenclature

    # Mostrar la nomenclatura en un cuadro estilizado
    st.subheader("Nomenclatura de Campaña generada:")
    st.markdown(
        f"""
        <div style="background-color:#e0f7fa; padding:10px; border-radius:5px; border: 1px solid #81d4fa;">
            <p style="color:#0277bd; font-size:16px; font-family:monospace;">{campaign_nomenclature}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    return campaign_nomenclature




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

    # Campo de selección para Segmentación
    segmentation_options = ["Introduce el público objetivo o segmento", "Lkl", "Int", "Kw", "Bbdd", "Personalizado"]
    segmentation = st.session_state.get("segmentation", "Introduce el público objetivo o segmento")
    if segmentation not in segmentation_options:
        segmentation = "Introduce el público objetivo o segmento"
    segmentation_index = segmentation_options.index(segmentation)

    segmentation = st.selectbox(
        "Público objetivo o segmento (lookalike, intereses, keywords, bbdd...)",
        segmentation_options,
        index=segmentation_index
    )
    if segmentation == "Personalizado":
        segmentation = st.text_input(
            "Introduce manualmente el público objetivo o segmento",
            st.session_state.get("segmentation_custom", ""),
            help="Escribe manualmente el público objetivo o segmento si seleccionaste 'Personalizado'."
        )
        st.session_state["segmentation_custom"] = segmentation
    st.session_state["segmentation"] = segmentation

    # Campo de selección para Formato
    group_format_options = ["Introduce el tipo de formato", "Imagen", "Video", "Carrusel", "Audio", "Personalizado"]

    group_format = st.session_state.get("group_format", "Introduce el tipo de formato")
    if group_format not in group_format_options:
        group_format = "Introduce el tipo de formato"

    group_format_index = group_format_options.index(group_format)

    group_format = st.selectbox(
        "Formato, (opcional, si todos los anuncios dentro del grupo comparten el formato):",
        group_format_options,
        index=group_format_index
    )

    if group_format == "Personalizado":
        group_format = st.text_input(
            "Introduce manualmente el formato",
            st.session_state.get("group_format_custom", ""),
            help="Escribe manualmente el formato si seleccionaste 'Personalizado'."
        )
        st.session_state["group_format_custom"] = group_format

    st.session_state["group_format"] = group_format

    # Añadir Campos Personalizados para Grupos de Anuncios
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir para Grupos de Anuncios",
        min_value=0,
        max_value=10,
        value=st.session_state.get("num_campos_grupos", 0),
        step=1
    )
    st.session_state["num_campos_grupos"] = num_campos

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(
            f"Nombre del Campo personalizado Grupo de Anuncio {i + 1}",
            st.session_state.get(f"nombre_campo_grupo_{i}", "")
        )
        valor_campo = st.text_input(
            f"Valor para {nombre_campo}",
            st.session_state.get(f"valor_campo_grupo_{i}", "")
        )
        st.session_state[f"nombre_campo_grupo_{i}"] = nombre_campo
        st.session_state[f"valor_campo_grupo_{i}"] = valor_campo
        if valor_campo:
            campos_personalizados.append(valor_campo)

    # Añadir un selectbox para elegir la estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        index=0
    )
    st.session_state["structure_type"] = structure_type

    # Generar nomenclatura para Grupo de Anuncios según la estructura seleccionada
    nomenclature_parts = [segmentation, group_format] + campos_personalizados

    if any(part.startswith("Introduce") for part in nomenclature_parts) or not any(nomenclature_parts):
        group_nomenclature = ""  # Mostrar cuadro vacío hasta que los campos estén completos
    else:
        if structure_type == "Estructura clásica (_)":
            group_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Estructura clásica
        elif structure_type == "Estructura con corchetes ([valor]-[valor])":
            group_nomenclature = '-'.join([f"[{part}]" for part in filter(None, nomenclature_parts)])  # Estructura con corchetes

    st.session_state["group_nomenclature"] = group_nomenclature

    # Mostrar la nomenclatura en un cuadro estilizado
    st.subheader("Nomenclatura de Grupo de Anuncios generada:")
    st.markdown(
        f"""
        <div style="background-color:#e0f7fa; padding:10px; border-radius:5px; border: 1px solid #81d4fa;">
            <p style="color:#0277bd; font-size:16px; font-family:monospace;">{group_nomenclature}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    return group_nomenclature

def nivel_anuncios():
    st.header("Nivel 3: Anuncios")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 3: Anuncios")
        st.write("""
        Define los detalles específicos del anuncio, como el tipo de creativo, la variante para pruebas A/B y un identificador único del anuncio.
        Puedes añadir campos personalizados para especificar más detalles si es necesario.
        """)

    # Campo de selección para Tipo de Creativo
    type_creative_options = ["Introduce el tipo de creativo", "Personalizado", "Video", "Imagen", "Carousel", "Banner", "Audio", "Native", "Pop-up"]
    type_creative_default = "Introduce el tipo de creativo"

    # Verificamos si el valor actual está en las opciones; si no, usamos el valor predeterminado
    current_type_creative = st.session_state.get("type_creative", type_creative_default)
    if current_type_creative not in type_creative_options:
        current_type_creative = type_creative_default

    # Configuramos el selectbox con un índice seguro
    type_creative = st.selectbox(
        "Tipo de Creativo",
        type_creative_options,
        index=type_creative_options.index(current_type_creative),
        help="Selecciona el tipo de creativo o introduce uno manual."
    )

    # Guardamos en session_state
    if type_creative == "Personalizado":
        type_creative = st.text_input(
            "Introduce el tipo de creativo",
            st.session_state.get("type_creative_custom", ""),
            help="Escribe el tipo de creativo si seleccionaste 'Personalizado'."
        )
        st.session_state["type_creative_custom"] = type_creative

    st.session_state["type_creative"] = type_creative

    # Campo manual para la variación creativa
    variant = st.text_input(
        "Variación creativa (introduce el valor manualmente para pruebas A/B)",
        st.session_state.get("variant", ""),
        help="Especifica la variante para las pruebas A/B (e.g., A, B, etc.)."
    )
    st.session_state["variant"] = variant

    # Nuevo campo: Ángulo creativo
    creative_angle = st.text_input(
        "Ángulo creativo (introduce el valor manualmente)",
        st.session_state.get("creative_angle", ""),
        help="Especifica el ángulo creativo del anuncio (e.g., Oferta, Solución, Innovación, etc.)."
    )
    st.session_state["creative_angle"] = creative_angle

    # Campo manual para ID del Anuncio
    ad_id = st.text_input(
        "ID del Anuncio (opcional, introduce el valor manualmente)",
        st.session_state.get("ad_id", ""),
        help="Introduce un identificador único para el anuncio."
    )
    st.session_state["ad_id"] = ad_id

    # Añadir Campos Personalizados para Anuncios
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input(
        "Número de campos personalizados a añadir para Anuncios",
        min_value=0,
        max_value=10,
        value=st.session_state.get("num_campos_anuncios", 0),
        step=1
    )
    st.session_state["num_campos_anuncios"] = num_campos

    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(
            f"Nombre del Campo personalizado Anuncio {i + 1}",
            st.session_state.get(f"nombre_campo_anuncio_{i}", "")
        )
        valor_campo = st.text_input(
            f"Valor para {nombre_campo}",
            st.session_state.get(f"valor_campo_anuncio_{i}", "")
        )
        st.session_state[f"nombre_campo_anuncio_{i}"] = nombre_campo
        st.session_state[f"valor_campo_anuncio_{i}"] = valor_campo
        if valor_campo:
            campos_personalizados.append(valor_campo)

    # Añadir un selectbox para elegir la estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        index=0
    )
    st.session_state["structure_type"] = structure_type

    # Generar nomenclatura para Anuncio según la estructura seleccionada
    nomenclature_parts = [type_creative, variant, creative_angle, ad_id] + campos_personalizados

    if any(part.startswith("Introduce") for part in nomenclature_parts) or not any(nomenclature_parts):
        ad_nomenclature = ""  # Mostrar cuadro vacío hasta que los campos estén completos
    else:
        if structure_type == "Estructura clásica (_)":
            ad_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Estructura clásica
        elif structure_type == "Estructura con corchetes ([valor]-[valor])":
            ad_nomenclature = '-'.join([f"[{part}]" for part in filter(None, nomenclature_parts)])  # Estructura con corchetes

    st.session_state["ad_nomenclature"] = ad_nomenclature

    # Mostrar la nomenclatura en un cuadro estilizado
    st.subheader("Nomenclatura de Anuncio generada:")
    st.markdown(
        f"""
        <div style="background-color:#e0f7fa; padding:10px; border-radius:5px; border: 1px solid #81d4fa;">
            <p style="color:#0277bd; font-size:16px; font-family:monospace;">{ad_nomenclature}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Botón de copiar usando HTML y JavaScript
    copy_button_code = f"""
        <style>
            .copy-button {{
                background-color: #0277bd;
                color: white;
                font-size: 18px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            .copy-button:hover {{
                background-color: #01579b;
            }}
        </style>
        <button class="copy-button" onclick="copyToClipboard()">Copiar Nomenclatura de Anuncio</button>
        <script>
            function copyToClipboard() {{
                var text = `{ad_nomenclature}`;
                navigator.clipboard.writeText(text).then(function() {{
                    alert('Copiado al portapapeles');
                }}, function(err) {{
                    console.error('Error al copiar: ', err);
                }});  
            }}
        </script>
    """
    st.components.v1.html(copy_button_code)

    return ad_nomenclature


def nivel_utms(campaign_nomenclature, group_nomenclature, ad_nomenclature):
    st.header("Nivel 4: UTMs")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 4: UTMs")
        st.write("""
        Genera la URL con parámetros UTM para el seguimiento de la campaña publicitaria.
        Configura la fuente, el medio, la campaña y otros parámetros para crear un enlace rastreable.
        """)

    # Campo personalizado para URL base
    base_url = st.text_input("URL base para la campaña", "https://midominio.com", help="Introduce la URL base sobre la cual se construirán los parámetros UTM.")

    # Campos predefinidos para UTMs
    source = st.selectbox("Fuente (utm_source)", ["Google", "Facebook", "LinkedIn", "Newsletter"])
    medium = st.selectbox("Medio (utm_medium)", ["CPC", "Display", "Email", "Social"])

    # Lógica para mostrar valores heredados o permitir edición
    if campaign_nomenclature:
        campaign_utm = st.text_input(
            "Campaña (utm_campaign)",
            campaign_nomenclature,
            help="Este campo ya contiene la campaña heredada, pero puedes ajustarlo si es necesario."
        )
    else:
        campaign_utm = st.text_input(
            "Campaña (utm_campaign)",
            "",
            help="Introduce el nombre de la campaña si no se hereda de los niveles anteriores."
        )

    if group_nomenclature:
        term_utm = st.text_input(
            "Término (utm_term)",
            group_nomenclature,
            help="Este campo ya contiene el término heredado, pero puedes ajustarlo si es necesario."
        )
    else:
        term_utm = st.text_input(
            "Término (utm_term)",
            "",
            help="Introduce el término relacionado al grupo de anuncios si no se hereda de los niveles anteriores."
        )

    if ad_nomenclature:
        content_utm = st.text_input(
            "Contenido (utm_content)",
            ad_nomenclature,
            help="Este campo ya contiene el contenido heredado, pero puedes ajustarlo si es necesario."
        )
    else:
        content_utm = st.text_input(
            "Contenido (utm_content)",
            "",
            help="Introduce el contenido relacionado al anuncio si no se hereda de los niveles anteriores."
        )

    # Construir los parámetros UTM
    utm_parts = [
        f"utm_source={source}",
        f"utm_medium={medium}",
        f"utm_campaign={campaign_utm}"
    ]

    if content_utm:
        utm_parts.append(f"utm_content={content_utm}")
    if term_utm:
        utm_parts.append(f"utm_term={term_utm}")

    # Validar si todos los campos obligatorios tienen valores válidos
    if base_url.startswith("http") and campaign_utm:
        utm_nomenclature = f"{base_url}?{'&'.join(utm_parts)}"
    else:
        utm_nomenclature = ""  # Mostrar vacío si falta algún campo obligatorio

    # Mostrar la URL generada en un cuadro estilizado
    st.subheader("URL con Nomenclatura de UTM generada:")
    st.markdown(
        f"""
        <div style="background-color:#e0f7fa; padding:10px; border-radius:5px; border: 1px solid #81d4fa;">
            <p style="color:#0277bd; font-size:16px; font-family:monospace;">{utm_nomenclature}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Botón de copiar usando HTML y JavaScript
    copy_button_code = f"""
        <style>
            .copy-button {{
                background-color: #0277bd;
                color: white;
                font-size: 18px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            .copy-button:hover {{
                background-color: #01579b;
            }}
        </style>
        <button class="copy-button" onclick="copyToClipboard()">Copiar URL con Nomenclatura de UTM</button>
        <script>
            function copyToClipboard() {{
                var text = `{utm_nomenclature}`;
                navigator.clipboard.writeText(text).then(function() {{
                    alert('Copiado al portapapeles');
                }}, function(err) {{
                    console.error('Error al copiar: ', err);
                }});  
            }}
        </script>
    """
    st.components.v1.html(copy_button_code)

    return utm_nomenclature






def exportar_nomenclaturas(campaign_nomenclature, group_nomenclature, ad_nomenclature, utm_nomenclature):
    # Exportar todas las nomenclaturas en un resumen
    st.header("Resumen de Nomenclaturas Generadas")
    data = {
        "Nivel": ["Campaña", "Grupo de Anuncios", "Anuncio", "UTM"],
        "Nomenclatura": [campaign_nomenclature, group_nomenclature, ad_nomenclature, utm_nomenclature]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, width=1000)  # Ajuste para visualizar completamente la nomenclatura UTM

    # Botón para descargar como Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Nomenclaturas')
        writer.book.close()
        st.download_button(
            label="Descargar nomenclaturas como Excel",
            data=output.getvalue(),
            file_name="nomenclaturas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )



def acerca_de():
    st.title("Acerca de")
    st.write("""
    **¡Hola, encantado de saludarte!**

    Soy Jordi Quiroga, 
    analista de datos, especialista en integración de fuentes y científico de datos en proyecto. 

    Llevo más de 15 años ayudando a agencias y profesionales del marketing a transformar sus datos en insights accionables.
    
    He creado esta herramienta para solucionar uno de los problemas más frustrantes que encuentro en el día a día con mis clientes: la falta de consistencia en las nomenclaturas.
   
    Esta situación, que muchas veces pasa desapercibida, siempre lleva a un escenario de error seguro cuando se quieren integrar las fuentes para hacer un buen análisis y una gestión eficiente de las campañas.
    
    Esta aplicación pretende ayudar a los profesionales del marketing y a sus equipos a dar el primer paso hacia la automatización de procesos mediante la adquisición de buenas prácticas tecnológicas que brillan por su eficiencia y notable ahorro de tiempo y recursos.
    
    Estás ante una prueba de concepto. La herramienta la sigo mejorando día a día con tus comentarios. Si quieres dejarme feedback o que personalice esta aplicación para tí, puedes hacerlo a través de esta dirección: **jordi@jordiquiroga.com**

    Puedes descubrir más sobre mi en mi sitio web y en mi perfil de linkedin
                 
    """)
    st.write("**Sitio web:** https://www.jordiquiroga.com")
    st.write("**Perfil de LinkedIn:** [Jordi Quiroga Fernández](https://www.linkedin.com/in/jordiquirogafernandez/)")
    st.image("images/Jordi-portrait.jpg", caption="Jordi Quiroga", width=200)


if __name__ == "__main__":
    if 'campaign_nomenclature' not in st.session_state:
        st.session_state['campaign_nomenclature'] = ""
    if 'group_nomenclature' not in st.session_state:
        st.session_state['group_nomenclature'] = ""
    if 'ad_nomenclature' not in st.session_state:
        st.session_state['ad_nomenclature'] = ""
    if 'utm_nomenclature' not in st.session_state:
        st.session_state['utm_nomenclature'] = ""
    main()






