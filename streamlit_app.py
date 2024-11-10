import streamlit as st
import streamlit_authenticator as stauth

from utils import load_config


def app():
    hide_streamlit_style = """
            <style>
            #_profileContainer_51w34_53 {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    config = load_config()
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    if st.session_state["authentication_status"]:
        pages = {
            "Dashboard": [
                st.Page("pages/checkin.py", title="Checkin"),
                st.Page("pages/checkout.py", title="Checkout"),
                st.Page("pages/rent.py", title="Thuê sân"),
                st.Page("pages/shopping.py", title="Mua đồ"),
            ]
        }
        if "admin" in st.session_state.get("roles", []):
            pages.update(
                {
                    "Admin": [
                        st.Page("pages/admin.py", title="Quản lý"),
                        st.Page("pages/order.py", title="Đơn hàng"),
                    ]
                }
            )
        pg = st.navigation(pages)
        pg.run()


if __name__ == "__main__":
    app()
