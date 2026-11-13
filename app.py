
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
    st.write("Jeszcze dzisiaj ci chyba nie powiedziałam że jesteś piękna. kropka")
    st.write("W tle powinna leciec piosenka ale nwm czy to dziala")
    st.write("Ale jak leci to chce zebys wiedziala ze ja jestem dla ciebie jak ten fragment a ty jestes dla mnie najwazniejsza na swiecie i lubie z toba spedzac czas ale tak naprawde lubie kocham z toba spedzac czas kocham wszystko co z toba zwiazane i jakbym miala cie porownac do czegokolwiek to nawet nie wiem bo nie wazne ile bym dala porownan ze pasujesz do mnie jak 6 do 7 albo jak spolka do ograniczonej odpowiedzialnosci to i tak zadne slowa nie sa w stanie tego opisac ale po prostu jestes idealna w kazdym tego slowa znaczeniu")
    st.write("Kocham cię!!!!!!!!!!")
    st.audio("piosenka.mp3", format="audio/mpeg",
             autoplay=True, loop=True)
