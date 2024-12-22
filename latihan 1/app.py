import streamlit as st

#st.title("Hello Masbro")
#st.write("Apa Kabar")
#st.image("th.jpeg", caption="ini kamuuuu")

# sidebar direktory
dashboard = st.Page("./fitur/dashboard.py", title="dashboard")
nabung= st.Page("./fitur/nabung.py", title="menabung")

pg = st.navigation(
    {
        "Menu Utama": [dashboard],
        "transaksi": [nabung]

    }
)
if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()