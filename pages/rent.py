import streamlit as st


@st.dialog("Đăng ký sân")
def vote(number):
    name = st.text_input("Tên")
    date = st.date_input("Ngày đăng ký")
    hour = st.time_input("Giờ đăng ký")
    if st.button("Đăng ký"):
        st.session_state.form_register = {
            "court": number,
            "name": name,
            "date": date,
            "hour": hour,
        }
        st.rerun()


def page():
    st.title("Thuê sân")
    with st.container(border=True):
        if st.button("**Sân 1: Ngày, giờ**"):
            vote(1)
    with st.container(border=True):
        if st.button("**Sân 2: Ngày, giờ**"):
            vote(2)
    with st.container(border=True):
        if st.button("**Sân 3: Ngày, giờ**"):
            vote(2)


page()
