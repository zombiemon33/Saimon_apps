import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# ================== CONFIGURACIÓN GENERAL ==================

#PARA CREAR UN MODULO CON SUBMODULOS, HAY QUE INICIALIZAR EL SUBMODULO, Y LUEGO EL SESSION STATE EN USAR EL MENÚ

# ---------- INICIALIZAR ESTADO ----------
if "menu" not in st.session_state:
    st.session_state.menu = "Inicio"

if "submodulo" not in st.session_state:
    st.session_state.submodulo = "pediatria"

if "nefromodulo" not in st.session_state:
    st.session_state.nefromodulo = "nefro"

if "cardiomodulo" not in st.session_state:
    st.session_state.cardiomodulo = "cardio"

if "respimodulo" not in st.session_state:
    st.session_state.respimodulo = "respiratorio"

if "metamodulo" not in st.session_state:
    st.session_state.metamodulo = "metabolico"

if "hematomodulo" not in st.session_state:
    st.session_state.hematomodulo = "hemato"

if "ginecomodulo" not in st.session_state:
    st.session_state.ginecomodulo = "gineco"

st.set_page_config(
    page_title="HELEN M.O.R",
    page_icon="🩺"
)


st.sidebar.title("HELEN M.O.R")
st.sidebar.markdown("### Módulos clínicos")


# ---------- BOTONES ----------
if st.sidebar.button("🏠 Home"):
    st.session_state.menu = "Inicio"

if st.sidebar.button("🫁 Respiratorio"):
    st.session_state.menu = "respiratorio"

if st.sidebar.button("🫀 Cardiovascular"):
    st.session_state.menu = "cardio"

if st.sidebar.button("🟡 Endocrino-metabólico"):
    st.session_state.menu = "metabolico"

if st.sidebar.button("🩸 Hematología"):
    st.session_state.menu = "hemato"

if st.sidebar.button("🧴 Nefrología"):
    st.session_state.menu = "nefro"

if st.sidebar.button("🤱🏽👩🏽 Ginecobstetricia"):
    st.session_state.menu = "gineco"

if st.sidebar.button("👶Pediatría"):
    st.session_state.menu = "pediatria"

# ---------- USAR EL MENÚ ----------
menu = st.session_state.menu

submodulo = st.session_state.submodulo

nefromodulo = st.session_state.nefromodulo

cardiomodulo = st.session_state.cardiomodulo

respimodulo = st.session_state.respimodulo

hematomodulo = st.session_state.hematomodulo

ginecomodulo = st.session_state.ginecomodulo


# ================== INICIO ==========================================
#=====================================================================
#=====================================================================


if menu == "Inicio":
    col1,col2 = st.columns([1,3])

    with col1:
        st.image("helen_doctora.png",width=600)

    with col2:
     st.header("HELEN M.O.R.")
     st.write("¿Es un pájaro?¿Es un avión? No, es la heredera de I.V.A.N. MOR !!!")
     st.write("""
           HELEN M.O.R. es una plataforma clínica desarrollada con el fin de brindar herramientas
              para estudio y cálculo de variables que se utilizan frecuentemente en el área de la salud
              de una manera más sencilla.
    """)
     st.info("Selecciona un módulo en el menú lateral")





# ================== MODULO DE SISTEMA RESPIRATORIO ==================
#=====================================================================
#=====================================================================

