# %%
import streamlit as st

st.title("👨‍💻 Interaktiver Lebenslauf – Fabian Streib")

# === Berufserfahrung ===
with st.expander("💼 Berufserfahrung"):
    st.markdown("Hier findet Ihr mehr über meine beruflichen Erfahrungen.")

    tabs = st.tabs(["Produktmanager", "Hiwi", "Consultant", "Praktikant"])

    with tabs[0]:
        st.subheader("Produktmanagement Energieprodukte – EWS Schönau")
        st.caption("Januar 2022 – September 2024")
        st.markdown("""
        - **Rolle**: Schnittstelle zwischen Entwicklung, Marketing und Markt  
        - **Fokus**: Ökostromprodukte  
        - **Highlights**:  
            • \nProjektleitung "Dynamischer Tarif"  
            • \nNeutarifentwicklungen, Tarifkalkulation Mieterstrom  
        - **Detailiertere Beschreibung**:  
            •	Management von ca. 200.000 Haushaltskund:innen im Bereich Strom  
            •	Entwicklung neuer Strom- und Gastarife unter Berücksichtigung gesetzlicher Vorgaben (EnWG, EEG)  
            •	Tarifkalkulation und Pricing unter Berücksichtigung von Strompreisschwankungen und Risikofaktoren, insbesondere während der Energiekrise 2022/2023  
            •	Wirtschaftlichkeitsberechnungen für Mieterstromprojekte zur strategischen Bewertung und Entscheidungsvorbereitung  
            •	Mitarbeit am Reporting für das unternehmensweite Risikokomitee – insbesondere zu Energiemengen und Beschaffungsrisiken  
            •	Aufbau und Pflege von Energiedaten- und Kundenportfolioreportings  
            •	Wettbewerbsanalysen zur kontinuierlichen Marktbeobachtung und strategischen Ausrichtung  
            •	Projektleitung "Dynamischer Tarif" – inklusive Konzeption, Koordination, Durchführung von Weeklys und Nutzerinterviews  
            •	Verantwortung für Zertifizierungen (TÜV, OK POWER+) sowie Konzeption und Durchführung interner Schulungen  
            •	Zusammenarbeit mit nahezu allen Fachbereichen: Vertrieb, Energiebeschaffung, Controlling, Recht, Abrechnung, Marketing und weitere  
        - **Tools**: Excel, ERP (First Sale, SQL), WEKAN/Youtrack, Miroboard, Confluence, Microsoft Office
        """)
 
    with tabs[1]:
        st.subheader("Wissenschaftliche Hilfskraft – Universität Freiburg")
        st.caption("Januar 2020 – Oktober 2020 (während Master)")
        st.markdown("""
        - **Einrichtung**: Zentrum für Erneuerbare Energien Freiburg  
        - **Aufgaben**:  
            •	Mitarbeit an Projekten zu Carsharing-Wettbewerb und Sozialer Nachbarschaft und Technik  
            •	Datenaufbereitung und Interviewdurchführung, Qualitative Auswertung mit objektiver Hermeneutik, Erstellung von Blogartikel  
        - **Tools**: Microsoft Office / Excel
        """)

    with tabs[2]:
        st.subheader("Junior-Kurzzeitexperte – Sparkassenstiftung für internationale Kooperation")
        st.caption("Januar 2018 – April 2018 (Accra, Ghana)")
        st.markdown("""
        - **Aufgaben**:  
            •	Entwicklung von Schulungsmaterialien für den Mikrofinanzsektor in Ghana und Gambia  
            •	Impact Assessment und Vorbereitung eines Stakeholder-Workshops  
        - **Tools**: Microsoft Office / Excel
        """)

    with tabs[3]:
        st.subheader("Praktika – Wirtschaftsforschung")
        st.caption("Juli 2017 – Dezember 2018")
        st.markdown("""
        - **Einrichtungen**:  
                    ZEW - Zentrum für Europäische Wirtwschaftsforschung, Mannheim  
                    RWI - Leibnitz-Institut für Wirtschaftsforschung, Essen  
        - **Themen**:  
            •	Neuausrichtung Finanzmarktreport,  
            •	Meta-Analyse kausaler Effekte von verhaltensökonomischen Interventionen auf den Energieverbrauch privater Haushalte (https://www.econstor.eu/bitstream/10419/177816/1/1018512411.pdf)  
            •	Clusteranalyse zu Determinanten von Produktivität  
        - **Tools**: Excel, Stata, Citavi, Microsoft Office
        """)#
   

