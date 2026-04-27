import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(page_title="Helmet Hygiene ROI (€)", layout="centered")
st.title("⛑️ Helmet Hygiene ROI Calculator")

# --- ΔΕΔΟΜΕΝΑ ΕΙΣΟΔΟΥ ---
st.sidebar.header("1. Ρυθμίσεις Εσόδων")
price = st.sidebar.number_input("Τιμή ανά κύκλο (€)", value=8.0, step=0.5)
daily_runs = st.sidebar.number_input("Κύκλοι την ημέρα (Μ.Ο.)", value=12, step=1)
active_days = st.sidebar.slider("Ημέρες λειτουργίας/μήνα", 1, 30, 30)
venue_share = st.sidebar.slider("Μερίδιο Χώρου (%)", 0, 50, 15)

st.sidebar.header("2. Κόστος Υγρών (Consumables)")
cost_per_liter = st.sidebar.number_input("Κόστος ανά λίτρο (€)", value=23.0, step=1.0)
cleans_per_4l = 500 # Σταθερά βάσει των στοιχείων σου

# --- ΥΠΟΛΟΓΙΣΜΟΙ ---
# Υπολογισμός κόστους ανά καθαρισμό: (4 λίτρα * τιμή_λίτρου) / 500 καθαρισμούς
liquid_cost_per_clean = (4 * cost_per_liter) / cleans_per_4l

gross_monthly = price * daily_runs * active_days
venue_cut = gross_monthly * (venue_share / 100)
total_liquid_cost = (daily_runs * active_days) * liquid_cost_per_clean
net_monthly = gross_monthly - venue_cut - total_liquid_cost
annual_profit = net_monthly * 12

# --- ΕΜΦΑΝΙΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ---
st.header("Οικονομική Ανάλυση (€)")

col1, col2, col3 = st.columns(3)
col1.metric("Μηνιαίος Τζίρος", f"{gross_monthly:,.0f}€")
col2.metric("Καθαρό Κέρδος", f"{net_monthly:,.0f}€")
col3.metric("Ετήσιο Κέρδος", f"{annual_profit:,.0f}€")

st.info(f"Το κόστος υγρού ανά καθαρισμό είναι: {liquid_cost_per_clean:.3f}€")

# Πίνακας Ανάλυσης
st.subheader("Ανάλυση Εξόδων & Εσόδων")
st.table({
    "Περιγραφή": ["Ακαθάριστα Έσοδα (Monthly Gross)", "Μερίδιο Χώρου (Venue Share)", "Κόστος Υγρών (Consumables)", "Τελικό Καθαρό (Net Profit)"],
    "Ποσό (€)": [
        f"{gross_monthly:.2f}€", 
        f"-{venue_cut:.2f}€", 
        f"-{total_liquid_cost:.2f}€", 
        f"{net_monthly:.2f}€"
    ]
})

st.caption("Σημείωση: Ο υπολογισμός υγρών βασίζεται σε απόδοση 500 καθαρισμών ανά 4 λίτρα.")