elif menu == "respiratorio":

    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/lungs.png",width=360)

    with col2:
        st.header("Modulo de sistema respiratorio")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

    st.selectbox("Selecciona el cálculo",("Gases arteriales","Indice paquete-año")
                 , key="respimodulo")
    

    #AQUI SE CALCULAN LOS GASES ARTERIALES
    if st.session_state.respimodulo == "Gases arteriales":


        st.header("Análisis de Gases Arteriales")
        st.write("Ajusta los resultados de los gases arteriales de tu paciente")

        # -------- INPUTS --------
        ph = st.number_input("pH", 6.8, 7.8,  value=7.4, step=0.01)
        pco2 = st.number_input("PaCO₂ (mmHg)", 10.0, 100.0, value = 40.0, step=1.0)
        hco3 = st.number_input("HCO₃⁻ (mEq/L)", 5.0, 45.0, value = 24.0, step=1.0)
        po2 = st.number_input("PaO₂ (mmHg)", 20.0, 600.0, value = 90.0, step=1.0)
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, value = 21.0, step=1.0) / 100
        na = st.number_input("Na⁺ (mEq/L)", 100.0, 180.0, value = 140.0, step=1.0)
        cl = st.number_input("Cl⁻ (mEq/L)", 60.0, 140.0, value = 100.0, step=1.0)
        eb = st.number_input("Exceso de base (mmol/L)", -30.0, 30.0, value = 0.0, step=1.0)

        # -------- BOTÓN --------
        if st.button("Analizar gasometría"):

            dx = []
            causas = ""

            # -------- TRASTORNO PRIMARIO --------
            if ph < 7.35 and pco2 > 45:
                dx.append("acidosis respiratoria")
                causas += "Depresión respiratoria, EPOC, enfermedades neuromusculares. "

            if ph > 7.45 and pco2 < 35:
                dx.append("alcalosis respiratoria")
                causas += "Sepsis, hepatopatía, embarazo, hiperventilación. "

            if ph > 7.45 and hco3 > 26:
                dx.append("alcalosis metabolica")
                causas += "Vómitos, diuréticos, exceso de mineralocorticoides. "

            if ph < 7.35 and hco3 < 22:
                dx.append("acidosis metabolica")

            # -------- pH NORMAL (SOSPECHA MIXTO) --------
            if 7.35 <= ph <= 7.45:
                if pco2 < 35 and hco3 < 22:
                    dx.append("alcalosis respiratoria")
                if pco2 > 45 and hco3 > 26:
                    dx.append("acidosis respiratoria")
                if pco2 < 35 and hco3 > 26:
                    dx.extend(["alcalosis respiratoria", "alcalosis metabolica"])
                if pco2 > 45 and hco3 < 22:
                    dx.extend(["acidosis respiratoria", "acidosis metabolica"])

            # -------- MIXTO --------
            if ("acidosis respiratoria" in dx and "acidosis metabolica" in dx) or \
            ("alcalosis respiratoria" in dx and "alcalosis metabolica" in dx):
                dx = ["Trastorno mixto"]
                causas = "Alteraciones ácido–base coexistentes."


            # -------- SIN TRASTORNOS --------
            if 7.35 <= ph <= 7.45 and 35 <= pco2 <= 45 and 22 <= hco3 <= 26:
                dx.append("Sin estado ácido base alterado")

            # -------- COMPENSACIÓN RESPIRATORIA --------
            try:
                if dx[0] in ["acidosis respiratoria", "alcalosis respiratoria"]:
                    eb_esperado = (pco2 - 40) * 0.4

                    if abs(eb) < 2:
                        dx.append("aguda")
                    else:
                        if abs(eb - eb_esperado) <= 2:
                            dx.append("crónica compensada")
                        elif eb > eb_esperado + 2:
                            dx.append("con alcalosis metabólica agregada")
                        else:
                            dx.append("con acidosis metabólica agregada")

            except:
                pass

            # -------- COMPENSACIÓN METABÓLICA --------
            try:
                if dx[0] == "acidosis metabolica":
                    pco2_esp = (1.5 * hco3) + 8
                    dx.append("compensada" if abs(pco2 - pco2_esp) <= 2 else "no compensada")

                if dx[0] == "alcalosis metabolica":
                    pco2_esp = (0.7 * hco3) + 21
                    dx.append("compensada" if abs(pco2 - pco2_esp) <= 2 else "no compensada")
            except:
                pass

            # -------- ANIÓN GAP --------
            try:
                if "acidosis" in dx[0]:
                    ag = na - (cl + hco3)
                    if ag > 12:
                        dx.append("con anión gap elevado")
                        causas += "Cetoacidosis, acidosis láctica, insuficiencia renal. "
                    else:
                        dx.append("hiperclorémica")

            except:
                pass

            # -------- OXIGENACIÓN --------
            paffi = po2 / fio2
            if paffi > 300:
                dx.append("sin hipoxemia")
            elif 200 < paffi <= 300:
                dx.append("hipoxemia leve")
            else:
                dx.append("SDRA moderado o grave")

            try:
                if dx[0] == "" or dx[0] not in ["alcalosis respiratoria","alcalosis metabolica","acidosis metabólica","acidosis respiratoria", "trastorno mixto","Sin estado ácido base alterado"]:
                    dx.append(". No encuentro un diagnóstico claro, ¿Estas simulando?")
                    causas = causas + "Ninguna"

            except:
                pass

            # -------- RESULTADOS --------
            st.success("Diagnóstico")
            st.write(" ".join(dx))

            st.info("Posibles causas")
            st.write(causas)

    
    #AQUI SE CALCULA EL IPA
    elif st.session_state.respimodulo == "Indice paquete-año":

        st.header("Índice Paquetes-Año (IPA)")

        # ---------- INPUTS ----------
        ncigarros = st.number_input(
            "Número de cigarrillos al día",
            min_value=0,
            max_value=200,
            step=1
        )

        añosfuma = st.text_input(
            "Años fumando (o rango de edades, ej: 18-35)"
        )

        # ---------- FUNCIÓN RESTA ----------
        def resta(dato):
            x = dato.split("-")
            a = int(x[1]) - int(x[0])
            return a

        # ---------- BOTÓN ----------
        if st.button("Calcular IPA"):

            try:
                # ---------- Años fumando ----------
                if "-" in añosfuma:
                    años = resta(añosfuma)
                else:
                    años = float(añosfuma.replace(",", ".").replace(" ", ""))

                # ---------- Cálculo IPA ----------
                ipa = (ncigarros * años) / 20

                st.success(f"IPA: {round(ipa,2)} paquetes/año")

                # ---------- Clasificación ----------
                if ipa < 5:
                    st.info("Grado de tabaquismo: Leve.")
                elif 5 <= ipa <= 15:
                    st.warning("Grado de tabaquismo: Moderado.")
                elif 16 <= ipa <= 25:
                    st.error("Grado de tabaquismo: Grave.")
                elif ipa > 25:
                    st.error("Grado de tabaquismo: Muy grave.")

            except Exception:
                st.error("Ups, error al ingresar los datos. Inténtalo de nuevo.")





# ================== SISTEMA METABÓLICO-ENDOCRINO ==================
#=====================================================================
#=====================================================================

