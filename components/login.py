from fasthtml.common import *


def LoginForm():
    return Div(
        Div(
            H2("Đăng nhập"),
            Form(
                Div(
                    Label(
                        "Tài khoản",
                        for_="username",
                    ),
                    Input(
                        type="text",
                        id="username",
                        name="username",
                        required=True,
                    ),
                ),
                Div(
                    Label(
                        "Mật khẩu",
                        for_="password",
                    ),
                    Input(
                        type="password",
                        id="password",
                        name="password",
                        required=True,
                    ),
                ),
                Button("Đăng nhập", type="submit"),
                action="/login",
                method="post",
            ),
            style="width: 50%; margin: 0 auto;",  # Set width and center alignment
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh;",  # Center vertically
    )
