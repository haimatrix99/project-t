import numpy as np
import streamlit as st
from PIL import Image


def page():
    st.title("Checkin")
    picture = st.camera_input("Camera")
    model = st.session_state["model"]
    confidence = st.session_state["confidence"]
    if picture is not None:
        img = Image.open(picture)
        img_array = np.array(img)
        res = model.predict(img_array, conf=confidence)
        if len(res[0].boxes) > 0:
            st.success("Đã checkin thành công!")
        else:
            st.error("Không tìm thấy mặt trong ảnh. Vui lòng thử lại!")

    send = st.button("Gửi", type="primary", use_container_width=True)

    if send:
        st.image(picture)


page()