# === Ausbildung ===
with st.expander("🎓 Studium & Weiterbildung"):
    auswahl = st.selectbox("Wähle Abschnitt:", ["Weiterbildung Data Science", "M.Sc.", "B.Sc."])

    if auswahl == "Weiterbildung Data Science":
        st.subheader("📊 Weiterbildung zum (Junior) Data Scienctist")
        st.caption("Juni 2025 – August 2025 (laufend)")
        st.markdown("""
        - **Bildungsträger**: ComCave College GmbH  
        - **Inhalte**:  
            •	Deskriptive Statistik mit Python und R  
            •	Big Data Management mit SQL und R  
            •	Business Intelligence - Microsoft Power Bi Certification PL300  
        - **Tools**: pandas, matplotlib, seaborn, ggplot2, tidyverse, streamlit, more2come..  
        - **Ziel**: Kombination aus ökonomischem Wissen & Datenkompetenz, Objektivität durch Fakten
        """)

    elif auswahl == "M.Sc.":
        st.subheader("M.Sc. Volkswirtschaftslehre")
        st.caption("2017 – 2021")
        st.markdown("""
        - **Einrichtung**: Albert Ludwigs Universität Freiburg  
        - **Vertiefung**: Empirical Economics, International & Development Economics  
        - **Masterarbeit**: "Distance as a Determinant of Migration: A Gravity Analysis of Africa and Asia" (Note: 1,7)  
        - **Methoden**: Stata, Excel, erste R-Experimente  
        - **Abschlussnote**: 2,2  
        """)

    elif auswahl == "B.Sc.":
        st.subheader("B.Sc. Economics and Business Administration")
        st.caption("2013 – 2017")
        st.markdown("""
        - **Einrichtung**: Eberhard-Karls-Universität Tübingen  
        - **Schwerpunkte**: Managerial Accounting, Organisation & Marketing  
        - **Bachelorarbeit**: "Does Youth Bulge have an Effect on Homicide Rates?" (Note: 2,0)  
        - **Methoden**: Stata, Excel  
        - **Abschlussnote**: 2,3
        """)

# === Projekte (optional) ===
with st.expander("🛠️ Projekte & Demos"):
    st.markdown("""
    - 📁 **GitHub-Portfolio**  
      [➡️ Zur Repository-Übersicht auf Github](https://github.com/61-192018)
    - 📊 **SMARD Strom-Dashboard** – Analyse deutscher Stromerzeugung (Python)  
      [➡️ Zum Repository auf Github](https://github.com/61-192018/Analyse_Erzeugungsleistung_Deutschland_Marktstammdatenregister)
    - 📊 **Weather Data and Graphs** – Analyse monatlicher Wetterdaten (Finnland, 2017) (R - aggregate functions with tidyverse: dplyr, ggplot) 
      [➡️ Zum Repository auf Github](https://github.com/61-192018/weatherdata_finland_2017)

    """)

# === Kontakt ===
with st.expander("✉️ Kontakt"):
    st.markdown("""
    - ✉️ E-Mail: jf.streib@outlook.de  
    - 💼 LinkedIn: [linkedin.com/in/fabian-s-03aa92158](https://linkedin.com/in/fabian-s-03aa92158)  
    - 📞 Mobil: +49 157 770 465 54
    - 📍 Standort: Freiburg im Breisgau (remote offen)
    """)