elif menu == "metabolico":

    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/liver.png",width=360)

    with col2:
        st.header("Modulo de sistema metabólico-endocrino")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

    st.selectbox("Selecciona el cálculo",("IMC","Perfil lipídico","Sodio corregido")
                 , key="metamodulo")
    
    
    #AQUI SE CALCULA EL IMC
    if st.session_state.metamodulo == "IMC":


        st.header("Calcula el IMC")
        st.info("Introduce tu peso y tu talla.")

        masa = st.number_input("Masa (kg)")
        estatura = st.number_input("Estatura (m)")

        if st.button("Calcular IMC"):

            imc = masa / (estatura**2)
            st.write("IMC es " + str(round(imc,2)) + "Kg/m2")

            if imc < 18.5:
                st.write("~Su clasificación corresponde a: Delgadez o bajo peso.")
                st.write(
                    "Te recomendamos subir "
                    + str(round(-masa + 21.7 * (estatura ** 2), 2))
                    + " kg."
                )

            elif 18.5 <= imc <= 24.9:
                st.write("~Su clasificación corresponde a: Peso normal o saludable.")

            elif 25.0 <= imc <= 29.9:
                st.write("~Su clasificacion corresponde a: Sobrepeso.")
                st.write(
                    "Te recomendamos bajar "
                    + str(round(masa - 21.7 * (estatura ** 2), 2))
                    + " kg."
                )

            elif 30 <= imc <= 34.9:
                st.write("~Su clasificacion corresponde a: Obesidad I o moderada.")
                st.write(
                    "Te recomendamos bajar "
                    + str(round(masa - 21.7 * (estatura ** 2), 2))
                    + " kg."
                )

            elif 35 <= imc <= 39.9:
                st.write("~Su clasificacion corresponde a: Obesidad II o severa.")
                st.write(
                    "Te recomendamos bajar "
                    + str(round(masa - 21.7 * (estatura ** 2), 2))
                    + " kg."
                )

            elif imc >= 40.0:
                st.write("~Su clasificacion corresponde a: Obesidad III o mórbida.")
                st.write(
                    "Te recomendamos bajar "
                    + str(round(masa - 21.7 * (estatura ** 2), 2))
                    + " kg."
                )      

    #AQUI SE CALCULA EL PERFIL LIPÍDICO
    elif st.session_state.metamodulo == "Perfil lipídico":

        st.header("Perfil lipídico (LDL, HDL, Triglicéridos)")
        st.info("Usamos la ecuación de Friedewald utilizada para estimar LDL")

        sexo = st.radio("Sexo biológico", ["Hombre", "Mujer"])

        colesteroltotal = st.number_input(
            "Colesterol total (mg/dL)",
            min_value=0.0,
            step=1.0
        )

        hdl = st.number_input(
            "Colesterol HDL (mg/dL)",
            min_value=0.0,
            step=1.0
        )

        trigliceridos = st.number_input(
            "Triglicéridos (mg/dL)",
            min_value=0.0,
            step=1.0
        )

        if st.button("Calcular perfil lipídico"):

            try:
                # ---------- Cálculo LDL (Friedewald) ----------
                ldl = colesteroltotal - hdl - (trigliceridos / 5)

                st.success(f"LDL: {round(ldl,2)} mg/dL")

                # ---------- Interpretación LDL ----------
                if ldl >= 190:
                    st.error(
                        "Implica riesgo mayor y manejo farmacológico. "
                        "No necesitas usar tablas para calcular el riesgo."
                    )
                elif 160 <= ldl <= 189:
                    st.warning(
                        "Colesterol LDL alto. Se sugiere manejo con estatinas "
                        "de moderada intensidad."
                    )
                elif 130 <= ldl <= 159:
                    st.warning("Colesterol LDL por encima del rango normal.")
                elif 100 <= ldl <= 129:
                    st.info("Colesterol LDL casi óptimo. Entre más bajo mejor :)")
                elif ldl < 100:
                    st.success("Colesterol LDL óptimo (lo mejor para la salud).")

                # ---------- HDL (dependiente de sexo) ----------
                if sexo == "Hombre":
                    if hdl >= 60:
                        st.success(
                            f"{round(hdl,2)} mg/dL. HDL protector contra enfermedad cardiovascular."
                        )
                    elif 40 <= hdl <= 59:
                        st.info(
                            f"{round(hdl,2)} mg/dL. HDL en rango límite inferior."
                        )
                    elif hdl < 40:
                        st.error(
                            f"{round(hdl,2)} mg/dL. Factor de riesgo cardiovascular."
                        )

                if sexo == "Mujer":
                    if hdl >= 60:
                        st.success(
                            f"{round(hdl,2)} mg/dL. HDL protector contra enfermedad cardiovascular."
                        )
                    elif 50 <= hdl <= 59:
                        st.info(
                            f"{round(hdl,2)} mg/dL. HDL en rango límite inferior."
                        )
                    elif hdl < 50:
                        st.error(
                            f"{round(hdl,2)} mg/dL. Factor de riesgo cardiovascular."
                        )

                # ---------- Colesterol total ----------
                if colesteroltotal < 200:
                    st.success(
                        f"{round(colesteroltotal,2)} mg/dL. Colesterol total deseable."
                    )
                elif 200 <= colesteroltotal <= 239:
                    st.warning(
                        f"{round(colesteroltotal,2)} mg/dL. Colesterol total por encima del rango normal."
                    )
                elif colesteroltotal >= 240:
                    st.error(
                        f"{round(colesteroltotal,2)} mg/dL. Colesterol total alto."
                    )

                # ---------- Validaciones Friedewald ----------
                if trigliceridos >= 400 or trigliceridos <= 50:
                    st.warning(
                        "La fórmula de Friedewald no es tan precisa para este "
                        "valor de triglicéridos (> 400 o < 50)."
                    )

                if ldl < 0:
                    st.error("Ups, ingresa los datos nuevamente.")

            except Exception:
                st.error("Ups, inténtalo de nuevo.")


    elif st.session_state.metamodulo == "Sodio corregido":

        st.header("Sodio corregido y osmolaridad efectiva")

        sodioserico = st.number_input(
            "Sodio sérico (mEq/L)",
            min_value=0.0,
            value= 140.0,
            step=1.0
        )

        glucosa = st.number_input(
            "Glucosa sérica (mg/dL)",
            min_value=0.0,
            value=90.0,
            step=1.0
        )

        if st.button("Calcular sodio corregido"):

            try:
                # ---------- SODIO CORREGIDO ----------
                if glucosa >= 400:
                    sodiocorregido = round(
                        sodioserico + 2.4 * ((glucosa / 100) - 1),
                        2
                    )

                elif 400 > glucosa >= 100:
                    sodiocorregido = round(
                        sodioserico + 1.6 * ((glucosa / 100) - 1),
                        2
                    )

                else:
                    sodiocorregido = sodioserico

                st.success(f"Na corregido: {sodiocorregido} mEq/L")

                # ---------- OSMOLARIDAD EFECTIVA ----------
                osm_efectiva = (2 * sodiocorregido) + (glucosa / 18)

                st.info(
                    f"Osmolaridad efectiva: {round(osm_efectiva,2)} mOsm/L"
                )

                # ---------- INTERPRETACIÓN ----------
                if osm_efectiva > 290:
                    st.warning("Estado hiperosmolar.")

                elif osm_efectiva < 275:
                    st.warning("Estado hipoosmolar o hipotónico.")

                else:
                    st.success("Osmolaridad normal.")

            except Exception:
                st.error("Ups, inténtalo de nuevo.")





# ================== SECCION DE NEFROLOGIA ===========================
#=====================================================================
#=====================================================================

