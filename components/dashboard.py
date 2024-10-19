from fasthtml.common import *


def Dashboard():
    return Div(
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
        Form(
            # Tags with a `name` attr will have `name` auto-set to the same as `id` if not provided
            Button(
                "Đăng xuất",
                type="submit",
                style="""
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 150px;
            """,
            ),
            action="/logout",
            method="post",
        ),
    )
