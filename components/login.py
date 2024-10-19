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
                onsubmit="handleSubmit(event)",
            ),
            style="width: 50%; margin: 0 auto;",  # Set width and center alignment
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh;",  # Center vertically
    )


def handleSubmit(event):
    event.preventDefault()
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    console.log("Login submitted:", {"username": username, "password": password})
    # Here you would typically handle the login logic
