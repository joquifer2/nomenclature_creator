import streamlit as st
import pandas as pd
from io import BytesIO
from collections import OrderedDict


def check_password():
    """Función que pide al usuario la contraseña y la valida.
       Retorna True si es correcta, False si no."""
    
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    # Solo mostramos el formulario si no está autenticado
    if not st.session_state["password_correct"]:
        st.subheader("Por favor, ingresa la clave para acceder")
        
        pwd_input = st.text_input("Contraseña:", type="password")
        if st.button("Enviar"):
            SECRET_PASSWORD = "1234"  # <-- O usa st.secrets["password"]
            
            if pwd_input == SECRET_PASSWORD:
                st.session_state["password_correct"] = True
                st.success("Contraseña correcta. ¡Bienvenido!")
                # Al poner st.experimental_rerun(), se volverá a dibujar la app
                st.experimental_rerun()
            else:
                st.error("Contraseña incorrecta. Inténtalo de nuevo.")
                st.stop()  # Evitamos que se ejecute el resto de la app

    # Si ya está autenticado, simplemente retornamos True
    return st.session_state["password_correct"]



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
# FUNCIÓN PARA CAPITALIZAR LA PRIMERA LETRA
# ======================================

def capitalize_first_letter(text):  # <-- Nuevo
    """
    Recibe un string y devuelve ese mismo string
    pero con la primera letra en mayúscula (si la hay).
    """
    return text[:1].upper() + text[1:] if text else ""

# ======================================
# FUNCIÓN PRINCIPAL (MAIN)
# ======================================
def main():
# 1) VERIFICAR CONTRASEÑA
    if not check_password():
        st.stop()  # Si la contraseña no es correcta, paramos la ejecución aquí mismo.
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
    

