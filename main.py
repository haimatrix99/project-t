from fasthtml.common import *

from components.dashboard import Dashboard
from components.login import LoginForm

app, rt = fast_app(live=True)


@dataclass
class Login:
    username: str
    password: str


@rt("/")
def get():
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


@rt("/login")
def post(login: Login, sess):
    sess["auth"] = login.username
    return RedirectResponse("/dashboard", status_code=303)


@rt("/dashboard")
def get():
    return Div(Dashboard())


@rt("/logout")
def post():
    return RedirectResponse("/", status_code=303)


@rt("/process_image")
async def post(request: Request, sess):
    print(await request.json())
    return {"status": "OK"}


serve()
