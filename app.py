import streamlit as st

# Ρύθμιση τίτλου και εμφάνισης
st.set_page_config(page_title="Helmet Hygiene ROI (€)", layout="centered")
st.title("⛑️ Υπολογιστής ROI - Helmet Hygiene")

# --- ΔΕΔΟΜΕΝΑ ΕΙΣΟΔΟΥ ---
st.header("1. Ρυθμίσεις Δεδομένων")

col1, col2 = st.columns(2)
with col1:
    price = st.number_input("Τιμή ανά κύκλο (€)", value=8.0, step=0.5)
    daily_runs = st.number_input("Κύκλοι την ημέρα (Μ.Ο.)", value=12, step=1)
with col2:
    venue_share = st.slider("Μερίδιο Χώρου (%)", 0, 50, 15)
    active_days = st.slider("Ημέρες λειτουργίας/μήνα", 1, 30, 30)

# --- ΥΠΟΛΟΓΙΣΜΟΙ ---
# Κόστος αναλώσιμων ανά κύκλο (περίπου 0.46€)
cost_per_cycle = 0.46

gross_monthly = price * daily_runs * active_days
venue_cut = gross_monthly * (venue_share / 100)
total_costs = daily_runs * active_days * cost_per_cycle
net_monthly = gross_monthly - venue_cut - total_costs
annual_profit = net_monthly * 12

# --- ΑΠΟΤΕΛΕΣΜΑΤΑ ---
st.divider()
st.header("2. Αποτελέσματα")

c1, c2, c3 = st.columns(3)
c1.metric("Μηνιαίος Τζίρος", f"{gross_monthly:,.0f}€")
c2.metric("Καθαρό Κέρδος", f"{net_monthly:,.0f}€")
c3.metric("Ετήσιο Κέρδος", f"{annual_profit:,.0f}€")

# Πίνακας Ανάλυσης
st.table({
    "Περιγραφή": ["Ακαθάριστα Έσοδα", "Μερίδιο Χώρου", "Έξοδα (Αναλώσιμα)", "Τελικό Καθαρό"],
    "Ποσό (€)": [f"{gross_monthly:.2f}€", f"-{venue_cut:.2f}€", f"-{total_costs:.2f}€", f"{net_monthly:.2f}€"]
})