elif menu == "nefro":
    
    col5, col6 = st.columns([1,3])

    with col5:
        st.image("images/kidneys.png",width=360)

    with col6:
        st.header("Modulo de nefrología")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

    st.selectbox("Selecciona el cálculo",("KDIGO")
                 , key="nefromodulo")
    
    #AQUI SE CALCULA EL KDIGO CON LA TFG
    if st.session_state.nefromodulo == "KDIGO":
       
       st.header("KDIGO")
       st.info("Vamos a calcular la clasificación KDIGO para el riesgo de enfermedad renal crónica (ERC)")
       st.write("La ERC se define como anomalías de la estructura o función renal, presentes durante un mínimo de 3 meses, con implicaciones para la salud.")
       st.image("images/kdigo.png",width=600)

       col1, col2 = st.columns(2)

       with col1:
           sexo = st.radio("Selecciona el sexo", ["Mujer", "Hombre"])
           creatinina = st.number_input("Creatinina sérica (mg/dL)", value = 0.9, step= 1.0)
           albuminuria = st.number_input("Ingrese el valor de albuminuria")

       with col2:
           raza = st.radio("Selecciona la raza",["Blanca","Negra"])                
           edad = st.number_input("Edad (años)", step = 1)
           unidades = st.radio("¿En qué unidades está reportada la albuminuria", ["mg/g","mg/mmol"])


       if st.button("Calcular TFG"):
           
           try:

            # ================= MUJER =================
                if sexo == "Mujer":

                  if creatinina <= 0.7:
                    tfg = 144 * ((creatinina / 0.7) ** -0.329) * ((0.993) ** edad)
                    tfgblack = tfg * 1.159
                  else:
                    tfg = 144 * ((creatinina / 0.7) ** -1.209) * ((0.993) ** edad)
                    tfgblack = tfg * 1.159

            # ================= HOMBRE =================
                else:

                  if creatinina <= 0.9:
                    tfg = 141 * ((creatinina / 0.9) ** -0.411) * ((0.993) ** edad)
                    tfgblack = tfg * 1.159
                  else:
                    tfg = 141 * ((creatinina / 0.9) ** -1.209) * ((0.993) ** edad)
                    tfgblack = tfg * 1.159

            # ================= RESULTADOS =================

                if unidades == "mg/mmol":
                    albuminuria = albuminuria*10

                
                if raza == "Negra":
                    tfg = tfgblack

                       #AQUI VAMOS A PONER LOS DATOS DE LOS BLANCOS

                st.info(f"TFG: {round(tfg,1)} mL/min/1.73 m²")
                              # ================= ESTADIOS =================
                      #A1
                if tfg >= 90 and albuminuria < 30:
                        st.success("C G1 A1")
                        st.write("Bajo riesgo de ERC")

                if  60 <= tfg <= 89 and albuminuria < 30:
                        st.success("C G2 A1")
                        st.write("Bajo riesgo de ERC")

                if  45 <= tfg <= 59 and albuminuria < 30:
                        st.warning("C G3a A1")
                        st.write("Riesgo moderadamente incrementado")

                if  30 <= tfg <= 44 and albuminuria < 30:
                        st.warning("C G3b A1")
                        st.write("ALTO RIESGO")

                if  15 <= tfg <= 29 and albuminuria < 30:
                        st.error("C G4 A1")
                        st.write("MUY ALTO RIESGO")

                if  tfg < 15  and albuminuria < 30:
                        st.error("C G5 A1")
                        st.write("MUY ALTO RIESGO")

                      #A2
                if tfg >= 90 and (30 <= albuminuria <= 300):
                        st.warning("C G1 A2")
                        st.write("Riesgo moderadamente incrementado")

                if  60 <= tfg <= 89 and (30 <= albuminuria <= 300):
                        st.warning("C G2 A2")
                        st.write("Riesgo moderadamente incrementado")

                if  45 <= tfg <= 59 and (30 <= albuminuria <= 300):
                        st.warning("C G3a A2")
                        st.write("ALTO RIESGO")

                if  30 <= tfg <= 44 and (30 <= albuminuria <= 300):
                        st.error("C G3b A2")
                        st.write("MUY ALTO RIESGO")

                if  15 <= tfg <= 29 and (30 <= albuminuria <= 300):
                        st.error("C G4 A2")
                        st.write("MUY ALTO RIESGO")

                if   tfg < 15  and (30 <= albuminuria <= 300):
                        st.error("C G5 A2")
                        st.write("MUY ALTO RIESGO")

                      #A3
                if tfg >= 90 and (albuminuria > 300):
                        st.warning("C G1 A3")
                        st.write("ALTO RIESGO")

                if  60 <= tfg <= 89 and (albuminuria > 300):
                          st.warning("C G2 A3")
                          st.write("ALTO RIESGO")

                if  45 <= tfg <= 59 and (albuminuria > 300):
                        st.error("C G3a A3")
                        st.write("MUY ALTO RIESGO")

                if  30 <= tfg <= 44 and (albuminuria > 300):
                        st.error("C G3b A3")
                        st.write("MUY ALTO RIESGO")

                if  15 <= tfg <= 29 and (albuminuria > 300):
                        st.error("C G4 A3")
                        st.write("MUY ALTO RIESGO")

                if  tfg < 15 and (albuminuria > 300):
                        st.error("C G5 A3")
                        st.write("MUY ALTO RIESGO")

           except:
              st.error("Ingreso de datos erróneo. Inténtalo de nuevo.")






#stwarning, sterror colorean las cosas. stinfo colorea el texto en azul  

# ================== GINECOBSTETRICIA  ===================================
#=====================================================================
#=====================================================================


