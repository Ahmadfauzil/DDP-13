import streamlit as st

st.title("Halaman Nabung")

with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("jumlah (RP.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    button = st.form_submit_button(label="Nabung Yaa!!")

    if button and jumlah >= 50000:
        st.session_state['total_semua'].append({
            "Tipe" : "Menabung", 
            "Jumlah" : jumlah
        })
        st.success("Jangan Maen Slot Ya....!")
    else:
        st.error("Kamu Gagal Menabung, Nominal Kurang Dari 50000")