import streamlit as st
from PIL import Image # Χρειάζεται για την επεξεργασία της εικόνας

# 1. ΑΛΛΑΓΗ ΤΙΤΛΟΥ ΣΤΟ TAB ΤΟΥ BROWSER
st.set_page_config(page_title="HelmetLab", page_icon="⛑️")

# 2. ΠΡΟΣΘΗΚΗ LOGO
# Ανέβασε το αρχείο logo.png στο GitHub σου για να δουλέψει αυτό
try:
    image = Image.open('FULL LOGO ICON AND TEXT-04.png')
    st.image(image, width=600) # Μπορείς να αλλάξεις το 200 για να μεγαλώσει/μικρύνει
except:
    st.warning("Ανέβασε ένα αρχείο με όνομα logo.png στο GitHub για να δεις το λογότυπό σου!")

# 3. ΚΥΡΙΟΣ ΤΙΤΛΟΣ ΕΦΑΡΜΟΓΗΣ
st.title("Custom ROI Calculator") # Γράψε εδώ όποιον τίτλο θέλεις
st.write("HelmetLab")

# --- ΤΟ ΥΠΟΛΟΙΠΟ ΤΗΣ ΕΦΑΡΜΟΓΗΣ (ΟΠΩΣ ΠΡΙΝ) ---
st.sidebar.header("Παράμετροι")
price = st.sidebar.number_input("Τιμή ανά κύκλο (€)", value=8.0, step=0.5)
daily_runs = st.sidebar.number_input("Κύκλοι την ημέρα (Μ.Ο.)", value=12, step=1)
active_days = st.sidebar.slider("Ημέρες λειτουργίας/μήνα", 1, 30, 30)
venue_share = st.sidebar.slider("Μερίδιο Χώρου (%)", 0, 50, 15)

cost_per_liter = st.sidebar.number_input("Κόστος ανά λίτρο (€)", value=23.0, step=1.0)
cleans_per_4l = 500

liquid_cost_per_clean = (4 * cost_per_liter) / cleans_per_4l
gross_monthly = price * daily_runs * active_days
venue_cut = gross_monthly * (venue_share / 100)
total_liquid_cost = (daily_runs * active_days) * liquid_cost_per_clean
net_monthly = gross_monthly - venue_cut - total_liquid_cost

st.header(f"Μηνιαίο Καθαρό Κέρδος: {net_monthly:,.2f}€")

# Πίνακας Ανάλυσης
st.table({
    "Περιγραφή": ["Έσοδα", "Venue Share", "Υγρά", "Καθαρό"],
    "Ποσό": [f"{gross_monthly:.2f}€", f"-{venue_cut:.2f}€", f"-{total_liquid_cost:.2f}€", f"{net_monthly:.2f}€"]
})