elif menu == "gineco":

    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/gineco.png",width=360)

    with col2:
        st.header("Modulo de ginecobstetricia")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

    st.selectbox("Selecciona el cálculo",("FPP")
                 , key="ginecomodulo")
    

    #AQUI SE CALCULAN LOS GASES ARTERIALES
    if st.session_state.ginecomodulo == "FPP":


        st.header("📅 Fecha Probable de Parto (FPP)")

        fum = st.date_input(
            "Fecha de Última Menstruación (FUM)",
            format="DD/MM/YYYY"
        )

        hoy = datetime.date.today()

        if st.button("Calcular FPP"):

            try:
                # FPP por FUM (regla de Naegele)
                fpp = fum + relativedelta(months=9) + datetime.timedelta(days=7)

                if fum.day >= 24:
                    fpp = fpp - relativedelta(months=1)

                semanas = (hoy - fum).days // 7

                st.write(f"**FUM:** {fum.strftime('%d/%m/%Y')}")
                st.write(f"**Edad gestacional:** {semanas} semanas")

                # Clasificación del embarazo
                if semanas < 37:
                    st.info("Embarazo pretérmino")
                elif 37 <= semanas <= 38:
                    st.success("Embarazo a término temprano")
                elif 39 <= semanas <= 40:
                    st.success("Embarazo a término completo")
                elif 40 < semanas <= 41:
                    st.warning("Embarazo a término tardío")
                elif semanas >= 42:
                    st.error("Embarazo post-término")

                # -------------------------------
                # Corrección por ecografía
                # -------------------------------
                usar_eco = st.checkbox("Tengo ecografía del primer trimestre")

                if usar_eco:
                    fecha_eco = st.date_input(
                        "Fecha de la ecografía",
                        format="DD/MM/YYYY",
                        key="eco"
                    )

                    eg_eco = st.number_input(
                        "Edad gestacional por ecografía (semanas)",
                        min_value=4,
                        max_value=20,
                        step=1
                    )

                    eg_fum = (fecha_eco - fum).days // 7
                    diferencia_dias = abs((eg_eco - eg_fum) * 7)

                    corregir = False

                    if eg_eco <= 8 and diferencia_dias >= 5:
                        corregir = True
                    elif 9 <= eg_eco <= 13 and diferencia_dias >= 7:
                        corregir = True
                    elif 14 <= eg_eco <= 20 and diferencia_dias >= 10:
                        corregir = True

                    if corregir:
                        fpp = fecha_eco + datetime.timedelta(weeks=(40 - eg_eco))
                        st.success("📌 FPP corregida según ecografía")
                    else:
                        st.info("📌 Se mantiene FPP calculada por FUM")

                st.write(f"### 📆 FPP final: {fpp.strftime('%d/%m/%Y')}")

            except Exception:
                st.error("Error en los datos. Verifica la información ingresada.")





# ================ SISTEMA CARDIOVASCULAR ============================
#=====================================================================
#=====================================================================


