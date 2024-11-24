import streamlit as st
import pandas as pd
from io import BytesIO
import pyperclip


def main():
    # Sidebar con los pasos del proceso
    st.sidebar.title("Pasos del Proceso de Nomenclatura")
    paso = st.sidebar.radio("Selecciona un paso para configurarlo:", [
        "Inicio",
        "Nivel 1: Campañas",
        "Nivel 2: Grupos de Anuncios",
        "Nivel 3: Anuncios",
        "Nivel 4: UTMs",
        "Exportar Nomenclaturas"
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
        campaign_nomenclature = st.session_state.get("campaign_nomenclature", "")
        group_nomenclature = st.session_state.get("group_nomenclature", "")
        ad_nomenclature = st.session_state.get("ad_nomenclature", "")
        if campaign_nomenclature and group_nomenclature and ad_nomenclature:
            utm_nomenclature = nivel_utms(campaign_nomenclature, group_nomenclature, ad_nomenclature)
            st.session_state["utm_nomenclature"] = utm_nomenclature
        else:
            st.warning("Por favor, completa los niveles anteriores antes de generar UTMs.")
    elif paso == "Exportar Nomenclaturas":
        exportar_nomenclaturas(
            st.session_state.get("campaign_nomenclature", ""),
            st.session_state.get("group_nomenclature", ""),
            st.session_state.get("ad_nomenclature", ""),
            st.session_state.get("utm_nomenclature", "")
        )


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

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 1: Campañas")
        st.write("""
        En esta pantalla puedes configurar los parámetros principales de la campaña, como la plataforma, el formato del anuncio, la audiencia y la geografía.
        También puedes añadir campos personalizados para describir más detalladamente la campaña.
        """)

    # Campos predefinidos para Campañas
    platform = st.selectbox("Plataforma", ["Meta", "Google", "LinkedIn", "TikTok"])
    ad_format = st.selectbox("Formato", ["Display", "Video", "Search", "Carousel", "Audio", "Native", "Banner", "Pop-up"])
    audience = st.selectbox("Audiencia", ["Prospectos", "Retargeting", "Clientes"])
    geography = st.selectbox("Geografía", ["ES", "LATAM", "EU", "Global"])

    # Campos manuales para Campañas
    product = st.text_input("Producto (introduce el valor manualmente)", "CursoSEO", help="Este campo es manual, puedes modificar el valor según el producto que desees.")
    if product and not product.istitle():
        st.warning("Por favor, asegúrate de que la primera letra de 'Producto' esté en mayúscula. Se ha capitalizado automáticamente.")
        product = product.capitalize()

    promotion = st.text_input("Promoción (introduce el valor manualmente)", "BlackFriday2024", help="Este campo es manual, personalizable para cada promoción.")
    if promotion and not promotion.istitle():
        st.warning("Por favor, asegúrate de que la primera letra de 'Promoción' esté en mayúscula. Se ha capitalizado automáticamente.")
        promotion = promotion.capitalize()

    objective = st.selectbox("Objetivo", ["Awareness", "Conversiones", "Leads", "Engagement", "Tráfico", "Ventas", "Registro"])

    # Añadir Campos Personalizados para Campañas
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input("Número de campos personalizados a añadir", min_value=0, max_value=10, value=0, step=1)
    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Campaña {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo and not valor_campo.istitle():
            st.warning("Por favor, asegúrate de que la primera letra del campo esté en mayúscula. Se ha capitalizado automáticamente.")
            valor_campo = valor_campo.capitalize()
        campos_personalizados.append(valor_campo)

    # Generar nomenclatura para Campaña
    nomenclature_parts = [platform, ad_format, audience, geography, product, promotion, objective] + [campo for campo in campos_personalizados if campo]
    campaign_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Añadiendo solo el valor del campo

    st.write("Nomenclatura de Campaña generada:", campaign_nomenclature)

    # Botón para copiar nomenclatura
    if st.button("Copiar Nomenclatura de Campaña"):
        pyperclip.copy(campaign_nomenclature)
        st.success("Nomenclatura de Campaña copiada al portapapeles.")

    return campaign_nomenclature


def nivel_grupos_anuncios():
    st.header("Nivel 2: Grupos de Anuncios")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 2: Grupos de Anuncios")
        st.write("""
        Configura las características del grupo de anuncios, incluyendo la segmentación y el formato.
        Además, puedes añadir campos personalizados para definir mejor las características del grupo de anuncios.
        """)

    # Campos predefinidos para Grupos de Anuncios
    segmentation = st.selectbox("Segmentación", ["Lookalike", "Intereses", "Keywords", "Engagement"])
    group_format = st.selectbox("Formato", ["Display", "Video", "Search", "Carousel", "Audio", "Native", "Banner", "Pop-up"])
    group_objective = st.selectbox("Objetivo", ["Awareness", "Conversion", "Leads", "Engagement", "Tráfico", "Ventas", "Registro"])

    # Campos manuales para Grupos de Anuncios
    creative_theme = st.text_input("Tema del Creativo (introduce el valor manualmente)", "Descuento", help="Este campo es manual, puedes modificarlo según el tema creativo del grupo de anuncios.")
    if creative_theme and not creative_theme.istitle():
        st.warning("Por favor, asegúrate de que la primera letra de 'Tema del Creativo' esté en mayúscula. Se ha capitalizado automáticamente.")
        creative_theme = creative_theme.capitalize()

    # Añadir Campos Personalizados para Grupos de Anuncios
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input("Número de campos personalizados a añadir para Grupos de Anuncios", min_value=0, max_value=10, value=0, step=1)
    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Grupo de Anuncio {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo and not valor_campo.istitle():
            st.warning("Por favor, asegúrate de que la primera letra del campo esté en mayúscula. Se ha capitalizado automáticamente.")
            valor_campo = valor_campo.capitalize()
        campos_personalizados.append(valor_campo)

    # Generar nomenclatura para Grupo de Anuncios
    nomenclature_parts = [segmentation, group_format, group_objective, creative_theme] + [campo for campo in campos_personalizados if campo]
    group_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Añadiendo solo el valor del campo

    st.write("Nomenclatura de Grupo de Anuncios generada:", group_nomenclature)

    # Botón para copiar nomenclatura
    if st.button("Copiar Nomenclatura de Grupo de Anuncios"):
        pyperclip.copy(group_nomenclature)
        st.success("Nomenclatura de Grupo de Anuncios copiada al portapapeles.")

    return group_nomenclature


def nivel_anuncios():
    st.header("Nivel 3: Anuncios")

    # Sidebar informativo
    with st.sidebar:
        st.subheader("Nivel 3: Anuncios")
        st.write("""
        Define los detalles específicos del anuncio, como el tipo de creativo, la variante para pruebas A/B y un identificador único del anuncio.
        Puedes añadir campos personalizados para especificar más detalles si es necesario.
        """)

    # Campos predefinidos para Anuncios
    type_creative = st.selectbox("Tipo de Creativo", ["Video", "Imagen", "Carousel", "Banner", "Audio", "Native", "Pop-up"])

    # Campos manuales para Anuncios
    variant = st.text_input("Variante (introduce el valor manualmente para pruebas A/B)", "A", help="Este campo es manual, especifica la variante para las pruebas A/B.")
    if variant and not variant.istitle():
        st.warning("Por favor, asegúrate de que la primera letra de 'Variante' esté en mayúscula. Se ha capitalizado automáticamente.")
        variant = variant.capitalize()

    ad_id = st.text_input("ID del Anuncio (opcional, introduce el valor manualmente)", "01", help="Este campo es manual y opcional, puedes personalizarlo según la identificación del anuncio.")
    if ad_id and not ad_id.istitle():
        st.warning("Por favor, asegúrate de que la primera letra de 'ID del Anuncio' esté en mayúscula. Se ha capitalizado automáticamente.")
        ad_id = ad_id.capitalize()

    # Añadir Campos Personalizados para Anuncios
    st.subheader("Añadir Campos Personalizados")
    num_campos = st.number_input("Número de campos personalizados a añadir para Anuncios", min_value=0, max_value=10, value=0, step=1)
    campos_personalizados = []
    for i in range(num_campos):
        nombre_campo = st.text_input(f"Nombre del Campo personalizado Anuncio {i + 1}")
        valor_campo = st.text_input(f"Valor para {nombre_campo}")
        if valor_campo and not valor_campo.istitle():
            st.warning("Por favor, asegúrate de que la primera letra del campo esté en mayúscula. Se ha capitalizado automáticamente.")
            valor_campo = valor_campo.capitalize()
        campos_personalizados.append(valor_campo)

    # Generar nomenclatura para Anuncio
    nomenclature_parts = [type_creative, variant, ad_id] + [campo for campo in campos_personalizados if campo]
    ad_nomenclature = '_'.join(filter(None, nomenclature_parts))  # Añadiendo solo el valor del campo

    st.write("Nomenclatura de Anuncio generada:", ad_nomenclature)

    # Botón para copiar nomenclatura
    if st.button("Copiar Nomenclatura de Anuncio"):
        pyperclip.copy(ad_nomenclature)
        st.success("Nomenclatura de Anuncio copiada al portapapeles.")

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

    # Campos dependientes y manuales para UTMs
    campaign_utm = st.text_input("Campaña (utm_campaign, introduce el valor manualmente)", campaign_nomenclature, help="Este campo es manual, puedes ajustar el nombre de la campaña.")
    content_utm = st.text_input("Contenido (utm_content, introduce el valor manualmente)", ad_nomenclature, help="Este campo es manual, ajusta según el contenido del anuncio.")
    term_utm = st.text_input("Término (utm_term, introduce el valor manualmente)", group_nomenclature, help="Este campo es manual, ajusta según el término relacionado al grupo de anuncios.")

    # Generar URL con nomenclatura para UTMs
    utm_parts = [
        f"utm_source={source}",
        f"utm_medium={medium}",
        f"utm_campaign={campaign_utm}"
    ]
    if content_utm:
        utm_parts.append(f"utm_content={content_utm}")
    if term_utm:
        utm_parts.append(f"utm_term={term_utm}")
    utm_nomenclature = f"{base_url}?{'&'.join(utm_parts)}"

    st.write("URL con Nomenclatura de UTM generada:", utm_nomenclature)

    # Botón para copiar nomenclatura
    if st.button("Copiar URL con Nomenclatura de UTM"):
        pyperclip.copy(utm_nomenclature)
        st.success("URL con Nomenclatura de UTM copiada al portapapeles.")

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





























