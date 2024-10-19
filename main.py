from fasthtml.common import *

from components.dashboard import Dashboard
from components.login import LoginForm

app, rt = fast_app(live=True)


@rt("/")
def root():
    return Div(
        LoginForm(),
        Script("""
            function handleSubmit(event) {
                event.preventDefault();
                var username = document.getElementById("username").value;
                var password = document.getElementById("password").value;
                console.log("Login submitted:", {"username": username, "password": password});
                // Here you would typically handle the login logic
            }
        """),
    )


@rt("/dashboard")
def dashboard():
    return Div(Dashboard())


serve()
