
import streamlit as st

st.set_page_config(page_title="Dla Martyny", page_icon="💗")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #ffdce9);
}
.stButton > button {
    background-color: #d63384;
    color: white;
    border-radius: 20px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title("💌 Dla Martyny")
st.write("Mam dla Ciebie małą niespodziankę...")

odpowiedz = st.text_input(
    "Jakie jedno słowo kojarzy Ci się z nami? 💗"
)

if st.button("Otwórz list 💌"):
    if odpowiedz.strip():
        st.session_state.odpowiedz = odpowiedz
        st.session_state.otwarte = True
    else:
        st.warning("Najpierw coś wpisz! ❤️")

if st.session_state.get("otwarte", False):
    st.divider()
    st.subheader("Kochana Martyno ❤️")

    st.write(
        f"Ty napisałaś: {st.session_state.odpowiedz}"
    )

    st.write("""
    Chciałam przygotować dla Ciebie coś wyjątkowego.

    Nie jest to zwykły list, bo przecież musiałam
    zrobić coś trochę po swojemu.

    Chcę Ci tylko przypomnieć, jak bardzo
    cieszę się, że jesteś w moim życiu.

    ❤️
    """)

    if st.button("Jeszcze jedna niespodzianka 💗"):
        st.balloons()
        st.success("Jesteś moją ulubioną osobą! ❤️")