elif menu == "cardio":

    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/heart.png",width=400)

    with col2:
        st.header("Modulo de Cardiología")
        st.info("Aquí puedes encontrar tanto cálculos como escalas clínicas referentes al sistema cardiovascular.")

    st.selectbox("Selecciona el cálculo",("HTA","wifi","CHAD VASc","Escala Wells (TEP)","Escala Wells (TVP)")
                 , key="cardiomodulo")
    
    #AQUI SE CALCULA LA HTA CON LA TFG
    if st.session_state.cardiomodulo == "HTA":

        st.header("Hipertensión Arterial")
        st.info("Agrega una presión y luego calcula si hay HTA.")
        st.info("Agregar más presiones calculará su promedio")

        # Inicializar lista de presiones
        if "presiones" not in st.session_state:
            st.session_state.presiones = []

        # ---------- Inputs ----------
        pas = st.number_input(
            "Presión Sistólica (mmHg)",
            min_value=10,
            max_value=300,
            value = 120,
            step=1
        )

        pad = st.number_input(
            "Presión Diastólica (mmHg)",
            min_value=30,
            max_value=200,
            value = 80,
            step=1
        )

        # ---------- Agregar presión ----------
        if st.button("Agregar presión"):
            if pad >= pas:
                st.error("Ingreso de datos inadecuado. Recuerda PAS / PAD.")
            else:
                st.session_state.presiones.append((pas, pad))
                st.success(f"Presión agregada: {pas}/{pad} mmHg")

        # ---------- Mostrar presiones ----------
        if st.session_state.presiones:
            st.write("Presiones registradas:")
            for i, p in enumerate(st.session_state.presiones, 1):
                st.write(f"{i}. {p[0]}/{p[1]} mmHg")

        # ---------- Calcular ----------
        if st.button("Calcular HTA") and st.session_state.presiones:

            # Promedios
            pas_prom = sum(p[0] for p in st.session_state.presiones) / len(st.session_state.presiones)
            pad_prom = sum(p[1] for p in st.session_state.presiones) / len(st.session_state.presiones)

            st.write(f"**PA promedio:** {round(pas_prom)}/{round(pad_prom)} mmHg")

            grado = []

            # ---------- Clasificación (TU lógica) ----------
            if pas_prom <= 90 and pad_prom <= 60:
                grado.append(-1)

            if pas_prom < 120 and pad_prom < 80:
                grado.append(0)

            if 120 <= pas_prom < 130 and 80 <= pad_prom < 85:
                grado.append(1)

            if 130 <= pas_prom <= 139 or 85 <= pad_prom <= 89:
                grado.append(2)

            if 140 <= pas_prom <= 159 or 90 <= pad_prom <= 99:
                grado.append(3)

            if 160 <= pas_prom <= 179 or 100 <= pad_prom <= 109:
                grado.append(4)

            if pas_prom >= 180 or pad_prom >= 110:
                grado.append(5)

            # ---------- Resultado ----------
            g = max(grado)

            if g < 0:
                st.info("Hipotensión arterial.")
            elif g == 0:
                st.success("Presión arterial óptima.")
            elif g == 1:
                st.success("Presión arterial normal.")
            elif g == 2:
                st.warning("Presión normal alta / Prehipertensión.")
            elif g == 3:
                st.error("Hipertensión Grado 1.")
            elif g == 4:
                st.error("Hipertensión Grado 2.")
            elif g == 5:
                st.error("Hipertensión Grado 3.")

            # ---------- PAM ----------
            pam = (pas_prom + 2 * pad_prom) / 3
            st.write(f"**Presión Arterial Media:** {round(pam)} mmHg")

            if pam < 60:
                st.error("Riesgo de isquemia e infarto.")
            elif pam > 100:
                st.warning("Presión arterial media elevada.")
            else:
                st.success("Presión arterial media normal.")

            # ---------- Presión de pulso ----------
            pp = pas_prom - pad_prom
            st.write(f"**Presión de pulso:** {round(pp)} mmHg")

            if pp > 60:
                st.warning("Riesgo cardiovascular aumentado.")
            elif pp <= 0:
                st.error("Datos inadecuados para presión de pulso.")

        # ---------- Limpiar ----------
        if st.button("Reiniciar"):
            st.session_state.presiones = []

    
    #AQUI CALCULAMOS LA ESCALA WIFI

    elif st.session_state.cardiomodulo == "wifi":

        st.header("🦶 Escala WIfI (Wound – Ischemia – Foot Infection)")
        st.write("Evalúa el riesgo de amputación a 1 año y orienta la necesidad de revascularización según consenso Delphi.")

        # ===============================
        # 🩹 WOUND (HERIDA)
        # ===============================
        st.subheader("🩹 Wound (Herida)")

        wound_options = [
            "No úlcera",
            "Úlcera/s pequeña/s, superficial/es en pie o pierna distal; no exposición del hueso, salvo falange distal",
            "Úlcera profunda con exposición de hueso, articulación o tendón; sin afectación del talón o superficial en talón sin calcáneo",
            "Úlcera extensa y profunda en antepié o mediopié; o úlcera profunda de todo el espesor del talón ± afectación del calcáneo"
        ]

        wound = st.radio("Seleccione la descripción que mejor corresponde:", wound_options)

        wound_map = {
            wound_options[0]: 0,
            wound_options[1]: 1,
            wound_options[2]: 2,
            wound_options[3]: 3,
        }

        # ===============================
        # 🩸 ISQUEMIA
        # ===============================
        st.subheader("🩸 Isquemia")

        ischemia_options = [
            "≥ 0,8",
            "0,6 – 0,79",
            "0,4 – 0,59",
            "≤ 0,39"
        ]

        isquemia = st.radio("Índice tobillo-brazo (ITB):", ischemia_options)

        isquemia_map = {
            ischemia_options[0]: 0,
            ischemia_options[1]: 1,
            ischemia_options[2]: 2,
            ischemia_options[3]: 3,
        }

        # ===============================
        # 🦠 FOOT INFECTION
        # ===============================
        st.subheader("🦠 Foot Infection (Infección)")

        infection_options = [
            "Sin signos ni síntomas de infección",
            "Infección local limitada a piel y tejido celular subcutáneo, sin SRIS",
            "Infección local con eritema >2 cm o afectación de estructuras profundas (absceso, osteomielitis, fascitis), sin SRIS",
            "Infección con signos de SRIS (≥2 criterios sistémicos)"
        ]

        infeccion = st.radio("Grado de infección:", infection_options)

        infeccion_map = {
            infection_options[0]: 0,
            infection_options[1]: 1,
            infection_options[2]: 2,
            infection_options[3]: 3,
        }

        # ===============================
        # 🔢 CONVERSIÓN A GRADOS
        # ===============================
        wound_grade = wound_map[wound]
        ischemia_grade = isquemia_map[isquemia]
        infection_grade = infeccion_map[infeccion]

        # ===============================
        # 📊 MATRIZ DELPHI WiFi
        # ===============================
        wifi_matrix = {
            0: [
                ["VL", "VL", "L",  "M"],
                ["VL", "VL", "L",  "M"],
                ["L",  "L",  "M",  "H"],
                ["M",  "M",  "H",  "H"],
            ],
            1: [
                ["VL", "L",  "M",  "H"],
                ["VL", "L",  "M",  "H"],
                ["M",  "M",  "H",  "H"],
                ["H",  "H",  "H",  "H"],
            ],
            2: [
                ["L",  "L",  "M",  "H"],
                ["L",  "M",  "H",  "H"],
                ["M",  "H",  "H",  "H"],
                ["H",  "H",  "H",  "H"],
            ],
            3: [
                ["L",  "M",  "M",  "H"],
                ["M",  "M",  "H",  "H"],
                ["H",  "H",  "H",  "H"],
                ["H",  "H",  "H",  "H"],
            ],
        }


        #MATRIZ DE REVASCUARIZACIÓN

        revasc_matrix = {
                0: [  # Isquemia 0
                    ["VL", "VL", "VL", "VL"],
                    ["VL", "VL", "VL", "VL"],
                    ["VL", "VL", "VL", "VL"],
                    ["VL", "VL", "VL", "VL"],
                ],
                1: [  # Isquemia 1
                    ["VL", "L",  "L",  "M"],
                    ["VL", "M",  "M",  "M"],
                    ["VL", "M",  "H",  "H"],
                    ["VL", "M",  "M",  "H"],
                ],
                2: [  # Isquemia 2
                    ["L",  "L",  "M",  "M"],
                    ["M",  "H",  "H",  "H"],
                    ["H",  "H",  "H",  "H"],
                    ["H",  "H",  "H",  "H"],
                ],
                3: [  # Isquemia 3
                    ["M",  "H",  "H",  "H"],
                    ["H",  "H",  "H",  "H"],
                    ["H",  "H",  "H",  "H"],
                    ["H",  "H",  "H",  "H"],
                ],
}


        riesgo = wifi_matrix[ischemia_grade][wound_grade][infection_grade]
        beneficio_revasc = revasc_matrix[ischemia_grade][wound_grade][infection_grade]


        # ===============================
        # 🎨 VISUALIZACIÓN CLÍNICA
        # ===============================
        st.divider()
        st.subheader("📊 Interpretación clínica WIfI")

        color_map = {
            "VL": "green",
            "L": "goldenrod",
            "M": "orange",
            "H": "red",
        }

        nivel_texto = {
            "VL": "Muy bajo",
            "L": "Bajo",
            "M": "Moderado",
            "H": "Alto",
        }


        conducta_amputacion = {
            "VL": "Manejo conservador y seguimiento ambulatorio.",
            "L": "Optimizar manejo médico y control estrecho.",
            "M": "Valoración por cirugía vascular. Riesgo intermedio de amputación.",
            "H": "Intervención urgente. Alto riesgo de amputación a 1 año.",
        }


        conducta_revasc = {
            "VL": "No se recomienda revascularización. Manejo conservador.",
            "L": "Revascularización generalmente no indicada.",
            "M": "Valorar revascularización según contexto clínico y anatomía vascular.",
            "H": "Alta probabilidad de beneficio. Revascularización indicada si es técnicamente posible.",
        }


        # ---- Riesgo de amputación ----
        st.markdown(
            f"""
            <h3 style="color:{color_map[riesgo]}">
            Riesgo de amputación a 1 año: {nivel_texto[riesgo]} ({riesgo})
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.info(conducta_amputacion[riesgo])

        # ---- Revascularización ----
        st.markdown(
            f"""
            <h3 style="color:{color_map[beneficio_revasc]}">
            Probabilidad de beneficio con revascularización: {nivel_texto[beneficio_revasc]} ({beneficio_revasc})
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.warning(conducta_revasc[beneficio_revasc])


        st.caption("Referencias: DOI: 10.1016/j.angio.2016.08.002")




# ====================== HEMATOLOGÍA ================================
#=====================================================================
#=====================================================================

elif menu == "hemato":

    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/hemato.png",width=360)

    with col2:
        st.header("Modulo de hematología")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

    st.selectbox("Selecciona el cálculo",("Clasificación morfológica de la anemia")
                 , key="hematomodulo")
    

    #AQUI SE CALCULAN LOS VALORES DEL VCM Y HCM
    if st.session_state.hematomodulo == "Clasificación morfológica de la anemia":

        st.header("Clasificación morfológica de la anemia")

        # ---------- INPUTS ----------
        recuento = st.number_input(
            "Recuento eritrocitario (millones/µL)",
            min_value=0.1, value= 5.0,
            step=0.1
        )

        hto = st.number_input(
            "Hematocrito (%)",
            min_value=0.0, value= 45.0,
            step=1.0
        )

        hb = st.number_input(
            "Hemoglobina (g/dL)",
            min_value=0.0, value= 14.0,
            step=0.1
        )

        # ---------- BOTÓN ----------
        if st.button("Clasificar anemia"):

            try:
                # ---------- VCM ----------
                hto_frac = hto / 100
                vcm = (hto_frac / recuento) * 1000

                if 80 <= vcm <= 100:
                    st.success(
                        f"VCM: {round(vcm,2)} fL. Eritrocito normocítico."
                    )

                elif vcm < 80:
                    st.warning(
                        f"VCM: {round(vcm,2)} fL. Eritrocito microcítico."
                    )

                elif vcm > 100:
                    st.warning(
                        f"VCM: {round(vcm,2)} fL. Eritrocito macrocítico."
                    )

            except Exception:
                st.error("Ups, me faltan datos para calcular el VCM 😕")

            try:
                # ---------- HCM ----------
                hcm = (hb / recuento) * 10

                if 27 <= hcm <= 34:
                    st.success(
                        f"HCM: {round(hcm,2)} pg/célula. Eritrocito normocrómico."
                    )

                elif hcm < 27:
                    st.warning(
                        f"HCM: {round(hcm,2)} pg/célula. Eritrocito hipocrómico."
                    )

                elif hcm > 34:
                    st.warning(
                        f"HCM: {round(hcm,2)} pg/célula. Eritrocito hipercrómico."
                    )

            except Exception:
                st.error("Ups, me faltan datos para calcular el HCM 😕")




# ================== PEDIATRIA ==================
#=====================================================================
#=====================================================================


elif menu == "pediatria":


    col1, col2 = st.columns([1,3])

    with col1:
        st.image("images/pediatra.png",width=360)

    with col2:
        st.header("Cálculos en pediatría")
        st.info("Selecciona la herramienta clínica que necesitas en la caja de abajo.")

        st.selectbox("Selecciona el cálculo",("Liquidos mantenimiento","Disnatremias","DisKalemias")
                    , key="submodulo")
    

    if st.session_state.submodulo == "Liquidos mantenimiento":
        st.header("Líquidos de mantenimiento")
        st.info("Selecciona los líquidos que necesita el nené de mantenimiento según su grado de deshidratación")
        st.image("images/deshidratacion.png", width= 500)

        DAD = 5 #Dextrosa en agua destilada

        peso = st.number_input("Ingresa el peso del bebé en kg",min_value= 0.0, step= 1.0)
        edad = st.number_input("Ingresa la edad en años", min_value= 0, step= 1)
        deshidra = st.radio("Selecciona el grado de deshidratación", ["Leve", "Moderada","Grave"])
        bolos = st.number_input("Ingresa la cantidad de bolos que le han dado justo antes", min_value=0, step= 1)

#calculemos los liquidos de mantenimiento

        if peso <= 10:
         M = 100 * peso

        if 11 <= peso < 20:
         M = 1000 + 50*(peso - 10)

        if peso >= 20:
         M = 1500 + 20*(peso -20)

# Ahora vamos a calcular la reposicion

        if deshidra == "Leve" and edad < 6:
         rep = 50
        elif deshidra == "Leve" and edad >= 6:
         rep = 30

        if deshidra == "Moderada" and edad < 6:
         rep = 100
        elif deshidra == "Moderada" and edad >= 6:
         rep = 60

        if deshidra == "Grave" and edad < 6:
         rep = 150
        elif deshidra == "Grave" and edad >= 6:
         rep = 90


        if deshidra == "Nada":
         rep = 0

    #calculemos cuánto debemos reponer

        reposi = rep*peso - bolos*peso


    #calculemos el flujo metabolico

        fmeta = (M * DAD * (1000/(100*1440)))/12


        st.success("El volumen total a reponer es: " + str(M + reposi) + " ml/día o " + str(round(((M+reposi)/24),1)) + "ml/h")

        st.info("La dosis de mantenimiento es: " + str(M) + " ml/día, o " + str(round(M/24,1)) + "ml/h")

        st.info("La dosis de reposición es: " + str(round(reposi,1)) + "ml/día o"+ str(round(reposi/24,1)) + " ml/h" )

        st.warning("El flujo metabólico (si usas DAD 5%) es: " + str(round(fmeta,2) )+ " mg/kg/min")


     #DISNATERMIAS
    elif st.session_state.submodulo == "Disnatremias":

        st.header("Reposición de sodio")
        st.info("Usaremos la fórmula de Adrogué para calcular el sodio que le falta al nené y evitar la mielinólisis pontina")


        nap = st.number_input("Ingrese el valor de Na del nené: ",min_value=50.0, value=140.0, step=0.1)
        peso = st.number_input("Ingrese el peso en kg: ", min_value=0.0, value= 2.0, step=0.1)
        ss = st.radio("Selecciona la concentración de solución salina que vas a usar:",["0.9%","0.45%","3%"])

        ACT = peso * 0.6

            # Aca miramos cuantos meq tiene cada salino
        if ss == "0.9%":
            meq = 154
        elif ss == "0.45%":
            meq = 77
        elif ss == "3%":
            meq = 513


        if st.button("Calcular Na requerido"):


            if nap < 125:
            #Aca vamos a calcular cuánto debemos subir
              cuantosub = 125 - nap   #La meta es 125 meq, y no podemos subir más de 10 meq/día por riesgo de desmielinización pontina

              if cuantosub == 10:
               cuantosub = 10

            #Fórmula de Adrogué para calcular cuántos meq subo por cada litro de ss (0.45, 0.9 o 3 %) que le doy
              adro = (meq - nap)/(ACT + 1)

  #Vamos a calcular cuántos cc debo administrar para subir hasta el valor meta

              cc = (1000*cuantosub)/adro

              st.success("Se le debe administrar " + str(round(cc,1)) + "cc de ss al " + str(ss) + " % para pasar a " + str(round(cc/24,1)) + " cc/h en 24 h")
              st.info("Por cada litro de ss al " + str(ss) + " %, subo " + str(round(adro,2)) + " meq de la natremia del paciente.")

              st.caption("Unos tips para que enfoques al bebé")
              st.image("images/hiponatremia.png",width=800)
              st.caption("Imagen tomada de la presentación de la pediatra NATALY OSPINA GARCÍA")

            elif nap > 155:
   #Aca vamos a calcular cuánto debemos subir

               cuantobaj = nap - 155   #La meta es 155 meq, y no podemos bajar más de 10 meq/día por riesgo de desmielinización pontina

               if cuantobaj == 10:
                cuantobaj = 10


   #Fórmula de Adrogué para calcular cuántos meq subo por cada litro de ss (0.45, 0.9 o 3 %) que le doy
               adro = (meq - nap)/(ACT + 1)

  #Vamos a calcular cuántos cc debo administrar para subir hasta el valor meta

               cc = (1000*cuantobaj)/adro

               st.success("Se le debe administrar " + str(round(abs(cc),1)) + "cc de ss al " + str(ss) + " % para pasar a " + str(round(abs(cc)/24,1)) + " cc/h en 24 h")

               st.info("Por cada litro de ss al " + str(ss) + " %, bajo " + str(round(adro,2)) + " meq de la natremia del paciente.")

               st.caption("Unos tips para que enfoques al bebé")
               st.image("images/hipernatremia.png",width=800)
               st.caption("Imagen tomada de la presentación de la pediatra NATALY OSPINA GARCÍA")

            else:
               st.success("No hay necesidad de correjir sodio")

        
        #DISKALEMIAS

    elif st.session_state.submodulo == "DisKalemias":

        st.header("Corrección de DisKalemias")
        st.info("Aquí vamos a corregir los valores bajos de potasio del bebé")

        kpa = st.number_input("Ingresa el K sérico del paciente: ", min_value=0.0, max_value=20.0, step= 0.1, value= 4.0)
        peso = st.number_input("Ingresa el peso del paciente en kg: ",  min_value=0.0, max_value=100.0, step= 0.1, value= 4.0)

        if kpa < 2.5:
                dosis = st.number_input("Ingresa la dosis deseada 0.5-1 meq/kg/día: ", min_value=0.5, max_value=1.0, step=0.1)
                vi = st.number_input("Ingresa la velocidad de infusión de 0.25-0.5 meq/kg/h: ", min_value=0.25, max_value=0.5, step=0.1)

        if st.button("Calcular disKalemia"):
            
            if 2.5 <= kpa < 3.5:
                st.warning("Le puedes dar " + str(round((peso*(15/20)),1)) + " a " + str(round((3*peso*(15/20)),1)) + " cc/día de Ion K jarabe por 3 - 4 dosis VO")
                st.write("Si está en ayuno, le puedes dar " + str(round((2*peso*(15/20)),1)) + " a " + str(round((4*peso*(15/20)),1)) + " cc/día por 3 - 4 dosis VO" )
                st.write("Control cada 4 h de K sérico")


            if kpa < 2.5:

                st.success("Diluir " + str(round((dosis*peso/2),1)) + " cc de Katrol en " + str(round((25*peso*dosis),1)) + " a "
                               + str(round(((100/6)*peso*dosis),1)) + " cc de ss 0.9 % y pasar en " + str(round((dosis/vi),1)) + " h por vía periférica.")


                st.success("Diluir " + str(round((dosis*peso/2),1)) + " cc de Katrol en " + str(round((10*peso*dosis),1)) + " a "
                               + str(round(((20/3)*peso*dosis),1)) + " cc de ss 0.9 % y pasar en " + str(round((dosis/vi),1)) + " h por catéter venoso central.")
                

                st.caption("Unos tips para que enfoques al bebé")
                st.image("images/hipokalemia.png",width=800)
                st.caption("Imagen tomada de la presentación de la pediatra NATALY OSPINA GARCÍA")
                
            if kpa > 5.1:

                st.warning("Tiene una hiperKalemia")

                st.caption("Aquí te doy un enfoque de tratamiento")
                st.image("images/hiperkalemia.png",width=800)
                st.caption("Imagen tomada de la presentación de la pediatra NATALY OSPINA GARCÍA")

            if 3.5 <= kpa <= 5.1:

                st.success("Tiene el potasio normal")


# ================== PRONTO NUEVAS FUNCIONES ==================


# ================== FOOTER ==================
st.markdown("---")
st.caption("HELEN M.O.R · Medicina & Ingeniería · Uso académico")
st.caption("Hecho por Simón Tirado Posada")