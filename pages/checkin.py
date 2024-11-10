import streamlit as st


def page():
    st.title("Checkin")
    picture = st.camera_input("Camera")

    send = st.button("Gửi", type="primary", use_container_width=True)

    if send:
        st.image(picture)


page()
