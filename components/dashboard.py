from fasthtml.common import *


def Dashboard():
    return Div(
        Div(
            Div(
                Button("Check in", type="button", style="margin: 20px;"),
                Button("Check out", type="button"),
                style="""
                position: absolute;
                top: 20px;
                left: 20px;
                """,
            ),
            Button(
                "Đăng xuất",
                type="button",
                style="""
                position: absolute;
                bottom: 20px;
                right: 20px;
                """,
            ),
        ),
    )
