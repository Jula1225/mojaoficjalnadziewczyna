
import streamlit as st

st.set_page_config(page_title="Dla mojej oficjalnej dziewczyny")

st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
h1, p, label {
    color: white !important;
}
.stTextInput input {
    background-color: #111111;
    color: white;
    border: 1px solid white;
}
.stButton button {
    background-color: black;
    color: white;
    border: 1px solid white;
}
.stButton button:hover {
    background-color: #222222;
    color: white;
}
</style>
""", unsafe_allow_html=True)

if "odblokowane" not in st.session_state:
    st.session_state.odblokowane = False

if not st.session_state.odblokowane:
    st.title("Dla mojej oficjalnej dziewczyny")

    haslo = st.text_input("wpisz hasło", type="password")

    if st.button("dalej"):
        if haslo == "67":
            st.session_state.odblokowane = True
            st.rerun()
        else:
            st.error("nieprawidłowe hasło")
else:
    st.write("Jeszcze dzisiaj ci chyba nie powiedziałam że jesteś piękna.")
    st.write("Kocham cię!!!!!!!!!!")
