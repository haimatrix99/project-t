from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

import constants
import helper
from utils import load_config

# Selecting Detection Or Segmentation
model_path = Path(constants.DETECTION_MODEL)


# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
    st.session_state["model"] = model
    st.session_state["confidence"] = 0.4

except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)


def app():
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
