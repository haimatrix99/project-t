import streamlit as st


def create_image_grid(images, cols=3):
    rows = len(images) // cols + (1 if len(images) % cols != 0 else 0)

    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            idx = row * cols + col
            if idx < len(images):
                with columns[col]:
                    img = images[idx]
                    st.image(
                        img, use_container_width=True, caption=f"Product {idx + 1}"
                    )


def page():
    st.title("Mua đồ")

    image_paths = [
        "images/Picture1.jpg",
        "images/Picture2.jpg",
        "images/Picture3.jpg",
        "images/Picture4.jpg",
    ]

    create_image_grid(image_paths, cols=3)


page()
