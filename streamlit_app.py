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
            •	Management von ca. 200.000 Haushaltskund:innen im Bereich Strom<br>
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
        - **Aufgaben**: ..
        - **Fokus**: Objektive Hermeneutik, Interview...
        - **Tools**: Microsoft Office / Excel
        """)

    with tabs[3]:
        st.subheader("Praktika – Wirtschaftsforschung")
        st.caption("Juli 2017 – April 2018")
        st.markdown("""
        - **Einrichtungen**: 
                    ZEW - Zentrum für Europäische Wirtwschaftsforschung, Mannheim
                    RWI - Leibnitz-Institut für Wirtschaftsforschung, Essen
        - **Themen**: 
                    Neuausrichtung Finanzmarktreport, 
                    Meta-Analyse kausaler Effekte von verhaltensökonomischen Interventionen auf den Energieverbrauch privater Haushalte (https://www.econstor.eu/bitstream/10419/177816/1/1018512411.pdf)
                    Clusteranalyse zu Determinanten von Produktivität
        - **Tools**: Excel, Stata, Citavi, Microsoft Office
        """)#
   

# === Ausbildung ===
with st.expander("🎓 Studium & Weiterbildung"):
    auswahl = st.selectbox("Wähle Abschnitt:", ["Data Science Weiterbildung", "M.Sc.", "B.Sc."])

    if auswahl == "Data Science Weiterbildung":
        st.subheader("📊 Weiterbildung – Data Science")
        st.caption("Juni 2025 – August 2025 (laufend)")
        st.markdown("""
        - Intensivkurs bei [XY-Bildungsträger]  
        - **Inhalte**: Python, R, SQL, Machine Learning  
        - **Tools**: pandas, matplotlib, seaborn, scikit-learn, ggplot2, tidyverse  
        - **Ziel**: Kombination aus ökonomischer Expertise & Datenkompetenz
        """)

    elif auswahl == "M.Sc.":
        st.subheader("M.Sc. Volkswirtschaftslehre")
        st.caption("2017 – 2021")
        st.markdown("""
        - Universität Freiburg  
        - **Vertiefung**: Energieökonomik, Umwelt, Policy  
        - **Projekte**: Emissionshandel, Strommarktanalysen  
        - **Methoden**: Stata, Excel, erste R-Experimente
        """)

    elif auswahl == "B.Sc.":
        st.subheader("B.Sc. Economics and Business Administration")
        st.caption("2013 – 2017")
        st.markdown("""
        - Universität Freiburg  
        - **Schwerpunkte**: Mikroökonomik, Finanzmärkte, Statistik  
        - **Abschlussnote**: 1,X
        """)

# === Projekte (optional) ===
with st.expander("🛠️ Projekte & Demos"):
    st.markdown("""
    - 📊 **SMARD Strom-Dashboard** – Analyse deutscher Stromerzeugung (Python, Streamlit)  
      [➡️ Zur Demo](https://dein-dashboard.streamlit.app)

    - 📁 **GitHub-Portfolio**  
      [➡️ github.com/deinusername](https://github.com/deinusername)
    """)

# === Kontakt ===
with st.expander("✉️ Kontakt"):
    st.markdown("""
    - ✉️ E-Mail: jf.streib@outlook.de  
    - 💼 LinkedIn: [linkedin.com/in/fabian-s-03aa92158](https://linkedin.com/in/fabian-s-03aa92158)  
    - 📍 Standort: Freiburg im Breisgau (remote offen)
    """)



