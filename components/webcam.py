from fasthtml.common import *


def Webcam():
    return Div(
        Video(id="video", autoplay=True, style="width: 640px; height: 480px;"),
        Canvas(id="canvas", style="display:none;"),
        Script(src="/static/webcam.js"),
        P(
            id="datetimeDisplay", style="margin-top: 10px;"
        ),  # New paragraph for datetime display
        Button(
            "Snapshot",
            id="snapshotButton",
            onclick="takeSnapshot()",
            style="margin-top: 20px",
        ),
        style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;",
    )
