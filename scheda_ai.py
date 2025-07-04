import streamlit as st

def genera_scheda(obiettivo, livello, frequenza, carico_base):
    scheda = []
    esercizi = ["Squat", "Panca", "Stacco", "Trazioni", "Military Press"]
    moltiplicatore = {
        "principiante": 0.6,
        "intermedio": 0.75,
        "avanzato": 0.85
    }

    for esercizio in esercizi:
        base = int(carico_base * moltiplicatore[livello])
        settimane = [
            base,
            int(base * 1.05),
            int(base * 1.10),
            int(base * 1.15)
        ]
        scheda.append({
            "esercizio": esercizio,
            "serie": 4,
            "ripetizioni": 8 if obiettivo == "massa" else 5,
            "carichi": settimane
        })

    return scheda

st.title("🏋️ Scheda AI - Progressione ogni 2 settimane")

obiettivo = st.selectbox("Obiettivo", ["massa", "forza", "resistenza"])
livello = st.selectbox("Livello", ["principiante", "intermedio", "avanzato"])
frequenza = st.slider("Allenamenti a settimana", 2, 6, 3)
carico_base = st.number_input("Carico iniziale di riferimento (kg)", 20, 200, 60)

if st.button("Genera scheda"):
    scheda = genera_scheda(obiettivo, livello, frequenza, carico_base)
    for esercizio in scheda:
        st.subheader(esercizio["esercizio"])
        st.write(f"Serie: {esercizio['serie']} | Ripetizioni: {esercizio['ripetizioni']}")
        st.write(f"Progressione carichi (4 settimane): {esercizio['carichi']}")