def nivel_campanas():
    st.header("Nivel 1: Campañas")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    with st.sidebar:
        st.subheader("Nivel 1: Campañas")
        st.write("""
        En esta pantalla puedes configurar los parámetros principales de la campaña, 
        como la plataforma, red publicitaria, tipo de embudo, tipo de tráfico, u objetivo publicitario, entreo otros.
        También puedes añadir campos personalizados para describir más detalladamente la campaña.
        """)

    # ---------------------------
    # CAMPOS PRINCIPALES
    # ---------------------------
    platform_options = ["Selecciona la plataforma publicitaria", "MT","IG","FB","GG","YT","TT","LK","Personalizado"]
    platform = st.selectbox(
        "Plataforma publicitaria (MT=Meta, IG=Instagram, FB=Facebook,  GG=Google, YT= Youtube...)",
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

    ad_network_options = ["Selecciona la red publicitaria", "Social", "Search", "GDN", "PMAX", "DIS", "Personalizado"]
    network = st.selectbox(
        "Red publicitaria, si procede (Social, Search, Display, PMAX, Discovery...)",
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

    funnel_type_options = ["Selecciona el tipo de embudo", "LM", "WB", "VSL", "Personalizado"]
    funnel_type = st.selectbox(
        "Tipo de embudo, si procede (LM=Lead Magnet, WB=Webinar, VSL...)",
        funnel_type_options,
        key="funnel_type",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if funnel_type == "Personalizado":
        funnel_type = st.text_input(
            "Introduce manualmente el tipo de embudo",
            key="funnel_type_custom",
            help="Escribe manualmente el tipo de embudo si seleccionaste 'Personalizado'."
        )

    traffic_type_options = ["Selecciona el tipo de tráfico", "TF", "TT", "TC", "Personalizado"]
    traffic_type = st.selectbox(
        "Tipo de tráfico, si procede (TF= Tráfico frío, TT= Tráfico templado, TC= Tráfico caliente...)",
        traffic_type_options,
        key="trafrc_type",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if traffic_type == "Personalizado":
        traffic_type = st.text_input(
            "Introduce manualmente el tipo de tráfico",
            key="traffic_type_custom",
            help="Escribe el acrónimo del tipo de tráfico si seleccionaste 'Personalizado'."
        )

    objective_options = ["Selecciona el objetivo de campaña", "AW", "TR", "IT","CP", "VT", "Personalizado"]
    objective = st.selectbox(
        "Objetivo publicitario, si procede (AW= Awareness, TR= Tráfico, IT= Interacción, CP=Clientes potenciales, VT= Ventas...)",
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
            valor_campo = capitalize_first_letter(valor_campo)
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura de la nomenclatura (clásica o con corchetes)
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_campaign",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # ======================================
    # MOSTRAR VISTA PREVIA SIN BOTÓN
    # ======================================
    # 1) Construimos en tiempo real la lista 'parts_preview'
    parts_preview = [
        p for p in [
            platform, network, funnel_type, traffic_type, objective, campaign_type
            # Eliminados: product, promotion
        ]
        if p and not p.startswith("Selecciona") and not p.startswith("Introduce")
    ]
    for _, valor_campo in campos_personalizados:
        parts_preview.append(valor_campo)

    # 2) Creamos la nomenclatura de vista previa
    if len(parts_preview) == 0:
        campaign_preview = ""
    else:
        if structure_type == "Estructura clásica (_)":
            campaign_preview = "_".join(parts_preview)
        else:
            campaign_preview = "-".join(f"[{p}]" for p in parts_preview)

    # 3) Creamos un diccionario "temporal" con los campos (y la nomenclatura) para mostrarlo
    pre_dict = OrderedDict()
    if platform and not platform.startswith("Selecciona") and not platform.startswith("Introduce"):
        pre_dict["Plataforma"] = platform
    if network and not network.startswith("Selecciona") and not network.startswith("Introduce"):
        pre_dict["Red"] = network
    if funnel_type and not funnel_type.startswith("Selecciona") and not funnel_type.startswith("Introduce"):
        pre_dict["Tipo de embudo"] = funnel_type
    if traffic_type and not traffic_type.startswith("Selecciona") and not traffic_type.startswith("Introduce"):
        pre_dict["Tipo de tráfico"] = traffic_type
    if objective and not objective.startswith("Selecciona") and not objective.startswith("Introduce"):
        pre_dict["Objetivo"] = objective
    if campaign_type and not campaign_type.startswith("Selecciona") and not campaign_type.startswith("Introduce"):
        pre_dict["Tipo de campaña"] = campaign_type

    # (Eliminadas referencias a "Producto" y "Promoción")

    for n_cp, v_cp in campos_personalizados:
        pre_dict[n_cp] = v_cp

    pre_dict["Nomenclatura (Vista Previa)"] = campaign_preview

    # 4) Mostramos la vista previa en pantalla
    st.subheader("Vista Previa de la Campaña (Aún No Guardada)")
    if len(pre_dict) == 1 and pre_dict.get("Nomenclatura (Vista Previa)") == "":
        st.info("No hay nada que mostrar. Completa campos para ver la vista previa.")
    else:
        df_temporal = pd.DataFrame([pre_dict])
        st.dataframe(df_temporal)

    # ======================================
    # BOTÓN PARA GUARDAR CAMPaña
    # ======================================
    if st.button("Guardar Campaña"):
        # Movemos "Nomenclatura (Vista Previa)" --> "Nomenclatura generada"
        final_dict = OrderedDict(pre_dict)
        final_nomenclature = final_dict.pop("Nomenclatura (Vista Previa)", "")
        final_dict["Nomenclatura generada"] = final_nomenclature

        # Guardamos en la lista global
        if "campaign_data_list" not in st.session_state:
            st.session_state["campaign_data_list"] = []
        st.session_state["campaign_data_list"].append(dict(final_dict))

        st.success(f"Campaña guardada. Nomenclatura generada: {final_nomenclature}")
        st.experimental_rerun()

    # ======================================
    # LISTADO DE CAMPAÑAS GUARDADAS
    # ======================================
    st.subheader("Campañas guardadas hasta ahora:")
    if "campaign_data_list" not in st.session_state or len(st.session_state["campaign_data_list"]) == 0:
        st.info("No has guardado ninguna campaña todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["campaign_data_list"])
        st.dataframe(df_preview)




def nivel_grupos_anuncios():
    st.header("Nivel 2: Grupos de Anuncios")
    st.warning("Si no quieres que aparezca algún campo, selecciona -Personalizado- y déjalo en blanco.")

    with st.sidebar:
        st.subheader("Nivel 2: Grupos de Anuncios")
        st.write("""
        Configura las características del grupo de anuncios, incluyendo la audiencia, segmentación o el formato.
        Además, puedes añadir campos personalizados para definir mejor las características del grupo de anuncios.
        """)

    # Campos principales
    segmentation_options = ["Introduce la audiencia o segmento", "AVG+", "LKL", "INT", "KW", "BD","VIS", "Personalizado"]
    segmentation = st.selectbox(
        "Audiencia o tipo de segmentación (AVG+= Advantatge+, LKL= lookalikes, INT= Intereses, KW= keywords, BD= Bbdd, VIS= Visitantes...)",
        segmentation_options,
        key="segmentation",
        help="Si no quieres que aparezca, selecciona 'Personalizado' y déjalo en blanco."
    )
    if segmentation == "Personalizado":
        segmentation = st.text_input(
            "Introduce manualmente el tipo de audiencia o segmentación",
            key="segmentation_custom",
            help="Escribe manualmente el tipo de audiencia o segmento si seleccionaste 'Personalizado'."
        )

    group_format_options = ["Introduce el tipo de formato", "Imagen", "Video", "Carrusel", "Audio", "Personalizado"]
    group_format = st.selectbox(
        "Formato (opcional, si todos los anuncios dentro del grupo comparten el formato)",
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

    # Campos personalizados
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
            valor_campo = capitalize_first_letter(valor_campo)
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura de la nomenclatura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_group",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # ======================================
    # VISTA PREVIA EN TIEMPO REAL
    # ======================================
    parts_preview = []
    if segmentation and not segmentation.startswith("Introduce"):
        parts_preview.append(segmentation)
    if group_format and not group_format.startswith("Introduce"):
        parts_preview.append(group_format)
    for _, valor_campo in campos_personalizados:
        parts_preview.append(valor_campo)

    if len(parts_preview) == 0:
        group_preview = ""
    else:
        if structure_type == "Estructura clásica (_)":
            group_preview = "_".join(parts_preview)
        else:
            group_preview = "-".join(f"[{p}]" for p in parts_preview)

    pre_dict = OrderedDict()
    if segmentation and not segmentation.startswith("Introduce"):
        pre_dict["Segmentación"] = segmentation
    if group_format and not group_format.startswith("Introduce"):
        pre_dict["Formato"] = group_format
    for (n_cp, v_cp) in campos_personalizados:
        pre_dict[n_cp] = v_cp

    # Agregamos la clave de vista previa
    pre_dict["Nomenclatura (Vista Previa)"] = group_preview

    # Mostramos la vista previa
    st.subheader("Vista Previa del Grupo de Anuncios (Aún No Guardado)")
    if len(pre_dict) == 1 and pre_dict.get("Nomenclatura (Vista Previa)") == "":
        st.info("No hay nada que mostrar. Completa campos para ver la vista previa.")
    else:
        df_temporal = pd.DataFrame([pre_dict])
        st.dataframe(df_temporal)

    # ======================================
    # BOTÓN PARA GUARDAR
    # ======================================
    if st.button("Guardar Grupo de Anuncios"):
        final_dict = OrderedDict(pre_dict)
        final_nomenclature = final_dict.pop("Nomenclatura (Vista Previa)", "")
        final_dict["Nomenclatura generada"] = final_nomenclature

        if "group_data_list" not in st.session_state:
            st.session_state["group_data_list"] = []
        st.session_state["group_data_list"].append(dict(final_dict))

        st.success(f"Grupo de Anuncios guardado. Nomenclatura: {final_nomenclature}")
        st.experimental_rerun()

    # ======================================
    # LISTADO DE GRUPOS GUARDADOS
    # ======================================
    st.subheader("Grupos de Anuncios guardados hasta ahora:")
    if "group_data_list" not in st.session_state or len(st.session_state["group_data_list"]) == 0:
        st.info("No has guardado ningún grupo de anuncios todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["group_data_list"])
        st.dataframe(df_preview)



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

    # Campos principales
    type_creative_options = ["Introduce el tipo de creativo", "VD", "IMG", "CAR", "BN", "AUD", "Personalizado"]
    type_creative = st.selectbox(
        "Tipo de Creativo (VD= Video, IMG= Imagen, CAR= Carrusel, BN= Banner, AUD= Audio)",
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

    

    # Campos personalizados
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
            valor_campo = capitalize_first_letter(valor_campo)
            campos_personalizados.append((nombre_campo, valor_campo))

    # Estructura
    structure_type = st.selectbox(
        "Elige la estructura para la nomenclatura:",
        ["Estructura clásica (_)", "Estructura con corchetes ([valor]-[valor])"],
        key="structure_type_ad",
        help="La forma en que se concatenarán los valores en la nomenclatura final."
    )

    # ======================================
    # VISTA PREVIA EN TIEMPO REAL
    # ======================================
    parts_preview = []
    if type_creative and not type_creative.startswith("Introduce"):
        parts_preview.append(type_creative)
    if variant:
        parts_preview.append(variant)
    if creative_angle:
        parts_preview.append(creative_angle)
    
    for _, valor_cp in campos_personalizados:
        parts_preview.append(valor_cp)

    if len(parts_preview) == 0:
        ad_preview = ""
    else:
        if structure_type == "Estructura clásica (_)":
            ad_preview = "_".join(parts_preview)
        else:
            ad_preview = "-".join(f"[{p}]" for p in parts_preview)

    pre_dict = OrderedDict()
    if type_creative and not type_creative.startswith("Introduce"):
        pre_dict["Tipo de creativo"] = type_creative
    if variant:
        pre_dict["Variación creativa"] = variant
    if creative_angle:
        pre_dict["Ángulo creativo"] = creative_angle
    
    for (n_cp, v_cp) in campos_personalizados:
        pre_dict[n_cp] = v_cp

    pre_dict["Nomenclatura (Vista Previa)"] = ad_preview

    # Mostramos la vista previa
    st.subheader("Vista Previa del Anuncio (Aún No Guardado)")
    if len(pre_dict) == 1 and pre_dict.get("Nomenclatura (Vista Previa)") == "":
        st.info("No hay nada que mostrar. Completa campos para ver la vista previa.")
    else:
        df_temporal = pd.DataFrame([pre_dict])
        st.dataframe(df_temporal)

    # ======================================
    # BOTÓN PARA GUARDAR
    # ======================================
    if st.button("Guardar Anuncio"):
        final_dict = OrderedDict(pre_dict)
        final_nomenclature = final_dict.pop("Nomenclatura (Vista Previa)", "")
        final_dict["Nomenclatura generada"] = final_nomenclature

        if "ad_data_list" not in st.session_state:
            st.session_state["ad_data_list"] = []
        st.session_state["ad_data_list"].append(dict(final_dict))

        st.success(f"Anuncio guardado. Nomenclatura: {final_nomenclature}")
        st.experimental_rerun()

    # ======================================
    # LISTADO DE ANUNCIOS GUARDADOS
    # ======================================
    st.subheader("Anuncios guardados hasta ahora:")
    if "ad_data_list" not in st.session_state or len(st.session_state["ad_data_list"]) == 0:
        st.info("No has guardado ningún anuncio todavía.")
    else:
        df_preview = pd.DataFrame(st.session_state["ad_data_list"])
        st.dataframe(df_preview)


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

    # ======================================
    # VISTA PREVIA EN TIEMPO REAL
    # ======================================
    # 1) Construimos la URL preliminar
    final_source = source if source and not source.startswith("Introduce") else ""
    final_medium = medium if medium and not medium.startswith("Introduce") else ""

    utm_url_preview = (
        f"{base_url}"
        f"?utm_source={final_source}"
        f"&utm_medium={final_medium}"
        f"&utm_campaign={campaign_utm}"
        f"&utm_term={term_utm}"
        f"&utm_content={content_utm}"
    )

    # 2) Previsualizamos en un diccionario
    pre_dict = OrderedDict()
    if base_url:
        pre_dict["URL Base"] = base_url
    if final_source:
        pre_dict["Fuente"] = final_source
    if final_medium:
        pre_dict["Medio"] = final_medium
    if campaign_utm:
        pre_dict["Campaña"] = campaign_utm
    if term_utm:
        pre_dict["Término"] = term_utm
    if content_utm:
        pre_dict["Contenido"] = content_utm

    pre_dict["URL (Vista Previa)"] = utm_url_preview

    # 3) Mostramos la vista previa
    st.subheader("Vista Previa de la UTM (Aún No Guardada)")
    if len(pre_dict) == 1 and pre_dict.get("URL (Vista Previa)") == f"{base_url}?utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=":
        st.info("No hay nada que mostrar. Completa más campos para ver la vista previa.")
    else:
        df_temporal = pd.DataFrame([pre_dict])
        st.dataframe(df_temporal)

    # ======================================
    # BOTÓN PARA GUARDAR UTM
    # ======================================
    if st.button("Guardar UTMs"):
        final_dict = OrderedDict(pre_dict)
        # Cambiamos "URL (Vista Previa)" -> "Nomenclatura generada" (o como quieras llamarlo)
        final_url = final_dict.pop("URL (Vista Previa)", "")
        final_dict["Nomenclatura generada"] = final_url

        if "utm_data_list" not in st.session_state:
            st.session_state["utm_data_list"] = []
        st.session_state["utm_data_list"].append(dict(final_dict))

        st.success(f"UTM guardada. URL generada: {final_url}")
        st.experimental_rerun()

    # ======================================
    # LISTADO DE UTMs GUARDADAS
    # ======================================
    st.subheader("UTMs guardadas hasta ahora:")
    if "utm_data_list" not in st.session_state or len(st.session_state["utm_data_list"]) == 0:
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




  







